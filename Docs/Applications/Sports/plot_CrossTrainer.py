# -*- coding: utf-8 -*-
r"""
Cross Trainer 
===============================

This model is based on a SolidWorks CAD model of a cross trainer fitness machine
extended with the human.This model is also the subject of the AnyBody Tutorial
called "Making Models using SolidWorks".


"""

import matplotlib.pyplot as plt
import matplotlib.image as mimg

image = mimg.imread("../images/CrossTrainer.jpg")
plt.axis('off')
plt.imshow(image)
plt.show()