# -*- coding: utf-8 -*-
r"""
Femoral Torsion tool
=======================================

This is an example of modifying the femoral torsion of the default leg
({ref}`TLEM 2.0 <tlem2>`) geometry by using a model utility tool included within
the model repository. The  model is the simple standing model where the femoral
torsion has been altered to 20 degrees. The model is also a good example on how
a similar morphing approach can be used to personalize different body segments.

.. rst-class:: without-title 

.. seealso:: **Model location in AMMR:** 

  :menuselection:`Application --> Examples --> FemoralTorsion -->
  StandingModel.Main.any` 


The tool was developed by Enrico De Pieri, from the University of Basel
Children’s Hospital (UKBB), and Morten E. Lund, from AnyBody Technology A/S.

This tool was made to generate personalized models that account for
subject-specific values of femoral torsion, and investigate the effect of
torsional alignment on hip loading. This work is published in 'Frontiers in
Bioengineering and Biotechnology' [DFLM21]_. Please cite this article when using
this tool. 


.. figure:: /Applications/Orthopedics_and_rehab/femoral-torsion.png
   :align: center

   The tool works by adding a 8 control points around the hip center and knee
   center, which control a RBF scale function. The control points are scaled
   with the default model scaling, while the femoral torsion is added on top.

.. figure:: /Applications/Orthopedics_and_rehab/femoral-torsion_2.png
   :align: center

   The origin and insertion points of the muscles follow the morphed femoral
   geometry.


The model tool is a simple include file located in the model repository. It can
be included in any model using the following code:

.. code-block:: AnyScriptDoc

  // The femoral torsion tool expects the following variables to be defined
  Main.HumanModel.Anthropometrics = {
     AnyVar FemoralTorsionRight = 20;
     AnyVar FemoralTorsionLeft = 20;
  };

  // This line must be included before the "HumanModel". 
  #include "<ANYBODY_PATH_MODELUTILS>/FemoralTorsion/Include.any""


.. note:: This tool takes as input the nominal value of femoral torsion that is
   to be expected in the final morphed model. It automatically subtracts the
   torsional value of the original model’s femoral geometry and introduces a twist
   in the transversal plane according to the difference between the two values. The
   femoral torsion in the geometry of the unscaled (TLEM 2.0 cadaver) model is
   approximately 3.5 degrees, so setting the femoral torsion to 3.5 degrees will
   not modify the model. In the original publication, a slightly different
   definition of joint axes for the calculation of torsion in the unscaled model
   was used, leading to a value of 5.5 degrees. The adjusted value does not alter
   the functionality of this tool nor the conclusions of the afore-mentioned
   publication.

The Femoral torsion tool uses a functionality override scaling for thigh segments. In this case
the include file sets ``#define CUSTOM_SCALING_Right_Thigh`` and ``#define
CUSTOM_SCALING_Left_Thigh`` to override the default scaling for the right/left
thigh. 

.. seealso:: See the :doc:`scaling tutorial <tutorials:Scaling/lesson4>` for
   more information on how to use the custom scaling functionality in the
   general case. 


References
-----------------------

.. [DFLM21] De Pieri E, Friesenbichler B, List R, Monn S, Casartelli NC, Leunig
   M, Ferguson SJ. Subject-Specific Modeling of Femoral Torsion Influences the
   Prediction of Hip Loading During Gait in Asymptomatic Adults. Front Bioeng
   Biotechnol. 2021;9: 679360. doi:`10.3389/fbioe.2021.679360
   <https://doi.org/10.3389/fbioe.2021.679360>`__



"""
import sys
sys.path.insert(0, '../../exts')
import gallery

gallery.plot("../images/FemoralTorsion.jpg")
gallery.show()

