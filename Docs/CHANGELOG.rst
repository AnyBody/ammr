
#########
Changelog
#########


AMMR 2.0.0 (2017-10-30)
=============================

Major changes:
---------------------------

* New lower extremity model (TLEM2.1)

   * The `Tweente Lower Extremity Model version 2.0 dataset
     <http://dx.doi.org/10.1016/j.jbiomech.2014.12.034>`_, developed in the
     TLEMSafe EU project was implmented in the AMMR repostory. The model is not
     the default model, but can be enabled with the :ref:`BM parameter
     <bm-config>` ``#define BM_LEG_MODEL _LEG_MODEL_TLEM2_``
   * The model is versioned TLEM 2.1, to indicate the number of changes and
     correction which has been added in process. The changes and updates to the
     TLEM2 dataset was done in the `Life Long Joints
     <https://lifelongjoints.eu/>`_ EU research project (paper submitted for publication). 
   * The most important changes to the TLEM 2 dataset include the following: 
     
        * Updated wrapping for the Gluteus Maximus, Iliacus, Psoas around the hip.
        * Reworked muscle topology for Gluteus Medius and Gluetus Minimus
        * Updated wrapping for Hamstring muscles, and Gastrocnemius around the knee. 
        * Redfinened revolute knee axis (thanks to Marco Antonio Marra (Radboudumc)
          for this improvement)

    * See the :doc:`TLEM2.1 documenation </Appl>` page for more information.


* Updates to the TLEM 1 model

    * The exisitng implementaion of the Twente Lower Extremity model has also been updated. 
      The version of is now called 1.2. Changes include the following: 

        *   See the TLEM2.1 documenation page for more information.
  

* New topology for the Trunk Pelvis


* The Anatomical frame for the Pelvis segment has been updated.

* Added new initial guess for wrapping muscles, which make the wrapping 
  more when the model starts in extreme postures. 



Configuration parameters

   * 



  * Previously used system to configure human body using a BodyPartSetup file was completely 
    replaced with the new body model (BM) parameters. Please see the tutorials:
    .. seealso:: :doc:`The documentation on BM configuration </BM_Config/HumanBody_configurations.rst>`.
  * Scaling 









  * An additional scaling law based on individual segmental scaling factors was added to the 
    repository. It can be enabled using *_SCALING_XYZ_* constant.




* Spine model 
    

    * BM parameters were updated to have control over each section of the spine and relevant components.

    

    * Pelvic anatomical reference frame was changed to provide a more physiological pelvic tilt. 
      All associated kinematic measures use the anatomical ref. frame.
    
    * Anatomical reference frame of the thorax segment was modified. This change reflects a change 
      in the pelvic anatomical reference, and ensures upright posture for the standing postures, to 
      align C1C0 joint with the hip joint centers. 

    * Boney surfaces of both pelvis and sacrum were updated and now correspond better to the relevant 
      muscle attachments. These segments now also share a common scaling function. Hip joint centers 
      were corrected for the old Leg model.
    
    * Improved wrapping surface for Psoas Major muscles based on the TLEM2.0 MR scans 
    
    * Insertion, via, and attachment nodes of relevant muscles have been updated to match new geometries 
      of pelvis and sacrum.

  
* Arm model 

    * The model now facilitates individual personalization for each side using nonlinear morphing schemes 
      in a more consistent manner. Previously the morphing needed to be done on the right side and then 
      reflect to have the left side morphing. This change removes an extra mirroring step. 

    * Arm calibration was updated
    
    * BM parameters have been updated for more convenient use. *BM_ARM_DETAIL_HAND_LEFT/RIGHT* and 
      *BM_ARM_SHOULDER_RHYTHM_LEFT/RIGHT* were deprecated. Please see documentation for new controlling 
      parameters.

    * Muscle wrapping surfaces were updated for more physiological behaviour.
    
    * Scapula reaction contact forces were simplified, and do not longer utilize slider segments. 

  

Minor Changes: 
------------------------



* BM mannequin drivers are now implemented with a class_template allowing all weights and other settings to be customized. 

* The initial positions of the pelvis now use the anatomical reference frame.
  This follows the logic from the initial rotation of the pelvis which also uses
  the anatomical frame.

* In TLEM models make the opacity of the patellar tendon dependent on the opacity of the patellar surface.



Fixed:
------------------------

* Sign for the plantar flexion variable were reversed in some section of the model. This has been fixed.

* Bug in Mannequin drivers for the neck, where velocities were not set correctly. (Thanks to Assoc. Prof. Michael Skipper Andersen for reporting this)

* Fix small bug preventing `StandingModelScalingDisplay` from loading when using the :ref`Leg <old_leg_model>` model. 

* Fixed the opacity of the patellar surface in TLEM models, which pointing erroneously to the opacity of the talus.


Removed:
-----------------------

* Old MoCap examples have been moved to :file:`Application/Examples/Deprecated`

* Removed the deprecated AMMR1.4 hip rotation sequences. 

 


New Tweente Lower Eximity Model V. 2.1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 



Tweente Lower Eximity Model V. 1.1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^






Fixed:
--------------------------------





Removed:
-------------------------


Deprecated:
------------------------


