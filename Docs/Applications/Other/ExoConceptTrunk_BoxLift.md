---
gallery_title: "Trunk exoskeleton model"
gallery_image: "/Applications/images/ExoConceptTrunk_BoxLift.webp"
---

(sphx_glr_auto_examples_Other_plot_ExoConceptTrunk_BoxLift.py)=
(example_exo_concept_trunk)=
# Trunk exoskeleton concept model


````{div} margin sd-text-center
<img src="/Applications/images/ExoConceptTrunk_BoxLift.webp" width="100%" align="center">

{anylink-button}`Application/Examples/ExoskeletonTrunk/ExoConceptTrunk_BoxLift.main.any`
````

Trunk exoskeleton concept model.

This simple example shows how the effects of an exoskeleton can be investigated by applying assistive torque
directly at the human joints.

:::{admonition} In Model Repository:
:class: seealso

{anylink-file}`Application/Examples/ExoskeletonTrunk/ExoConceptTrunk_BoxLift.main.any`

:::

The model points to the existing {ref}`BVH Box Lift model <example_bvh_boxlift>` in the AMMR and implements
the trunk exoskeleton concept. In this example, a spring force is applied at the pelvis-thorax extension measure of the body model.
