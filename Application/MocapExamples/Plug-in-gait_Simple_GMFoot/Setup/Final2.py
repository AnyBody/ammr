# -*- coding: utf-8 -*-



from scipy import interpolate

#*********************************************************
#INPOUT TO BE PROVIDED BY AMS THROUGH THE HOOK

# Matrix of pressure cells global coordinates (size [i][3])
#cell = [[0.5, 0.5, 0], [0.52, 0.5, 0], [0.5, 0.52, 0], [0.52, 0.52, 0]]

# Matrix of foot force-nodes global coordinates (size [j][3])
#foottest = [[0.19, 0.19, 0.1], [0.21, 0.19, 0.1], [0.21, 0.21, 0.1], [0.22, 0.21, 0.1], [0.23, 0.22, 0.1]]

# Current time step value of the anybody simulation
#timesteptest = 0.247
#*********************************************************


CellW = 0.00508
CellL = 0.00762


def PressureFunction(context, foot, timestep, path):
    
    
    
    # Reads the pressure data text file
    #**********************************
    def ReadData(fname):
        oFile = open(fname, 'r')
        lines = oFile.readlines()
        res = []
        step = None
        flag = 0
        rl=rb=rw=rh=0
        for i in range(len(lines)):
            if not lines[i].lower().find("rectangle left"):
                rl = float(lines[i+1])
            if not lines[i].lower().find("rectangle width"):
                rw = float(lines[i+1])
            if not lines[i].lower().find("rectangle height"):
                rh = float(lines[i+1])
            if not lines[i].lower().find("rectangle bottom"):
                rb = float(lines[i+1])
            if not lines[i].lower().find("frame") == -1:
                if not step == None:
                    res.append(step)
                step = []
                flag = 1
                s = lines[i].replace("(", " ")
                s = s.replace(")", " ")
                s = s.split()
                step.append(float(s[2])/1000)
                i = i + 1
            if flag == 1:
                for c in lines[i].split():
                    step.append(float(c))
        
        box = [rb, rl, rw, rh]
        return res, box
    
    
    
    Data = ReadData(path)[0]
    Box = ReadData(path)[1]
    Rb = int(Box[0])
    Rl = int(Box[1])
    Rw = int(Box[2])
    Rh = int(Box[3])
    #print Data
    #print Box
    
    
    
    
    # Zipped Data matrix, first line is time, second line is cell1, etc...
    #*******************************************************************
    DataZip = list(zip(*Data))
    Time = DataZip[0]
    Force = DataZip[1:]
    
    
    # Transform force data into coeff (to use when force plate present)
    #******************************************************************
    ForceZip = list(zip(*Force))
    CoeffZip = []
    for row in ForceZip:
        sum = 0
        SubCoeffZip = []
        for i in range(len(row)):
            sum = sum + row[i]
        for i in range(len(row)):
            if sum == 0:
                SubCoeffZip.append(row[i]/1)
            else:
                SubCoeffZip.append(row[i]/sum)
        CoeffZip.append(SubCoeffZip)
    
    Coeff = list(zip(*CoeffZip))
    
    
    
    
    # Create a global interpolation function: f(time)[cell]
    #******************************************************
    #CellForceFunction = interpolate.interp1d(Time, Force)
    CellCoeffFunction = interpolate.interp1d(Time, Coeff)
    
    #print CellCoeffFunction(0.342)[5]
    
    
    
    
    
    
    
    # Create the matrix of pressure cells global coordinates (size [i][3])
    #*********************************************************************
    cell = []
    cell0 = [0.4 -0.049 -64*CellW + (Rl+0.5)*CellW, 0.049 + (Rb+0.5)*CellL, 0] #theoretical value
    #cell0 = [0.4 -0.049 -64*CellW + (Rl+0.5)*CellW, 0.049 -0.01 + (Rb+0.5)*CellL, 0] #with offset
    for h in range(Rh):
        for w in range(Rw):
            cell.append([cell0[0] + CellW*w, cell0[1] + CellL*h, cell0[2]])
    
    #print cell
    
    
    
    
    
    
    
    # Temporary bell shape function.
    #*******************************
    #BellShapeDistance = [0, 0.004, 0.01, 0.016, 0.02, 0.5, 1, 2]
    BellShapeDistance = [0, 0.003, 0.006, 0.009, 0.014, 0.025, 0.5, 1, 2]
    BellShapeValues = [1, 0.9, 0.5, 0.1, 0.01, 0, 0, 0, 0]
    BellFunction = interpolate.interp1d(BellShapeDistance, BellShapeValues)
    
    
    
    
    
    
    # Takes all the combinations of cell/foot nodes and store it in matrix (size [i][j])
    #***********************************************************************************
    def CoeffUnscaled (c, f):
        CoeffMat = []
        CoeffSumVec = []
        for i in range(len(c)):
            SubCoeffMat = []
            CoeffSum = 0
            for j in range(len(f)):
                vec = [f[j][0] - c[i][0], f[j][1] - c[i][1]]
                dist = ((vec[0])**2 + (vec[1])**2)**0.5
                coeff = float(BellFunction(dist))
                SubCoeffMat.append(coeff)
                CoeffSum = CoeffSum + coeff
            CoeffMat.append(SubCoeffMat)
            CoeffSumVec.append(CoeffSum)
        return CoeffMat, CoeffSumVec
    
    CoeffMat = CoeffUnscaled (cell, foot)[0]
    CoeffSumVec = CoeffUnscaled (cell, foot)[1]
    #print UnscaledCoeffMat
    #print CoeffSumVec
    
    
    
    
    
    # Scale the bell function coeff sum to match the measured cell coeff
    #*******************************************************************
    for i in range(len(CoeffMat)):
        if CoeffSumVec[i] == 0:
            ScaleFactor = 0
        else:
            ScaleFactor = CellCoeffFunction(timestep)[i] / CoeffSumVec[i]
        for j in range(len(CoeffMat[0])):
            CoeffMat[i][j] = CoeffMat[i][j] * ScaleFactor
    
    
    #print CoeffMat
    
    
    
    
    # Sum the contribution of all cells for each foot node
    #*****************************************************
    FinalCoeffVec = []
    for j in range(len(CoeffMat[0])):
        finalcoeff = 0
        for i in range(len(CoeffMat)):
            finalcoeff = finalcoeff + CoeffMat[i][j]
        FinalCoeffVec.append(finalcoeff)
    
    #print FinalCoeffVec
    
    FinalCoeffVecTuple = tuple(FinalCoeffVec)
    
    return FinalCoeffVecTuple






