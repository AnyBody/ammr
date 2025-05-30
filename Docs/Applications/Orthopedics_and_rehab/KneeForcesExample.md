---
gallery_title: "Simple Knee force estimation"
gallery_image: "/Applications/images/KneeForceExample.webp"
---

(sphx_glr_auto_examples_Orthopedics_and_rehab_plot_KneeForcesExample.py)=
(example_knee_forces_estimate)=
# Knee forces example


````{sidebar} **Example**
<img src="/Applications/images/KneeForceExample.webp" width="70%" align="center">
````

Example of calculating the medial/lateral knee force from the total force and moment.

Most musculoskeletal models uses a simplified knee joint (revolute joint). But we can still estimate
what the medial and lateral femoral condyle contact forces are on the tibial plateau.


:::{caution}
The medial and lateral knee forces calculated here are only crude
estimate for the actual knee condyle contact force.
:::

This example shows how to find the knee reaction forces and moments and decompose them into
two equivalent forces which represent the medial and lateral knee force components acting from the
femur to the tibial tray.

:::{figure} /Applications/Orthopedics_and_rehab/knee_forces.svg
:align: center
:width: 50%
:::

The vertical knee force with regards to the shank and the knee moment in the
shank frontal plane is decomposed into a lateral and medial force component.
These forces can be thought as a representation of the knee condyle forces on
the tibial plateau.

The figure above shows the concept. The relationship between the forces and moment can be expressed as:

$$
F_{total} = F_{med} + F_{lat}

M_{total}= F_{med}\cdot  l_{med} - F_{lat}\cdot l_{lat}
$$

From the above equations we can find the medial and lateral knee forces:

$$
F_{lat} = \left( F_{total}\cdot l_{med} - M_{total} \right) / \left( l_{lat} + l_{med} \right)

F_{med} = F_{total} - F_{lat}
$$

The model shows how this can be added to any model and walks through the AnyScript code.

> :::{figure} /Applications/Orthopedics_and_rehab/KneeForces2.png
> :align: center
> :width: 50%
> :::