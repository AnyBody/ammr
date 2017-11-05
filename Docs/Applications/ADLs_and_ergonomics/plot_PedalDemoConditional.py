# -*- coding: utf-8 -*-
r"""
Pedel demo
===============================

A leg pressing down a pedal. This
demonstrates conditional contact between the foot and the
pedal.

**Main file:** :file:`Application/Examples/PedalDemoConditional/PedalDemoConditional.Main.any`

This model is for design of a pedal that is comfortable to use 
for a seated operator depending on the stiffness of the embedded
spring and the distance of the seat from the pedal. The model is
a copy of the PedalDemo example with the exception that this model
has conditional contact between the foot and the pedal, such that
the contact becomes active when the two elements are in proximity
with each other

"""

import matplotlib.pyplot as plt
import matplotlib.image as mimg

image = mimg.imread("../images/PedalDemoConditional.jpg")
plt.axis('off')
plt.imshow(image)
plt.show()