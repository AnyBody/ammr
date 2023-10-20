---
gallery_title: "Seated Human"
gallery_image: "/Applications/images/SeatedHuman.webp"
---

(sphx-glr-auto-examples-adls-and-ergonomics-plot-seatedhuman-py)=
(example_seatedhuman)=
# Seated Human


````{sidebar} **Example**
<img src="/Applications/images/SeatedHuman.webp" width="70%" align="center">

````

A model of a seated human consisting of the full body model, a chair, and an
interface between the two.


:::{seealso}
**Main file location in AMMR:**

{menuselection}`Application --> Examples --> SeatedHuman -->
SeatedHuman.Main.any`
:::

The Seated Human is a family of models resulting from a
research project involving the furniture industry. This
model is a human sitting in a generic chair where the seat,
backrest, arm rests, foot rest and head rest can be adjusted
and their influence on the forces in the human body can be
investigated.

:::{note}
The contact conditions are conditional with
respect to the distance between the body and the surface
in question so that they are only active when the contact
pair is close to each other.
:::

The contact between the human body and the chair is by means
of contact elements that can only provide compression and
friction but no tension. The available friction is proportional
to the normal force and the user can supply a friction
coefficient for each surface such that the effect of different
surface fabrics can be investigated.

