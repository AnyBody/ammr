# -*- coding: utf-8 -*-
r"""
Inertial MoCap example
===============================

Example of a MoCap mdoel using data from an inertial motional caputure suit.
The model uses a BVH file with data from an Xsens suit. The ground reaction
forces are predicted using the GRF prediction algorithm.

The model works using a virtual markers placed on the BVH rig (i.e. the stick-figure
model specified by the BVH file). The virtual markers are used to make the
Musculoskeletal model moved similar to marker based mocap models.


.. versionadded:: 2.2.3
   This example is updated to fix problems with gimbal locks and multiple
   solutions (N*2*pi) to the euler angle equations of the BVH joint angles.

   The virtual marker positions are now calculated by the 
   ``AnyInputBVH`` class directly using a forward kinematics approch which circuvent
   the problems of the AnyScript implementation that used the more general inverse-kinematics
   solver. This also eliminates the step of preprocessing the BVH files to generate 
   Marker trajectories.



``Application/MocapExamples/BVH_Xsens/Trials/BVH01/Main.any``

"""
import sys
sys.path.insert(0, '../../exts')
import gallery

# dummy call to categorize as certain 
# type for back referencing.
gallery.anymocap()


gallery.plot("../images/BVH.jpg")
gallery.show()