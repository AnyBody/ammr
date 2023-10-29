---
gallery_title: "Inertial MoCap (Xsens)"
gallery_image: "/Applications/images/BVH.webp"
---

(sphx_glr_auto_examples_Mocap_plot_BVH.py)=
(example_mocap_bvh)=
# Inertial MoCap example

````{sidebar} **Example**
<img src="/Applications/images/BVH.webp" width="70%" align="center">
````

Example of a MoCap model using data from an inertial motion capture suit.
The model uses a BVH file with data from an Xsens suit. The ground reaction
forces are predicted using the GRF prediction algorithm.



:::{seealso}
**Main file Example:**

{menuselection}`Application --> MocapExamples --> BVH_Xsens --> Subjects --> S1 --> S01_Trial01 --> Main.any`
:::

The model works using virtual markers placed on the BVH rig (i.e. the stick-figure
model specified by the BVH file). The virtual markers are used to make the
Musculoskeletal model moved similar to marker based MoCap models.

AnyBody automatically calculates the virtual markers positions, and the model is scaled directly from
the size of the BVH stick figure. Hence the model contains no *Parameter identification* step to find the parameters.
The remaining parts of the model are equivalent to other {ref}`MoCap model <anymocap>`  based on C3D files.



:::{versionadded} 2.2.3 The example uses features added in v.7.2.3 of the AnyBody Modeling system. It fixes the problems which can occur in some BVH files due to gimbal locks and multiple solutions ($N2\pi$) to the euler angle equations. See the section below on how to update old examples.
:::


::::{dropdown} Updating old (ammr \< 2.2.3) BVH based models

The safest approach is to reimplement your model based on the newest BVH example and AMMR v.2.3.

However, it is also possible to change a few files in existing models to utilize the
new BVH improvements in AnyBody v.7.3.

:::{Important}
Make sure your use the new AMMR (>=2.3) and new AnyBody Modeling System (>=7.3).
You can copy your existing model folder into the new AMMR, or edit the local `libdef.any` file to point to the new AMMR.
:::

::::