""" Script for batch processing all data in the walking dataset.
   
   The script runs batch processing in three steps:

   1. Runs all the standing reference trials to 
      calculate scaling and marker positions for each subject. 

   2. Runs marker tracking for all trials, saving joint angles to files. 

   3. It runs the inverse dyanmic analysis for all trials.
      This steps outputs the EKin variable. But can be extended
      to output any variable from the model. 

   Note: The script uses AnyPyTools, which is an open source library for 
         working with the AnyBody Modeling System. If you use this library 
         for publication please cite:

         Lund et al., (2019). AnyPyTools: A Python package for reproducible 
         research with the AnyBody Modeling System. Journal of Open Source 
         Software, 4(33), 1108, https://doi.org/10.21105/joss.01108

"""
import os
import glob
import shutil
import warnings

try:
    from anypytools import AnyPyProcess
    from anypytools import macro_commands as mc
except ImportError as exp:
    msg = (
        "AnyPyTools missing. Please install the AnyPyTools library to run batch processing: "
        "https://anybody-research-group.github.io/anypytools-docs/"
    )
    raise ImportError(msg) from exp


# Check if the full dataset is present
if len(glob.glob("c3dfiles/**/*.c3d")) < 3:
    warnings.warn(
        "Dataset not present. Please see "
        "Schreiber & Moissenet (2019) https://doi.org/10.1038/s41597-019-0124-4 "
        "and download the data from https://ndownloader.figshare.com/articles/7734767/versions/8 "
    )

# Create folder for storing batch processing logfiles
# NOTE: Log files are automatically deleted unless the model fails.
os.makedirs("BatchProcessingLogs", exist_ok=True)

#%% Process all standing reference trials
macro = [mc.Load("Main.any"), mc.OperationRun("Main.RunParameterIdentification")]

app = AnyPyProcess(num_processes=3)
app.start_macro(
    macro,
    search_subdirs=r"\d{7}_ST\\Main.any",
    logfile="BatchProcessingLogs/ParameterOptimization.txt",
)


#%% Process all marker tracking

macro = [
    mc.Load("Main.any"),
    mc.OperationRun("Main.RunAnalysis.LoadParameters"),
    mc.OperationRun("Main.RunAnalysis.MarkerTracking"),
]

app = AnyPyProcess(num_processes=3, ignore_errors=[".anyset"])
app.start_macro(
    macro,
    search_subdirs=r"\d{7}_C\d_\d\d\\Main.any",
    logfile="BatchProcessingLogs/MarkerTracking.txt",
)

#%% Process all Inverse dynamics and export results

macro = [
    mc.Load("Main.any"),
    mc.OperationRun("Main.RunAnalysis.LoadParameters"),
    mc.OperationRun("Main.RunAnalysis.InverseDynamics"),
    mc.Dump("Main.Studies.InverseDynamicStudy.Ekin"),
    # Add more output here
]

app = AnyPyProcess(num_processes=3, ignore_errors=[".anyset"])
results = app.start_macro(
    macro,
    search_subdirs=r"\d{7}_C\d_\d\d\\Main.any",
    logfile="BatchProcessingLogs/InverseDynamics.txt",
)

# Please see
# https://anybody-research-group.github.io/anypytools-docs/Tutorial/01_Getting_started_with_anypytools.html
# for how to work with the results from AnyPyTools
