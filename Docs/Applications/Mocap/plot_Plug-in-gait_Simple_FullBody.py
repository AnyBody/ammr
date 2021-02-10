# -*- coding: utf-8 -*-
r"""
Simple Full body model
===============================

Example of full body MoCap model using the Plug-in-Gait marker protocol, and
walking on three typ4 force platforms. The model is fairly simple and a good
starting point for new users. If you plan to have many trials/subjects, take
a look at the example which better support multiple trails.

.. rst-class:: without-title
.. seealso:: **Main file location in AMMR:** 


  :anylink-ammr:`Application/MocapExamples/Plug-in-gait_Simple/FullBody.main.any`


"""


import sys
sys.path.insert(0, '../../exts')
import gallery

# dummy call to categorize as certain 
# type for back referencing.
gallery.anymocap()


gallery.plot("../images/Plug-in-gait_Main.jpg")
gallery.show()

