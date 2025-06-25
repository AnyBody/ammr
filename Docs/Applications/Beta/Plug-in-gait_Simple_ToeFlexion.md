---
gallery_title: "C3D driven models with Toe Flexion"
gallery_image: "/Applications/images/Plug-in-gait_simple_lowerbody_ToeFlex_GM.webp"
---

(sphx_glr_auto_examples_Mocap_plot_Plug-in-gait_Simple_LowerExtremity_ToeFlexion)=

# C3D driven models with Toe Flexion


````{sidebar} **Example**
<img src="/Applications/images/Plug-in-gait_simple_lowerbody_ToeFlex_GM.webp" width="70%" align="center">
````

These are variants of the {ref}`Simple Lower extremity <sphx_glr_auto_examples_Mocap_plot_Plug-in-gait_Simple_LowerExtremity>`
and {ref}`Simple Full Body <sphx_glr_auto_examples_Mocap_plot_Plug-in-gait_Simple_FullBody.py>`
models, showing toe flexion. These models show how the RotationPenetrationCombiDriver class
template can be used to bend toes even without measured data. This class template
ensures that toes bend to prevent penetration with the ground at toe-off, while they
stay in the neutral posture otherwise.

<!-- See https://sphinxcontrib-video.readthedocs.io/en/latest/quickstart.html -->
:::{video} ../../body/_static/FootGaitNormal_1_ToeFlex_GM.webm
:autoplay:
:loop:
:muted:
:width: 45%
:align: center
:nocontrols:
:controlslist: nofullscreen

:::

:::{seealso}
**Main file location in AMMR:**

{menuselection}`Application --> Beta --> Plug-in-gait_Simple_ToeFlex_GM -->
LowerExtremity.main.any`

{menuselection}`Application --> Beta --> Plug-in-gait_Simple_ToeFlex_GM -->
FullBody.main.any`
:::

If you have measured motion for the toes, for example, with a toe marker, you can instead use the marker to drive the bending
of toes. See the {ref}`BVH driven model with Toe Flexion <example_mocap_bvh_toe_flexion>`.
