# -*- coding: utf-8 -*-
r"""
Bike Model 
===============================

Bicycle rider model that runs either as
FullBody or as LowerExtremity version.


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