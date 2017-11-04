# -*- coding: utf-8 -*-
r"""
Pedel demo
===============================

A leg pressing down a pedal. This
demonstrates conditional contact between the foot and the
pedal.

"""

import matplotlib.pyplot as plt
import matplotlib.image as mimg

image = mimg.imread("../images/PedalDemoConditional.jpg")
plt.axis('off')
plt.imshow(image)
plt.show()