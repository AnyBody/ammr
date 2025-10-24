---
gallery_title: "GM Foot MoCap Model"
gallery_image: "/Applications/images/Plug-in-gait_simple_lowerbody_DetailedFoot_GM.webp"
anylink: Application/Beta/Plug-in-gait_Simple_DetailedFoot_GM/LowerExtremity.main.any
---

(sphx_glr_auto_examples_Mocap_plot_Plug-in-gait_Simple_LowerExtremity_DetailedFootGM)=

# GM Foot MoCap Model

:::{anylink-gallery}
:margin:
:::

This model ports the GM Foot MoCap model from the [repository on GitHub](https://github.com/AnyBody/gm-foot)
to the AMMR. The model is updated to run with the detailed foot model that is available in the AMMR, and is
enabled by the BM Statement ```#define BM_FOOT_MODEL _FOOT_MODEL_DETAILED_GM_```

Some changes are needed to run the model as close to the original model as possible:
- Custom scaling is introduced to scale the detailed foot model back to the source foot model,
  using the same set of points that were used to interface morph the GM foot to TLEM foot.
- A new legacy reference node is created inside each foot segment so that the original marker
  protocol file can be used with minimal changes.
- Markers on the shank are adjusted slightly to account for the update in the coordinate system
  used for scaling shank in AMMR 3.0. {ref}`See this page <update_shank_marker_ammr3>`.

:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `
:::
