Application examples
=============================

In the repository, you can find musculoskeletal applications from a wide area of
interests. These models are from various AnyBody users, and all demonstrate
features from the AnyBody Modeling System. 

.. note:: All examples are powerful computational models where variables of interest have been
      biomechanically checked to make sense. However, when modifying or using
      models for other purposes results may occur that cannot be interpreted by
      anatomical or physiological considerations.


Motion Caputure and gait analysis
----------------------------------

All MoCap examples uses the base *AnyMoCap* model, which is a new framework for 
making MoCap models in the AMMR.

- **Simple Lower extremity model** 
    Example of lower body MoCap model using the Plug-in-Gait marker protocol,
    and walking on three typ4 force platforms. The model is fairly simple and a
    good starting point for new users. If you plan to have many trials/subjects,
    take a look at 

- **Simple Full body model**
    Example of full body MoCap model using the Plug-in-Gait marker protocol, and
    walking on three typ4 force platforms. The model is fairly simple and a good
    starting point for new users. If you plan to have many trials/subjects, take
    a look at 

- **Simple GRF prediction model**
    Example of full body MoCap mocdel using the Plug-in-Gait marker protocol but
    without force plates. The external forces are predicted using the GRF
    algorithms. 

- **Multi trial MoCap model**
    Example of MoCap model structured for analysing data from multiple trials
    and subjects. The subject antropometry is scaled/optimized from a single
    static (or dynamic) referece. The model is organized so each trial has its
    own mainfile. A structure makes it much easier to work with large datasets.
    This is the best starting point for analysing bigger MoCap experiments. 

- **Inertial MoCap example**
    Example of a MoCap mdoel using data from a inertial motional caputure suit.
    The model uses a BVH file with data from an Xsens suit. The ground reaction
    forces are predicted using the GRF prediction algorithm. 
    
- **Special AnyMocap features**
    A collection of small models that show-off special features of the
    *AnyMocap* framework. This includes offset to forceplates, individual cutoff
    frequencies for markers,  normalization with respect to gait cycle events,
    using time-varying weight for markers, plus more. 


Orthopedics and rehab
----------------------

- **Spine Fixation Model using Force Dependent Kinematics:** 
      This application is an example of how to use the new force-dependent
      kinematics. The force dependent kinematics allows the kinematic spine
      rhythm which normally drives the vertebras to be switched entirely off.

- **Total Hip Arthroplasty (THA) Model:** 
      Model of a total hip replacement using a contact implant model and
      force-dependent kinematics (FDK).

- **Wheel Chair Model:** 
      A model of a person sitting in a wheelchair, the model is driven by motion
      capture data.

- **Facet Joint Model:** 
      A spine model with facet joints.


Sports 
--------------------------

- **Cross Trainer Model:**
      This model is based on a SolidWorks
      CAD model of a cross trainer fitness machine extended with the
      human.This model is also the subject of the AnyBody Tutorial
      called "Making Models using SolidWorks".

- **Leg Press Machine:**
      A model illustrating a leg press
      exercise and it demonstrates the use of the SolidModeling Class
      Template in the ToolBox of AMMR.

- **Bike Model:** 
      Bicycle rider model that runs either as
      FullBody or as LowerExtremity version.

- **2D Bike Model:**
      A simple bicycle rider model using a planar
      leg model.

- **Push-up Model:** 
      A full-body model doing push-ups with
      assumed drivers.

- **Bench Press Model:**
      A full-body model doing push-ups with   assumed drivers.


Daily activities and ergonomics
-------------------------------

- **Free Posture Model:**
      A full-body model that is easy to put
      into specific static postures. It is equipped with drivers on
      intuitive anatomical joint angle and by default without
      muscles.

- **Standing Model:** 
      A basic static full-body model standing on a floor.

- **Lifting Model:**
      Standing body model lifting a box.

- **Hand Pump:**
      Model of a person operating an old-fashioned pump by hand. The model is
      based on the standing model.

- **Seated Human:** 
      A model of a seated human consisting of the full body model, a chair, and an
      interface between the two.

- **Pedal Demo Model:**
      A leg pressing down a pedal. This
      demonstrates conditional contact between the foot and the
      pedal.

- **Simple Pedal Demo:**
      This model demonstrates the construction
      of a foot pedal example.


Validation 
----------------------
This folder includes some models from users that show
how certain aspects of the models have been validated versus in vivo
measured data:

- **Gait Vaughan:**
      Gait model based on data from the book by Vaughan et al. comparing AnyBody predicted muscle activations with
      EMG measurements.

- **Mandible Chewing Model:**
      Model simulating chewing and comparing 
      values to measurements from de Zee et al., J. of Biomechanics 2007.

- **Wilke Spine Disc Pressure Model:**
      Several models comparing loads in the spine with in vivo measurements
      during daily activities from Wilke et al., Spine 1999.

- **Bergmann GH:**
      Model simulating arm-lift motion adapted from Bergmann et al., J. of
      Biomechanics 2007 to compare the results to in vivo measurements from that
      study.


Other examples
--------------------

- **Total Knee Arthroplasty (TKA) Model (Beta):**
      Demo example of a total knee replacement using contact forces on the implant
      and force-dependent kinematics (FDK).

- **John Wu finger model (Beta):**
      Model from a finger with muscles only, there is no attachment to the rest of
      the body, not even the hand. This model was kindly provided by John Wu.

-  **Cow:(beta)** 
      Model of a cows leg. Driven by a motion caputure and with measured ground reaction forces.



