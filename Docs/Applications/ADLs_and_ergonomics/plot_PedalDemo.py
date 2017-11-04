# -*- coding: utf-8 -*-
r"""
Pedel demo simple
===============================

This model demonstrates the construction
of a foot pedal example.

"""

import matplotlib.pyplot as plt
import matplotlib.image as mimg

image = mimg.imread("../images/PedalDemo.jpg")
plt.axis('off')
plt.imshow(image)
plt.show()