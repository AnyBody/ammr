
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
  TLEMSafe EU project was implemented in the AMMR repository. The model is not
  the default model, but can be enabled with the :ref:`BM parameter
  <bm-config>` ``#define BM_LEG_MODEL _LEG_MODEL_TLEM2_``
* The model is versioned TLEM 2.1, to indicate the number of changes and
  correction which has been added in process. The changes and updates to the
  TLEM2 dataset was done in the `Life Long Joints
  <https://lifelongjoints.eu/>`_ EU research project (paper submitted for publication). 
* The most important changes to the TLEM 2 dataset include the following: 
  
    * Updated wrapping for the Gluteus Maximus, Iliacus, Psoas around the hip.
    * Reworked muscle topology for Gluteus Medius and Gluteus Minimus
    * Updated wrapping for Hamstring muscles, and Gastrocnemius around the knee. 
    * Redefined revolute knee axis and patella joint axis and patella tendon length based on the bone geometry. 
      The original TLEM knee axis was estimated from functional trial, and was only valid 
      for very small flexion angles. 
      Thanks to Marco Antonio Marra (Radboudumc) for this for this improvement.
    * The  ratio of volume between Gluteus Maximus superior/inferior has been re-estimated 
      based on the original cadaver MRI scans.
    * Update the Sartorius via points.
    * Included a more detailed version of the patella bone.
    * Various minor bug fixes from the original implementation used in the TLEMSafe project. 
    * Corrected the femoral attachment points for the popliteus muscle
    * Small correction to wrong insetion points for Adductor Longus and Vastus Medialis.

* See the dedicated :doc:`TLEM2.1 page </body/leg_tlem2_model>` page for more information.


AnyMocap
--------

* New framework for running MoCap models. The AnyMoCap framework is an effort to
  create a simple and unified framework for doing any kind of MoCap analysis with
  the AnyBody Modeling System. See the :ref:`AnyMocap example gallery <mocap_examples>`
  for more information.
* Algorithms and file for Ground reaction force prediction are added to: ``ammr/tools/GRFPrediction/``. 
  See the 
  :ref:`MoCap examples <sphx_glr_auto_examples_Mocap_plot_Plug-in-gait_Simple_FullBody_GRFPrediction.py>`
  for how they are used.

TLEM 1 updates
--------------

* The cumulated smaller bug fixes and updates to the TLEM1 model means that we now 
  denote the model 1.2.
* Changed the position of the Heel contact node, to align the heights of the
  TLEM1 and TLEM2 models. 
* Added missing ``GeomScale`` function to the patella
  segment. 
* PSCA is now calculated based on the scaled fiber length. This aligns
  the TLEM 1 model with the new TLEM 2 model. It also means that scaling the model
  without changing the muscle volumes will change the strength of the model.
* Update scaling of the Patella tendon to work with non-linear scaling laws.
* Added visualization of the Fibula bone. 


AMMR restructure
-----------------

* Added a top level ``Tools`` folder helper files and other models which don't belong in ``Body/`` or ``Application``. 
* Moved ``Body/AAUHuman/Toolbox`` to ``Tools/ModelUtilities`` 
* Renamed the ``Body/AUHuman`` to ``Body/Mandible_AU`` 
* Restructured the antropometric ("AnyMan") folder.  The folder ``HumanModel.AntroDataSubject`` is renamed to 
  ``HumanModel.Antropometics``. The structure of the folder has also changed with a ``SegmentDimensions`` and ``SegmentMasses`` subfolder. 


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
* Default scaling is now :any:`_SCALING_STANDARD_` (e.g  ``#define BM_SCALING _SCALING_STANDARD_``)
  which scales all models to default standard 50% male. 
* Introduced :any:`_SCALING_NONE_`, which disables scaling. E.g. models gets the original unscaled size. 


New Mandible model
------------------

* Added new mandible model based on a CT scan of a 40 year old male.
  For more information see :doc:`the documentation for the model </body/aalborg_mandible>` or the 
  :ref:`validation example <sphx_glr_auto_examples_Validation_plot_AalborgMandible.py>`.






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
* Muscle wrapping surfaces were updated for more physiological behavior.
* Scapula reaction contact forces were simplified, and do not longer utilize slider segments. 
* Conoid ligament length now scales along with the scapula width.
* Add a ``GeomScale`` function the the Clavicula segment.


Muscle models
-------------

* All muscle models are updated to support the structure of the new
  ``AnyMuscleModel3E`` and ``AnyMuscleModel`` in the AnyBody Modeling System 7.1. 
  The following variables are renamed: 
    
    * The "optimal fiber length" varaible renamed from ``Lfbar`` to ``Lf0`` 
    * The "Pennation angle" variable renamed from ``Gammabar`` to ``Gamma0``
    * The "Tendon strain at F0" variable renamed from ``Epsilonbar`` to ``Epsilon0``
    
* Restructured the muscle model section of the both TLEM1 and TLEM2 models. 
  
  * All the orignal TLEM based muscle parameter are now located under: ``Leg/ModelParameters/Muscles``
  * All scaled muscle paramters are located in ``Leg/MusPar/SubjectMusPar``. This folder references 
    the TLEM muscle and applies strength scaling etc. The ``SubjectMusPar`` folder and all subfolders are
    implemented with ``class_template``. Thus, all muscle parameter can now be overridden in applications
    by just assigning the variables a new value: E.g.

    .. code-block:: AnyScriptDoc

      Main.HumanModel.BodyModel.Right.Leg.MusPar.SubjectMusPar = {
        GastrocnemiusMedialis.MuscleVolume = 300; // Volume in mililiters
        GastrocnemiusMedialis.Pennationangle = 15; // (in degrees)
      };


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
* Extra Mannequin drivers for the individual shoulder degrees of freedom:
  :any:`Sterno clavicula protraction <BM_MANNEQUIN_DRIVER_STERNOCLAVICULAR_PROTRACTION_RIGHT>`,
  :any:`Sterno clavicula elevation <BM_MANNEQUIN_DRIVER_STERNOCLAVICULAR_ELEVATION_RIGHT>`,
  :any:`Sterno clavicula axial rotation <BM_MANNEQUIN_DRIVER_STERNOCLAVICULAR_AXIAL_ROTATION_RIGHT>`
* The initial positions of the pelvis now use the anatomical reference frame.
  This follows the logic from the initial rotation of the pelvis which also uses
  the anatomical frame.
* DeltoidMuscleConnector segment loading time positioning now depends on the Humerus segment.  
* Added `class template to easily create videos from AnyScript model <https://anyscript.org/tips-n-tricks/creating-videos-from-your-simulations/>`_.
  The tool requires that `FFmpeg <https://www.ffmpeg.org/>`_ is installed. 
  The class template can be found in: ``<ANYBODY_PATH_MODELUTILS>/Video/CameraClassTemplate.any``. 
  See `this blog post <https://anyscript.org/tips-n-tricks/creating-videos-from-your-simulations/>`_. 
* In TLEM models make the opacity of the patellar tendon dependent on the opacity of the patellar surface.
* New ``AnyDoc`` classes are added to the different body model, so the GUI
  can create direct links to the documentation.
* Simplify the Scapular reactions to the thorax segment. 
* Updated the Wilke Validation example to reflect the forces for the AMMR 2.0 repository.
* Updates to BM parameters:

  * New :bm_statement:`BM_ARM_DETAILED_HAND` parameter for the detailed hand.
    The old ``BM_ARM_DETAIL_HAND_RIGHT``/``LEFT`` are deprecated.
  * New :bm_statement:`BM_ARM_SHOULDER_RHYTHM` parameter for controlling the shoulder rhythm.
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
* Latissimus Dorsi 5 fascicle was missing in ``MuscleNames.any``  and thus from 
  many symmetry measures. 
* Fixed a symmetry problem for the Deltoid muscles at the shoulder.
* Fixed a symmetry problem for the Disc stiffness from L1 to L5
* Fix white surfaces in examples with flat STL surfaces. For example 
  :ref:`sphx_glr_auto_examples_Sports_plot_CrossTrainer.py`. 
* Fixed an issue preventing 
  :ref:`sphx_glr_auto_examples_ADLs_and_ergonomics_plot_StandingModel.py` 
  from working with one leg.
* Fixed a problem with the drawings of the bones in the Arm model which were not
  always symmetrical.
* Fixed symmetry issues in scaling laws for scapula and clavicula, 
  and humerus. 
* Fixed a bug where a the Pectoralis wrapping cylinder was not a included in the calibration study.
* Fixed wrong sign for the AnklePlantarFlexion variable.
* Added missing GeomScale and AnatomicalFrame for Ulna segment. 




Removed:
===========

* Old MoCap examples have been moved to ``Application/Examples/Deprecated``
* Removed the deprecated AMMR1.4 hip rotation sequences. 
* The GM-foot model. A new version of this in the pipeline. Contact us if you are 
  interested in this work. 
* All older BodyModels which were deprecated in AMMR1.3

