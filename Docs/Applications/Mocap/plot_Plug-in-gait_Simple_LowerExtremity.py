# -*- coding: utf-8 -*-
r"""
Simple Lower extremity model
===============================

Example of lower body MoCap model using the Plug-in-Gait marker protocol,
and walking on three typ4 force platforms. The model is fairly simple and a
good starting point for new users. If you plan to have many trials/subjects,
take a look at the example which better support multiple trails.

``Application/MocapExamples/Plug-in-gait_Simple/LowerExtremity.main.any``

"""

import sys
sys.path.insert(0, '../../exts')
import gallery

# dummy call to categorize as certain 
# type for back referencing.
gallery.anymocap()

gallery.plot("../images/LowerExtremity-Plug-in-gait.jpg")
gallery.show()
