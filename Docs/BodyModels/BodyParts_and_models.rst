The Body Models
===============

Each body part is implemented utilizing data from detailed cadaveric/anatomic
studies ensuring high accuracy and anatomical fidelity. 

See the section below for a more detailed description of the models and the data behind.


.. rst-class:: html-toggle

Background (tl;dr)
----------------------

The body model live in the ``Body/`` subfolder. Here you find body model collections. 
The folder names and organization here
is historical depending on the origin of the models. By far the more important
is the AAUHuman, which contains the AnyBody full body model. It was originally
developed at Aalborg University, Denmark (with the acronym AAU) but it consists
of body-parts (trunk and extremities), which are either developed elsewhere or
based on data sets from elsewhere. At Århus University, Denmark, a mandible
model was developed, but so far never assembled with the AAUHuman. This is still
found in its original location the AUHuman folder. The Beta section contains
less developed and tested models.


The different body parts from the full body model are derived from
various anatomical databases from literature. The full body model
contains a mandible, shoulder/arm, different leg, trunk and foot models
that can run in several possible combinations. Please notice that all
parts of the AAUHuman (i.e., all parts except the mandible) are
connected, so they together form a quite complete full body model.

.. warning:: In most cases, it is not necessary (and not
    recommended) to edit the files in the ``Body/`` subfolder in the AMMR.
    Most changes can done in the application. 


Upper body models
----------.-------

.. toctree::
    :maxdepth: 1

    Shoulder-arm_model
    Lumbar-spine_model
    Cervical-spine_model
    Detailed-hand_model
    Thoracic_model

Lower extremity Models 
-----------------------
.. toctree::
    :maxdepth: 1

    Leg_model
    Leg-TLEM_model
    Leg-TLEM2_model


Other models
-----------------

.. toctree::
    :maxdepth: 1

    Mandible_model
    MandibleAAU_model