# -*- coding: utf-8 -*-
r"""
Knee Simulator Model
=======================================

Model of a Knee Simulator using a knee implant model and force-dependent kinematics (FDK). 
For an indepth description of the mathematics and mechanics behind FDK please see [AZDN17]_.

**Main file:** ``Application/Examples/KneeSimulator/AnyKneeSimulator.Main.any``


.. figure:: /Applications/images/KneeSimulator_Full.jpg
    :align: center

    Overview of the knee simulator


This is stand alone demo model of a knee simulator device resembling the principles of the Kansas Knee simulator [HCMT10]_.
The model is contructed as a stand-alone model and doesn't use any elements and body parts from the model repository (AMMR). 
Data for the total knee replacement (TKR) implant comes from the `6th Grand Challenge Competition to Predict In Vivo Knee Loads <https://simtk.org/projects/kneeloads>`_. 


Segments
---------------------
The model is constructed of five main segments (femur, patella, tibia, ankle-fixture, and hip-fixture). 
In practice more segments are included. The mass of the femur/tibia is implemented as separate segments
for easier specification of the moments of inertia. Likewise, the trans-spherical mechanism between ankle
and ground segments is implmented using three segments connected with revolute and slider joints. 


Ligaments
-----------------------------
The ligaments are modeled using one-dimensional nonlinear elastic spring elements. In order to prevent 
ligaments from penetrating the bone/implant surfaces, they were wrapped around various geometrical shapes (cylinder, ellipsoid,...).
Ligament properties (stiffness and reference strains) were adopted from the literature [BKHG91]_ & [MVFK15]_.


.. figure:: /Applications/images/KneeSimulator_Ligaments.jpg
    :align: center

    Ligaments in the model, abbreviations adopted from [SbTP06]_ Figure 1.



Contacts
--------------------------------
Three STL-based rigid-rigid contact models were defined: between the patella and femoral component,  the femoral component and tibia insert (lateral side), 
and the femoral component and tibia insert (medial side).


.. figure:: /Applications/images/KneeSimulator_Contacts.jpg
    :align: center

    Contact surfaces in the model





Settings
-------------------------
Model settings can be added and removed here: ``UserDefinedSettings.Main.any`` to apply FDK to the tibiofemoral joint, patellofemoral joint, or both together.

.. code-block:: AnyScriptDoc

      #define USE_FDK_TIBIOFEMORAL
      #define USE_FDK_PATELLOFEMORAL

Other adjustable settings include: ligament parameters, femur and tibia mass ratios, load applied to the hip fixture, and desired knee flexion. 

.. code-block:: AnyScriptDoc

    #define DEF_KNEE_FLEXION_MIN 10
    #define DEF_KNEE_FLEXION_MAX 60

    #define DEF_HIP_AXIAL_LOAD_MIN 200
    #define DEF_HIP_AXIAL_LOAD_MAX 200  

    #define FEMUR_MASS_RATIO 0.135
    #define TIBIA_MASS_RATIO 0.0465

    #include "Input/Ligament_Properties.any"

Please note that this simulation is only a demo example.

References
-----------------------

.. [AZDN17] Andersen, M. S., de Zee, M., Damsgaard, M., Nolte, D., & Rasmussen, J. Introduction to Force-Dependent Kinematics: Theory and Application 
   to Mandible Modeling. J Biomech Eng. 139(9), 091001 (2017). doi: `10.1115/1.4037100 <https://doi.org/10.1115/1.4037100>`__
.. [HCMT10] Halloran JP, Clary CW, Maletsky LP, Taylor M, Petrella AJ, Rullkoetter PJ. Verification 
   of predicted knee replacement kinematics during simulated gait in the Kansas knee simulator. J 
   Biomech Eng. 132(8), 081010 (2010). doi:`10.1115/1.4001678 <http://dx.doi.org/10.1115/1.4001678>`__
.. [BKHG91] Blankevoort, L., Kuiper, J. H., Huiskes, R., and Grootenboer, H. J., “Articular Contact 
   in a Three-Dimensional Model of the Knee,” J. Biomech., 24(11), pp. 1019–1031, (1991). doi:`10.1016/0021-9290(91)90019 <https://doi.org/10.1016/0021-9290(91)90019-J>`__  
.. [MVFK15] Marra, M. A. et al. A subject-specific musculoskeletal modeling framework to predict in
   vivo mechanics of total knee arthroplasty. J. Biomech. Eng. 137, 020904 (2015). doi:`10.1115/1.4029258 <http://dx.doi.org/10.1115/1.4029258>`__
.. [SbTP06] Shelburne, K. B., Torry, M. R. & Pandy, M. G. Contributions of muscles, ligaments, and the ground-reaction force to tibiofemoral joint loading
   during normal gait. J. Orthop. Res. 24, 1983–1990 (2006). doi:`10.1002/jor.20255 <http://dx.doi.org/10.1002/jor.20255>`__




"""

import sys
sys.path.insert(0, '../../exts')
import gallery

gallery.plot("../images/KneeSimulator.jpg")
gallery.show()
