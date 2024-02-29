---
gallery_title: "Squat"
gallery_image: "/Applications/images/Squat.webp"
---

(sphx_glr_auto_examples_ADLs_and_ergonomics_plot_Squat.py)=
(example_squat)=
# Squat

````{sidebar} **Example**
<img src="/Applications/images/Squat.webp" width="70%" align="center">

````

This model demonstrates parameterized squating motion.

:::{admonition} **Main file location in AMMR:**
:class: see-also

  {menuselection}`Application --> Examples --> Squat --> Squat.main.any`
:::



Users can try to change different parameters of this model in the 'Input\Parameters.any' file including:

* Time periood of a squat cycle
* FPS(frames per second) for simulation
* Minimum knee flexion angle of a squat cycle (in degrees)
* Maximum knee flexion angle of a squat cycle (in degrees)
* Distance between two medial contact nodes of both feet (in meters)
* Rotation angle of both feet (in degrees)

Ground reaction force(GRF) of the human model is predicted and you can check the implementation of this GRF prediction in 'Model\Supports.any' file.

The parametric motion elements are defined in 'Model\JointsAndDrivers.any'.

