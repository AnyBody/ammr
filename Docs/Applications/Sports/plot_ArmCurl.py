# -*- coding: utf-8 -*-
r"""
Arm curl
===============================

Example of an Arm Curl fitness machine.


"""

import matplotlib.pyplot as plt
import matplotlib.image as mimg

image = mimg.imread("../images/ArmCurl.jpg")
plt.axis('off')
plt.imshow(image)
plt.show()