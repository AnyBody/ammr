# -*- coding: utf-8 -*-






def ReadBoxFunction(context, path):
    
    
    
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
    
    
    
    Box = ReadData(path)[1]
    
    BoxTuple = tuple(Box)
    
    return BoxTuple






