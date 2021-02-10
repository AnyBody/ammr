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

* Offset to forceplates:  :anylink-ammr:`📂 <Application/MocapExamples/SpecialFeatures/ForcePlateSurfaceOffset.main.any>`

* Individual cutoff frequencies for markers: :anylink-ammr:`📂 <Application/MocapExamples/SpecialFeatures/IndividualMarkerCutoffFrequency.main.any>`

* Normalization with respect to gait cycle events: :anylink-ammr:`📂 <Application/MocapExamples/SpecialFeatures/GaitCycleNormalization.main.any>`

* Using time-varying weight for markers: :anylink-ammr:`📂 <Application/MocapExamples/SpecialFeatures/MarkerWeightsExample.main.any>`

"""
import sys
sys.path.insert(0, '../../exts')
import gallery

# dummy call to categorize as certain 
# type for back referencing.
gallery.anymocap()

gallery.plot("../images/force_plate_offset.jpg")
gallery.show()