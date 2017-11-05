# -*- coding: utf-8 -*-
r"""
Standing Model
===============================

A full-body model that is easy to put into specific static postures. It is
equipped with drivers on intuitive anatomical joint angle and by default without
muscles.

**Main file:** :file:`Application/Examples/StandingModel/StandingModel.Main.any`


"""

import matplotlib.pyplot as plt
import matplotlib.image as mimg

image = mimg.imread("../images/StandingModel.jpg")
plt.axis('off')
plt.imshow(image)
plt.show()