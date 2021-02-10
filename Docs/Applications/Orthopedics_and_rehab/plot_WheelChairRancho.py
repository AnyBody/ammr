# -*- coding: utf-8 -*-
r"""
Wheel Chair model
===============================

A model of a person sitting in a wheelchair, the model is driven by motion
capture data.

.. rst-class:: without-title
.. seealso:: **Main file location in AMMR:** 

  :anylink-ammr:`Application/Examples/WheelChairRancho/WheelChairRancho.main.any`



This is a model of a person sitting in a wheelchair. The model only comprises
the upper right arm.

The model is driven using motion capture data from kindly provided by:

    Philip S. Requejo Ph.D.
    Pathokinesiology Laboratory
    Rancho Los Amigos National Rehabilitation Center

The force between the hand and the rim is also based on measurements.

"""


import sys
sys.path.insert(0, '../../exts')
import gallery

gallery.plot("../images/WheelChairRancho.jpg")
gallery.show()
