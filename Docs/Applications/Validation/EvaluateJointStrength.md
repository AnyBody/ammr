# Evaluate joint strength

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

```{eval-rst}
.. rst-class:: without-title
```

:::{seealso}
**Main file location in AMMR:**

{menuselection}`Application --> Validation --> EvaluateJointStrength --> EvaluateJointStrength.main.any`
:::
