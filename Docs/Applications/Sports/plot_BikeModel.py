# -*- coding: utf-8 -*-
r"""
Bike Model 
===============================

Bicycle rider model that runs either as
FullBody or as LowerExtremity version.

.. rst-class:: without-title
.. seealso:: **Main file location in AMMR:** 

  :menuselection:`Application --> Examples --> BikeModel` 
  
  Two variants of the model exist:

  *  :anylink-ammr:`BikeModel-FullBody.main.any <Application/Examples/BikeModel/BikeModel-FullBody.main.any>`
  *  :anylink-ammr:`BikeModel-LowerBody.main.any <Application/Examples/BikeModel/BikeModel-LowerBody.main.any>`



The model illustrates several important topics in model 
construction:

- Block building techniques
- Include files
- Structuring of models using directories
- Modeling of an environment as a mechanism, in this case the bicycle

The human model is included as a block from the Body (BodyRepository) directory. 

The model of the bike including bike frame, crank, wheels, definition of 
crank moment etc. can be found in the include file "BikeFrameAndWheels.any".

The connections between the "human model" and the bicycle are defined in 
BikeLegConnection.any.

The model can run in two configurations FullBodyModel and LowerExtremityModel this 
can be changed in the "Config.any" file

"""

import sys
sys.path.insert(0, '../../exts')
import gallery

gallery.plot("../images/BikeModel-FullBody.jpg")
gallery.plot("../images/BikeModel-LowerBody.jpg")
gallery.show()
