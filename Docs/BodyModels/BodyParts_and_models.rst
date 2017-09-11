The Body Models
===============

The **Body** section contains necessary folders and files to assemble a
generic human body model. In most cases, it is not necessary (and not
recommended) to edit files directly in this body folder, as the models
can be modified to individual needs in your application. This section
also includes tools to connect the body model to the environment, or to
drive the model with motion capture data.

At top level in the Body section, you find body model collections. The
division here is historical depending on the origin of the models. By
far the more important is the AAUHuman, which contains the AnyBody
well-known full body model. It was originally developed at Aalborg
University, Denmark (with the acronym AAU) but it consists of body-parts
(trunk and extremities), which are either developed elsewhere or based
on data sets from elsewhere. At Århus University, Denmark, a mandible
model was developed, but so far never assembled with the AAUHuman. This
is still found in its original location the AUHuman folder. The Beta
section contains less developed and tested models.

This tutorial is focused on the human models. This lesson will give an
overview of how to use the AAUHuman and AUHuman Body Models and what can
be edited. More details on how to change the body model can be found in
various other tutorials.

The different body parts from the full body model are derived from
various anatomical databases from literature. The full body model
contains a mandible, shoulder/arm, different leg, trunk and foot models
that can run in several possible combinations. Please notice that all
parts of the AAUHuman (i.e., all parts except the mandible) are
connected, so they together form a quite complete full body model.