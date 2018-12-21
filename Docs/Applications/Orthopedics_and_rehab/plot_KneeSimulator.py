# -*- coding: utf-8 -*-
r"""
Knee Simulator Model
=======================================

Model of a Knee Simulator using a knee implant model and force-dependent kinematics (FDK).

**Main file:** ``Application/Examples/KneeSimulator/AnyKneeSimulator.Main.any``


.. figure:: /Applications/Orthopedics_and_rehab/KneeSimulator_Full.png
    :align: center

    Overview of the knee simulator


This is stand alone demo model of a knee simulator device resembling the principles of the Kansas Knee simulator [HCMT10]_.
The model is contructed as a stand-alone model and doesn't use any elements and body parts from the model repository (AMMR). 
Data for the knee implant comes from the `"6th Grand Challenge Competition to Predict In Vivo Knee Loads"<https://simtk.org/projects/kneeloads)>`__. 


Segments
---------------------
The model is constructed with five main segments (femur, patella, tibia, ankle-fixture, hip-fixture). 
In practice more segments are included. The mass of the femur/tibia is implmented as separate segments
for easier specification of the moments of enertia. Likewise, the transspherical mechanism beween ankle
and ground segments is implmented with three  segments connected with revolute and slider joints. 


Ligaments
-----------------------------



.. figure:: /Applications/Orthopedics_and_rehab/KneeSimulator_Ligaments.png
    :align: center

    Ligaments in the model



Contacts
--------------------------------




.. figure:: /Applications/Orthopedics_and_rehab/KneeSimulator_Contacts.png
    :align: center

    Contact surfaces in the model





Settings
-------------------------




















Please notice that this simulation is only a demo example. 

References
-----------------------

.. [HCMT10] Halloran JP, Clary CW, Maletsky LP, Taylor M, Petrella AJ, Rullkoetter PJ. Verification 
   of predicted knee replacement kinematics during simulated gait in the Kansas knee simulator. J 
   Biomech Eng. 2010; doi:`10.1115/1.4001678<http://dx.doi.org/10.1115/1.4001678>`__
.. [SbTP06] Shelburne, K. B., Torry, M. R. & Pandy, M. G. 
   Contributions of muscles, ligaments, and the ground-reaction force to tibiofemoral joint loading
   during normal gait. J. Orthop. Res. 24, 1983–1990 (2006). doi:`10.1002/jor.20255 <http://dx.doi.org/10.1002/jor.20255>`__
.. [MVFK15] Marra, M. A. et al. A subject-specific musculoskeletal modeling framework to predict in
   vivo mechanics of total knee arthroplasty. J. Biomech. Eng. 137, 020904 (2015). doi:`10.1115/1.4029258 <http://dx.doi.org/10.1115/1.4029258>`__




"""

import sys
sys.path.insert(0, '../../exts')
import gallery

gallery.plot("../images/KneeSimulator.jpg")
gallery.show()
