# -*- coding: utf-8 -*-
r"""
Simple GRF prediction model
===============================

Example of full body MoCap mocdel using the Plug-in-Gait marker protocol but
without force plates. The external forces are instead predicted using the GRF
algorithms.

``Application/MocapExamples/Plug-in-gait_Simple/FullBody_GRFPrediction.main.any``

"""


import sys
sys.path.insert(0, '../../exts')
import gallery

# dummy call to categorize as certain 
# type for back referencing.
gallery.anymocap()


gallery.plot("../images/GRFPrediction-Plug-in-gait.jpg")
gallery.show()