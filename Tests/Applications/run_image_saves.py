
# Small script for updating the wilke test files with the new reference values

from pathlib import Path
import re
from anypytools import AnyPyProcess, macro_commands as mc
from pandas import Series
#%%

files = Path(__file__).parent.glob("test_*.any")


filelist = list(files)

# print(filelist)

macros = []

for file in filelist:
    defs ={
        "CREATE_IMAGE": "1",
        "TEST_NAME": f'"{file.stem + "_0"}"'
    }
    macros.append(
        [
            mc.Load(str(file), defs=defs),
            mc.OperationRun("Main.RunTest"),
        ]
    )
# #%%

anybodycon = r"C:\Program Files\AnyBody Technology\AnyBody.7.5_Beta\AnyBodyCon.exe"

app = AnyPyProcess(num_processes=1, anybodycon_path=anybodycon)

results = app.start_macro(macros)

# #%%

# REFVALUE_RE = re.compile(r"(AnyVar RefValue = )(?P<val>.+);")

# results_table = {}

# for file, result in zip(files, results):
#     file = Path(file)
#     val = round(result["Main.Study.L5SacrumReac"],1)
#     oldval = float(REFVALUE_RE.search(file.read_text()).group('val'))
#     status = 'OK' if  'ERROR' not in result else 'failed'

#     results_table[Path(file)] = val
    
#     print(f"{file.stem}: {val} ({status}: {oldval})")


# # %%

# for file, val in results_table.items(): 
#     text = file.read_text()

#     text = REFVALUE_RE.sub(fr"\g<1>{val};", text)

#     #print(text)
#     file.write_text(text)


# # %%
# Series(results_table.values()).to_clipboard(excel=True, index=False, header=False)

# %%
