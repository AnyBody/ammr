---
gallery_title: "Standing Model"
gallery_image: "/Applications/images/StandingLift.jpg"
---

(sphx_glr_auto_examples_ADLs_and_ergonomics_plot_StandingLift.py)=
(example_standinglift)=
# Lifting Model

````{sidebar}
<img src="/Applications/images/StandingLift.jpg" width="70%" align="center">

````

Standing body model lifting a box.

:::{seealso}
**Main files location in AMMR:**

{menuselection}`Application --> Examples --> StandingLift -->`

{menuselection}`StandingLift.Main.any` /
{menuselection}`StandingLiftFEA.Main.any`
:::

This application can be a good starting point for new applications involving
the entire body, doing lifts from a standing posture. The model uses artificial
muscles between the feet and the floor for creating non-sticking boundary conditions.
Similarly there are non-sticking boundary conditions between the hands and the box.
The drivers for the model are listed in the file "JointsAndDrivers.any".

Please note that this model can also output computed forces to be used by FEA. It is also
used by FEA tutorial.


