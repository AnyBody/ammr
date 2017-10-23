The Body Models
===============

Each body part is implemented utilizing data from detailed cadaveric/anatomic
studies ensuring high accuracy and anatomical fidelity. 

See the section below for a more detailed description of the models and the data behind.


.. rst-class:: html-toggle

Background (tl;dr)
----------------------

The body model live in the ``Body/`` subfolder. Here you find body model
collections. The folder names and organization here is historical depending on
the origin of the models. 

By far the more important is the AAUHuman, which
contains the AnyBody full body model. It was originally developed at Aalborg
University, Denmark (with the acronym AAU) but it consists of body-parts (trunk
and extremities), which are either developed elsewhere or based on data sets
from elsewhere. 

Two mandible models have also been developed but has so far never assembled with
the AAUHuman. These two mandible models can be found in ``Body/Mandible`` 

The Beta section contains less developed and tested models.

The different body parts included in the full body model are derived from
various anatomical databases from literature. The full body model
contains shoulder/arm, different leg, trunk and foot models
that can run in several possible combinations. 

Please notice that all parts of the AAUHuman (i.e., all parts except the
mandible) are connected, so they together form a quite complete full body model.
See the :doc:`/BM_Config/HumanBody_configurations` for how to configure the the
different body parts into a complte model. 


.. warning:: In most cases, it is not necessary (and not
    recommended) to edit the files in the ``Body/`` subfolder in the AMMR.
    Most changes can done in the application. 


Trunk models
------------------

.. toctree::
    :maxdepth: 1

    Lumbar-spine_model
    Cervical-spine_model



Upper extremity models
-------------------------

.. toctree::
    :maxdepth: 1

    Shoulder-arm_model
    Detailed-hand_model

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