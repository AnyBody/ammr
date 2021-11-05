# -*- coding: utf-8 -*-
r"""
Femoral Torsion tool
=======================================

This is an example of modifying the femoral torsion using a model utility tool
included with the model repository. The  model is simple standing model where
the femoral torsion has been altered to -5 degrees. The model is also a good 
example on how a similar approach can be used for other body parts. 


.. rst-class:: without-title 

.. seealso:: **Model location in AMMR:** 

  :menuselection:`Application --> Examples --> FemoralTorsion --> StandingModel.Main.any` 


The tool was developed by Enrico De Peiri at University of Basel Children’s
Hospital as part of his work on how hip joint loadings are influenced by femoral
torsion which is published in 'Fronties in Bioengineering and Biotechnology'
[DFLM21]_. Please cite his work if you use this tool. 


.. figure:: /Applications/Orthopedics_and_rehab/femoral-torsion.png
   :align: center

   The tools works by adding a 8 control points around the hip center and knee center, which control a RBF scale function.
   The control points are scaled witht the default model scaling with the femoral torsion added on top.

The model tool is a simple include file located in the model repository. It can
be included in any model using the following code:

.. code-block:: AnyScriptDoc

  // The femoral torsion tool expects the following variables to be defined 
  Main.HumanModel.Anthropometrics = {
     AnyVar FemoralTorsionRight = -5;
     AnyVar FemoralTorsionLeft = -5;
  };
  
  // This line must be included before the "HumanModel".
  #include "<ANYBODY_PATH_MODELUTILS>/FemoralTorsion/FemoralTorsionInclude.any"


.. note:: The current tibial torsion in the unscaled (TLEM 2.0 cadaver) model
        approx. 5 degrees. So setting the femoral torsion to 5 degrees will not
        modify the model.

The tool uses a functionality override scaling for thigh segments. In this case
the include file sets ``#define CUSTOM_SCALING_Right_Thigh`` and ``#define
CUSTOM_SCALING_Left_Thigh`` to override the default scaling for the right/left
thigh. 

.. seealso:: The tool uses a functionality override scaling for thigh segments. In this case
   the include file sets ``#define CUSTOM_SCALING_Right_Thigh`` and ``#define
   CUSTOM_SCALING_Left_Thigh``. See the :doc:`scaling tutorial <tutorials:Scaling/lesson4>` for more
   information on how to use the custom scaling functionality in the general
   case. 


References
-----------------------

.. [DFLM21] De Pieri E, Friesenbichler B, List R, Monn S, Casartelli NC, Leunig
   M, et al. Subject-Specific Modeling of Femoral Torsion Influences the
   Prediction of Hip Loading During Gait in Asymptomatic Adults. Front Bioeng
   Biotechnol. 2021;9: 679360. doi:`10.3389/fbioe.2021.679360
   <https://doi.org/10.3389/fbioe.2021.679360>`__



"""

import sys
sys.path.insert(0, '../../exts')
import gallery

gallery.plot("../images/FemoralTorsion.jpg")
gallery.show()
