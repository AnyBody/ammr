#########################
Getting Started with AMMR
#########################


AMMR Intallation
================


The *AnyBody Model Repository* (AMMR) comes bundled with the 
`AnyBody Modelling System`_. But it must be installed/unpacked manually after you installed AnyBody. 
You can install the AMMR from the *AnyBody Assistent* dialog which is presented when AnyBody starts. 

.. seealso:: :doc:`Detailed guide on how to install the AMMR <AMMR_Installation>`:


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
use the :ref:`Human Model <the_body_model>`. Regardless of complexity, all models share a
common structure used to set them up.

The models will typically look like this:


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

Let us go throught the different components to understand how they work:


Path to AMMR
------------

.. code-block:: AnyScriptDoc

    #include "path/to/AMMR/libdef.any"


When having multiple versions of AMMR available on your computer, you have to 
specify which one will be used by AnyBody. Each AMMR includes a file called ``libdef.any``
located at the top level folder. The AnyScript line used for instructing AnyBody
which line to use should be at the very beginning of your ``.any`` file:



Configuring the Human Model
---------------------------

.. code-block:: AnyScriptDoc

    Main =
    {
      // Configure and include the Human Model
      #define BM_LEG_MODEL _LEG_MODEL_TLEM2_
      #define BM_ARM_LEFT OFF
      #define BM_ARM_RIGHT OFF



The Human Body Model is configured through a number of ``#define`` and ``#path``
statements. These statements are all prefixed with ``BM_`` inside AnyScript,
and they can also be referred to as "bm-statements". 

.. seealso:: :doc:`The documentation on BM configuration </BM_Config/index>`


Including the Human Model
---------------------------

.. code-block:: AnyScriptDoc

      #include "<ANYBODY_PATH_BODY>/HumanModel.any"


After the configuration statements the HumanModel is include. It is important that any configuration 
paramters comes before this line. 


Compsing the Model
---------------------------------------

.. code-block:: AnyScriptDoc

      AnyFolder Model =
      {
        AnyFolder& Body = .HumanModel.BodyModel;
        AnyFolder Drivers = {...};
        AnyFolder Environment = {...};
      };


Most examples have a section where the model is composed. This is where we
combine the ``Body`` from the HumanModel, and add extra things like drivers,
external loads, and constraints. 

It could also be any models of the environment which the body interacts with.


The Study section
-------------------------------

.. code-block:: AnyScriptDoc

      AnyBodyStudy Study =
      {
        Gravity = {0,-9.81,1}; // Gravity Vector
        AnyFolder &Model= Main.Model;
      };


The ``AnyBodyStudy`` is where you configure and define your simulation. It
specificies start and end times of the simulation, and number of steps. It also
configures which solvers are used. 

Only the model elements which are referenced from within the Study, will be included in
the simulation. In this case everything in ``Main.Model`` folder is part of the simulation.


.. seealso:: :doc:`The full tutorial on how to create a HumanModel from scratch </Creating_model_from_scratch>`


.. _AnyBody Modelling System: https://www.anybodytech.com/software/ams/
.. _AnyScript: https://anyscript.org/tutorials/A_Getting_started_anyscript/index.html
.. _Human Model: https://anyscript.org/tutorials/A_Getting_started/lesson1.html