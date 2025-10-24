---
gallery_title: "C3D driven models with Toe Flexion"
gallery_image: "/Applications/images/Plug-in-gait_simple_lowerbody_ToeFlex_GM.webp"
anylink: Application/MocapExamples/Plug-in-gait_Simple/LowerExtremity_ToeFlexion.main.any
---

(sphx_glr_auto_examples_Mocap_plot_Plug-in-gait_Simple_LowerExtremity_ToeFlexion)=

# C3D driven model with Toe Flexion

:::{anylink-gallery}
:margin:
:::

This is a variant of the {ref}`Simple Lower extremity <sphx_glr_auto_examples_Mocap_plot_Plug-in-gait_Simple_LowerExtremity>`
model, showing toe flexion. The model shows how the RotationPenetrationCombiDriver class
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

If you have measured motion for the toes, for example, with a toe marker, you can instead use the marker to drive the bending
of toes. See the {ref}`BVH driven model with Toe Flexion <example_mocap_bvh_toe_flexion>`.

:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `
:::
