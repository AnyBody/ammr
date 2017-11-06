# -*- coding: utf-8 -*-
r"""
Bike Model 
===============================

Bicycle rider model that runs either as
FullBody or as LowerExtremity version.

**Main files:** 

* :file:`Application/Examples/BikeModel/BikeModel-FullBody.main.any`
* :file:`Application/Examples/BikeModel/BikeModel-LowerBody.main.any`

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

import matplotlib.pyplot as plt
import matplotlib.image as mimg

image = mimg.imread("../images/BikeModel-FullBody.jpg")
plt.axis('off')
plt.imshow(image)

plt.figure()
image = mimg.imread("../images/BikeModel-LowerBody.jpg")
plt.axis('off')
plt.imshow(image)

plt.show()