---
gallery_title: "Evaluate moment arms"
gallery_image: "/Applications/images/EvaluateMomentArms.jpg"
---

(sphx_glr_auto_examples_Validation_plot_EvaluateMomentArms.py)=
(example_evaluate_momentarms)=
# Evaluate moment arms

````{sidebar}
<img src="/Applications/images/EvaluateMomentArms.jpg" width="70%" align="center">
````

This model shows how to enable the built-in moment arm evaluation studies.
The studies can be enabled by setting the switch: `#define EVALUATE_MOMENT_ARMS 1`

The studies will appear in the `HumanModel.EvaluateMomentArms`
folder.

:::{figure} /Applications/Validation/EvalMomentArms_plot.png
:align: center

The figure shows the moment arms (in meters) for Iliacus and GluteusMaximus inferior) during the hip flexion.
Agonists muscles (Iliacus) have positive moment arms, and anatagonist (GluetusMaximus) have negative moment arms.
:::

:::{note}
This  will include a lot of studies (one per DOF) so they will
affect performance when loading and switching between tabs/operations.
:::



:::{seealso}
**Main file location in AMMR:**

{menuselection}`Application --> Validation --> EvaluateMomentArms --> EvaluateMomentArms.main.any`
:::
