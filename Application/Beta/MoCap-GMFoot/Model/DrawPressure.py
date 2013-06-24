# -*- coding: utf-8 -*-



from scipy import interpolate


def PressureDrawFunction(context,timestep,path):
    
    
    
    # Reads the pressure data text file
    #**********************************
    def ReadData(fname):
        oFile = open(fname, 'r')
        lines = oFile.readlines()
        res = []
        step = None
        flag = 0
        rl=rb=rw=rh=0
        for i in xrange(len(lines)):
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
    DataZip = zip(*Data)
    Time = DataZip[0]
    Force = DataZip[1:]
    
    
    
    
    
    
    #Complete the [Rw][Rh] matrix with zeros to get a [33][46] matrix
    #for each time step
    #****************************************************************
    ForceZip = zip(*Force)    #first line is cell1, cell2, ...
    ForceZipComplete = []
    
    for k in range(len(Time)):
        SubForceZipComplete = []
        for i in range(Rh):
            for j in range(Rw):
                SubForceZipComplete.append(ForceZip[k][i*Rw+j])
            for j in range(Rw,33):
                SubForceZipComplete.append(0)
        for i in range(Rh,46):
            for j in range(33):
                SubForceZipComplete.append(0)
        ForceZipComplete.append(SubForceZipComplete)
    
    ForceComplete = zip(*ForceZipComplete)
    
    
    
   
    # Create a global interpolation function: f(time)[cell]
    #******************************************************
    ForceFunction = interpolate.interp1d(Time, ForceComplete)
    
    #print CellCoeffFunction(0.342)[5]
    
    FinalVec = ForceFunction(timestep)
    
    
    
    FinalVecTuple = tuple(FinalVec)
    
    return FinalVecTuple






