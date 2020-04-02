"""
   Example script for how to batch process trials in the model.

   The script uses AnyPyTools, which is an open source library for 
   working with the AnyBody Modeling System. If you use this library 
   for publication please cite:

   Lund et al., (2019). AnyPyTools: A Python package for reproducible 
   research with the AnyBody Modeling System. Journal of Open Source 
   Software, 4(33), 1108, https://doi.org/10.21105/joss.01108

"""
import glob
import shutil

from anypytools import AnyPyProcess
from anypytools import macro_commands as mc


if not bool(glob.glob("c3dfiles/**/*.c3d")):
    raise (
        "Dataset not present. Please see "
        "Schreiber & Moissenet (2019) https://doi.org/10.1038/s41597-019-0124-4 "
        "and download data from  https://ndownloader.figshare.com/files/14397965 "
    )

#%% Process all standing reference trials
macro = [mc.Load("Main.any"), mc.OperationRun("Main.RunParameterIdentification")]

app = AnyPyProcess()
app.start_macro(
    macro, search_subdirs=r"\d{7}_ST\\Main.any", logfile="ParameterOptLog.txt"
)

#%% Process all marker tracking

macro = [
    mc.Load("Main.any"),
    mc.OperationRun("Main.RunAnalysis.LoadParameters"),
    mc.OperationRun("Main.RunAnalysis.MarkerTracking"),
]

app = AnyPyProcess()
app.start_macro(
    macro, search_subdirs=r"\d{7}_C\d_\d\d\\Main.any", logfile="MarkerTrackingLog.txt"
)

#%% Process all Inverse dynamics and export results


macro = [
    mc.Load("Main.any"),
    mc.OperationRun("Main.RunAnalysis.LoadParameters"),
    mc.OperationRun("Main.RunAnalysis.InverseDynamics"),
    mc.Dump("Main.Studies.InverseDynamicStudy.Ekin"),
]

app = AnyPyProcess()
results = app.start_macro(
    macro, search_subdirs=r"\d{7}_C\d_\d\d\\Main.any", logfile="InverseDynamicsLog.txt"
)

# Please see 
# https://anybody-research-group.github.io/anypytools-docs/Tutorial/01_Getting_started_with_anypytools.html
# for how to work with the results from AnyPyTools
