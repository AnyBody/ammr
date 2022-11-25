# Changelog

% To minimize the risk of merge conflicts insert the your changes at a
% random empty or make a new entry a random place in the bullet lists.

## AMMR beta

**Fixed:**
* The `Main.ModelSetup.CreateVideo` operation was missing in some of the
  MoCap examples. This has been fixed. If you have this problem update the `CreateVideo.any` file in your application. 
* Fixed wrapping problem with the posterior deltoid muscle in the 2 parameter shoulder calibration. 
* Inconsistencies in arm muscles paramaeters have been resolved. The same underlying parameters are now used for both
  the simple and the 3-element muscle models. 

**Changed:**

* The glenoid reaction forces are now expressed in the coordinate system of the
  glenoid cup instead of the general scapula coordinate system.
  The three force variables `GlenoHumeral_DistractionForce`,
  `GlenoHumeral_InferoSuperiorForce`, `GlenoHumeral_AnteroPosteriorForce` now
  represents the three directions given by the glenoid cup. 

  This means that the variables will be slightly different even though the force is the same. 


**Added:**

* Added a few utility helper class templates (`Template_OperationSaveValues`/`Template_OperationLoadValues`/`Template_OperationUpdateValues`) 
  to make it easier to do common class operations without manually having to create the operations with macros.

  To create a operation which loads a file do: 

  ```{code-block} AnyScriptDoc
  Template_OperationLoadValues LoadAnySetFile = {
     FileName= "MyFile.anyset";
  };
  ```
* Added two small helper code macro `NON_UNIQUE_VALUES()`/`NON_UNIQUE_POINTERS()` to 
  find duplicate (i.e. non-unique) entries in arrays of values and pointers.
* A new set of hip joint measures (`Interface.Right.HipISB`) have been added which  
  measures the hip joint strictly according to the definition by the 
  International Society of Biomechanics (ISB).  
  These measures are almost identical to the existing angles except that they do not
  have zero hip-flexion in they neutral postion. This is because they define the pelvis 
  coordinate system with respect to a plane define by the ASIS-PSIS points.   

**Changed:**

* A new `AnatomicalFrameTrunk` reference frame has been added to the pelvis segment. The frame is
  consistent with the anatomical frames in the rest of the trunk model. Also, all joint angles in relative to the pelvis segment now uses this frame. This implies that the neutral position of the model is identical to the neutral position of the trunk dataset. 

  The result is more pelvic tilt in the neutral position, which seem to better reflect reported 
  values in the litterature. 

  The existing `PelvisSeg.AnatomicalFrame` defined ASIS/PSIS bony landmarks remains unchanged.

* The trend validation in the ["Wilke Spine Pressure validation models"](example_wilkespinepressure) have been updated to 
  reflect the changes to thoracic model and pelvis frames. Although the absolute pressures in the spine have changed, the 
  trends (relative changes in spine pressure between models) remains the same. 

* The implemenation of the muscle parameter in the arm model have been refactored. All parematers are now given as
  muscle volume, optimal fiberlenth and tendon slacklength. The physiological cross sectional area (PCSA),
  was previously hard coded parameter, but is now only an intermediate value used for calculating muscle strength from the muscle volume and optimal fiber length.

  This new structure allows for overwritting the the complete set of muscles volumes. For example with alternative dataset. 

  ```{code-block} AnyScriptDoc
  Main.HumanModel.BodyModel.Right.ShoulderArm.ModelParameters.Muscles = {
     biceps_brachii_caput_breve.MuscleVolume = 25.8;

  };
  ```

* The load-time position of the box in the {ref}`BVH_BoxLift model <sphx_glr_auto_examples_Mocap_plot_BVH_BoxLift.py>` is now 
  calculated using the position of the hands. Also, `Main.ModelSetup.EnvironmentParameters.GravityDirection` defined in `box.any` file
  is now calculated automatically from `Main.ModelSetup.LabSpecificData.Gravity` defined in `LabSpecificData.any` file. These changes should 
  make the model more robust when dealing with different bvh files.

* It is no longer necessasry to supply the `MarkerName` argument in the CreateMarkerDriver template
  MoCap models. The argument can still be used if the marker name and the data entry in the c3d file 
  are different.
  
* The implementaion of muscles parameters section of the models have changed to ultize
  the the new `??=` (optional assigment) operator introduced in AnyBody 7.4.1.
  
  It is now possible to directy override/redefine the muscle paramters and muscle volumes. 
  
  For example overriding the muscle volumes with a new set of data: 
  ```{code-block} AnyScriptDoc
  Main.HumanModel.BodyModel.Right.Leg.ModelParameters.Muscles = {
     SoleusMedialis.MuscleVolume = 540; //ml
     SoleusLateralis.MuscleVolume = 450; /ml
  };
  ```
  The TLEM leg model previously had a similar functionality using 
  `class_template`s and an extra level of indirection of the muscle paramters
  (the `SubjectMusPar` section in the muscle model folder). This functionality has 
  been replaced by the new simpler implementation.

* Changed the methods for distributing muscle volume among discretized muscle
  elements. This new method allows for different optimal
  fiber lengths among elements of a muscle. If one element of a muscle get a
  smaller optimal fiber length (i.e. through calibration) the volume of the muscles
  element gets redistributed, and PCSA remains contant across elements. 
  
  If the optimal fiber length of the different elements are the same, then this method 
  will yield the same result as before.


* In many body parts the folder holding muscles models were named shortly as `MusPar`. 
  It is now renamed to `MuscleModels` for better clarity. 
   
* The references to muscle models in the joint muscles of the detailed hand have been renamed to avoid future naming conflicts.
* The "via-points" for the Psoas Major muscle has been adjusted to ensure that the muscles can better act the role of stabilizing muscle for the lumbar spine.

(ammr-2.4-changelog)=
## AMMR 2.4.2 (2022-07-08)
[![Zenodo link](https://zenodo.org/badge/DOI/10.5281/zenodo.6809697.svg)](https://doi.org/10.5281/zenodo.6809697)

AMMR version 2.4.2 contains only a few minor changes and fixes compared to  version 2.4.1.


**Changed:**

* Changed defintion (sign) of the `SkullThoraxRotation` and `SkullThoraxLateralbending` variable
  in the `interface` folder. They are now consistent with similar difinitions in the rest of the spine.
* The location of the foot drawing generated by the `OptimizeBVH_Origin` class template 
  for visualization of the target location and orientation of
  "LFOOT" and "RFOOT" has been updated to better match the expected actual foot location.
 

**Fixed:**

* Fixed the {ref}`Evaluate moments arms example <sphx_glr_auto_examples_Validation_plot_EvaluateMomentArms.py>`
  where a few branches of the latisimus dorsi, pectoralis major and trapezius muscles were not included. 
* Fixed a problem that caused the `OptimizeBVH_Origin` class template to fail to load 
  if the same human segment was used more than one time in the same model.

  

## AMMR 2.4.1 (2022-05-30)
[![Zenodo link](https://zenodo.org/badge/DOI/10.5281/zenodo.6533249.svg)](https://doi.org/10.5281/zenodo.6533249)

**New example models:**

- Added a model using a new class template to optimize the origin of BVH model. This model shows how to optimize
  the origin of the BVH model such that a target segment of the human model (Left/Right Foot/Hand) hits a known 
  position and orientation in a given time interval while following the recorded motion from the trial.
  <[See more](examples_mocap_bvhorigin)>


**Fixed:**
* Fixed a small syntax error which caused the BVH example `S1/S01_Trial02/` to fail loading. 
* Fixed a problem with the "interface" morphing between the TLEM2 pelvis and Trunk Pelvis at the tip of the scarum bone. 
  This bug was visible when using `#define BM_LEG_TRUNK_INTERFACE _MORPH_LEG_TO_TRUNK_`, (i.e. when using the trunk pelvis morphology with the TLEM2 model), which is not the default. 
* Fixed missing calibration for the new latissimus dorsi elements introduced in AMMR 2.4. This fix also ensures that all
  latissimus dorsi elements are calibrated in the same arm posture.

**Changed:**

* The anyscript implemenatation of the acromio-clavicuala, sterno-clavicular, gleno-humeral, and elbow
  joints have been refactored. They now use explicit AnyScript joint classes (e.g. `AnySphericalJoint`)
  instead of implementing the joints directly with measures and constraints. This simplifies the 
  implementation, but also changes the structure of the model tree. However, it has no influence 
  the kinematics of the model, which remains identical. 

  The new names of the explicit joint objects in `ShoulderArm.Jnt` are:

  * `SternoClavicularJoint` (-3 DOF)
  * `AcromioClavicularJoint` (-3 DOF)
  * `GlenoHumeralJoint` (-3 DOF)
  * `HumeroUlnarJoint` (-5 DOF)
  * `HumeroRadialJoint` (-1 DOF)
  * `ProximalRadioUlnarJoint` (-2 DOF)
  * `DistalRadioUlnarJoint` (-2 DOF)

The `HumeroUlnarJoint` is the elbow flexion extension, and together `HumeroRadialJoint`, `ProximalRadioUlnarJoint` and `DistalRadioUlnarJoint` adds 5 constraints leaving the forearm rotation degree of freedom. 
   
  
**Added:**
* A few previously renamed nodes in pelvis were added back to improve backwards compatibility when loading old seating models. 


## AMMR 2.4 (2022-04-28)
[![Zenodo link](https://zenodo.org/badge/DOI/10.5281/zenodo.6471999.svg)](https://doi.org/10.5281/zenodo.6471999)


**New example models:**

- Added a new trunk exoskeleton concept model 
  for simulating assistance at the trunk in a box lifting task. This simple example shows how to apply assistive torque directly
  to the human model. <[See more](example_exo_concept_trunk)>
- Added a new exoskeleton concept model 
  for simulation-driven conceptual design of exoskeletons. The model was developed by Prof. John Rasmussen from
  Aalborg University. Please see the [web cast](https://www.anybodytech.com/simulation-driven-conceptual-design-of-exoskeletons/)
  for more details. <[See more](example_exo_concept_boxlift)>
- Added a new femoral torsion tool to apply femoral torsion to the TLEM2.0 leg model.
  This model tool was developed by Dr. Enrico De Pieri from University of Basel
  Children’s Hospital (UKBB). Please see the documentation 
  or the [web cast](https://www.anybodytech.com/modeling-subject-specific-femoral-torsion-for-the-analysis-of-lower-limb-joint-loads/)
  by Enrico on his work and publication on femoral torsion. <[See more](example_femoral_torsion)>
- Added a new knee force model 
  example. The model shows how to calculate a simple estimate of the medial and lateral knee force. <[See more](example_knee_forces_estimate)>
- A new box lifting motion capture model has been added. The model is based on data from an inertial measurement 
  unit based suit ([Xsens](https://www.xsens.com/products/mtw-awinda)), and illustrates how to connect MoCap models with objects in the environment. 
  <[See more](example_bvh_boxlift)>


**New features:**

- Many AnyScript example models now include an option to automatically 
  create a video from the model. To use this functionality find and run 
  the new `VideoTool.CreateVideo` operation under the Study folder.
  This will automatically run the example model, output still frames,
  and combine them into a video afterwards. The script can easily be
  adapted and moved to other examples. 
- Two new utility macros, which make it easier to create 3D grid arrays, have been added to the model repository.
  `MESHTRIPLES(xarr, yarr, zarr)` and  `MESHGRID(xarr,yarr,zarr)`. i.e. for
  creating arrays of all points in a 3D grid array. More information in the file: 
  {menuselection}`Body --> AAUHuman --> BodyModels --> GenericBodyModel --> Helper.ClassTemplates.any`

- Added a warning when the glenohumeral flexion/abduction in the 
  mannequin values can cause problems as start guess for the kinematic solver. A small automatic pertubation of the Humerus orientation (`Axes0`) is also added in these cases so the shoulder rhythm will work as expected. 
- There is a new option to override more settings in the `DefaultMannequinDrivers` section. Now the driver 
  type (`CType=Hard/Soft`), can be overridden directly by the users.
- Fixed a lack of robustness with muscle recruitment of the abdominal muscles (`buckle support`). 
  Muscle recruitment could previously fail with high lumbar flexion.
  A small support "artificial muscle" has beeen added to the buckle 
  segment, preventing muscle recruitment from failing. 

**Fixed:**

- Improved the selected output by adding the m. Semimembranosus and m.
  Semitendinosus contributions to the knee flexor group for both muscle activity (`KneeFlexorMuscleActivity`)
  and muscle force (`KneeFlexorMuscleForce`).
- Updated and improved origin of the hamstring muscles. The muscles biceps
  femoris, semitendinosus and semimembranosus have been updated to improve their
  moment arms in certain lunge movements. The origin points at pelvis has been
  moved down a bit to ensure the muscles wraps correctly in lunge movements,
  while maintaining the same moment arm in gait etc.
- Fixed a bug in scaling where the mass of the trunk model pelvis was used in some cases instead of the 
  pelvis mass from the leg model. This could cause a slightly incorrect mass to be used for the pelvis segment.
- Fixed wrong sign for the WristJoint flexion variable. The values users provided in the mannequin 
  section was incorrectly interpreted as wrist extension.
- Fixed a problem where custom scaling and {bm_constant}`_SCALING_XYZ_` would 
  prevent the model from loading.
- Fixed some logical issues with the `ContactSurfaceDistanceAndVelocityDepLinPush.any` file.
   
   - Fix length calculation and drawing of the normal force
   - Fixed an extrapolation error when changing the internal setting `_SMOOTHING_FUNCTION_PROFILE_` to
     `FUNC_PROFILE_BSPLINE`. We now cap the height ratio to only be in the interpolation area. 
     Values outside this area infer that no contact is present.

- Refactored the way Trunk nodes are mirrored between left and right. This is more consistent 
  with the remaining body parts and handled in the cadaver data files.
- Fixed a problem in MoCap models where calibration studies were not run automatically in models 
  that only had 3-element muscles on the upper body.
- The [example to evaluate moments arms](example_evaluate_momentarms) 
  now works when the shoulder rhythm is enabled. 


**Changed:**

- Ensure consistency of arm muscle parameters when switching between simple muscle models and 3 element muscle models.
  The two muscles had a few differences in the underlying parameters. Mostly due
  to the 3 element models being implemented based on newer publications, and
  some changes not being backported properly to the simple muscle model. The two muscle models now give the same overall muscles strength `F0` when switching.

  - Fix a bug in Anconeus_1 PCSA for the 3 element muscle model. 
  - Fix the distribution of PCSA in simple muscle models for Latisimus dorsi to match 3 element muscle models.
  - Fix the total PCSA of the 3-element muscle models of the Latisimus dorsi muscles to match the simple muscles.
  - Fixed a typo in the calculation of the PCSA for one element of the pronator quadratus (`Pron_quadr_2`) with the simple muscle models.
  - Fixed the PCSA of pectoralis major muscle model to match the 3-element muscle models. 
  - Corrected Coracobrachialis pennation angle for 3-element muscle models.
  - Fixed the PCSA of the deltoid simple muscle models to match the 3 element muscle models.
  - Fixed the PCSA of the subscapularis simple muscle models to match the 3 element muscle models.



- Improve the trunk model's strength for trunk external rotation. This change
  improves the implementation of the internal/external obliques and latissimus
  dorsi muscles. More branches are added to the internal obliques and the
  geometry is updated to better match anatomical text books. Likewise, the
  latissimus dorsi muscles is discretized into more branches so it has branches
  inserting on every vertebra.
- The `clavicle` entry in the `Anthropometric.SegmentMasses` folder have been renamed to `shoulder`. 
  This makes it consistent with the rest of varaibles in the folder, and correctly reflect that 
  the mass is assigned to both the scapula and clavicle segment. 
- The `OptimalFiberLength` and `TotalTendonLength` in the TLEM leg models are no longer 'DesignVar' when the
  parameters are also calibrated. This prevents the huge amount of warnings when calibrating the leg muscles.
- The `L5LContactNode`,`L4LContactNode`,`L3LContactNode`,
  `L4LContactNode`,`L1LContactNode` nodes were scaled using the Right node Z-axis. This
  is now changed to use the Left node Z-axis.
- The trunk model has been restructured in preparation for a full Thoracic model. 
  This means that all the vertebra and ribs have been created in the model structure, but only as
  `AnyFolder&` references to the single rigid thorax segment.
  
  :::{note} 
  A number of nodes have been renamed in the process. If you have problems loading old model due to missing nodes, please consult the new model examples to find the new names. 
  :::

- Updated the neutral scapula position and scapula sliding. The default neutral scapula position 
  (medial rotation) has been updated to a more realistic position. Additionally, the node at scapula
  TS point, on which the scapula slides, has been moved to provide a more realistic clearance between 
  the scapula and the ellipsoid sliding surface representing thorax.  
  Thanks to Johanna Menze (@menzejo) from the University of Bern for updating the model.
- Renamed a few variables named `r` which could collide with built-in `r` variable. 

**Removed:**

- The previously deprecated BM keyword `_LEG_MODEL_Leg_` has been completely removed.
- The special mannequin driver switches for the old leg model (`BM_MANNEQUIN_DRIVER_ANKLE_EVERSION_RIGHT/LEFT`) 
  have been deprecated. Instead the switch used for the TLEM1/2 leg models
  ({bm_statement}`BM_MANNEQUIN_DRIVER_ANKLE_SUBTALAR_EVERSION_RIGHT`) can now be used for all leg models. 
- Renamed all deprecated ligament class names. `AnyViaPointLigament`-> `AnyLigamentViaPoint`.

## AMMR 2.3.4 (2021-07-05)
[![Zenodo link](https://zenodo.org/badge/DOI/10.5281/zenodo.5060249.svg)](https://doi.org/10.5281/zenodo.5060249)

**Fixed:**

- Improved the intial guess for Latissimus dorsi wrapping, so the wrapping solutions becomes more
  robust to extreeme starting postions.
- Fix a problem with `<ANYBODY_PATH_MODELUTILS>/Reactions` support files preventing models from loading correctly.
  Thanks to prof. Michael Skipper Andersen (Aalborg University) for finding this bug.

**Added:**

- Add small helper class template `DriverBasedOnLoadPos` which makes it easy to add constraints
  between two segments based on their load time positions.
- Refactor the way pelvis rotations are measured in the interface folder. This allows the user to
  override the default implicit global reference frame and thus output pelvis rotation relative to
  a custom frame.
- Add a new ability to evaluate trunk strength into the built-in studies for
  [joint strength evaluation](example_evaluate_joint_strength).
- New ligaments connecting the Sacrum and Pelvis segments are added. They are enabled
  togehter with the ligaments on the lumbar spine through the `BM_TRUNK_LUMBAR_LIGAMENTS`
  define statement.

**Changed:**

- The ["ADL gait (MoCap model)"](example_adlgait) has been updated with
  most recent improvements from our internal projects. The marker protocol has
  been adjust and a lot of small data problems (marker dropouts etc) has been
  fixed.
- The posture of [the standing lift example](example_standinglift)
  have been modified to make the example more robust.
- The `Tuber_ischiadicum` node to `Seat_contact` as it was misaligned to the actual bony
  landmark position. New `Tuber_ischiadicum` nodes have been added at the bony landmark.
  The renaming also makes it easier to identify what the node is used for across the ammr
  models.
- Changed the way the arm joint moment measures are calculated. This affect the output when no muscles are added to the model, and the  
  moments are now calculated and expressed in same way as when muscles are included. The moments are
  expressed in a fixed proximal reference frame instead of using the euler axis of rotation which may not be othogonal.
  All moment contribution also now found using search function which will be more robust. 

## AMMR 2.3.3 (2021-03-24)

[![Zenodo link](https://zenodo.org/badge/DOI/10.5281/zenodo.4616316.svg)](https://doi.org/10.5281/zenodo.4616316)



**Fixed:**

- Fix a problem single leg models in AnyMocap. The file `OptimizeAnthropometricsOnOff.any`
  preventing models with only one leg included from being loaded.
- Removed two unused measures with references to thorax in the scapula and clavicula segments.
  The references could cause problems for ´AnyKinCOM\` which uses search when including segments.
  Thanks to Handa Kensuke from Terrabyte helping fix this error.
- Fix bug in initial wrapping guess for Triceps LH muscle wrapping. This bug could cause the
  left side Triceps LH muscle to wrap incorrectly at shoulder.
- Fix calibration of of element 4 and 5 of the latissimus dorsi muscle. These two stands of
  the muscles where not included correctly in the calibration study when using the three element
  muscles model.

**Changed:**

- The settings of the [Knee Simulator example](example_kneesimulator) has been
  tweaked to make it run faster.

## AMMR 2.3.2 (2021-01-21)


[![Zenodo link](https://zenodo.org/badge/DOI/10.5281/zenodo.4305559.svg)](https://doi.org/10.5281/zenodo.4305559)




```{rst-class} without-title
```

:::{warning} **Model results can change!**

A bug related to scaling was fixed in AMMR 2.3.2. This affect models using the
{bm_constant}`length-mass-fat<_SCALING_LENGTHMASSFAT_>` and
{bm_constant}`uniform <_SCALING_UNIFORM_>` scaling, when only Body Height is
specified. The results can change as models more accurately match the
requested body height.
:::


**Fixed:**

- Fixed tibialis anterior/posterior variables in the `SelectedOutput`
  section. The force values were represented as the `max()` of the muscle elements
  instead of the `sum()`. Thanks to Dr. Enrico De Pierie from University Children's
  Hospital Basel for fixing this issue.
- Fixed a bug when using {bm_constant}`_SCALING_LENGTHMASSFAT_` and  {bm_constant}`_SCALING_UNIFORM_`
  and only specifying the body height as input. The segment lengths were set to
  slightly smaller values, which caused the total body height to be less than
  what was used as input. The bug occurred since a standard body height in some
  'AnyMan' files was assumed to be 1.8 m instead of the correct 1.75 m. This fix
  aligns the results with {bm_constant}`_SCALING_XYZ_` (used in the MoCap
  models) and {bm_constant}`_SCALING_STANDARD_` (50 percentile) which were both
  correct.
- Fixed a problem with foot support in the
  ["Spine Pressure validation model"](example_wilkespinepressure) lying flat on
  the back. The foot is now supported in the right direction.
- Fixed a problem with the Standing Model template which was using an alternate
  mode where foot constraints were disabled.
- Fixed a problem with the ADL gait MoCap example, where the batch processing
  script would report some trials as failed even if they succeeded correctly.
- Use correct times in the Xsens example MoCap (trial "S01-Trial2"). The model
  stopped walking after a number of time steps
  because `tEnd` was set after the last data point in the BVH data file.
- Fixed/improved the wrapping surface for the subscapularis muscles. The muscles
  can no longer slide off
  its wrapping surface in extreme range of motions.
- Fixed infraspinatus muscle wrapping for high arm positions. This fix adds a
  torus for infraspinatus wrapping on the humerus.
  It fixes a problem where infraspinatus could slide of its wrapping surface in
  high arm postures.
- Fix problem with latissimus dorsi muscle wrapping in over-head arm postures. A
  new wrapping ellipsoid has been added at the humeral head.

**Changed:**

- The rectus femoris muscle wrapping surface at the hip has been adjusted to prevent
  collision between the rectus femoris origin and the wrapping surface. Further,
  the surface is now used for both the straight and reflected head of the rectus
  femoris.
- Increase the discretization (StringMesh) on approx 30 muscles to improve wrapping.
- The results for the ["Wilke Spine Pressure"](example_wilkespinepressure)
  validation model has been updated due to the fix for the
  {bm_constant}`_SCALING_UNIFORM_`. The updated model improved the validation
  results slightly.
- The new large scale ["MoCap model (ADL gait)"](example_adlgait)
  has been updated so the results of running all standing reference trials have
  been added to the model. This means that all the dynamic trials will work even
  if the user forgets to first run the standing reference trials. It is still
  necessary to run the standing reference trials again if any changes are made to the model.
- The wrapping for the "Triceps Long Head" muscle has been updated at the humeral head
  to avoid the muscle wrapping incorrectly in over-head arm postures. This fix
  also adds a via point at the middle of the humerus to make the wrapping solution
  more robust.
- The `VideoLookAtCamera` camera class template in the AMMR now saves videos as they look in
  the model view. I.e. if things are hidden in the model view they will not show up in the video.
  This feature is enabled by a new setting `AnyCameraLookAt.RenderUserInterfaceViewState` in
  AnyBody version 7.3.2. The old behavior can be restored by setting `Camera.RenderUserInterfaceViewState=Off;`
  in the class template.
 
## AMMR 2.3.1 (2020-09-30)

[![Zenodo link](https://zenodo.org/badge/DOI/10.5281/zenodo.4023956.svg)](https://doi.org/10.5281/zenodo.4023956)

**Added:**

- All models now run with the new wrapping solver by default, which makes all models with wrapping
  muscles run much faster. Hence the `AnyBody73_ExperimentalShortestPathSolver` setting is
  deprecated and no effect. The old wrapping algorithm can be enabled (not recommended) by setting:

  ```{code-block} AnyScriptDoc
  System.Compatibility.ShortestPathSolverVersion = 2; // 4 is default (new wrapping)
  ```

- New dedicated wrapping ellipsoid for Triceps at the glenohumeral head. This
  addition solves a few problems with overhead arm postures.

**Changed:**

- Improvements to the new ["ADL Gait"](example_adlgait)
  example. The model now has muscles enabled and the marker protocol has been adjusted
  for a better shoulder posture. Also, the batch processing script now runs all trials without hickups.
- Improve the shoulder rhythm. Scapula position when using the shoulder rhythm
  is now determined by the Conoideum ligament driver, like how scapula kinematic is
  controlled with no shoulder rhythm. The rhythm is now controlled
  based on the **plane of elevation** and **humerus elevation** from the
  'ThoraxHumerus' measures in the interface folder. This tracks the original
  specification of the shoulder rhythm in "De Groot, J. H. *The shoulder: a kinematic and dynamic analysis of motion and loading.* (1998)".
  One difference is still shoulder protraction/retraction where regression coefficients needed
  to be tweaked for the shoulder to work in the full range of motion. De Groot et al (1998) had
  only based their shoulder rhythm on arm position in front of the body (e.i. positive elevation planes).
- Removed metabolic power (`Pmet`) contributions from artificial muscles defined
  as `AnyMuscle` derived classes. `Pmet` contributions from tools, such as GRF
  prediction, modelled as `AnyGeneralMuscles` will no longer be part of
  studies' Pmet calculations.
- Adjusted the wrapping segments for deltoid posterior so it doesn't affect the muscle in overhead arm posturess.
- Teres minor now uses a torus for wrapping at the humeral head.

**Fixed:**

- Fixed incorrect values in "SelectedOutput" for four reaction moments
  variables, which were wrong due an implementation change of
  `AnyRevoluteJoint`. The following variables in
  `SelectedOutput.Trunk.JointReactionForce` were incorrect.

  - `C2C1FlexionExtensionMoment`
  - `C2C1LateralMoment`
  - `C1C0AxialMoment`
  - `C1C0LateralMoment`

  The values were wrong because they referered to the internal generalized force
  output of `AnyRevoluteJoint`.  (i.e. `Constraints.Reactions.Fout`). The
  values `Fout[3]` and `Fout[4]` can not be interpreted as real physical
  reaction moments because `AnyRevoluteJoint` is implemented using euler angles.

  :::{warning}
  The use of generalized forces (`Fout`) is
  discouraged, and will be removed in the AMMR. Instead use the force and moment
  variables in `AnyRefFrameOutput` subfolder instead.
  :::

- Fixed incorrect volume of Satorius muscle in TLEM1 and TLEM2. Thanks to Dr. Adam D. Sylvester
  from Johns Hopkins School of Medicine and Dr. Patricia A. Kramer from the University of
  Washington for pointing out the error. The error occurred since the satorius in the original [TLEM1 paper](https://linkinghub.elsevier.com/retrieve/pii/S0268003306001896) was muscles
  in series with a pseudo insertion/origin on the femur. Both of these muscle
  elements were therefore listed with the full PSCA of Satorius. This detail was
  missed in the AnyBody TLEM1 and TLEM2 implementation where Satorius was
  implemented two parallel elements (TLEM1) and a single element (TLEM2). Hence
  the Satorius had twice the correct volume.

- Fixed a problem when C3D files are malformed and doesn't contain a
  `FORCE_PLATFORM.ZERO` variable. The C3D standard specifies that the variable
  should exist but since it not used in the models the reference could just be
  remvoed.

- Fixed an problem which prevented the ANSUR scaling plugin example from working correctly 7.3.0

- Fixed incorrect output of `ThoraxHumerus` interface measures. The mesure wasn't used
  by other parts of the AMMR until now so the bug had no consequences in previous AMMR versions.

- Fixed mass calculation of the foot and talus segments in the `GaitVaughan` validation model.

**Removed:**

- Removed unused `BM_TRUNK_CERVICAL_LIGAMENTS` switch which had no effect since there were no ligaments defined in the neck model.

## AMMR 2.3 (2020-07-07)

[![Zenodo link](https://zenodo.org/badge/DOI/10.5281/zenodo.3932764.svg)](https://doi.org/10.5281/zenodo.3932764)


**Added:**

- Added a new Full Body {ref}`"ADL Gait" <example_adlgait>` MoCap
  Example based on the "Rehazenter Adult Walking Dataset" by [Schreiber and Moissenet (2019)](https://doi.org/10.1038/s41597-019-0124-4).
  The model is configured to run all 50 subjects and 1145 trials in the data set. However, you must
  download the actual data separately from
  [FigShare](https://figshare.com/articles/dataset/A_multimodal_dataset_of_human_gait_at_different_walking_speeds/7734767)
  where it is hosted under a Creative Commons license.

- New GUI plugin which uses statistical information from the ANSUR database to set anthropometric values in AnyBody. A small example model
  is added `Examples/StatisticalScalingPlugin` which shows how to use the plugin.

- Added a new option to optimize "head width" / "head depth" / "neck length" / "Tibia torsion" /
  "hand breadth" as part of the `OptimizeAnthropometricsOnOff` class_template in the AnyMoCap framework.

- Added new rotation vector based measures in the interface folder for the arm degrees of freedom.
  These measures (`Interface.Right.RotVectorMeasures.*`) for joint angles do not have a clinical
  meaning but are useful when exporting and importing joint angles.

- Added a new {ammr:bm_statement}`option for setting custom muscle calibration <BM_CALIBRATION_TYPE>`.
  I.e. an option which disables calibration so the user can add their own code.

  ```{code-block} AnyScriptDoc
  #define BM_CALIBRATION_TYPE _CALIBRATION_TYPE_CUSTOM_

  #include "<ANYBODY_PATH_BODY>\HumanModel.any"

  // Manually include calibration code.
  Main.HumanModel.Calibration = {
    #include "<ANYBODY_PATH_BODY>/LegTLEM/Calibration/CalibrationSequenceRight.any"
    #include "<ANYBODY_PATH_BODY>/LegTLEM/Calibration/CalibrationSequenceLeft.any"
    #include "<ANYBODY_PATH_BODY>/Arm/Calibration/CalibrationSequenceRight.any"
    #include "<ANYBODY_PATH_BODY>/Arm/Calibration/CalibrationSequenceLeft.any"
  };
  ```

  :::{note}
  If you need to modify the calibration code, copy it to the application folder and include it from there.
  :::

**Changed:**
 
- All application examples use the new and fast experimental wrapping algorithmn
  in the AnyBody Modeling System 7.3.0. A notice is shown in the output window to
  remind the users that the algorithm is enabled. The experimental wrapping algorithm
  can be used in all models by setting:

  ```{code-block} AnyScriptDoc
  System.Compatibility.AnyBody73_ExperimentalShortestPathSolver = On;
  ```

  :::{seealso}
  The release notes for the AnyBoy Modeling System has more information
  on the new and faster experimental wrapping algorithm.
  :::

- Split the SternoCleidomastoid muscle up into two muscle branches.
  This makes the two heads of the muscle able to work independent.

- Add extra muscle-via points on for the Latissimus dorsi on the Thorax segment.
  This change fixes wrapping problems where the Latissimus dorsi muscle strands
  would slide off the wrapping surface representing the thorax segment.

- Renamed all deprecated muscle class names. `AnyViaPointMuscle`-> `AnyMuscleViaPoint`
  and `AnyShortestPathMuscle`-> `AnyMuscleShortestPath`

- The AnyMoCap framework now uses a more robust way of saving optimized parameters from the parameter optimization studies, when using AMS 7.3.

- Pectoralis Major has been split from 5 into 10 branches to better represent the real fiber direction of the muscle.
  Similarly the origins of the new Pectoralis Major muscles have been moved to align with real anatomy of the muscle.

- Changed the format used by the AnyMoCap models when transferring joint angles from the mrker tracking step to
  inverse dynamics simulation.
  The joint-angles for the arms and pelvis rotation are now written in terms of rotation vectors instead of Euler angles. This fixes
  potential singularity problems. The temporary joint angle files produced by the MoCap models
  have been renamed to indicate the data is no longer Euler angles.

  :::{note}
  This means that the data in these temporary files can not easily be interpreted from a clinical
  point of view. Create your own output files with physiological joint angles if you need to export that data.
  :::

- The body model configuration plugin have been updated. This fixes a number of
  smaller issues and bugs.

- The via points of PeroneusLongus and PeroneusBrevis have been adjusted to
  ensure the muscles maintain moment arm in a larger range of motion.

- Rectus abdominis muscle has been split into eight branches to better represent geometry, than what is possible with one branch.
  The strength between the new branches has been split evenly. Additionally, the PCSA has been increased from $2.6 cm^2$ to $7.9 cm^2$ according
  to McGill et al 1988, the $2.6 cm^2$ originates from a study with elderly subjects, the McGill study used mid age subjects.

- Adjusted the origin of Serratus Anterior 1 so it aligns with the geometry of the rib on which it originates.

- Changed the way the deltoid wrapping surfaces move relative to humerus. This
  changes makes it wrapping more robust to deltoid flipping over to the wrong side
  of the wrapping surface in extreme postures.

- The BVH virtual marker protocol have been adjusted. If older BVH models is used
  with AMMR 2.3 a warning/error is triggered to warn the user that the protocol needs
  to be updated.

**Fixed:**

- Fixed problems with the following variables in the `SelectedOuput` folder: `HipAbductorMuscleForce`,
  `HipExtensorMuscleActivity`, `HipExtensorMuscleForce`, `KneeFlexorMuscleActivity` and `KneeFlexorMuscleForce`.
- Markers on BVH stick-figure model in the AnyMoCap framework now respects the
  setting: `Main.ModelSetup.BVHFileData.ModelDrawOnOff`.
- Fixed occasional kinematics problems with FullBody MoCap models during
  inverse dynamics simulation. This was fixed by changing the internal representation of the shoulder joint angles
  when transferring kinematics from marker tracking to the Inverse Dynamics simulations.
- Fixed a problem with the Body Model configurator plugin showing reporting: "No Human Model" when a configuration file already exists.
- Corrected the location of via points of Flexor_Digitorum_Superficialis_Digit2 to avoid wrapping surface collisions
  in certain hand positions.
- Corrected the location of via points of Flexor_Digitorum_Superficialis_Digit3 and 4, Palmaris_Longus, Extensor_Carpi_Radialis_Brevis and
  Extensor_Digitorum_Digit2 to avoid wrapping surface collisions in certain hand positions.
- The muscle via point representing the bicipital groove have been adjusted to ensure the Biceps Caput Longum wraps the humeral head correctly in
- Fixed a bug in the FreePosture model, where input for the Left/Right arm drivers was switched in some places.
- Fixed missing visual color indication of force plate forces for type 3 force plates in the MoCap models.
- Fixed a bug with in the built-in studies to
  {ref}`evaluate arm joint strength <example_evaluate_joint_strength>`.
  The range of motion for the left arm elbow pronation/supination were not correct.
- Fixed a bug preventing the model from loading with with {bm_constant}`_SCALING_XYZ_` and both legs excluded.
- Fixed the load-time position of the head segment when neck scaling is changed.
- Fixed a problem with visualization in GRF prediction class which prevented GRF
  prediction to be used with moving base frames (i.e. treadmills).
  Thanks to Marco Antonio Marra (University of Twente) for fixing this.
- Fixed the marker node orientation for BVH (inertial based) MoCap models in the
  CreateMarkerDriver class template. Marker orientations are now handles identical
  to normal C3D based markers.\`\`\`
- Fixed incorrect wrapping of teres minor and teres major at extreme shoulder range of motion. New
  wrapping surfaces have been added. One in Humerus and one on
  scapula. The meet at the glenohumeral joint to prevent the muscles from sliding
  to the wrong side of the humerus.

**Removed:**

- Removed unused support files for muscle contact. `Tools/ModelUtilities/ContactMuscles/*`

## AMMR 2.2.3 (2019-11-13)

[![Zenodo link](https://zenodo.org/badge/DOI/10.5281/zenodo.3521521.svg)](https://doi.org/10.5281/zenodo.3521521)


**Added:**

- Add new option to set the type of wrapping surface used in the deltoid wrapping implementation.
  The following will force the use of cylinders (which is faster) instead of ellipsoids.

  ```{code-block} AnyScriptDoc
  #define BM_ARM_DELTOID_WRAPPING _DELTOID_WRAPPING_CYLINDERS_
  ```

  See {bm_statement}`BM_ARM_DELTOID_WRAPPING` for possible options.

**Fixed:**

- Fixed problems with BVH models that have jumping angular data due to multiple
  solutions to the Euler angle equations when gimbal locks occur.
  The fix requires a new structure of the BVH model,
  where virtual marker trajectories are calculated by the `AnyInputBVH` class.
  See the updated {ref}`BVH_Xsens example <example_adlgait>`,
  and port your existing BVH models to the new example structure.
- Fixed a problem in {ref}`AnyMoCap models <anymocap>`, where model view operations in
  `Main.ModelSetup.Views.SetViewMacros` would not trigger
  a redraw of the model view when executed directly.

**Changed:**

- Increase the time offset when running MoCap inverse dynamics simulations.
  The offset was 2 frames which were skipped at the start/end
  of inverse dynamics simulations. But the accelerations of 4th order
  b-spline are only stable on the fourth frame, and hence the offset
  has been increased to three frames instead of two.
- ScalingXYZ scaling law has been extended to respect the following new variables
  in the `HumanModel.Anthropometrics.SegmentDimensions` folder: (`HeadWidth`, `HeadDepth`,
  `TrunkDepth`, `NeckLength`, `FootWidth`)

**Removed:**

- Remove the joint muscles' strength dependency on the range of motion. Joint
  muscles are the torque actuators embedded in the joints when the model is
  loaded without muscles. Previously, joint muscles would reduce their strength
  to 10% when the joint was outside the range of motion. The lower strength
  outside the range of motion was originally implemented to prevent
  inverse-inverse simulations finding non-physiological solutions. However, this
  problem is now better solved with kinematic joint limits, and the change in
  joint strength could sometimes cause models to fail with a muscle recruitment
  failure.
- Remove the warning for modified Body model files. The warning can still be enabled
  by setting the switch `#define ANYBODY_ENABLE_MODIFIED_AMMR_NOTICE`

**Added:**

- Added a warning to MoCap models when the number of frames is below 8. Since
  the low number of frames causes problems with both low-pass filters and b-spline
  interpolation. *Note:* C3D files with only a single frame works fine since that
  is handled specially and often used for static trials.

## AMMR 2.2.2 (2019-09-12)

[![Zenodo link](https://zenodo.org/badge/DOI/10.5281/zenodo.3404750.svg)](https://doi.org/10.5281/zenodo.3404750)


**Fixed:**

- Fixed kinematic problems when driving specific wrist-flexion/abduction values.
  The definition of wrist flexion in `BodyModel.Interface` now measures the
  flexion between the radius and small artificial `WristJointSeg` segment
  between the radius and the hand segment. This ensures that there is always
  unique solution when driving the wrist flexion and abduction.
- Fixed a bug in the AnyMoCap examples when setting {bm_statement}`BM_SCALING`
  to {bm_constant}`_SCALING_LENGTHMASSFAT_`.
- Fixed a number of smaller bugs with Body Model configuration plugin.
- Fixed a bug in calibration of 3 element leg muscles in the TLEM1 and TLEM2 model. The problem was
  that the first calibration study (`LegCal1`)
  included muscles which were also calibrated specifically in later calibrations. This could in some
  cases (certain scaling) lead to a problem where `LegCal1` would be forces to change the fiber-length
  even though later specific calibration of the muscle did not need that. Now, `LegCal1` only calibrates
  muscles which are not included in the later calibration studies.

**Changed:**

- Changed the posture of the push-up model example to something which looks more natural,
  and reduces the max muscle activity.

## AMMR 2.2.1 (2019-05-13)

[![Zenodo link](https://zenodo.org/badge/DOI/10.5281/zenodo.2657673.svg)](https://doi.org/10.5281/zenodo.2657673)


**Fixed:**

- Fixed a symmetry issue with Scapula scaling in the {bm_constant}`_SCALING_XYZ_` scaling law.
- Fixed a bug in the Knee Simulator example regarding an extra tibiofemoral `AnyForceSurfaceContact`.
- Fixed a bug in how the Conoid driver scales with scapula size.
- Fix bug in reference axes for SacrumPelvis Moment measures in selected output.
  Thanks to Divyaksh Chander from [Politecnico di Torino](https://www.polito.it) for fixing this.
- Attempt to fix muscle wrapping errors with Latissimus dorsi when the model bends forward. This was done
  by increasing the Augmented Lagrangian coefficient  `SPLine.AugLagCoef` value and the using full wrapping solver.
- Fix some muscle wrapping problems with subscapularis muscle by increasing the number of points in the string mesh.
- Fixed minor symmetry issue in the head markers of the Full Body MoCap example.

**Changed:**

- Changed the recruitment criterion to the power of 2 (quadratic) in the two MoCap examples using GRF prediction and weak human-ground residuals.
  ({ref}`link 1 <example_mocap_grf_prediction>`
  and {ref}`link 2 <example_mocap_bvh>`). This greatly increases the robustness of recruitment solver
  and prevents many muscle recruitment failures.

**Added:**

- New options to optimize pelvis-, trunk- and head- widths and depths in the `OptimizeAnthropometricsOnOff` class template.

- Simple library of Python utility functions which can be used from AnyScript. This first version only adds a few
  functions from the Python's `os.path` module. They are used by including the `Python.Utils.any` file:

  ```{code-block} AnyScriptDoc
  #include "<ANYBODY_PATH_MODELUTILS>/Python/Utils.any"

  AnySwitchVar file_exists = PyUtils.os.path.exist("some-file")
  ```

## AMMR 2.2 (2019-04-03)

[![Zenodo link](https://zenodo.org/badge/DOI/10.5281/zenodo.1481635.svg)](https://doi.org/10.5281/zenodo.1481635)


**Added:**

- New implementation of the Deltoid muscles that uses wrapping instead of previous rake-segment/via-point approach.
  The new wrapping deltoid was developed by Marta Strzelczak from
  Ecole de technologie superieure, Montreal, CA. The new implementation is used by default but the old
  implementation can be enabled with the {ammr:bm_statement}`BM_ARM_DELTOID_WRAPPING` switch. Please see the
  {ref}`Shoulder-Arm Documentation <DeltoidWrapping>` for more information.

- Added new example model of a Knee Simulator using a knee implant model and force-dependent kinematics (FDK).
  See the {ref}`Knee Simulator example <example_kneesimulator>`
  for more information.

- New model plugin (BodyModel Configurator) which provides a graphical user interface
  to configure the Body Model (i.e. setting the `BM_*` parameters). Please see
  the [blog post](https://anyscript.org/tools/body-model-configurator/)
  introducing the BM plugin.

- Added a new {ref}`Posture prediction model <example_posture_prediction>`
  based on standing posture. The model can predict posture as a consequence of applied loads in hands.
  It does this by minimizing joint torques and applying balance drivers which account for external applied loads.

- Added new standing model example which uses soft constraints and GRF
  prediction. {ref}`See this link <example_standingmodel>`.
  This new model is good starting point for making
  standing/balancing models, and the corresponding standing model in the template
  generator has also been updated.

- Added new kinematic rhythm to determine the
  Sterno-Clavicular axial rotation, effectively removing
  the degree of freedom from the shoulder model.  The rhythm distributes the
  axial rotation equally between SC and AC joint. The rhythm is active by default, but can be disabled
  with {bm_statement}`BM_ARM_CLAVICULA_ROTATION_RHYTHM` switch.

- More documentation on the {ref}`AnyMoCap framework and the settings available <anymocap-settings>` .

- New measures for shoulder angles based on recommendation from International Society of Biomechanics (ISB). The measures are available in the
  `BodyModel.Interface` folder. The new measures are:

  - `AcromioClavicular` ([Wu et al. 2005] section 2.4.3)

    - `Protraction`
    - `MedialRotation`
    - `PosteriorTilt`

  - `ScapulaHumerus` ([Wu et al. 2005] section 2.4.4)

    - `PlaneOfElevation`
    - `Elevation`
    - `InternalAxialRotation`

  - `ThoraxScapula`  ([Wu et al. 2005] section 2.4.6)

    - `Protraction`
    - `MedialRotation`
    - `PosteriorTilt`

  - `ThoraxHumerus` ([Wu et al. 2005] section 2.4.7)

    - `PlaneOfElevation`
    - `Elevation`
    - `InternalAxialRotation`

- Three new BM switches to control add default drivers for the individual neck degrees of freedom:

  - {bm_statement}`BM_MANNEQUIN_DRIVER_SKULL_THORAX_FLEXION`
  - {bm_statement}`BM_MANNEQUIN_DRIVER_SKULL_THORAX_LATERALBENDING`
  - {bm_statement}`BM_MANNEQUIN_DRIVER_SKULL_THORAX_ROTATION`

- A default center of mass kinematic measure were added

  - `Main.HumanModel.BodyModel.Interface.CenterOfMass`

- Markers in MoCap models now changes color to gray when they drop out (i.e. have a weight of zero).

- Added new `ASIS`/`PSIS`/`PT` bony-landmark nodes to the `PelvisSeg.Right`/`Left` folders.
  This ensures the bony landmarks are easily available as nodes in all models
  even if the legs are not included.

- Added a new setting (`#define MOCAP_FILTER_JOINT_ANGLES ON/OFF`) to the AnyMoCap frame work. If enabled a
  filter will be applied to the intermediate set of joint angles generated by the Marker Tracking step. This
  can be useful to remove high accelerations due to kinematic limit constraints
  (e.g. Joint angle limits, surface contacts etc.).

- Added a `#define MOCAP_PARAMETER_FILE_PREFIX` switch to override the prefix for parameter identification
  files (containing marker position and scaling). This can be useful in special cases where subjects share a
  common parameter identification file.

- Added two new default arguments (`MANNEQUIN_FOLDER`, `BODYMODEL_FOLDER`) to  the
  class_template `Template_MannequinDrivers`, making it easier to reuse the class
  template as a general-purpose driver for all joint angles.

- Added a `PreAnalysis` step to the video recorder template (`CameraClassTemplate.any`).
  Operations placed in the `PreAnalysis` step will be executed before the video recorder starts.

- Added a new warning if using low-pass filters in the AnyMoCap model without a zero phase filter
  (e.g. warn if  `FilterForwardBackwardOnOff` is set to `Off`)

- Added a new option for choosing a different implementation of the kinematic sliding between scapula and thorax.
  The new scapula sliding implementation uses multiple points on the ribs and a norm measures to surfaces on the scapula. This work is
  preparation of a new thoracic model where ribs are individual segments. Note that this implementation is still a work-in-progress. The new
  thorax-scapula contact can be enabled with the {bm_statement}`BM_ARM_THORAX_SCAPULA_CONTACT` switch:

  ```{code-block} AnyScriptDoc
  #define BM_ARM_THORAX_SCAPULA_CONTACT _MULTIPLE_POINT_CONTACT_
  ```

- New `DEFAULT_PARAMETER_FOLDER` class template for creating folders with default values
  which can be overridden. See the following example:

  ```{code-block} AnyScriptDoc
  DEFAULT_PARAMETER_FOLDER Settings(
      NPARAM = 2,
      PARAM_1 = TibialRotation, PARAM_1_TYPE = AnyMat33,
      PARAM_2 = Offset, PARAM_2_TYPE = AnyVar
  ) = {
      // Default values are specified in the defaults folder.
      Default.TibialRotation = RotMat(5*pi/180,y);
      Default.Offset = 0.005;
  };

  // Parameters can now be overridden if desired.
  Settings.TibialRotation = RotMat(10*pi/180,y);
  ```

**Changed:**

- Re-implemented the origins for the Semitendinosus and Biceps Caput Longum muscles in the
  TLEM-2.1 model based on the original digitized insertions and MRI scans. Better
  correspondence with the original MRI scans increases the moment-arms through
  range of motion.

- New wrapping surfaces for Semitendinosus and Biceps Caput Longum muscles based on original MRI scans.
  New surfaces ensure that muscles don't penetrate the pelvis bone at high hip flexion angles.

- Reimplement insertion of Gluteus Medius/Minimus of the TLEM2.1 model based
  on original TLEM2 dataset. This improves range of motion in which Gluteus
  Medius and Gluteus Minimus has a moment arm for internal rotation of the hip.

- Kinematic rhythms for the shoulder, lumber-spine and cervical-spine can now be specified as soft contraints.
  The setting is controlled by setting the BM control statement `BM_XXX RHYTHM` to {bm_constant}`_RHYTHM_SOFT_`.
  For example:

  ```{code-block} AnyScriptDoc
  #define BM_ARM_SHOULDER_RHYTHM _RHYTHM_SOFT_
  ```

- Re-implemented the origins for the Semitendinosus and Biceps Caput Longum muscles in the
  TLEM-2.1 model based on the original digitized insertions and MRI scans. Better
  correspondence with the original MRI scans increases the moment-arms through
  range of motion.

- New wrapping surfaces for Semitendinosus and Biceps Caput Longum muscles based on original MRI scans.
  New surfaces ensure that muscles don't penetrate the pelvis bone at high hip flexion angles.

- Reimplement insertion of Gluteus Medius/Minimus of the TLEM2.1 model based
  on original TLEM2 dataset. This improves range of motion in which Gluteus
  Medius and Gluteus Minimus has a moment arm for internal rotation of the hip.

- The {doc}`TLEM2 model</body/leg_tlem2_model>` is now the default leg model unless the model is configured otherwise.

- All AnyMoCap examples where changed to use the {bm_constant}`_SCALING_XYZ_` scaling law. This scaling law is
  similar to {bm_constant}`_SCALING_LENGTHMASSFAT_`, but allows for optimization of all segment dimensions
  (hence the `XYZ` name).

- Scaling law {ammr:bm_constant}`_SCALING_XYZ_` now has a scaling factors to
  control the neck scaling. Before neck scaling were controlled by
  the head scale factors.

- All MoCap model examples now use the option (`UseC3DWeightResiduals=ON`) in the marker protocols.
  This ensures that the marker weights are reduced to zero when a marker drops out (i.e. when the residual value in
  the C3D file becomes negative).

- AnyMoCap examples are updated with extra margin at the start/end of the analysis compared to the data in the
  C3D file. This prevents inaccurate kinematics due to low-pass filter transients.

- Add warning to AnyMoCap models when `tStart`/`tEnd` are very close to the start/end times of the
  data in the C3D file. This can cause inaccurate kinematics at the very start/end of the simulation due
  to low-pass filter transients.

- Increased the resolution tibia bones for the TLEM1 and TLEM2 models.

- All examples now have their body model configuration in a separate file
  (usually, `BodyModelConfiguration.any`) to accommodate the new Body Model
  Configurator plugin.

- The MoCap models now use joint angles for all degrees of freedom when transferring
  motion from MarkerTracking study to the Inverse dynamic study. This means that rhythms can now be
  soft constraints when running the Marker tracking study, and markers can override the kinematic
  rhythms if needed.

- Refactored all examples to avoid the confusing paradigm with a reference called `Model.HumanModel`
  pointing to `HumanModel.BodyModel`.

- Improvements to the accuracy of the wrapping cylinder used by Teres Minor and Teres Major.

- The interface morphing algorithm (which morphs pelvis of the trunk or leg dataset to match)
  now includes the ASIS/PSIS/PT bony landmarks as control points. This change ensures that
  bony-landmarks of the Trunk and Leg datasets map to the exact same point.

- Models generated from templates now fail with a descriptive error message if they are loaded with
  an older unsupported version of the AMMR.

**Fixed:**

- Fixed problem with the initial guess for Vastus wrapping which could cause
  the Vastus muscle to wrap incorrectly when the knee started in slightly over
  stretched posture.
- Fixed location of bicep longus via points to pass through bicipital groove
- Fixed a regression in bike model where the foot crank connection did not rotate around
  the correct point (`PedalConnectNode`). The point in the foot coordinate system
  was also updated to a more posteriorly location beneath the meta tarsal joints.
- Fixed an issue with over-constraint default mannequin drivers when shoulder
  rhythm was enabled. Now the default mannequin drivers will not create
  drivers for sterno-clavicular rotation, elevation, protraction when the
  shoulder rhythm is enabled.
- Fixed the initial wrapping guess for Teres Minor to prevent incorrect wrapping when
  starting model in postures which are close to range of motion.
- Fixed typo in `Flexor_Digitorum_Profundus_Digit5` name.
- Fixed an interpolation issue with BVH based AnyMoCap models when the models
  were using all frames in a BVH file.
- Added missing hand length/breadth values needed by Detailed Hand to the `CustomScaling.any` for custom scaling scenarios
- Fixed missing possibility for overriding the reaction forces for the Trunk flexion/extension/rotation
  drivers in `HumanModel.DefaultMannequinDrivers`.
- Add missing strength scaling factor to `pectoralis_major_thoracic_part_3` in the simple muscle configuration.
- Fixed issue with the {ref}`Standing Model example <example_standingmodel>`,
  where the elbow flexion velocity was incorrectly set to a non zero value.
- Fixed the problem with over-constraint models when adding the
  shoulder rhythm.
- Fixed a bug with the Video class (`CameraClassTemplate.any`) when specifying direct path to ffmpeg.
- Fixed a problem with the FullBody AnyMoCap example where a relative high weight
  on the soft clavicula rotation constraints could cause the model to fail
  kinematically in with the AnyBody Modeling System 7.2.

**Removed:**

- Removed previously deprecated MoCap model which were not based on the AnyMoCap framework.

- Removed all references to the previously deprecated `BM_TRUNK_NECK` switch.

- Removed outdated versions of `JointLimits_template.any` and `KinLimitsDriver_template.any` from the AnyMoCap folder.
  Updated version of the files still exists in the `Tools\ModelUtilities\KinematicLimits` folder.

- All uses of the Sterno-Clavicular axial rotation in all examples, since this
  DOF is now handled by a kinematic rhythm which distributes the
  rotation equally between SC and AC joint.

- The `BM_MANNEQUIN_DRIVER_INDIVIDUAL_WEIGHTS` switch was removed, since the individual weights can be set directly using

  ```{code-block} AnyScriptDoc
  Main.HumanModel.DefaultMannequinDrivers.KneeDriverRight.WeakDriverWeight = 0.1;
  ```

## AMMR 2.1.1 (2018-06-12)

[![Zenodo link](https://zenodo.org/badge/DOI/10.5281/zenodo.1287730.svg)](https://doi.org/10.5281/zenodo.1287730)

The AMMR 2.1.1 version is a minor release of the AMMR with smaller changes and bugfixes.
The AnyBody Managed Model Repository now has a DOI ([10.5281/zenodo.1250764](https://doi.org/10.5281/zenodo.1250764)).
This is handled by [Zenodo.org](https://zenodo.org/) (The European Open Science platform hosted at CERN).

**Added:**

- Added a `Leg.Seg.Foot.GroundJoint` RefNode to the foot segment of the TLEM2 model. This RefNode was
  also present in the TLEM1 model and was used by few applications.
- New `GroundVelocity` setting added to the `ForcePlateAutoDetection` class_template, which
  makes class usable with instrumented treadmills.
- All force plate types now have a user-definable `ForcePlate.CalMatrix` variable. The feature is useful to
  easily compensate for errors in the c3d file (i.e. swapped channel and wrong sign)

**Changed:**

- Enhanced the {ref}`multi-trial MoCap example
  <example_mocap_multitrial>` for best practice for
  MoCap trials with multiple subjects and trials. The example now shows how to deal with multiple
  subjects and storing the c3d files in a separate folder.

**Fixed:**

- Corrected the default mass of the patella segment in the TLEM2 model from zero to 0.025.

- Add missing unilateral reaction between TS node on Scapula and the Thorax when using the shoulder rhythm.

- Adjusted the initial wrapping vectors for the semitendinosus,
  semimembranosus, and biceps caput breve muscles around the knee. This has no
  influence on the output of the model, and is only done to reduce the risk of
  the muscles wrapping the wrong direction around the wrapping surface.

- AnyMoCap:

  - The high memory usage of the AnyMoCap BVH model has been fixed. The high memory usage was due to a reference in the `CreateMarkerDriver` class template
    which caused the studies to include the BVH input data multiple times in the output.
  - The BVH and multi-trial examples now use zero phase shift filtering of force plate forces.
    The zero-phase filter can be important to ensure that forces are synchronized with kinematic data.
  - Fix bug in Type 1 Force plate when data is not in meters (i.e. `PointScaleFactor != 1`).
    The PointScaleFactor was applied twice to the z moment component.
  - Fix a problem reading C3D files where force plate meta information
    is saved with the wrong dimensionality. Such a issue can, for example, happen if the c3d files
    are created manually in MATLAB.
  - The option to load parameter optimization results is no longer hidden when the
    `MOCAP_CREATE_PARAMETER_ID_SHORTCUT` is set to `OFF`.

## AMMR 2.1.0 (2018-03-22)

[![Zenodo link](https://zenodo.org/badge/DOI/10.5281/zenodo.1251276.svg)](https://doi.org/10.5281/zenodo.1251276)

**Added:**

- New {ref}`squat example <example_squat>`
  model which demonstrates a parameterized squatting motion.

- New `#class_template` for adding limit drivers to kinematic measures.
  Can be included with `#include "<ANYBODY_PATH_MODELUTILS>/KinematicLimits/KinLimit_template.any"`

- Muscle ColorScale can now be set from the `Main.DrawSettings.Muscles.ColorScale`.
  If you port an older model to the new AMMR you will need to update your `DrawSettings.any`
  file.

- AnyMoCap framework:

  - New argument `DRAW_SCALE` in the `CreateMarkerDriver` class_template to control the visual size of markers.
  - Added an option to the ForcePlateAutoDetection class template to make the limb1/2 contact detection
    mutually exclusive. Setting the option `ALLOW_MULTI_LIMB_CONTACT=OFF` will ensure that both legs cant
    be in contact with the plate at the same time. This can prevent accidental contact detection
    for the collateral leg in the swing phase.
  - New option to specify the contact nodes in ForcePlateAutoDetection class template. This makes the class useful
    for connecting force plate to other limbs than the feet.
  - Add support for the Shoulder Rhythm in AnyMoCap based models.
  - Add support for the {doc}`/body/detailed_hand_model` in AnyMoCap based models.

- New `BM_FOOT_MODEL` parameter, as preparation for integrating the Glasgow-Maastricht foot model (GM-Foot) back into the AMMR.
  Currently, the parameter can only be used for excluding the feet  (`#define BM_FOOT_MODEL _FOOT_MODEL_NONE_`).
  making it easier to work on integrating  the GM foot model.

:::{seealso}
Adding the GM-Foot to the TLEM2 model is a work in progress. An early version is
released on GitHub: <https://github.com/AnyBody/gm-foot>
:::

**Changed:**

- Default mannequin drivers for the Pelvis are changed to drive the Pelvis
  anatomical frame instead of the segmental reference frame. This also fixes the
  discrepancy between the load time position and the mannequin driver position and
  makes the driver consistent with the interface measures
  `BodyModel.Interface.Trunk.PelvisPosX/Y/Z`.

:::{warning}
This change will affect models using the default mannequin drivers unless
the driver values are updated.
:::

- The Wilke spine pressure  validation examples have been updated and now uses
  the TLEM2 lower extremity model.

- In {bm_constant}`_SCALING_XYZ_` scaling law the definition of
  length/depth/width of the scapula is corrected to match the anatomical
  definitions.

- Updated the AAU Mandible Model introduced in AMMR 2.0.0. By accident the authors did
  not share the exact same version of the model that was used in the publication by
  [Andersen et al. 2017](https://doi.org/10.1115/1.4037100)
  This is now corrected and the validation  example produces the same results as
  published version.

- TLEM 2 model

  - Pectineus implementation has been adjusted based on the original MRI
    Scans. Only the most lateral element of the pectineus muscle was changed. This
    was done to prevent it from penetrating the femoral head in some situations.
  - Tweaked the Gluteus Maximum Superior implementation to reduce the risk of
    collisions between muscle insertions and the wrapping surface. The two most
    proximal insertion points of the Gluteus Superior are shifted more distally, and
    the locations of the wrapping surfaces are tweaked.

- AnyMoCap Framework:

  - Models now uses the default kinematic solver for the inverse dynamic analysis.
  - Changed the set joint drivers used for transferring the
    joint angles from the over-determinate marker tracking to the inverse dynamic analysis.
    To improve the stability of the scapula kinematics the Scapula Thorax Elevation angle is
    used instead of the sterno clavicula elevation angle.
  - Changed the way marker drivers are excluded from the Inverse Dynamic analysis.
    The drivers are now excluded using the new `AnyMechObjectExcluder` class instead of
    the `MechObjectExlcude` member of the Study. This has no practical effect on model output
    but means that the `MechObjectExlcude` can now be assigned by the users.
  - Update to the BVH MoCap example. Pre-processing the BVH data is now a separate operation which saves the
    virtual marker positions to a file. Thus, this step can be skipped the next
    time the model is reloaded.
  - Changed the AnyMoCap Multi trial example `Plug-in-gait_MultiTrial_StandingRef` to
    make it a better starting point for creating new models. 1. Moved the
    Human-Ground residuals from the Trunk to the Pelvis segment. 2. Use the TLEM
    2 lower body model in the example. 3. Disable upper bounds for the muscle
    recruitment `Criterion.UpperBoundOnOff = Off;` to improve the stability of
    the simulations.

**Fixed:**

- Shoulder-arm model:

  - Fixed problems with Pectoralis Major wrapping. Wrapping could fail unpredictively when
    muscles wrapped in the intersection between the coracoid wrapping and pectoralis
    minor cylinder. The coracoid wrapping cylinder has been removed, and the
    others has been made longer. This creates a more robust wrapping for the
    Pectoralis Major muscle.
  - Better initial position for scapula and clavicula. The initial position is now calculated
    from the initial position of the chain from thorax through the clavicula to
    scapula. This will not change the model output but should make the arm model
    more robust solving the first step.
  - Improve the Teres Minor wrapping by adjusting the
    wrapping surface, and ensure that the insertion point is not directly on the surface.
  - The "Evaluate joint strength" studies now also work when the shoulder rhythm is enabled.
  - Fixed problems with via points of the wrist extensor muscles colliding with the wrist
    wrapping surface in normal range of motion. The via point of Extensor indicis
    `Via_Extensor_Indicis_pos` has been slightly adjusted and the location of
    the wrist wrapping cylinder `MedialExtensorCyl` has been improved.

- Detailed hand model:

  - Fix a problem causing the hand to scale incorrectly.
  - Fix a problem with the default mannequin drivers for the left
    thumb, where CMC  and MCP abduction was treated as adduction.
  - Fixed compatibility between the detailed hand and scaling law {bm_constant}`_SCALING_XYZ_`.

- Lower extremity models:

  - Fixed various warnings when running calibration routines with the lower extremity models.
  - Fixed muscle insertions for the old leg model (`#define BM_LEG_MODEL _LEG_MODEL_LEG_`).
    The misaligned pelvis muscles insertions was a regression due to the updated
    Trunk pelvis introduced in AMMR 2.0. The pelvis muscles insertions have been
    translated and rotated to fit the new Trunk geometry as best as possible.
  - Fix missing left leg calibration operations when right leg was excluded.

- MoCap models:

  - Weak residuals for GRF prediction: Ensure the same strength is used in all directions for
    the weak recruited actuators.
  - Fix bug in `CreateMarkerDriver` class template which prevented the
    `UseC3DWeightResiduals` from having any effect.
  - Fix the wrong visualization of the contact area in ground reaction force
    prediction class template, when the base frame is different from the global
    coordinate system.
  - Wrong masses in the deprecated "old" MOCAP models. The model was not using the
    body mass specified in `Main.TrialSpecificData.Anthropometrics.BodyMass`

- Other fixes:

  - Wrapping convergence for multiple muscles has been improved. This was done by
    tweaking the string-mesh of the muscles to improve the wrapping solvers ability to find
    the solution within the given number of iterations.

## AMMR 2.0.0 (2017-11-29)

[![Zenodo link](https://zenodo.org/badge/DOI/10.5281/zenodo.1251274.svg)](https://doi.org/10.5281/zenodo.1251274)

### Major changes:

#### New lower extremity model (TLEM2.1)

- The [Twente Lower Extremity Model version 2.0 dataset](https://doi.org/10.1016/j.jbiomech.2014.12.034), developed in the
  TLEM*safe* EU project was implemented in the AMMR repository. The model is not
  the default model, but can be enabled with the {ref}`BM parameter
  <bm-config>` `#define BM_LEG_MODEL _LEG_MODEL_TLEM2_`

- The model is versioned TLEM 2.1, to indicate the number of changes and
  correction which has been added in the process. The changes and updates to the
  TLEM2 dataset was done in the [Life Long Joints](https://lifelongjoints.eu/) EU research project (paper submitted for publication).

- The most important changes to the TLEM 2 dataset include the following:

  - Updated wrapping for the Gluteus Maximus, Iliacus, Psoas around the hip.
  - Reworked muscle topology for Gluteus Medius and Gluteus Minimus
  - Updated wrapping for Hamstring muscles, and Gastrocnemius around the knee.
  - Redefined revolute knee axis and patella joint axis and patella tendon length based on the bone   geometry.
    The original TLEM knee axis was estimated using a functional method, and was only valid
    for very small flexion angles.
    Thanks to Marco Antonio Marra (Radboudumc) for this for this improvement.
   - The  ratio of volume between Gluteus Maximus superior/inferior has been re-estimated
     based on the original cadaver MRI scans.
   - Update the Sartorius via points.
   - Re-implemented the Hip Joint location for the pelvis and the femur by fitting spheres to
     the femoral head and the acetabulum. This is in contrast to the original TLEM2.0 implementation
     where the hip joint center was found using a functional method.
   - Included a more detailed version of the patella bone.
   - Various minor bug fixes from the original implementation used in the TLEMSafe project.
   - Corrected the femoral attachment points for the popliteus muscle
   - Update ankle joint nodes with positions fitted to the bone geometry
   - Small correction to wrong insertion points for Adductor Longus and Vastus Medialis.

- See the dedicated {doc}`TLEM2.1 page </body/leg_tlem2_model>` page for more information.

#### AnyMoCap

- New framework for running MoCap models. The AnyMoCap framework is an effort to
  create a simple and unified framework for doing any kind of MoCap analysis with
  the AnyBody Modeling System. See the {ref}`AnyMoCap example gallery <mocap_examples>`
  for more information.
- Algorithms and file for Ground reaction force prediction are added to: `ammr/tools/GRFPrediction/`.
  See the
  {ref}`MoCap examples <example_mocap_grf_prediction>`
  for how they are used.

#### TLEM 1 updates

- The cumulated smaller bug fixes and updates to the TLEM1 model mean that we now
  denote the model 1.2.
- Changed the position of the Heel contact node, to align the heights of the
  TLEM1 and TLEM2 models.
- Added missing `GeomScale` function to the patella
  segment.
- Update ankle joint nodes with positions fitted to the bone geometry
- PSCA is now calculated based on the scaled fiber length. This aligns
  the TLEM 1 model with the new TLEM 2 model. It also means that scaling the model
  without changing the muscle volumes will change the strength of the model.
- Update scaling of the Patella tendon to work with non-linear scaling laws.
- Added visualization of the Fibula bone.

#### AMMR restructure

- Added a top-level `Tools` folder helper files and other models which don't belong in `Body/` or `Application`.
- Moved `Body/AAUHuman/Toolbox` to `Tools/ModelUtilities`
- Renamed the `Body/AUHuman` to `Body/Mandible_AU`
- Restructured the anthropometric ("AnyMan") folder.  The folder `HumanModel.AnthroDataSubject` is renamed to
  `HumanModel.Anthropometics`. The structure of the folder has also changed with a `SegmentDimensions` and `SegmentMasses` subfolder.

#### Configuration parameters

- The previously used system to configure human body using a BodyPartSetup file was completely
  replaced with the new body model (BM) parameters.
- Please see the documentation on: {ref}`BM parameters <bm-config>`.

#### Scaling laws

- An additional scaling law based on individual segmental scaling factors was added to the
  repository. It can be enabled using this {ref}`BM parameter<bm-config>` `#define BM_SCALING _SCALING_XYZ_`.
  See the {ref}`guide on scaling <scaling-intro>`.
- Default scaling is now {any}`_SCALING_STANDARD_` (e.g  `#define BM_SCALING _SCALING_STANDARD_`)
  which scales all models to default standard 50% male.
- Introduced {any}`_SCALING_NONE_`, which disables scaling. E.g. models gets the original unscaled size.

#### New Mandible model

- Added new mandible model based on a CT scan of a 40 year old male.
  For more information see {doc}`the documentation for the model </body/aalborg_mandible>` or the
  {ref}`validation example <example_aalborgmandible>`.

#### Spine model

- {ref}`BM parameters <bm-trunk-config>` were updated to have control over each section of the spine and relevant components.
- The anatomical reference frame of the thorax segment was modified. This change reflects a change
  in the pelvic anatomical reference, and ensures upright posture for the standing postures, to
  align C1C0 joint with the hip joint centers.
- Boney surfaces of both pelvis and sacrum were updated and now correspond better to the relevant
  muscle attachments. These segments now also share a common scaling function. Hip joint centers
  were corrected for the old Leg model.
- Improved wrapping surface for Psoas Major muscles based on the TLEM2.0 MR scans
- Insertion, via, and attachment nodes of relevant muscles have been updated to match new geometries
  of pelvis and sacrum.

#### Arm model

- The model now facilitates individual personalization for each side using nonlinear morphing schemes
  in a more consistent manner. Previously the morphing needed to be done on the right side and then
  reflect to have the left side morphing. This change removes an extra mirroring step.
- Arm calibration was updated
- {ref}`BM parameters <bm-arm-config>` have been updated for more convenient use. `BM_ARM_DETAILED_HAND` and
  `BM_ARM_SHOULDER_RHYTHM` are now used instead of individual switches for right and left side, which were deprecated.
- Muscle wrapping surfaces were updated for more physiological behavior.
- Scapula reaction contact forces were simplified, and do not longer utilize slider segments.
- Conoid ligament length now scales along with the scapula width.
- Add a `GeomScale` function the Clavicula segment.

#### Muscle models

- All muscle models are updated to support the structure of the new
  `AnyMuscleModel3E` and `AnyMuscleModel` in the AnyBody Modeling System 7.1.
  The following variables are renamed:

  > - The "optimal fiber length" variable renamed from `Lfbar` to `Lf0`
  > - The "Pennation angle" variable renamed from `Gammabar` to `Gamma0`
  > - The "Tendon strain at F0" variable renamed from `Epsilonbar` to `Epsilon0`

- Restructured the muscle model section of both TLEM1 and TLEM2 models.

  - All the original TLEM based muscle parameter are now located under: `Leg/ModelParameters/Muscles`

  - All scaled muscle parameters are located in `Leg/MusPar/SubjectMusPar`. This folder references
    the TLEM muscle and applies strength scaling etc. The `SubjectMusPar` folder and all subfolders are
    implemented with `class_template`. Thus, all muscle parameter can now be overridden in applications
    by just assigning the variables a new value: E.g.

    ```{code-block} AnyScriptDoc
    Main.HumanModel.BodyModel.Right.Leg.MusPar.SubjectMusPar = {
      GastrocnemiusMedialis.MuscleVolume = 300; // Volume in mililiters
      GastrocnemiusMedialis.Pennationangle = 15; // (in degrees)
    };
    ```

#### Calibration

- Updated calibration for Arms and TLEM legs in the Body Model to

  > - include muscles to the calibration study with search functions.
  > - drive the postures using the measures from the interface folder to remain anatomically
  >   similar throughout future versions.

- Added new **experimental** two-parameter calibration, which is based on range-of-motion postures.
  The calibration type is controlled by the {any}`BM_CALIBRATION_TYPE` parameter.

  For example:

  ```{code-block} AnyScriptDoc
  #define BM_CALIBRATION_TYPE _CALIBRATION_TYPE_2PAR_
  ```

### Minor Changes:

- Added new initial guess for wrapping muscles, which make the wrapping
  more when the model starts in extreme postures.

- Update many examples to use the TLEM 2.1 model. See the {ref}`example gallery <example-gallery>`.

- BM mannequin drivers are now implemented with a class_template allowing all weights and other settings to be customized.

- A default `HumanModel.Mannequin` folder is now automatically created with a `class_template` when no user-defined Mannequin file is set.

- A default `Main.DrawSettings` folder is now automatically created with a
  `class_template` when no user-defined {bm_statement}`DrawSettings
  <BM_DRAWSETTINGS_FILE>` file is set.

- Extra Mannequin drivers for the individual shoulder degrees of freedom:
  {any}`Sterno clavicula protraction <BM_MANNEQUIN_DRIVER_STERNOCLAVICULAR_PROTRACTION_RIGHT>`,
  {any}`Sterno clavicula elevation <BM_MANNEQUIN_DRIVER_STERNOCLAVICULAR_ELEVATION_RIGHT>`,
  {any}`Sterno clavicula axial rotation <BM_MANNEQUIN_DRIVER_STERNOCLAVICULAR_AXIAL_ROTATION_RIGHT>`

- The initial positions of the pelvis now use the anatomical reference frame.
  This follows the logic from the initial rotation of the pelvis which also uses
  the anatomical frame.

- DeltoidMuscleConnector segment loading time positioning now depends on the Humerus segment.

- Added [class template to easily create videos from AnyScript model](https://anyscript.org/tips-n-tricks/creating-videos-from-your-simulations/).
  The tool requires that [FFmpeg](https://www.ffmpeg.org/) is installed.
  The class template can be found in: `<ANYBODY_PATH_MODELUTILS>/Video/CameraClassTemplate.any`.
  See [this blog post](https://anyscript.org/tips-n-tricks/creating-videos-from-your-simulations/).

- In TLEM models make the opacity of the patellar tendon dependent on the opacity of the patellar surface.

- New `AnyDoc` classes are added to the different body model, so the GUI
  can create direct links to the documentation.

- Simplify the Scapular reactions to the thorax segment.

- Foot contact nodes are aligned with the AnatomicalFrame

- Updated the Wilke Validation example to reflect the forces for the AMMR 2.0 repository.

- Updates to BM parameters:

  - New {bm_statement}`BM_ARM_DETAILED_HAND` parameter for the detailed hand.
    The old `BM_ARM_DETAIL_HAND_RIGHT`/`LEFT` are deprecated.
  - New {bm_statement}`BM_ARM_SHOULDER_RHYTHM` parameter for controlling the shoulder rhythm.
    The old `BM_ARM_SHOULDER_RHYTHM_RIGHT`/`LEFT` are deprecated.
  - Added new `BM_JOINT_TYPE_<joint>_<side>` parameter for completely
    disabling joint and associated nodes in the lower extremity models. (See:
    for example {bm_statement}`BM_JOINT_TYPE_HIP_RIGHT`)
  - New {bm_statement}`BM_LEG_MODEL` parameter for setting the type of leg model
    used. The {bm_statement}`BM_LEG_RIGHT`/{bm_statement}`LEFT <BM_LEG_LEFT>` are
    now only {bm_constant}`ON`/{bm_constant}`OFF` options.

### Fixed:

- Sign for the plantar flexion variable were reversed in some section of the
  model. This has been fixed.
- Bug in Mannequin drivers for the neck, where velocities were not set correctly.
  (Thanks to Assoc. Prof. Michael Skipper Andersen for reporting this)
- Fix small bug preventing `StandingModelScalingDisplay` from loading when using
  the {ref}`Leg <old-leg-model>` model.
- Fixed the opacity of the patellar surface in TLEM models, which pointing
  erroneously to the opacity of the talus.
- Fixed wrong symmetry of nodes on the C7 segment of full neck model.
- Latissimus Dorsi 5 fascicle was missing in `MuscleNames.any`  and thus from
  many symmetry measures.
- Fixed a symmetry problem for the Deltoid muscles at the shoulder.
- Fixed a symmetry problem for the Disc stiffness from L1 to L5
- Fix white surfaces in examples with flat STL surfaces. For example
  {ref}`example_crosstrainer`.
- Fixed an issue preventing
  {ref}`example_standingmodel`
  from working with one leg.
- Fixed a problem with the drawings of the bones in the Arm model which were not
  always symmetrical.
- Fixed symmetry issues in scaling laws for scapula and clavicula,
  and humerus.
- Fixed a bug where a the Pectoralis wrapping cylinder was not a included in the calibration study.
- Fixed wrong sign for the AnklePlantarFlexion variable.
- Added missing GeomScale and AnatomicalFrame for Ulna segment.
- Fixed ScalingCustom.any to use Thorax folder instead of Trunk.

### Removed:

- Old MoCap examples have been moved to `Application/Examples/Deprecated`
- Removed the deprecated AMMR1.4 hip rotation sequences.
- The GM-foot model. A new version of this in the pipeline. Contact us if you are
  interested in this work.
- All older BodyModels which were deprecated in AMMR1.3


[wu et al. 2005]: https://isbweb.org/images/documents/standards/Wu%20et%20al%20J%20Biomech%2038%20(2005)%20981%E2%80%93992.pdf 
