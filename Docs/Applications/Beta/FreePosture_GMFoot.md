---
gallery_title: "Free posture with GM Foot"
gallery_image: "/Applications/images/FreePostureFullBodyStatic_GMFoot.webp"
---

(sphx-glr-auto-examples-adls-and-ergonomics-plot-freeposturegmfoot-py)=
(example_freeposture_gmfoot)=
# Free posture model with GM Foot


````{sidebar} **Example**
<img src="/Applications/images/FreePostureFullBodyStatic_GMFoot.webp" width="70%" align="center">

````

This is a variant of the {ref}`Free Posture model <example_freeposture>`
showing how to include the {ref}`GM foot model <GM Foot Model>` in the human model.


```{admonition} **Main file location in AMMR:**
:class: seealso
{menuselection}`Application --> Beta --> FreePostureGMFoot --> 
FreePostureFullBodyStaticGMFoot.Main.any`

```

The GM foot model can be enabled through a BM statement in one of the 
three configurations.

```AnyScriptDoc
Main = {

   // Add body model configuration. E.g.
   #define BM_FOOT_MODEL _FOOT_MODEL_TOE_FLEX_GM_
   // possible options:
   // #define BM_FOOT_MODEL _FOOT_MODEL_RIGID_GM_
   // #define BM_FOOT_MODEL _FOOT_MODEL_DETAILED_GM_
};
```
Additionally, foot muscles can be confiugred via a dedicated BM statement for the foot muscles.

:::{seealso}
:class: seealso
The {doc}`Foot configuration parameters <../../../bm_config/foot>` for a
full list of configuration parameters.
:::