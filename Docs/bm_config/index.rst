.. _bm-config:

Configuring the Body Model
===========================

The body model can be configured in multiple ways. This include what limb
segments are include, the type of muscles, scaling etc.

.. note:: To easily configure the body model, you can also use the 
    :doc:`/bm_config/bm_plugin`.

All these choises are controlled through a number of switches called Body Model
(BM) parameters. BM parameters are always prefixed with ``BM_`` and written in
uppercase.

.. rubric:: Simple example

The example below configures a model with no arms and enables the 3-element Hill
muscles model on the legs. 

.. code-block:: AnyScriptDoc
    :emphasize-lines: 1-3

    #define BM_ARM_LEFT OFF
    #define BM_ARM_RIGHT OFF
    #define BM_LEG_MUSCLES_BOTH _MUSCLES_3E_HILL_

    // Now include the HumanModel
    #include "<ANYBODY_PATH_BODY>\HumanModel.any"


.. note:: Some parameters have simple :ammr:bm_constant:`ON`/:ammr:bm_constant:`OFF`
    options, while others have more options. 

The next section shows an overview of what BM statements are available for the different body parts.


.. rubric:: BM parameters

There are body model parameters for configuring each body part, controlling scaling, controlling the default
mannequin drivers (click to see tutorial on :ref:`modelling from scratch <MannequinDriver>`), as well as other global options for the model. 

See the following links for details on BM parameters related to different body parts and modelling options:

.. toctree::
    :maxdepth: 1

    leg
    arm
    trunk
    mannequin
    scaling
    joint_type
    other
    bm_plugin

.. 
    Here is an example for the :ammr:bm_statement:`BM_LEG_MUSCLES_BOTH` parameter:

    .. admonition:: BM parameter options.

        .. ammr:bm_statement:: BM_LEG_MUSCLES_BOTH
            :noindex:

            Parameter to define muscle behavior of both right and left leg

            :Default: :ammr:bm_constant:`CONST_MUSCLES_SIMPLE`
            :Example: ``#define BM_LEG_MUSCLES_BOTH CONST_MUSCLES_SIMPLE``
            :Options: - :any:`CONST_MUSCLES_NONE`: Constant to switch off muscles
                    - :any:`CONST_MUSCLES_SIMPLE`: Constant to use simple muscles
                    - :any:`CONST_MUSCLES_3E_HILL`: Constant to use 3 element Hill-type muscle


All Parameters and contants
------------------------------------

The full list of all the parameter and their options is available in the links below:


.. toctree::
    :maxdepth: 1

    bm_statements
    bm_constants