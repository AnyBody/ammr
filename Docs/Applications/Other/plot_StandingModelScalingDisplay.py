# -*- coding: utf-8 -*-
r"""
Standin Model Scaling Display
===============================

This application shows all the scaling laws available.

| **Main file:** 
| ``Application/Examples/StandingModelScalingDisplay/StandingModelScalingDisplay.Main.any``

The model can be scaled either regarding to measures between joint center, 
or exteranal measures of bony tips, or by representation of a certain percentile of the population.

For further details see :doc:`the tutorial about scaling </Scaling/intro>`

"""


import sys
sys.path.insert(0, '../../exts')
import gallery

gallery.plot("../images/StandingModelScalingDisplay.jpg")
gallery.show()
