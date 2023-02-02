"""
Computes the intermediate files for the motion capture models in AMMR.

This a helper script to ensure that the intermediate files are up to date.
"""
import pathlib


import anypytools 
import anypytools.macro_commands as mc

mocap_path = pathlib.Path(__file__).parent.parent / "Application/MocapExamples"



macros1 =[
    [
        mc.Load(mocap_path / "Plug-in-gait_MultiTrial_StandingRef\Subjects\S1\S1_StandingRef\Main.any"),
        mc.OperationRun("Main.RunParameterIdentification"),
    ],
    [
        mc.Load(mocap_path / "Plug-in-gait_MultiTrial_StandingRef\Subjects\S2\S2_StandingRef\Main.any"),
        mc.OperationRun("Main.RunParameterIdentification"),
    ],
    [
        mc.Load(mocap_path / "Plug-in-gait_Simple\FullBody.main.any"),
        mc.OperationRun("Main.RunParameterIdentification"),
        mc.OperationRun("Main.RunAnalysis.MarkerTracking"),
    ],
    [
        mc.Load(mocap_path / "Plug-in-gait_Simple\LowerExtremity.main.any"),
        mc.OperationRun("Main.RunParameterIdentification"),
        mc.OperationRun("Main.RunAnalysis.MarkerTracking"),
    ],
    [
        mc.Load(mocap_path / "Plug-in-gait_Simple\FullBody_GRFPrediction.main.any"),
        mc.OperationRun("Main.RunParameterIdentification"),
        mc.OperationRun("Main.RunAnalysis.MarkerTracking"),
    ]
]

for standingref in (mocap_path / "ADL_Gait_[beta]\Subjects").glob("**/*_ST/Main.any"):
    macros1.append([
        mc.Load(standingref),
        mc.OperationRun("Main.RunParameterIdentification"),
    ])


macros2 = [
    [
        mc.Load(mocap_path / "Plug-in-gait_MultiTrial_StandingRef\Subjects\S1\S1_FlywheelSquat\Main.any"),
        mc.OperationRun("Main.RunAnalysis.LoadParameters"),
        mc.OperationRun("Main.RunAnalysis.MarkerTracking"),
    ],
]


abc_path = r"C:\Program Files\AnyBody Technology\AnyBody.7.5_Beta\AnyBodyCon.exe"

app1 = anypytools.AnyPyProcess(anybodycon_path=abc_path, num_processes=10)

app1.start_macro(macros1)

app2 = anypytools.AnyPyProcess(anybodycon_path=abc_path)
app2.start_macro(macros2)

