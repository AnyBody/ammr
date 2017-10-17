Configuring the Body Model
===========================

Configuration of the Human Model is done through a number of switches called 
Body Model (BM) parameters. BM parameters all prefixed with **BM_** and written in uppercase.

Setting the BM parameters can enable or disable body parts, 
change muscle types, or change other options. 

Simple example
--------------

The example below configures are model with no arms and enables the 3-element Hill muscles model on the legs. 

.. code-block:: AnyScriptDoc
    :emphasize-lines: 1-3

    #define BM_ARM_LEFT OFF
    #define BM_ARM_RIGHT OFF
    #define BM_LEG_MUSCLES_BOTH _MUSCLES_3E_HILL_

    // Now include the HumanModel
    #include "<ANYBODY_PATH_BODY>\HumanModel.any"


Available parameters:
---------------------------

There are body model parameters for configurating each body part, for controlling scaling, for controlling the default
mannequin drivers, as well as other global options for the model. 

See the following links for details on the different body parts:

.. toctree::
    :maxdepth: 1

    Leg_configurations
    Arm_configurations
    Trunk_configurations
    Mannequin_configurations
    Scaling_configurations
    Other_configurations

    
Some parameters have simple :ammr:bm_constant:`ON`/:ammr:bm_constant:`OFF`
options, while have more options. Here is an example for the :ammr:bm_statement:`BM_LEG_MUSCLES_BOTH` parameter:

.. admonition:: BM specification...

    .. ammr:bm_statement:: BM_LEG_MUSCLES_BOTH
        :noindex:

        Parameter to define muscle behavior of both right and left leg

        :Default: :ammr:bm_constant:`CONST_MUSCLES_SIMPLE`
        :Example: :anyscript:`#define BM_LEG_MUSCLES_BOTH CONST_MUSCLES_SIMPLE`
        :Options: - :any:`CONST_MUSCLES_NONE`: Constant to switch off muscles
                - :any:`CONST_MUSCLES_SIMPLE`: Constant to use simple muscles
                - :any:`CONST_MUSCLES_3E_HILL`: Constant to use 3 element Hill-type muscle


The full list of all the parameter and their options is available here: 

.. toctree::
    :maxdepth: 2
    :caption: All Body Model Configurations

    bm_statements
    bm_constants