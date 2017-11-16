
#########
Changelog
#########

.. default-domain:: ammr

***********************
AMMR 2.0.0 (2017-10-30)
***********************

Major changes:
==============

New lower extremity model (TLEM2.1)
-----------------------------------

* The `Twente Lower Extremity Model version 2.0 dataset
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
    * The  ratio of volume between Gluetus Maximus superior/inferior has been re-estimated 
      based on the orignal cadaver MRI scans.
    * Update the Sartorius via points.
    * Included a more detailed version of the patella bone.
    * Various minor bug fixes from the orignal implementation used in the TLEMSafe project. 
    *  Corrected the femoral attachment points for the popliteus muscle

* See the dedicated :doc:`TLEM2.1 page </body/Leg-TLEM2_model>` page for more information.


AnyMocap
--------

* New framework for runnning MoCap models. The AnyMoCap framework is an effort to
  create a simple and unified framework for doing any kind of mocap analysis with
  the AnyBody Modeling System. See the :ref:`AnyMocap example gallery <mocap_examples>`
  for more information.


AMMR restructure
-----------------

* Added a top level ``Tools`` folder helper files and other models which don't belong in ``Body/`` or ``Application``. 
* Moved ``Body/AAUHuman/Toolbox`` to ``Tools/ModelUtilities`` 
* Renamed the ``Body/AUHuman`` to ``Body/Mandible_AU`` 


Configuration parameters
------------------------

* Previously used system to configure human body using a BodyPartSetup file was completely 
  replaced with the new body model (BM) parameters. 
* Please see the documentation on: :ref:`BM parameters <bm-config>`.

Scaling laws
------------

* An additional scaling law based on individual segmental scaling factors was added to the 
  repository. It can be enabled using this :ref:`BM parameter<bm-config>` ``#define BM_SCALING _SCALING_XYZ_``. 
  See the :ref:`guide on scaling <scaling-intro>`.
* Default scaling is now :any:`_SCALING_STANDARD_` (e.g  ``#define BM_SCALING _SCALING_STANDARD_``
  which scales all models to default standard 50% male. 
* Introduced :bm_constant:`_SCALING_NONE_`, which disables scaling. E.g. models gets the orignal unscaled size. 



Spine model
-----------
    
* :ref:`BM parameters <bm-trunk-config>` were updated to have control over each section of the spine and relevant components.
* Anatomical reference frame of the thorax segment was modified. This change reflects a change 
  in the pelvic anatomical reference, and ensures upright posture for the standing postures, to 
  align C1C0 joint with the hip joint centers. 
* Boney surfaces of both pelvis and sacrum were updated and now correspond better to the relevant 
  muscle attachments. These segments now also share a common scaling function. Hip joint centers 
  were corrected for the old Leg model.
* Improved wrapping surface for Psoas Major muscles based on the TLEM2.0 MR scans 
* Insertion, via, and attachment nodes of relevant muscles have been updated to match new geometries 
  of pelvis and sacrum.

  
Arm model
---------

* The model now facilitates individual personalization for each side using nonlinear morphing schemes 
  in a more consistent manner. Previously the morphing needed to be done on the right side and then 
  reflect to have the left side morphing. This change removes an extra mirroring step. 
* Arm calibration was updated
* :ref:`BM parameters <bm-arm-config>` have been updated for more convenient use. ``BM_ARM_DETAILED_HAND`` and 
  ``BM_ARM_SHOULDER_RHYTHM`` are now used instead of individual switches for right and left side, which were deprecated. 
* Muscle wrapping surfaces were updated for more physiological behaviour.
* Scapula reaction contact forces were simplified, and do not longer utilize slider segments. 


Minor Changes: 
===============

* Added new initial guess for wrapping muscles, which make the wrapping 
  more when the model starts in extreme postures. 
* Update many examples to use the TLEM 2.1 model. See the :ref:`example gallery <examples-index>`. 
* BM mannequin drivers are now implemented with a class_template allowing all weights and other settings to be customized. 
* A default ``HumanModel.Mannequin`` folder is now automatically created with a ``class_template`` when no user-defined Mannequin file is set.
* A default ``Main.DrawSettings`` folder is now automatically created with a
  ``class_template`` when no user-defined :bm_statement:`DrawSettings
  <BM_DRAWSETTINGS_FILE>` file is set.
* The initial positions of the pelvis now use the anatomical reference frame.
  This follows the logic from the initial rotation of the pelvis which also uses
  the anatomical frame.
* Updates to the TLEM 1 model. The commulated small bug fixes and updates to the TLEM1 model means that we now 
  denote the model 1.2.
* In TLEM models make the opacity of the patellar tendon dependent on the opacity of the patellar surface.
* Simplify the Scapular reactions to the thorax segment. 
* updated the Wilke Validation example to reflect the forces for the AMMR 2.0 repository.
* Updates to BM parameters:

  * New :bm_statement:`BM_ARM_DETAILED_HAND` parameter for the detailed hand.
    The old ``BM_ARM_DETAIL_HAND_RIGHT``/``LEFT`` are deprecated.
  * New :bm_statement:`BM_ARM_SHOULDER_RHYTHM` parameter for controling the shoulder rythm.
    The old ``BM_ARM_SHOULDER_RHYTHM_RIGHT``/``LEFT`` are deprecated.
  * Added new ``BM_JOINT_TYPE_<joint>_<side>`` parameter for completely
    disabling joint and associated nodes in the lower extremity models. (See:
    for example :bm_statement:`BM_JOINT_TYPE_HIP_RIGHT`)
  * New :bm_statement:`BM_LEG_MODEL` parameter for setting the type of leg model
    used. The :bm_statement:`BM_LEG_RIGHT`/:bm_statement:`LEFT <BM_LEG_LEFT>` are 
    now only :bm_constant:`ON`/:bm_constant:`OFF` options. 


Fixed:
========

* Sign for the plantar flexion variable were reversed in some section of the
  model. This has been fixed.
* Bug in Mannequin drivers for the neck, where velocities were not set correctly.
  (Thanks to Assoc. Prof. Michael Skipper Andersen for reporting this)
* Fix small bug preventing ``StandingModelScalingDisplay`` from loading when using
  the :ref:`Leg <old_leg_model>` model. 
* Fixed the opacity of the patellar surface in TLEM models, which pointing 
  erroneously to the opacity of the talus.
* Fixed wrong symmetry of nodes on the C7 segment of full neck model.
* Latisimus Dorsi 5 fasicle was missing in ``MuscleNames.any``  and thus from 
  many symmery measures. 
* Fixed a symmetry problem for the Deltoid muscles at the shoulder.
* Fixed a symmetry problem for the Disc Stiffnesses from L1 to L5
* Fix white surfaces in examples with flat STL surfaces. For example 
  :ref:`sphx_glr_auto_examples_Sports_plot_CrossTrainer.py`. 
* Fixed an issue preventing 
  :ref:`sphx_glr_auto_examples_ADLs_and_ergonomics_plot_StandingModel.py` 
  from working with one leg.
* Fixed a problem with the drawings of the bones in the Arm model which were not
  always symmetrical.
* Fixed symmetry issues in scaling laws for scapula, clavicula, 
  and humerus. 




Removed:
===========

* Old MoCap examples have been moved to ``Application/Examples/Deprecated``
* Removed the deprecated AMMR1.4 hip rotation sequences. 
* The GM-foot model. A new version of this in the pipeline. Contact us if you are 
  interested in this work. 
* All older BodyModels which were deprecated in AMMR1.3

