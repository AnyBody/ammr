# -*- coding: utf-8 -*-
r"""
Bergmann GH
===============================

Model simulating arm-lift motion adapted from Bergmann et al., J. of
Biomechanics 2007 to compare the results to in vivo measurements from that
study.

**Main file:** :file:`Application/Validation/BergmannGH/BergmannGH.Main.any`


"""

import matplotlib.pyplot as plt
import matplotlib.image as mimg

image = mimg.imread("../images/BergmannGH.jpg")
plt.axis('off')
plt.imshow(image)
plt.show()