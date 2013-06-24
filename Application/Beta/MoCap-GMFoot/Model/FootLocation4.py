# -*- coding: utf-8 -*-





CellW = 0.00508
CellL = 0.00762


def LocationFunction(context,path):
    
    
    
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
    
    
    
    
    
    
    
    #First time step CoP, correspond to heel strike location
    #*******************************************************
    Step1Vec = Data[0][1:]
    
    LongWeightedStep1Vec = []
    for i in range(Rh):
        LongCoo = 0.049+(Rb+0.5+i)*CellL
        for j in range(Rw):
            LongWeightedStep1Vec.append(Step1Vec[i*Rw+j]*LongCoo)
    
    LongCooStrike = sum(LongWeightedStep1Vec)/sum(Step1Vec)
    
    LatWeightedStep1Vec = []
    for i in range(Rw):
        LatCoo = 0.4 -0.049 -64*CellW + (Rl+0.5+i)*CellW
        for j in range(Rh):
            LatWeightedStep1Vec.append(Step1Vec[j*Rw+i]*LatCoo)
    
    LatCooStrike = sum(LatWeightedStep1Vec)/sum(Step1Vec)
    
    
    
    
    
    
    
    
    
    
    
    
    
    # Take the max of each cell into a vector [max(cell1), max(cell2), ..]
    # and cut in anterior/posterior halfs
    #*********************************************************************
    MaxVec = []
    for i in range(len(Force)):
        MaxVec.append(max(Force[i]))
    
    RectangleMid = int(round(Rh/2)*Rw) #last cell of the mid line
    MaxVecPosterior = MaxVec[:RectangleMid]
    MaxVecAnterior = MaxVec[RectangleMid:]
    
    
    
    
    
    
    # Calculate the coordinate of max print posterior center of pressure
    #**********************************************************************
    LongWeightedMaxVecPosterior = []
    for i in range(int(round(Rh/2))):
        LongCoo = 0.049+(Rb+0.5+i)*CellL
        for j in range(Rw):
            LongWeightedMaxVecPosterior.append(MaxVecPosterior[i*Rw+j]*LongCoo)
    
    LongCooPosterior = sum(LongWeightedMaxVecPosterior)/sum(MaxVecPosterior)
    
    LatWeightedMaxVecPosterior = []
    for i in range(Rw):
        LatCoo = 0.4 -0.049 -64*CellW + (Rl+0.5+i)*CellW
        for j in range(int(round(Rh/2))):
            LatWeightedMaxVecPosterior.append(MaxVecPosterior[j*Rw+i]*LatCoo)
    
    LatCooPosterior = sum(LatWeightedMaxVecPosterior)/sum(MaxVecPosterior)
    
    
    
    
    
    
    
    
    
    
    
    # Calculate the coordinate of medial max print 
    #**********************************************************************
    
    LatMaxCooVecAnteriorMedial = []
    for i in range(Rw):
        LatCoo = 0.4 -0.049 -64*CellW + (Rl+0.5+i)*CellW
        for j in range(Rh-int(round(Rh/2))):
            if MaxVecAnterior[j*Rw+i]>0:
                coeff = 1
            else:
                coeff = 1000
            LatMaxCooVecAnteriorMedial.append(coeff*LatCoo)
    
    LatCooAnteriorMedial = min(LatMaxCooVecAnteriorMedial)
    
    VecIndexMedial = LatMaxCooVecAnteriorMedial.index(LatCooAnteriorMedial)
    LineLocalIndexMedial = VecIndexMedial - (Rh-int(round(Rh/2)))*int(VecIndexMedial/(Rh-int(round(Rh/2))))
    LineIndexMedial = LineLocalIndexMedial + int(round(Rh/2)) #longitudinal index
    ColumnIndexMedial = int(VecIndexMedial/(Rh-int(round(Rh/2)))) #lateral index
    LongCooAnteriorMedial = 0.049+(Rb+int(round(Rh/2))+0.5+LineLocalIndexMedial)*CellL
    
    #print VecIndexMedial
    #print LineIndexMedial
    
    
    
    
    
    # Calculate the coordinate of lateral max print 
    #**********************************************************************
    
    LatMaxCooVecAnteriorLateral = []
    for i in range(Rw):
        LatCoo = 0.4 -0.049 -64*CellW + (Rl+0.5+i)*CellW
        for j in range(Rh-int(round(Rh/2))):
            if MaxVecAnterior[j*Rw+i]>0:
                coeff = 1
            else:
                coeff = 0
            LatMaxCooVecAnteriorLateral.append(coeff*LatCoo)
    
    LatCooAnteriorLateral = max(LatMaxCooVecAnteriorLateral)
    
    VecIndexLateral = LatMaxCooVecAnteriorLateral.index(LatCooAnteriorLateral)
    LineIndexLateral = VecIndexLateral - (Rh-int(round(Rh/2)))*int(VecIndexLateral/(Rh-int(round(Rh/2))))
    LongCooAnteriorLateral = 0.049+(Rb+int(round(Rh/2))+0.5+LineIndexLateral)*CellL
    
    #print VecIndexLateral
    #print LineIndexLateral
    
    
    
    
    
    
    
    # Calculate the coordinate of distal max print 
    #**********************************************************************
    
    LongMaxCooVecDistal = []
    for i in range(Rh):
        LongCoo = 0.049+(Rb+0.5+i)*CellL
        for j in range(Rw):
            if MaxVec[i*Rw+j]>0:
                coeff = 1
            else:
                coeff = 0
            LongMaxCooVecDistal.append(coeff*LongCoo)
    
    LongCooDistal = max(LongMaxCooVecDistal)
    
    VecIndexDistal = LongMaxCooVecDistal.index(LongCooDistal)
    ColumnIndexDistal = VecIndexDistal - Rw*int(VecIndexDistal/Rw) #lateral index
    LineIndexDistal = int(VecIndexDistal/Rw) #longitudinal index
    LatCooDistal = 0.4 -0.049 -64*CellW + (Rl+0.5+ColumnIndexDistal)*CellW
    
    
    
    
    
    # Calculate the center of pressure of distal phalange 1
    #(from a box made from distal and medial points)
    #***********************************************************************
    Phal1MaxVec = MaxVec[((LineIndexDistal-4)*Rw+(ColumnIndexMedial+1)):((LineIndexDistal-4)*Rw+(ColumnIndexMedial+8))]+MaxVec[((LineIndexDistal-4)*Rw+(ColumnIndexMedial+1)+Rw):((LineIndexDistal-4)*Rw+(ColumnIndexMedial+8)+Rw)]+MaxVec[((LineIndexDistal-4)*Rw+(ColumnIndexMedial+1)+2*Rw):((LineIndexDistal-4)*Rw+(ColumnIndexMedial+8)+2*Rw)]+MaxVec[((LineIndexDistal-4)*Rw+(ColumnIndexMedial+1)+3*Rw):((LineIndexDistal-4)*Rw+(ColumnIndexMedial+8)+3*Rw)]+MaxVec[((LineIndexDistal-4)*Rw+(ColumnIndexMedial+1)+4*Rw):((LineIndexDistal-4)*Rw+(ColumnIndexMedial+8)+4*Rw)]
    
    
    LongWeightedMaxVecPhal1 = []
    for i in range(LineIndexDistal-4, LineIndexDistal+1):
        LongCoo = 0.049+(Rb+0.5+i)*CellL
        for j in range(ColumnIndexMedial+1, ColumnIndexMedial+8):
            LongWeightedMaxVecPhal1.append(MaxVec[i*Rw+j]*LongCoo)
    
    LongCooPhal1 = sum(LongWeightedMaxVecPhal1)/sum(Phal1MaxVec)
    
    LatWeightedMaxVecPhal1 = []
    for i in range(ColumnIndexMedial+1, ColumnIndexMedial+8):
        LatCoo = 0.4 -0.049 -64*CellW + (Rl+0.5+i)*CellW
        for j in range(LineIndexDistal-4, LineIndexDistal+1):
            LatWeightedMaxVecPhal1.append(MaxVec[j*Rw+i]*LatCoo)
    
    LatCooPhal1 = sum(LatWeightedMaxVecPhal1)/sum(Phal1MaxVec)
    
    
    
    
    
    
    
    
    
    
    
    # Calculate the center of pressure of distal phalange 2
    #(from a box made from distal and medial points)
    #***********************************************************************
    Phal2MaxVec = MaxVec[((LineIndexDistal-4)*Rw+(ColumnIndexMedial+7)):((LineIndexDistal-4)*Rw+(ColumnIndexMedial+12))]+MaxVec[((LineIndexDistal-4)*Rw+(ColumnIndexMedial+7)+Rw):((LineIndexDistal-4)*Rw+(ColumnIndexMedial+12)+Rw)]+MaxVec[((LineIndexDistal-4)*Rw+(ColumnIndexMedial+7)+2*Rw):((LineIndexDistal-4)*Rw+(ColumnIndexMedial+12)+2*Rw)]+MaxVec[((LineIndexDistal-4)*Rw+(ColumnIndexMedial+7)+3*Rw):((LineIndexDistal-4)*Rw+(ColumnIndexMedial+12)+3*Rw)]+MaxVec[((LineIndexDistal-4)*Rw+(ColumnIndexMedial+7)+4*Rw):((LineIndexDistal-4)*Rw+(ColumnIndexMedial+12)+4*Rw)]
    
    
    LongWeightedMaxVecPhal2 = []
    for i in range(LineIndexDistal-4, LineIndexDistal+1):
        LongCoo = 0.049+(Rb+0.5+i)*CellL
        for j in range(ColumnIndexMedial+7, ColumnIndexMedial+12):
            LongWeightedMaxVecPhal2.append(MaxVec[i*Rw+j]*LongCoo)
    
    LongCooPhal2 = sum(LongWeightedMaxVecPhal2)/sum(Phal2MaxVec)
    
    LatWeightedMaxVecPhal2 = []
    for i in range(ColumnIndexMedial+7, ColumnIndexMedial+12):
        LatCoo = 0.4 -0.049 -64*CellW + (Rl+0.5+i)*CellW
        for j in range(LineIndexDistal-4, LineIndexDistal+1):
            LatWeightedMaxVecPhal2.append(MaxVec[j*Rw+i]*LatCoo)
    
    LatCooPhal2 = sum(LatWeightedMaxVecPhal2)/sum(Phal2MaxVec)
    
    
    
    
    
    
    
    
    
    
    
    CooVec = [LatCooStrike,LongCooStrike,
    LatCooPosterior,LongCooPosterior,
    LatCooAnteriorMedial,LongCooAnteriorMedial,
    LatCooAnteriorLateral,LongCooAnteriorLateral,
    LatCooDistal,LongCooDistal,
    LatCooPhal1,LongCooPhal1,
    LatCooPhal2,LongCooPhal2]
    
    CooVecTuple = tuple(CooVec)
    
    return CooVecTuple




