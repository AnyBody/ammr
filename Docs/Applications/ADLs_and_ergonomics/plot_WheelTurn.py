# -*- coding: utf-8 -*-
r"""
Hand cranck model
===============================

Model of a person operating an old-fashioned pump by hand. The model is
based on the standing model.


"""

import matplotlib.pyplot as plt
import matplotlib.image as mimg

image = mimg.imread("../images/WheelTurn.jpg")
plt.axis('off')
plt.imshow(image)
plt.show()