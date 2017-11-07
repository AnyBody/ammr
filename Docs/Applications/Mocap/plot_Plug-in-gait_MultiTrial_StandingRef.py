# -*- coding: utf-8 -*-
r"""
Multi trial MoCap model
===============================

Example of a MoCap model structured for analyzing data from multiple trials
and subjects. 

This example shows the AnyMoCap framework applied to a set of squatting trials.
The subject specific scaling and marker optimization is done on a standing
reference recording, and the values are then applied two squatting trials.

The data is provided by Maria Jönsson from KTH (Royal Institute of Technology
School of Technology and Health) in Sweden.

:file:`Application/MocapExamples/Plug-in-gait_MultiTrial_StandingRef`

The files are structured so each trials has its own folder with a main file
(``Main.any``), a file with trial specific data (``TrialSpecificData.any```) and a
C3D data file. (The C3D files could have been placed together in a separate folder if
that was desirable.)

.. code-block: none

    │   BodyModelConfig.any
    │   C3DSettings.any
    │   ExtraDrivers.any
    │   ForcePlates.any
    │   LabSpecificData.any
    │   MarkerProtocol.any
    │   libdef.any
    │
    ├───Output\
    │
    └───Trials\
        │   SubjectSpecificData.any
        │
        ├───FlywheelSquat_1\
        │       FlywheelSquat_1.c3d
        │       Main.any
        │       TrialSpecificData.any
        │
        └───StandingRef_1\
                Main.any
                StandingRef_1.c3d
                TrialSpecificData.any



.. image:: /Applications/Mocap/MultiTrialStructure.png

This special structure makes it much easier to work with large datasets. And
this model is the best starting point for analyzing bigger MoCap experiments. 

"""


import sys
sys.path.insert(0, '../../exts')
import gallery

gallery.plot("../images/Plug-in-gait_Squat_StandigRef.jpg")
gallery.plot("../images/Plug-in-gait_Squat_Flywheel.jpg")
gallery.show()
