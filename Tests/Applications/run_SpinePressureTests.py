
# Small script for updating the wilke test files with the new reference values
#%%
from pathlib import Path
import re
from anypytools import AnyPyProcess, macro_commands as mc
from pandas import Series
#%%

files = [
    "test_SpinePressureLyingOnBack.any",
    "test_SpinePressureSeatingRelaxed.any",
    "test_SpinePressureSeatingStraitNoSupport.any",
    "test_SpinePressureStanding.any",
    "test_SpinePressureStandingFlexed.any",
    "test_SpinePressureStandingLiftClose.any",
    "test_SpinePressureStandingLiftFlexed.any",
    "test_SpinePressureStandingLiftStretchedArms.any",
]

files = [elm.replace("Spine", "FlexibleSpine") for elm in files]

macros = []
for file in files:
    macros.append(
        [
            mc.Load(file),
            mc.OperationRun("Main.RunTest"),
            mc.Dump("Main.Study.L5SacrumReac"),
        ]
    )
#%%
app = AnyPyProcess(num_processes=2)

results = app.start_macro(macros)

#%%

REFVALUE_RE = re.compile(r"(AnyVar RefValue = )(?P<val>.+);")

results_table = {}

for file, result in zip(files, results):
    file = Path(file)
    val = round(result["Main.Study.L5SacrumReac"],1)
    oldval = float(REFVALUE_RE.search(file.read_text()).group('val'))
    status = 'OK' if  'ERROR' not in result else 'failed'

    results_table[Path(file)] = val
    
    print(f"{file.stem}: {val} ({status}: {oldval})")


# %%
if False:
    for file, val in results_table.items(): 
        text = file.read_text()

        text = REFVALUE_RE.sub(fr"\g<1>{val};", text)

        #print(text)
        file.write_text(text)


# %%
Series(results_table.values()).to_clipboard(excel=True, index=False, header=False)
