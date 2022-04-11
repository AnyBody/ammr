# -*- coding: utf-8 -*-
r"""
Exoskeleton concept model
===============================

Exoskeleton concept model.


.. rst-class:: without-title
.. seealso:: **Main file location in AMMR:** 

  :menuselection:`Application --> Examples --> ExoskeletonConcept --> ExoConcept_BoxLift.Main.any`

This example shows how to study different exoskeleton concepts on an activity. The model is 
based on the `webcast <https://www.anybodytech.com/simulation-driven-conceptual-design-of-exoskeletons/>` 
presented by Prof. John Rasmussen from Aalborg University on March 28, 2022.

The model points to the existing BVH Box Lift model in the AMMR and implements the different steps
described in the webcast. In this model, two different concepts can be studied: 

```{toctree}
:maxdepth: 1

Rotational springs at the knees
Extensible rods crossing the knees, hips and lumbar spine.
```
For each concept, you can apply idealized forces through AnyReacForce. The idealized
forces are like hypothetical actuators that will provide as much force as is needed by the system. This 
can be useful to study requirement of assistive force and its relation with kinematic data such as joint
angles. Subsequently, the assistive force can be implemented through springs whose characteristics
have been determined by the idealized force required at the joints.

Thus, there are four possibilities in this exoskeleton concept model:
1.  Idealized force at knees.
2.  Spring force at knees.
3.  Idealized extensible rods crossing the knees, hips and lumbar spine.
4.  Spring force-based extensible rods crossing the knees, hips and lumbar spine.
 

"""

import sys
sys.path.insert(0, '../../exts')
import gallery

gallery.plot("../images/ExoskeletonConcept_BoxLift.jpg")
gallery.show()
