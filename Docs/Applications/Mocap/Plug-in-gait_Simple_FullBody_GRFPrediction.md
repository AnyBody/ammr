---
gallery_title: "GRF prediction model"
gallery_image: "/Applications/images/GRFPrediction-Plug-in-gait.jpg"
---

(sphx_glr_auto_examples_Mocap_plot_Plug-in-gait_Simple_FullBody_GRFPrediction.py)=
(example_mocap_grf_prediction)=

# Simple GRF prediction model


````{div} margin sd-text-center
<img src="/Applications/images/GRFPrediction-Plug-in-gait.jpg" width="100%" align="center">

{anylink-button}`Application/MocapExamples/Plug-in-gait_Simple/FullBody_GRFPrediction.main.any`

````

Example of full body MoCap model using the Plug-in-Gait marker protocol but
without force plates. The external forces are instead predicted using the GRF
algorithms.



:::{admonition} In Model Repository:
:class: seealso

{anylink-file}`Application/MocapExamples/Plug-in-gait_Simple/FullBody_GRFPrediction.main.any`
:::

Motion capture data is often recorded without force plates. In traditional
inverse dynamics, this would make it impossible to perform a dynamic analysis.
However, AnyBody has the possibility to predict ground reaction forces (GRF), so
you can make inverse dynamics models based on recorded motion without GRF force
measurement (Fluit et al., 2014; Jung et al., 2014).

More information is available in the {doc}`documentation for the GRF prediction </anymocap/grf-prediction>`.
