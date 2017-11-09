
#########
Changelog
#########


AMMR 2.0.0 (2017-10-30)
=============================

Major changes:
---------------------------

* Configuration parameters

  * Previously used system to configure human body using a BodyPartSetup file was completely 
    replaced with the new body model (BM) parameters. Please see the tutorials:
    .. seealso:: :doc:`The documentation on BM configuration </BM_Config/HumanBody_configurations.rst>`.
  * Scaling 

  * An additional scaling law based on individual segmental scaling factors was added to the 
    repository. It can be enabled using *_SCALING_XYZ_* constant.
  
* Leg model

    * **Twente Lower Extremity Model* **TLEM 2.1**
   
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

* Folder: :file: 'Body/AAUHuman/Toolbox' was moved to :file: 'Tools/ModelUtilities'



Fixed:
------------------------




Removed:
-----------------------






New Twente Lower Extremity Model V. 2.1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 



Twente Lower Extremity V. 1.1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^






Fixed:
--------------------------------





Removed:
-------------------------


Deprecated:
------------------------


