# -*- coding: utf-8 -*-
r"""
Push Up
===============================

A full-body model doing push-ups with assumed drivers.


.. rst-class:: without-title
.. seealso:: **Main file location in AMMR:** 

  :menuselection:`Application --> Examples --> PushUp --> PushUp.main.any`


The model displays several topics

-Block building techniques
-Include files
-Structuring of models using directories

The positions of the hands can be controlled by chaning variables in the file
Environment.any

.. caution:: The model seems to be too weak for the load applied when doing pushups, this
  is a sign that the shoulder needs more adjustments before it becomes reliable

"""

import sys
sys.path.insert(0, '../../exts')
import gallery

gallery.plot("../images/PushUp.jpg")
gallery.show()
