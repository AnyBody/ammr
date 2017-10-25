Quick start
##########################################

Common model structure
===========================

Most examples and application you will encounter in the *AnyBody Model Repository* use the Human Model in one way or another. 

Even thought the models wary greatly in complexity they mostly follow this common structure:


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




libdef.any
--------------------------

All models must have the ``#include "<path to the AMMR>/libdef.any"``. This will instruct AnyBody to use a certain AMMR.
You can place your models anywhere on your computer, as long as you include the ``libdef.any`` which is found in the top level folder of the AMMR.



Configure and include the Human Model
---------------------------------------------

The AnyBody Human Model is included using the ``#include "<ANYBODY_PATH_BODY>/HumanModel.any"```. 

Before that happens the model must be configured using ``BM_*`` configuration statements. 
These configurations are all ``#define`` or ``#path`` statements prefixed with ``BM_``. 


Composing the model
-----------------------------

After the Human Model is including. 