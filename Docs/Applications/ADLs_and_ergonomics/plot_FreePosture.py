# -*- coding: utf-8 -*-
r"""
Free posture Models
===============================

A basic static full-body model standing on a floor.

.. rst-class:: without-title
.. seealso:: **Model location in AMMR:** 

  :menuselection:`Application --> Examples --> FreePosture -->` 

  | :menuselection:`FreePostureFullBodyMove.Main.any`
  | :menuselection:`FreePostureFullBodyShoulderRhythmMove.Main.any`
  | :menuselection:`FreePostureFullBodyShoulderRhythmStatic.Main.any`
  | :menuselection:`FreePostureFullBodyShoulderRhythmStatic.Main.any`


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

import sys
sys.path.insert(0, '../../exts')
import gallery

gallery.plot("../images/FreePostureFullBodyStatic.jpg")
gallery.show()