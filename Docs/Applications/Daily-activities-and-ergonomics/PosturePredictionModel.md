---
gallery_title: "Posture Prediction Model"
gallery_image: "/Applications/images/StandingPosturePredictionModel.webp"
---


(sphx_glr_auto_examples_adls_and_ergonomics_plot_PosturePredictionModel.py)=
(example_posture_prediction)=
# Posture Prediction Model


````{sidebar} **Example**
<img src="/Applications/images/StandingPosturePredictionModel.webp" width="70%" align="center">

````

This is a model which can predict the posture as a consequence of applied loads in hands.
It does this by minimizing joint torques and applying balance drivers which account for external
applied loads.


:::{seealso}
**Main file location in AMMR:**

{menuselection}`Application --> Examples --> StandingPosturePredictionWithLoad -->
StandingPosturePrediction.main.any`
:::


The model is driven by a combination of the following drivers:
: - Drivers which minimize the joint moments (arising from gravity and applied loads in hands) in elbow, shoulder, L4L5 and knee
  - Driver which tries to keep the CoP inside the foot stance area.
  - Feet maintain contact with the ground, but the position can be controlled by widgets
  - Hands are linked to an object, of which positioning can be altered using widgets


:::{figure} /Applications/images/StandingPosturePredictionModel_UpwardsForce.jpg
:align: center
:::


Two type of loads can be applied, either a fixed weight of the object and/or a force vector.

## Usage

To run the model
: - Load the model

:::{figure} /Applications/images/StandingPosturePredictionModel_UponLoading.jpg
:align: center
:::

The example model has a force vector applied on the object, currently the object has no weight (this is editable)

```AnyScriptDoc
AnyVar ObjectWeight = 0;   //weight of mass applied
```

- Try to drag (click and drag) one of the widgets in the ModelView (seen as small coordinate systems). For example the force vector widget:

:::{figure} /Applications/images/StandingPosturePredictionModel_WidgetMovement.jpg
:align: center
:::

- When the widget is release the model will run the analysis. The Force vector is shown by the blue arrow, the weight of the object is represented by a red line, and the resulting reaction force is depicted by the green arrow.

:::{figure} /Applications/images/StandingPosturePredictionModel_PickupBox.jpg
:align: center
:::

There are three remaining widgets, 2 controlling the starting position of the feet, and 1 controlling object's location.

:::{figure} /Applications/images/StandingPosturePredictionModel_FootWidgets.jpg
:align: center
:::

The model can also be adjusted to apply the load to both hands or a single hand.
Three combinations can be made using the define statements

```AnyScriptDoc
#define LoadInRightHand 1
#define LoadInLeftHand  1
```

In the following example a force vector is applied to only the right hand.

:::{figure} /Applications/images/StandingPosturePredictionModel_Onearm.jpg
:align: center
:::

The following video shows an example of how you can manipulate the multiple widgets to achieve different predictive postures:

```{raw} html
<video width="100%" style="display:block; margin: 0 auto;" controls autoplay loop>
    <source src="../../_static/StandingPosturePrediction.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>
```

**Please note the speed of the video was increased for viewing purposes.**

