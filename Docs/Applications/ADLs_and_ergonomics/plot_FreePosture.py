# -*- coding: utf-8 -*-
r"""
Free posture Models
===============================

A basic static full-body model standing on a floor.

**Main files:** 

* :file:`Application/Examples/FreePosture/FreePostureFullBodyMove.Main.any`
* :file:`Application/Examples/FreePosture/FreePostureFullBodyShoulderRhythmMove.Main.any`
* :file:`Application/Examples/FreePosture/FreePostureFullBodyShoulderRhythmStatic.Main.any`
* :file:`Application/Examples/FreePosture/FreePostureFullBodyStatic.Main.any`

This model uses the full body model, i.e. most of the body parts available
in the AAUHuman part of the Body directory. The model is grounded at the
pelvis and the posture if the model is controlled through a `mannequin.any`
file by means of joint angles.

This application is a really good starting point for new applications 
involving the entire body.

The model do not contain muscles and is only intended for running kinematic analysis

The model has several configurations which can be changed in the file `Config.any`

BodyModelSelection can be either "FullBodyModel"  or "FullBodySRHand" 
FullBodyModel is a fullbody model
FullBodyModelSRHand is a fullbody model with a detailed hand and shoulder rhythm

CONFIGURATION2 can be either "FreePostureStatic" or "FreePostureMove"
FreePostureStatic is a static model which do not move its joint angles are controlled in the "mannequin.any" file 
FreePostureMove is a dynamic model controlled through angles which can be set in the "MannequinInterpolation.any" file


"""

import matplotlib.pyplot as plt
import matplotlib.image as mimg

image = mimg.imread("../images/FreePostureFullBodyStatic.jpg")
plt.axis('off')
plt.imshow(image)
plt.show()