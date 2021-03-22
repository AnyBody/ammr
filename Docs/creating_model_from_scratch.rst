Creating a Human model from scratch
===================================

The following tutorial teaches you how to construct an AnyBody model, when starting with a blank AnyScript file. When you work with more complex models,
you will realize the given code structure is actually quite universal.

.. todo:: Need to provide a link to the tutorial that deals with templates. IMP!!! Need to generate all the images

.. rst-class:: centered
     
**STEP 1**

Open a new AnyScript file (Cntrl + I) and type in the ``Main`` declaration shown below. This file now becomes
the main model file, and all its contents (e.g, model objects, simulation objects) should be typed between the two curly braces.

.. code-block:: AnyScriptDoc
    
    Main =
    {

    };  


.. rst-class:: centered

**STEP 2** 

Link a ``libdef.any`` file to specify the AMMR directories that you wish to import the human model from. 
If instructions for installing the Demo AMMR in the :doc:`previous chapter <ammr_installation>` were exactly followed, the file path typed below should work. 
Otherwise, make the necessary changes.


.. code-block:: AnyScriptDoc
    :emphasize-lines: 1

    #include "<ANYBODY_PATH_MYFILES>/AnyBody.7.1.x/AMMR.v2.1.1-Demo/libdef.any"
    Main =
    {
        
    };

.. rst-class:: centered

**STEP 3**

Create an empty ``Model`` folder to hold your model components, and an ``AnyBodyStudy`` object (named ``Study``) which can run 
Kinematics and Inverse Dynamics simulations on your model. 

.. code-block:: AnyScriptDoc
    :emphasize-lines: 4-8,11-16

    #include "<ANYBODY_PATH_MYFILES>/AnyBody.7.1.x/AMMR.v2.1.1-Demo/libdef.any"
    Main =
    {

        AnyFolder Model =
        {
           
        };

        
        AnyBodyStudy Study =
        {
            Gravity = {0,-9.81,1}; // Gravity Vector
            tStart = 0; // Start time
            tEnd = 1; // End time
        };
    };

.. rst-class:: centered

**STEP 4**

The next statement will create a reference to the ``Model`` folder within ``Study``, thus instructing the simulation to only
consider model objects (i.e. segments, forces, motion drivers etc.) contained within ``Model``.

.. note:: You can create any number of such references. It allows mixing and matching of model components in simulations. 
          For example, if three separate ``AnyFolder`` objects contained models of a human, chair and bicycle, we could create
          two ``AnyBodyStudy`` objects - one with references to (human & chair) and the other simulating (human & bicycle).  


.. code-block:: AnyScriptDoc
    :emphasize-lines: 13

    #include "<ANYBODY_PATH_MYFILES>/AnyBody.7.1.x/AMMR.v2.1.1-Demo/libdef.any"
    Main =
    {

        AnyFolder Model =
        {
           
        };

        
        AnyBodyStudy Study =
        {
            AnyFolder &ModelForSim = .Model; // '&' creates a local reference to existing folder
            Gravity = {0,-9.81,1}; // Gravity Vector
            tStart = 0; // Start time
            tEnd = 1; // End time
        };
    };

.. rst-class:: centered

**STEP 5** 

The AMMR contains multiple musculoskeletal models (e.g., human cow, rat etc.). Type the following statement to import 
the human body model alone. The file path ``<ANYBODY_PATH_BODY>`` is defined in ``libdef.any`` - Have a look in there.

.. code-block:: AnyScriptDoc
    :emphasize-lines: 4

    #include "<ANYBODY_PATH_MYFILES>/AnyBody.7.1.x/AMMR.v2.1.1-Demo/libdef.any"
    Main =
    {
        #include "<ANYBODY_PATH_BODY>/HumanModel.any"

        AnyFolder Model =
        {
           
        };

        
        AnyBodyStudy Study =
        {
            AnyFolder &ModelForSim = .Model; // '&' creates a local reference to existing folder
            Gravity = {0,-9.81,1}; // Gravity Vector
            tStart = 0; // Start time
            tEnd = 1; // End time
        };
    };

.. rst-class:: centered

**STEP 6**

Create a reference to the human body model inside ``Model`` so that it is considered a part of the simulations in ``Study``. 

.. code-block:: AnyScriptDoc
    :emphasize-lines: 8

    #include "<ANYBODY_PATH_MYFILES>/AnyBody.7.1.x/AMMR.v2.1.1-Demo/libdef.any"
    Main =
    {
        #include "<ANYBODY_PATH_BODY>/HumanModel.any"

        AnyFolder Model =
        {
            AnyFolder &Human = .HumanModel.BodyModel;       
        };

        
        AnyBodyStudy Study =
        {
            AnyFolder &ModelForSim = .Model; // '&' creates a local reference to existing folder
            Gravity = {0,-9.81,1}; // Gravity Vector
            tStart = 0; // Start time
            tEnd = 1; // End time
        };
    };


.. rst-class:: centered

.. _MannequinDriver:

**STEP 7**

First add the lines of code highlighted in yellow below. An explanation follows.

While the previous step included the human body model in ``Model``, a key piece of machinery was still missing - Motion constraints. In fact, you will see a warning message 
if the model is loaded now. While motion prescription in elaborated on in :tutorials:doc:`the making things move tutorial <Making_things_move/index>`, a basic AnyBody requirement is that the number of motion constraints 
(called motion drivers in AnyBody) must at least equal the number of DOFs of the model. 

The total number of DOFs & motion constraints can be found by double clicking the ``Study`` object in the Model tree. This opens the Object Description which
will show 378 DOFs but only 336 constraints. Therefore 42 more motion constraints are needed to make the simulation work. 
The AMMR thankfully provides 42 default soft drivers (see this :tutorials:doc:`tutorial which introduces soft drivers <A_Getting_started_modeling/lesson3>`) which set joint angle values that hold the body in a default standing posture. 
These are termed ``DefaultMannequinDrivers`` and are included in the ``Model`` folder below.

Due to the inclusion of soft drivers, solver settings need to be readjusted (see yellow highlting in code below). 
You can now gradually add more complex hard drivers (e.g, to constrain feet to ground, maintain balance etc.) to your model, which automatically over-ride the 
constraints enforced by soft drivers. The alternative would have been to create all 42 constraints manually before the simulation could even be tested 
- a debugging nightmare in the making!   


.. code-block:: AnyScriptDoc
    :emphasize-lines: 9,20-21

    #include "<ANYBODY_PATH_MYFILES>/AnyBody.7.1.x/AMMR.v2.1.1-Demo/libdef.any"
    Main =
    {
        #include "<ANYBODY_PATH_BODY>/HumanModel.any"

        AnyFolder Model =
        {
            AnyFolder &Human = .HumanModel.BodyModel; 
            AnyFolder &MotionDrivers = .HumanModel.DefaultMannequinDrivers;       
        };

        
        AnyBodyStudy Study =
        {
            AnyFolder &ModelForSim = .Model; // '&' creates a local reference to existing folder
            Gravity = {0,-9.81,1}; // Gravity Vector
            tStart = 0; // Start time
            tEnd = 1; // End time

            InitialConditions.SolverType = KinSolOverDeterminate;
            Kinematics.SolverType = KinSolOverDeterminate;
        };
    };

.. rst-class:: centered

**STEP 8**

Add the highlighted code to create generalized reaction forces at the pelvis which support the model's weight. 

It consists of 6 generalized forces applied on the human model by the Ground frame and is composed of 3 linear forces and 3 moments. 
The reaction force is constructed by an ``AnyReacForce`` class containing references to the kinematic measures (see this :tutorials:doc:`tutorial on kinematic measures <The_mechanical_elements/lesson4>`) 
of the Pelvis w.r.t ground. 

.. code-block:: AnyScriptDoc
    :emphasize-lines: 11-19

    #include "<ANYBODY_PATH_MYFILES>/AnyBody.7.1.x/AMMR.v2.1.1-Demo/libdef.any"
    Main =
    {
        #include "<ANYBODY_PATH_BODY>/HumanModel.any"

        AnyFolder Model =
        {
            AnyFolder &Human = .HumanModel.BodyModel; 
            AnyFolder &MotionDrivers = .HumanModel.DefaultMannequinDrivers;      
            
            AnyReacForce HumanGroundResiduals = 
            {
            AnyKinMeasure& PelvisPosX = .Human.Interface.Trunk.PelvisPosX;
            AnyKinMeasure& PelvisPosY = .Human.Interface.Trunk.PelvisPosY;
            AnyKinMeasure& PelvisPosZ = .Human.Interface.Trunk.PelvisPosZ;
            AnyKinMeasure& PelvisRotX = .Human.Interface.Trunk.PelvisRotX;
            AnyKinMeasure& PelvisRotY = .Human.Interface.Trunk.PelvisRotY;
            AnyKinMeasure& PelvisRotZ = .Human.Interface.Trunk.PelvisRotZ;
            };
 
        };

        
        AnyBodyStudy Study =
        {
            AnyFolder &ModelForSim = .Model; // '&' creates a local reference to existing folder
            Gravity = {0,-9.81,1}; // Gravity Vector
            tStart = 0; // Start time
            tEnd = 1; // End time

            InitialConditions.SolverType = KinSolOverDeterminate;
            Kinematics.SolverType = KinSolOverDeterminate;
        };
    };



.. rst-class:: centered

**STEP 9**

Load the model and run the ``InverseDynamics`` analysis contained within ``Study``. Refer to :tutorials:doc:`this tutorial <Interface_features/lesson3>` on how to view/plot the simulation outputs.

We encourage you to experiment further by adding more complex model components such as motion drivers, external forces etc. to the current model. Refer 
to :tutorials:doc:`these tutorials <The_mechanical_elements/index>` to understand these features better. 

.. raw:: html 

    <video width="45%" style="display:block; margin: 0 auto;" controls autoplay loop>
        <source src="_static/Human_rotating_model.mp4" type="video/mp4">
    Your browser does not support the video tag.
    </video>
    