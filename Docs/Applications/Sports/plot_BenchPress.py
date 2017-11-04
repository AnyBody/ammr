# -*- coding: utf-8 -*-
r"""
Bench Press
===============================

A full-body model doing push-ups with assumed drivers.


"""

import matplotlib.pyplot as plt
import matplotlib.image as mimg

image = mimg.imread("../images/BenchPress.jpg")
plt.axis('off')
plt.imshow(image)
plt.show()