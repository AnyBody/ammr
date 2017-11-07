# -*- coding: utf-8 -*-
r"""
Inertial MoCap example
===============================

Example of a MoCap mdoel using data from a inertial motional caputure suit.
The model uses a BVH file with data from an Xsens suit. The ground reaction
forces are predicted using the GRF prediction algorithm. 
    
:file:`Application/MocapExamples/BVH/Trials/BVH01/Main.any`

"""
import sys
sys.path.insert(0, '../../exts')
import gallery

gallery.plot("../images/BVH.jpg")
gallery.show()