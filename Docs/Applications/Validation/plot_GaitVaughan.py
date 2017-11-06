# -*- coding: utf-8 -*-
r"""
Gait Vaughan
===============================
      
Gait model based on data from the book by Vaughan et al. comparing AnyBody predicted muscle activations with
EMG measurements.

**Main file:** :file:`Application/Validation/GaitVaughan/GaitVaughan.Main.any`

"""

import matplotlib.pyplot as plt
import matplotlib.image as mimg

image = mimg.imread("../images/GaitVaughan.jpg")
plt.axis('off')
plt.imshow(image)
plt.show()