# -*- coding: utf-8 -*-
r"""
Optimize BVH Origin example
===============================

Example of a MoCap model using data from an inertial motion capture suit.
The model uses a BVH file with data from an Xsens suit. The ground reaction
forces are predicted using the GRF prediction algorithm.


.. rst-class:: without-title
.. seealso:: **Main file Example:** 

  :menuselection:`Application --> MocapExamples --> BVH_Xsens_OptimizeOrigin --> Subjects --> S1 --> S01_Trial01 --> Main.any`

This particular example demonstrates a class template that can be used to optimize the origin of the 
BVH recording. The class template can be useful when BVH recordings consist of interaction of the subject
with environment objects. In such trials, it can be hard to locate the environment object relative to 
the subject. The origin of the BVH model (recording) can be set to another position and orientation with
respect to the Global Ref. This class template can optimize the origin of the BVH model such that a 
target segment of the human model (Left/Right Foot/Hand) hits a known position and orientation in a
given time interval while following the recorded motion from the trial.

Normally, in BVH models, AnyBody automatically calculates the virtual markers positions, and the model is scaled directly from
the size of the BVH stick figure. Hence the model contains no *Parameter identification* step to find the parameters.
In this model for optimizing the origin, the parameter identification step must be run manually prior 
to running the model.

Updating old (ammr < 2.2.3) BVH based models
-------------------------------------------------

The safest approach is to reimplement your model based on the newest BVH example and AMMR v.2.3. 

However, it is also possible to change a few files in existing models to utilize the 
new BVH improvements in AnyBody v.7.3. 

1.  **Important**: Make sure your use the new AMMR (>=2.3) and new AnyBody Modeling System (>=7.3).
    You can copy your existing model folder into the new AMMR, or edit the local ``libdef.any`` file to point to the new AMMR.


"""
import sys
sys.path.insert(0, '../../exts')
import gallery

# dummy call to categorize as certain 
# type for back referencing.
gallery.anymocap()


gallery.plot("../images/BVH_OptimizeOrigin.jpg")
gallery.show()