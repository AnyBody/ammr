import optparse
import re
import os

def ReadMLFile(context,filename, path = None):
    filelocation = os.path.join(path, filename)
    fin = open(filelocation, 'r')
    output =[]
    cnt = 0
    for line in fin:
        m = re.search('<point x="', line)
        if m == None:
            continue
        line = line[:m.start()] + line[m.end():]
        m = re.search('" y="', line)
        line = line[:m.start()] + ' ' + line[m.end():]
        m = re.search('" z="', line)
        line = line[:m.start()] + ' ' + line[m.end():]
        m = re.search('" active="1" name="', line)
        line = line[:m.start()] + ' ' + line[m.end():]
        m = re.search('"/>', line)
        res = line[:m.start()].split() 
        #line = '{' + res[0] + ','+ res[1] + ','+ res[2] + '}'
	vec = [float(res[0]), float(res[1]), float(res[2])]
        output.append(tuple(vec))
    fin.close()
    return tuple(output)

 

