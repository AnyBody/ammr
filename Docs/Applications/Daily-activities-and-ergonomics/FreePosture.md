---
gallery_title: "Free posture"
gallery_image: "/Applications/images/FreePostureFullBodyShoulderRhythmStatic.webp"
---

(sphx-glr-auto-examples-adls-and-ergonomics-plot-freeposture-py)=
(example_freeposture)=
# Free posture Models

````{div} margin sd-text-center
<img src="/Applications/images/FreePostureFullBodyShoulderRhythmStatic.webp" width="100%" align="center">

{anylink-button}`Application/Examples/FreePosture/FreePostureFullBodyMove.main.any`

````

A basic static full-body model standing on a floor.


This model uses the full body model, i.e. most of the body parts available
in the AAUHuman part of the Body directory. The model is grounded at the
pelvis and the posture if the model is controlled through a `mannequin.any`
file by means of joint angles.

:::{admonition} In Model Repository:
:class: seealso

{anylink-file}`Application/Examples/FreePosture/FreePostureFullBodyMove.Main.any`

{anylink-file}`Application/Examples/FreePosture/FreePostureFullBodyShoulderRhythmMove.Main.any`

{anylink-file}`Application/Examples/FreePosture/FreePostureFullBodyShoulderRhythmStatic.Main.any`

{anylink-file}`Application/Examples/FreePosture/FreePostureFullBodyShoulderRhythmStatic.Main.any`
:::

This application is a starting point for new applications involving the entire body.The model do not contain muscles and is only intended for running kinematic analysis

The model has several configurations which can be changed in the file `Config.any`

BodyModelSelection can be either "FullBodyModel"  or "FullBodySRHand"
FullBodyModel is a fullbody model
FullBodyModelSRHand is a fullbody model with a detailed hand and shoulder rhythm

CONFIGURATION2 can be either "FreePostureStatic" or "FreePostureMove"
FreePostureStatic is a static model which do not move its joint angles are controlled in the "mannequin.any" file
FreePostureMove is a dynamic model controlled through angles which can be set in the "MannequinInterpolation.any" file
