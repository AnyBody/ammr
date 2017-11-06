# -*- coding: utf-8 -*-
r"""
Wilke Spine Disc Pressure Model
===============================
      
Several models comparing loads in the spine with in vivo measurements
during daily activities from Wilke et al., Spine 1999.

.. figure:: /Applications/Validation/wilke.svg


"""

import matplotlib.pyplot as plt
import matplotlib.image as mimg

image = mimg.imread("../images/SpinePressureLyingOnBack.jpg")
plt.axis('off')
plt.imshow(image)

plt.figure()
image = mimg.imread("../images/SpinePressureSeatingFlexedNoSupport.jpg")
plt.axis('off')
plt.imshow(image)

plt.figure()
image = mimg.imread("../images/SpinePressureSeatingRelaxed.jpg")
plt.axis('off')
plt.imshow(image)

plt.figure()
image = mimg.imread("../images/SpinePressureStandingLiftStretchedArms.jpg")
plt.axis('off')
plt.imshow(image)

plt.figure()
image = mimg.imread("../images/SpinePressureStandingLiftClose.jpg")
plt.axis('off')
plt.imshow(image)

plt.figure()
image = mimg.imread("../images/SpinePressureSeatingStraitNoSupport.jpg")
plt.axis('off')
plt.imshow(image)

plt.figure()
image = mimg.imread("../images/SpinePressureStandingLiftFlexed.jpg")
plt.axis('off')
plt.imshow(image)


plt.show()