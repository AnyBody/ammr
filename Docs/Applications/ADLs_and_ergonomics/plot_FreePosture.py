# -*- coding: utf-8 -*-
r"""
Free posture Models
===============================

A basic static full-body model standing on a floor.

"""

import matplotlib.pyplot as plt
import matplotlib.image as mimg

image = mimg.imread("../images/FreePostureFullBodyStatic.jpg")
plt.axis('off')
plt.imshow(image)
plt.show()