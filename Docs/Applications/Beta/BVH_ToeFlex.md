---
gallery_title: "BVH driven model with Toe Flexion"
gallery_image: "/Applications/images/BVH_ToeFlex_GM.webp"
---

(sphx_glr_auto_examples_Mocap_plot_BVH_toe_flexion.py)=
(example_mocap_bvh_toe_flexion)=
# BVH driven model with Toe Flexion

````{sidebar} **Example**
<img src="/Applications/images/BVH_ToeFlex_GM.webp" width="70%" align="center">

````

This model is a variant of the {ref}`Inertial MoCap (Xsens) example <example_mocap_Bvh>` and
demonstrates toe flexion.

:::{admonition} **Main file location in AMMR:**
:class: see-also

  {menuselection}`Application --> Beta --> BVH_Xsens_ToeFlex_GM --> Subjects --> S1 --> S01_Trial01 --> Main.any`
:::


In this example, the left and right foot are treated differently for the user to see the different
options for toe flexion. The left foot uses the measured motion data to drive the bending of
the toes, while the right foot uses the RotationPenetrationCombiDriver class template to keep the
toes in the neutral position normally and bend them to prevent the penetration between toes and ground.

