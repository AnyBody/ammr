# -*- coding: utf-8 -*-
r"""
Hand cranck model
===============================

This is a model of a person turning a horizontal wheel by means of a handle.
The purpose of the model is shoulder validation.


**Main file:** :file:`Application/Examples/WheelTurn/WheelTurn.Main.any`


"""

import matplotlib.pyplot as plt
import matplotlib.image as mimg

image = mimg.imread("../images/WheelTurn.jpg")
plt.axis('off')
plt.imshow(image)
plt.show()