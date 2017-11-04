# -*- coding: utf-8 -*-
r"""
Airline passenger
===============================

The airline passenger example.

This is working


"""

import matplotlib.pyplot as plt
import matplotlib.image as mimg

image = mimg.imread("../images/AirlinePassenger.jpg")
plt.axis('off')
plt.imshow(image)
plt.show()