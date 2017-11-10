#########################
Getting Started with AMMR
#########################


AMMR Intallation
================


The newest version of the *AnyBody Model Repository* (AMMR) comes bundled with the 
`AnyBody Modelling System`_. This means that when you install AnyBody, the AMMR
version available at the time of its release will be installed together with it
inside the installation folder. (Morten)

.. seealso:: Detailed guide on how to install :doc:`your own version of the AMMR <AMMR_Installation>` :


.. toctree::
    :maxdepth: 1
    :hidden: 

    AMMR_Installation


.. 
..    1.. only:: draft
..
..    1.. rubric:: Before using AMMR
..

..      Before editing or create models, it is great to know how
        to track changes made along the development of your models. 
        Modelling with AnyBody makes use of `AnyScript`_ ,
        therefore version control software can be used to store the models safely in a remote
        repository for keeping them safe or for sharing them easily.

..        .. note:: If want to know more about versioning software see :doc:`this link <Before_Using>`


Understanding the AnyScript Models
==================================

Most examples you will encounter when using the AnyBody Managed Model Repository
use the `Human Model`_ . Regardless of complexity, all models share a
common `AnyScript`_ structure used to set them up:

* Path to the desired AMMR for using;
* The configuration of your human model and the inclusion of the human model
  itself;
* Model Integration: add external loads, drivers etc.;
* Model Study: this is where you set up the simulation parameters for the
  scenario in which you will use the model.

.. note:: AnyScript is a sequential language. This means that each of the instructions
    lines are executed by AnyBody in the order they are written inside the ``.any``
    files. The structure above also represents the order of the code sections
    for the models.


Path to AMMR
------------

When having multiple versions of AMMR available on your computer, you have to 
specify which one will be used by AnyBody. Each AMMR has a file called ``libdef.any``
located at the top level folder. The AnyScript line used for instructing AnyBody
which line to use should be at the very beginning of your ``.any`` file:

.. code-block:: AnyScriptDoc

    #include "path/to/AMMR/libdef.any"


Configuring the Human Model
---------------------------

The Human Body Model is configured through a number of ``#define`` and ``#path``
statements. These statements are all prefixed with ``BM_`` inside AnyScript,
and they can also be referred to as "bm-statements". The Human Body Model can
only be configured before it is included in your file. If no "bm-statements" are
found before including the Human Body Model, the default configuration will be used.

The structure of a "bm-statement" is the following: ``#define statement option``, where
"#define" is a *pre-processor directive*,  "statement" is the name of the Body Model
element you want to configure and "option" is the name of the option you want to apply.

Let us take the following simple example in which we want the Human Body Model to be
generated without limbs on the left side and using the *Twente Lower Extremity Model
version 2*. 

.. code-block:: AnyScriptDoc

    Main =
        {
        // Configure the Human Model
        #define BM_LEG_MODEL _LEG_MODEL_TLEM2_
        #define BM_ARM_LEFT OFF
        #define BM_LEG_LEFT OFF
        // Include the Human Model
        #include "<ANYBODY_PATH_BODY>/HumanModel.any"


.. seealso:: :doc:`The documentation on BM configuration </BM_Config/index>`


.. ``#include "HumanModel.any"`` 
.. -------------------------------------------------


.. ``AnyFolder Model``
.. ------------------------------------

Compsing the Model
---------------------------------------

Most examples have a section where the model is composed. This is where we combine the ``Body`` from the HumanModel, and add extra things like drivers, external loads, and constraints. 

It could also be any models of the environment which the body interacts with.

.. ``AnyBodyStudy``
.. -------------------------------

The Study section
-------------------------------

The ``AnyBodyStudy`` is where you configure and define your simulation. It
specificies start and end times of the simulation, and number of steps. It also
configures which solvers are used. 

Only the model elements which are referenced from within the Study, will be included in
the simulation. In this case everything in ``Main.Model`` folder is part of the simulation.


.. code-block:: AnyScriptDoc

    #include "path_to_AMMR/libdef.any"

    Main =
    {
      // Configure and include the Human Model
      #define BM_LEG_MODEL _LEG_MODEL_TLEM2_
      #define BM_ARM_LEFT OFF
      #define BM_ARM_RIGHT OFF
      #include "<ANYBODY_PATH_BODY>/HumanModel.any"

      // Compose the model
      AnyFolder Model =
      {
        AnyFolder& Body = .HumanModel.BodyModel;
        AnyFolder Drivers = {...};
        AnyFolder Environment = {...};
      };

      // Configuring  the Study
      AnyBodyStudy Study =
      {
        Gravity = {0,-9.81,1}; // Gravity Vector
        AnyFolder &Model= Main.Model;
      };
    };




.. rubric:: Footnotes


.. [#f1] The preinstalled and (read only) AMMR is located in: ``C:/Program files/AnyBody Technology/AnyBody_X.X/AMMR`` 


.. _AnyBody Modelling System: https://www.anybodytech.com/software/ams/
.. _AnyScript: https://anyscript.org/tutorials/A_Getting_started_anyscript/index.html
.. _Human Model: https://anyscript.org/tutorials/A_Getting_started/lesson1.html