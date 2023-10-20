# Script for creating in application images and copying them into the documentation. 

import os
import re
import shutil
from pathlib import Path

from PIL import Image
from anypytools import AnyPyProcess, macro_commands as mc

APP_FOLDER = Path(__file__).parent / "../../../Tests/Applications"
MOCAP_FOLDER = Path(__file__).parent / "../../../Tests/AnyMocap"
app_opts = {
    "anybodycon_path": r"C:\Program Files\AnyBody Technology\AnyBody.7.5_Beta\AnyBodyCon.exe",
    "num_processes": 2,
}

RUN_ANYBODY_MODELS = True


# Small script for updating the wilke test files with the new reference values

#%%

glob_str = "test_*.any"
test_files = [
    *APP_FOLDER.glob("test_*.any"),
    *MOCAP_FOLDER.glob("test_*.any"),
]

defines = {"CREATE_IMAGE": "1"}
macros = []

for file in test_files:
    if "CREATE_IMAGE" not in file.read_text():
        continue
    defines["TEST_NAME"] = f'"{file.name + "_0"}"'
    macros.append(
        [
            mc.Load(str(file), defs=defines),
            mc.OperationRun("Main.RunTest"),
        ]
    )

if RUN_ANYBODY_MODELS:
    app = AnyPyProcess(**app_opts)
    results = app.start_macro(macros)
    

for elem in results:
    if "ERROR" in elem:
        print(elem["ERROR"])


image_files = [
    *APP_FOLDER.joinpath("Output").iterdir(),
    *MOCAP_FOLDER.joinpath("Output").iterdir(),
]


RE_IMAGE = re.compile('.*[tT]est_(.+?)\.any_0_InitPos.png')

for fimg in image_files:
    m = RE_IMAGE.match(fimg.name)
    if m:
        im = Image.open(fimg).convert("RGB")

        targetfile = Path(__file__).parent / (m.group(1) +'.webp')
        #print(targetfile)
        im.save(targetfile, "WEBP")
