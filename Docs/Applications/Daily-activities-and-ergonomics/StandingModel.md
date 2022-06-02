---
gallery_title: "Standing Model"
gallery_image: "/Applications/images/StandingModel.jpg"
---

(sphx_glr_auto_examples_ADLs_and_ergonomics_plot_StandingModel.py)=

# Standing Model

````{sidebar}
<img src="/Applications/images/StandingModel.jpg" width="70%" align="center">
````

A full-body model that which uses a center of mass drivers to keep balance and Ground Reaction Force prediction for contact with the ground.

The model has the following features which makes it a good starting point for creating new models.

- Use soft default mannequin constraints.
- Have lower weight on ankles. Thus, the ankle angle is what is primarily adjusted to balance COM over the feet.
- Use ground reaction force prediction for contact with the ground.
- Hard constraints between both feet and the ground. E.g. feet doesn't move.
- Foot hard constraints are easy to remove to customize the model.
- CoM drivers should be easy to remove.
- Easy to specify the feet position and COM position in the main file.

The model is identical to the standing model created with the  template generator in the AnyBody Modeling System.


:::{seealso}
**Main file location in AMMR:**

{menuselection}`Application --> Examples --> StandingModel --> StandingModel.Main.any`
:::

