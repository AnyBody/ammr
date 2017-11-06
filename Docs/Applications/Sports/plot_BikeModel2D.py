# -*- coding: utf-8 -*-
r"""
Bike Model 2D
===============================

A simple bicycle rider model using a planar
leg model.

**Main file:** :file:`Application/Examples/BikeModel2D/BikeModel2D.main.any`


Although this model can be rotated in 3-D space it really is just a saggital
plane pedaling model with only a few muscles in each leg. The beauty of 
pedaling is that it is one of the few cases of biomechanics that can be modeled
reasonably on two dimensions only. 

The 2-D legs are supplemented with models of the bike frame, crank, and
wheels.

You can do lots of interesting stuff with this model:

- Investigate the influence of the bicycle design
- Change riding parameters sich as cadence and output power
- Separate internal work for acceleraton of body segments

from external work on the crank.


"""

import matplotlib.pyplot as plt
import matplotlib.image as mimg

image = mimg.imread("../images/BikeModel2D.jpg")
plt.axis('off')
plt.imshow(image)

plt.show()