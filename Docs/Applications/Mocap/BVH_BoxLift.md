---
gallery_title: "BVH driven box lift"
gallery_image: "/Applications/images/BVH_BoxLift.jpg"
---

(sphx_glr_auto_examples_Mocap_plot_BVH_BoxLift.py)=

# BVH driven box lift example


````{sidebar}
<img src="/Applications/images/BVH_BoxLift.jpg" width="70%" align="center">
````


Example of a MoCap model using data from an inertial measurement unit (IMU) based suit.
The model uses a BVH file with data from an Xsens suit. The ground reaction forces are
predicted using the GRF prediction algorithm.


```{admonition} **Main file Example:**
:class: seealso
{menuselection}`Application --> MocapExamples --> BVH_BoxLift --> Subjects --> S01 -->
S01_T01 --> Main.any`
```

The model works using virtual markers placed on the BVH rig (i.e. the stick-figure model
specified by the BVH file). The virtual markers are used to make the Musculoskeletal model
moved similar to marker based MoCap models.

AnyBody automatically calculates the virtual markers positions, and the model is scaled
directly from the size of the BVH stick figure. Hence the model contains no *Parameter
identification* step to find the parameters. The remaining parts of the model are equivalent to other
{ref}`MoCap model <anymocap>`  based on C3D files.

This particular example shows how to model a box which connects to the hand segments.
This is useful when investigation the effects of interaction with environment objects
even when there is no kinematic data for that object.

## Updating old (ammr \< 2.2.3) BVH based models

The safest approach is to reimplement your model based on the newest BVH example and AMMR
v.2.3.

However, it is also possible to change a few files in existing models to utilize the new
BVH improvements in AnyBody v.7.3.

1. **Important**: Make sure your use the new AMMR (>=2.3) and new AnyBody Modeling System
   (>=7.3). You can copy your existing model folder into the new AMMR, or edit the local
   `libdef.any` file to point to the new AMMR.


