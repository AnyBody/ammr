# -*- coding: utf-8 -*-
r"""
AnyMoCap Features
===============================

A collection of small models that show-off special features of the
*AnyMoCap* framework.


.. rst-class:: without-title
.. seealso:: **Model location in AMMR:** 

  :menuselection:`Application --> MocapExamples --> SpecialFeatures -->`

This includes:

* Offset to forceplates.
* Individual cutoff frequencies for markers.
* Normalization with respect to gait cycle events
* Using time-varying weight for markers
* Much more.

"""
import sys
sys.path.insert(0, '../../exts')
import gallery

# dummy call to categorize as certain 
# type for back referencing.
gallery.anymocap()

gallery.plot("../images/force_plate_offset.jpg")
gallery.show()