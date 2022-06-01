---
gallery_title: "Optimize BVH Origin"
gallery_image: "/Applications/images/BVH_OptimizeOrigin_Merged.jpg"
---

# Optimize BVH Origin example

Example of a MoCap model using data from an inertial motion capture suit.
The model uses a BVH file with data from an Xsens suit. The ground reaction
forces are predicted using the GRF prediction algorithm.

````{sidebar}
```{admonition} **Main file location in AMMR:**
:class: seealso
{menuselection}`Application --> MocapExamples --> BVH_Xsens_OptimizeOrigin --> Subjects --> S1 --> S01_Trial01 --> Main.any`
```
![](/Applications/images/BVH_OptimizeOrigin_Merged.jpg)
````


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

