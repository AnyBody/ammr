# -*- coding: utf-8 -*-
r"""
Mandible Models
===============================
      
Model simulating chewing and comparing 
values to measurements from de Zee et al., J. of Biomechanics 2007.


"""

import matplotlib.pyplot as plt
import matplotlib.image as mimg

image = mimg.imread("../images/MandibleChewingAndClenching.jpg")
plt.axis('off')
plt.imshow(image)
plt.show()