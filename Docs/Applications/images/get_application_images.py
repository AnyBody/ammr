# Script for copying in application images. 

import os
import re
import shutil
from pathlib import Path

folders  = [
    Path("../../../Tests/Applications/Output"),
    Path("../../../Tests/AnyMocap/Output"),
]


files = [
    img 
    for folder in folders 
    for img in folder.iterdir() 
    if 'InitPos' in img.name and img.name.endswith('jpg')
]

RE_IMAGE = re.compile('.*test_(.*).any_0_InitPos.jpg')

for fimg in files:
    m = RE_IMAGE.match(fimg.name)
    if m:
        targetfile = os.getcwd() +'/'+ m.group(1) +'.jpg'
        shutil.copyfile(fimg, targetfile)
