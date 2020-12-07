# -*- coding: utf-8 -*-
r"""
Lifting Model
===============================

Standing body model lifting a box.

.. rst-class:: without-title
.. seealso:: **Main files location in AMMR:** 

  :menuselection:`Application --> Examples --> StandingLift -->`

  :menuselection:`StandingLift.Main.any` / 
  :menuselection:`StandingLiftFEA.Main.any`


This application can be a good starting point for new applications involving 
the entire body, doing lifts from a standing posture. The model uses artificial 
muscles between the feet and the floor for creating non-sticking boundary conditions.
Similarly there are non-sticking boundary conditions between the hands and the box.
The drivers for the model are listed in the file "JointsAndDrivers.any".

Please note that this model can also output computed forces to be used by FEA. It is also
used by FEA tutorial.


"""


import sys
sys.path.insert(0, '../../exts')
import gallery

gallery.plot("../images/StandingLift.jpg")
gallery.show()