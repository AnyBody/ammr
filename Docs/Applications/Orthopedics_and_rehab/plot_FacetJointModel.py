# -*- coding: utf-8 -*-
r"""
Facet Joint Model
===============================

A spine model with facet joints.

**Main file:** :file:`Application/Examples/FacetJointModel/FacetJointModel.main.any`

This model presents a methodology for implementation of facet joints in the
lumbar spine model developed by De Zee et al. (2007: J Biomech. 40, 1219-1227).
It enables the facet joint forces to become part of a redundant system of
equilibrium equations for the entire system including the muscles. This
redundant system is subsequently solved uniquely thereby making it possible to
analyze the effect of whole body movements and loads on facet joint loading for
the whole lumbar spine together with its muscles.
 
More details can also be found in the webcast
"Implementation of facet joints in a lumbar spine model (Mark de Zee, 25. September, 2008)" 
it can be found at http://www.anybodytech.com
 
.. note:: For dynamic situation this model should be used with care since the facet 
    joint forces in this situation may add energy to the mechanical system.


"""

import matplotlib.pyplot as plt
import matplotlib.image as mimg

image = mimg.imread("../images/FacetJointModel.jpg")
plt.axis('off')
plt.imshow(image)
plt.show()