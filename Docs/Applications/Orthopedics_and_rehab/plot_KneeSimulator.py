# -*- coding: utf-8 -*-
r"""
Knee Simulator Model
=======================================

Model of a Knee Simulator using a knee implant model and force-dependent kinematics (FDK).

**Main file:** ``Application/Examples/KneeSimulator/AnyKneeSimulator.Main.any``

This is stand alone demo model of a knee simulator device resembling the principles of the Kansas Knee simulator [HCMT10]_.
The model is contructed as a stand-alone model and doesn't use any elements and body parts from the model repository (AMMR). 
Data for the knee implant comes from the `"6th Grand Challenge Competition to Predict In Vivo Knee Loads"<https://simtk.org/projects/kneeloads)>`__. 


Segments
---------------------
The model is constructed with five main segments (femur, patella, tibia, ankle-fixture, hip-fixture). 
In practice more segments are included. The mass of the femur/tibia is implmented as separate segments
for easier specification of the moments of enertia. Likewise, the transspherical mechanism beween ankle
and ground segments is implmented with three  segments connected with revolute and slider joints. 




Please notice that this simulation is only a demo example. 

References
-----------------------

.. [HCMT10] Halloran JP, Clary CW, Maletsky LP, Taylor M, Petrella AJ, Rullkoetter PJ. Verification 
   of predicted knee replacement kinematics during simulated gait in the Kansas knee simulator. J 
   Biomech Eng. 2010;132: 081010. doi:`10.1115/1.4001678<http://dx.doi.org/10.1115/1.4001678>`__


"""

import sys
sys.path.insert(0, '../../exts')
import gallery

gallery.plot("../images/KneeSimulator.jpg")
gallery.show()
