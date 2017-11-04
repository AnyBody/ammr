# -*- coding: utf-8 -*-
r"""
Seated Human
===============================

A model of a seated human consisting of the full body model, a chair, and an
interface between the two.

"""

import matplotlib.pyplot as plt
import matplotlib.image as mimg

image = mimg.imread("../images/SeatedHuman.jpg")
plt.axis('off')
plt.imshow(image)
plt.show()