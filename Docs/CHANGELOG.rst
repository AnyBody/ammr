
#########
Changelog
#########


AMMR 2.0.0 (2017-10-30)
=============================

Major changes:
---------------------------
* Move Body/AAUHuman/Toolbox to Tools/ModelUtilities

* Configuration system

  Previously used system to configure human body using a BodyPartSetup file was completely replaced with 
  the new body model (BM) parameters. 

* Scaling 
  An additional scaling law based on individual segmental scaling factors was added to the repository. It 
  can be enabled using _SCALING_XYZ_
  
* Leg model

	* **Twente Lower Extremity Model* **TLEM 2.1**
   
* Arm model 

    * The model facilitates individual personalization for each side using nonlinear morphing schemes
	
* Spine model 
    
    * Body model configuration parameters were updated to reflect each section better and have better control over all relevant components.
	
	* Pelvic anatomical reference frame was changed to 
	
	* Anatomical reference frame of the thorax segment was modified. This change reflects a change 
	  in the pelvic anatomical reference, and ensures upright posture for the standing postures, to align 
	  C1C0 joint with the hip joint centers. 

	* Boney surfaces of both pelvis and sacrum were updated and now correspond better to the relevant 
	  muscle attachments. These segments also share a common scaling function.
	
	* Improved wrapping surface for Psoas Major muscles based on the TLEM2.0 MR scans 

* Update hip positions for old Leg

This fixes the hip joint positions in the pelivis segment when using
the old leg model. The points were not updated when the New pelvis were
introduced. The Pelvis hip joint center are chosen be the center of the
hip socket, similar to what is used on TLEM1.

This entails that we also update the femural hip center of the old leg,
so the two center align correctly. The femural head center was not
 located at visual center of the femural head.



* Documentation for the pelvic interface morphing (DEV-638)


* Drawing of the pelvis and sacrum was lumped together. Sacrum uses the same scaling function as pelvis. DEV-637



* CoM of lumbar segments scaled using abdominal scaling; Subject-specific model was reworked to use a single scaling function to allow for disc scaling; Minor corrections


* Readability improvement for the disc stiffness models (recommendation for the linear stiffness)



* Anatomical reference frame determines the PelvisInitial Position.

The initial positions of the pelvis now uses the anatomical reference frame.
This follows the logic from the initial rotation of the pelvis which also uses
the anatomical frame.

* Updated Psoas wrapping surface.

The points for the wrapping surface were affected by 1. the move of the pelvic points the fit new thorax/pelvis/sacrum. 
2. The inclusion of the sarcrum has an effect of the interface morphing, 
causing the points which where not directly on the bones to move slightly.


* New wrapping for PsoasMajor. A via point PelvisSeg.IliopubicEminenceViaNodeR is introduced to ensure that the PsoasMajor muscle leaves the pelvis segment from a fixed point. This prevent the psoas muscle from sliding sideways on the wrapping surface during adduction/abduction.
The commit also introduces a new wrapping surface which gives the psoas muscles a larger moment arm in hip extension.

* Make sure measures use the anatomical frames.


* Merge branch 'change_to_bm_statements'


* Change logic to use BM statements


* Merge commit '50ecde3db494192836949c966fba95b0f2a6199b' into update-sacrum-symmetry


* Added some via points to MF and ES muscles for more anatomic representation to match new geometries


* Updated sacrum geometries and added a symmetric sacrum


* Updated positions of most spinal muscles to correspond to new pelvic and sacral geometry


* Fix wrong Switch PSOAS muscle parameters

This caused bugs when left leg was excluded

* fixed bug caused by mixing LEG and LEG_TD definitions (condition could never be true otherwise)



  


Minor Changes: 
------------------------




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


