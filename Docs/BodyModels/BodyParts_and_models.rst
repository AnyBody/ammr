The Body Models
===============

Each body part is implemented utilizing data from detailed cadaver/anatomy
studies, thus ensuring high accuracy and anatomical fidelity. 

See the section below for a more detailed description of the models and the underlying anatomical data.


.. rst-class:: html-toggle

Background
----------------------

The body models live in the ``Body/`` subfolder within your AMMR directory. The folder names and organization here depend on
the origin of the models. 

By far the most important folder is the ``Body/AAUHuman``, which
contains the AnyBody full body model. It was originally developed at Aalborg
University, Denmark (with the acronym AAU) but also consists of body-parts (trunk
and extremities) that were either developed elsewhere or based on data sets
from elsewhere. 

Two mandible models have also been developed but are yet to be assembled with
the AAUHuman. These two mandible models can be found in ``Body/Mandible`` 

The ``Body/Beta`` folder contains less developed and tested models.

The different body parts included in the full body model are derived from
various anatomical databases from literature. The full body model
contains shoulder/arm, trunk, foot and multiple leg models
which can be assembled into the full human in many combinations. 

.. note:: Parts of the AAUHuman (except the
    mandible) are by default assembled together into a full body model.
    See :doc:`/BM_Config/HumanBody_configurations` for re-configuring the model to for example, only represent the trunk, or use a different leg/muscle model.
    

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

Lower extremity models 
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