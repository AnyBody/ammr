# -*- coding: utf-8 -*-
r"""
Bench Press
===============================

A full-body model doing push-ups with assumed drivers.

**Main file:** :file:`Application/Examples/BenchPress/BenchPress.Main.any`

The model of a bench press exercise is developed from the free posture model.
The bench is simulated by reaction forces between the head, thorax, pelvis,
feet and the ground.

"""

import matplotlib.pyplot as plt
import matplotlib.image as mimg

image = mimg.imread("../images/BenchPress.jpg")
plt.axis('off')
plt.imshow(image)
plt.show()