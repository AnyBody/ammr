---
gallery_title: "Evaluate joint strength"
gallery_image: "/Applications/images/EvaluateJointStrength.webp"
---

(sphx_glr_auto_examples_Validation_plot_EvaluateJointStrength.py)=
(example_evaluate_joint_strength)=
# Evaluate joint strength

````{sidebar} **Example**
<img src="/Applications/images/EvaluateJointStrength.webp" width="70%" align="center">
````


This model shows how to enable the built-in studies to evaluate joint strength.
The studies can be enabled by setting the switch: `#define EVALUATE_JOINT_STRENGTH 1`

The studies will appear in the `HumanModel.EvaluateJointStrength`
folder.

:::{figure} /Applications/Validation/EvalJointStrength_model_tree.png
:align: center
:::

There are currently only joint strength studies for the arm model and the Leg models.

:::{note}
This  will include a lot of studies (two per DOF) so they will
affect perfomance when loading and switching between tabs/operations.
:::



:::{seealso}
**Main file location in AMMR:**

{menuselection}`Application --> Validation --> EvaluateJointStrength --> EvaluateJointStrength.main.any`
:::
