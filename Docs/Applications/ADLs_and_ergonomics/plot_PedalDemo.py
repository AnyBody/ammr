# -*- coding: utf-8 -*-
r"""
Pedel demo simple
===============================

This model demonstrates the construction
of a foot pedal example.

**Main file:** :file:`Application/Examples/PedalDemo/PedalDemo.Main.any`

This model is for design of a pedal that is comfortable to use 
for a seated operator depending on the stiffness of the embedded
spring and the distance of the seat from the pedal.

"""

import matplotlib.pyplot as plt
import matplotlib.image as mimg

image = mimg.imread("../images/PedalDemo.jpg")
plt.axis('off')
plt.imshow(image)
plt.show()