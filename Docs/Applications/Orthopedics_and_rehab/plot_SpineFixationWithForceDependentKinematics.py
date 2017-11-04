# -*- coding: utf-8 -*-
r"""
Spine Fixation Model using Force Dependent Kinematics
===============================

This application is an example of how to use the new force-dependent
kinematics. The force dependent kinematics allows the kinematic spine
rhythm which normally drives the vertebras to be switched entirely off.
"""

import matplotlib.pyplot as plt
import matplotlib.image as mimg

image = mimg.imread("../images/SpineFixationWithForceDependentKinematicsjpg")
plt.axis('off')
plt.imshow(image)
plt.show()