# -*- coding: utf-8 -*-
r"""
Wheel Chair model
===============================

A model of a person sitting in a wheelchair, the model is driven by motion
capture data.

This is a model of a person sitting in a wheelchair. The model only comprises
the upper right arm.

The model is driven using motion capture data from kindly provided by:

    Philip S. Requejo Ph.D.
    Pathokinesiology Laboratory
    Rancho Los Amigos National Rehabilitation Center

The force between the hand and the rim is also based on measurements.

"""

import matplotlib.pyplot as plt
import matplotlib.image as mimg

image = mimg.imread("../images/WheelChairRancho.jpg")
plt.axis('off')
plt.imshow(image)
plt.show()