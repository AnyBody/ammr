(anymocap)=

# The AnyMoCap Framework

The AnyMoCap model is an effort to create a simple and unified framework for
doing any kind of MoCap analysis with the [AnyBody Modeling
System](https://anybodytech.com).

:::{figure-md} 
:align: center

<img src="/_static/anymocap.jpg" width="50%">

Making MoCap models the easier
:::

## Features

- Adapts to any Mocap protocol
- Optimization of marker locations and anthropometrics.
- Support Marker based (C3D) and inertial based (BVH) input.
- Support for standard force plates: (Types 1-4) plus more.
- {doc}`Prediction of ground reaction forces <grf-prediction>`
- Easy setup with multiple trials and subjects

```{toctree}
:hidden: true
:maxdepth: 2

grf-prediction
```

## Over determinate kinematic analysis

Musculoskeletal models that use Motion capture data are different from other
types of models found the AMMR.  Most importantly, MoCap models usually require
an over-determinate kinematic solver to handle the excess in information that
the optical markers provide.

The over-determinate solver in AMS works great, but
it can only find velocities and accelerations numerically. That has some
performance issue when running inverse dynamics analysis. To overcome the
problem, the MoCap analysis is split into a two-step procedure, as illustrated on
the figure below:

(anymocap-flow-figure)=

:::{figure} /Applications/Mocap/anymocap_flow.png
Figure 1: The framework of the AnyMoCap model. Analysis is split into three
steps. *Parameter identification*, *Marker tracking*, *Inverse dynamic
analysis*.
:::

The over determinate kinematic analysis solves the model for positions, and
writes joint angles to a a set of files. These joint angles can then be used
with the determinate kinematic solver in the inverse dynamic analysis.

:::{seealso}
The AnyBody tutorials, and the lesson on using the
{doc}`AnyMoCap model <tutorials:Making_things_move/lesson5>`
:::

## AnyMoCap examples

The following gallery shows different examples using the AnyMoCap framework.

```{eval-rst}
.. include:: /auto_examples/backreferences/gallery.anymocap.examples
```

```{raw} html
<div style='clear:both'></div>
```

:::{note}
The *Multi trial MoCap model* is likely the best starting point when
working with many trials/subjects from a MoCap experiment.
:::

```{rst-class} emphasize-children
```

## Get started

The easiest way to get started, is to adapt one the example application above.

A typical application using the AnyMoCap framework will look something like this:

```{code-block} AnyScriptDoc
:linenos: true

 #include "../libdef.any"

 #path MOCAP_TRIAL_SPECIFIC_DATA "TrialSpecificData.any"
 #path MOCAP_SUBJECT_SPECIFIC_DATA "SubjectSpecificData.any"
 #path MOCAP_LAB_SPECIFIC_DATA "LabSpecificData.any"

 // Include the AnyMoCap Framwork
 #include "<ANYMOCAP_MODEL>"
```

You can place this main file anywhere on your computer as long the
`libdef.any` file points to model repository (AMMR) you want to use.

:::{caution}
It is recommended *not* to place working models inside the AMMR folder.
Copy the example elsewhere before using.
:::

### Model structure

When loading the AnyMoCap model the following layout shows up in the model tree:

:::{figure} model-structure.png
:::

```{rst-class} html-toggle
```

#### Description of Model folders

```{rst-class} plain
```

```{eval-rst}
.. table:: Top-level model structure

    ======================================= ==============================================================================================
    Folder name                             Description
    ======================================= ==============================================================================================
    ``ModelSetup``                          Contains contains all the machinery of the AnyMoCap Frame.
    ``HumanModel``                          Contain the Human model used. This is constructed automatically by the AnyMoCap framework.
    ``Main.EnvironmentModel``               Contains the model parts which are not part of the Human model. (e.g.  force plate and environment)
    ``Studies``                             Contains the three studies ``ParameterIdentification``, ``MarkerTracking``, and
                                            ``InverseDynamicStudy``. See :ref:`figure 1 <AnyMoCap-flow-figure>`.
    ``DrawSettings``                        Contains visual and color settings for the model.
    ``RunParameterIdentification``          Operation to run the Parameter Identification study and save the results.
    ``RunAnalysis``                         Operation to 1. load the optimized parameters (scaling and marker positions), 2. run marker
                                            tracking and finally 3. run inverse dynamics analysis, 4. save results to and HDF5 file for later replay.
    ``LoadAndReplay``                       This loads any previously saved data and starts the replay operation.
    ======================================= ==============================================================================================

```

(anymocap-settings)=

```{rst-class} emphasize-children
```

## Options and settings

The `Main.ModelSetup` folder contains the main machinery of the *AnyMoCap*
framework. It is controlled by a number of settings both `#define`/`#path` switches
and variables which can be set directly. For example:

```AnyScriptDoc
#define MOCAP_INPUT_DATA_TYPE "C3D"

Main.ModelSetup.TrialSpecificData.LastFrame = 240;
```

The following two sections gives an overview of the settings available:

```{rst-class} html-toggle
```

### Paths settings and switches

Path settings and switches are usually prefixed by `MOCAP_` to indicate that
they are specific to the AnyMoCap framework.

```{eval-rst}
.. table:: ``#path`` settings for AnyMoCap.

    ======================================= ============================================================================================== ========================================
    Settings                                Description                                                                                    Default
    ======================================= ============================================================================================== ========================================
    ``MOCAP_TRIAL_SPECIFIC_DATA``           Path to a file with trial specific data. This file is include within the                       None
                                            ``Main.ModelSetup.TrialSpecificData`` folder.
    ``MOCAP_SUBJECT_SPECIFIC_DATA``         Path to a file with subject/session specific data. This file is include within the             None
                                            ``Main.ModelSetup.SubjectSpecificData`` folder.
    ``MOCAP_LAB_SPECIFIC_DATA``             Path to a file with laboratory specific data (i.e. data common for the whole model or          None
                                            experimental setup. This file is include within the ``Main.ModelSetup.LabSpecificData``
                                            folder.
    ``MOCAP_C3DSETTINGS``                   A file with setting for the C3D file.                                                          None

    ``MOCAP_BVHSETTINGS``                   A file with setting for the C3D file.                                                          None
    ``MOCAP_EXTRA_DRIVERS_FILE``            A file with user defined extra drivers. Additional drivers are useful/necessary                None
                                            in some cases where the marker protocol doesn't provide enough information
                                            to specify all degrees of freedom. Hence, these drivers complement a
                                            specific driver protocol. This file is included in ``Main.ModelSetup.MoCapExtraDrivers``
    ``MOCAP_MARKER_PROTOCOL_FILE``          A file with the definition of the marker protocol.                                             None
                                            This file is included in ``Main.ModelSetup.MoCapDrivers``
    ``BODY_MODEL_CONFIG_FILE``              A file with the body model configuration.                                                      None
    ``MOCAP_FORCE_PLATE_FILE``              A file with the definition of the force plates.                                                None
    ``MOCAP_C3D_DATA_PATH``                 Path to folder where C3D files are stored.                                                     Main file directory
    ``ANYMOCAP_MODEL_PATH``                 Path to the AnyMoCap framework.                                                                The AnyMoCap implementation in the AMMR
    ``ANYBODY_PATH_OUTPUT``                 Path to where output files are saved.                                                          The main file directory
    ``TEMP_PATH``                           Path to where temporary files are saved (joint angles etc.)                                    ``ANYBODY_PATH_OUTPUT``
    ======================================= ============================================================================================== ========================================


```

```{eval-rst}
.. table:: ``#define`` settings for AnyMoCap.

    ============================================== ============================================================================================== ========================================
    Setting                                        Description                                                                                    Default value
    ============================================== ============================================================================================== ========================================
    ``MOCAP_INPUT_DATA_TYPE``                      Data type ("C3D", "BVH") used by the AnyMoCap application.                                     "C3D"
    ``MOCAP_CREATE_PARAMETER_ID_SHORTCUT``         Setting for creating the ``Main.RunParameterIdentification`` shortcut operation  .             ON
    ``MOCAP_OUTPUT_FILENAME_PREFIX``               Prefix added to all output files from the model.                                               ""
    ``MOCAP_PARAMETER_FILE_PREFIX``                Prefix for the parameter identfication files. Can be usefull to set explicitly                 ``MOCAP_OUTPUT_FILENAME_PREFIX``
                                                   in special cases where subjects share a common parameter file.
    ``MOCAP_USE_GRF_PREDICTION``                   Switch to indicate that the model uses Ground Reaction Force (GRF) prediction. It will ensure  OFF
                                                   that the AnyMoCap framework uses the appropriate settings. (e.g. recruited actuators as weak
                                                   residuals on the pelvis.
    ``MOCAP_FILTER_JOINT_ANGLES``                  Switch to enable extra low pass filtering of the output from the Marker tracking. Useful in    OFF
                                                   some cases where other drivers (e.g. joint limits) cause high accelerations in the output
                                                   from Marker tracking.
    ``MOCAP_HIDE_UPPERBODY``                       Switch hide the upper body (Thorax, neck, arms and skull).                                     OFF
    ``MOCAP_HUMAN_GROUND_RESIDUALS``               The type of Human Ground residuals (Hand of God) used. Possible values are                     "Pelvis"
                                                   "Pelvis", "Thorax", "PelvisWeak". "PelvisWeak" is default when using GRF prediction.
    ============================================== ============================================================================================== ========================================


```

```{rst-class} html-toggle
```

### Configurable variables

The `Main.ModelSetup` folder contains all the machinery of the AnyMoCap
framework. It has three important subfolder (`TrialSpecificData`,
`SubjectSpecificData` and `LabSpecificData`).

:::{figure} model-setup-structure.png
These three folders contain variables specific to the application but also has
a few variables which can be assigned directly by the user.
:::

```{eval-rst}
.. table:: Variables in the ``Main.ModelSetup.TrialSpecificData`` folder which can be overridden.

    ======================================= ============================================================================================== ========================================
    ``Main.ModelSetup.TrialSpecificData``   Description                                                                                     Default value
    ======================================= ============================================================================================== ========================================
    ``TrialFileName``                       Name of the current trial. This is usually used for naming output files and                     Name of the main-file directory
                                            locating the input c3d files (c3d filename without the extension)
    ``LoadParametersFrom``                  List of trial names from which the scaling and optimized marker postions are loaded from.       ``{TrialFileName}``
    ``FirstFrame``                          First frame of the C3D/BVH file to use as starting frame in the analysis                        First frame in the C3D/BVH file
    ``LastFrame``                           The last frame of the C3D/BVH file to use in the analysis                                       Last frame in the C3D/BVH
    ``tStart``                              Specifies the start time of the analysis. Setting this overides ``FirstFrame``                  Calculated based on ``FirstFrame``
    ``tEnd``                                Specifies the end time of the analysis. Setting this overides ``LastFrame``                     Calculated based on ``LastFrame``
    ``nStep``                               Number of time steps used in the analysis. (Note that the number of time-steps in the inverse   Calculate based on ``tStart``/``tEnd``
                                            dynamic analysis will be 4 less than this values)
    ======================================= ============================================================================================== ========================================


```

```{eval-rst}
.. table:: Variables in the ``Main.ModelSetup.LabSpecificData`` folder which can be overridden.

    ======================================= ============================================================================================== ========================================
    ``Main.ModelSetup.LabSpecificData``     Description                                                                                       Default value
    ======================================= ============================================================================================== ========================================
    ``Gravity``                             Specifies the gravity vector in global reference frame.                                         ``{0,0,-9.81}``
    ``LowPassFilterSettings``               Folder with filter settings used for markers and analog (force) data.
    ``.MarkerFilterCutOffFrequency``        The lowpass cutoff frequency used for the marker data.                                          ``5.0``
    ``.MarkerFilterOrder``                  The filter order used when low pass filtering the marker data.                                  ``2``
                                            Note: Since the filter is applied as a zero phase filter
                                            (**filtfilt** or forward/backward filter) the effective filter order is the
                                            double of this value.
    ``.ForceFilterCutOffFrequency``         The lowpass cutoff frequency used for the force/analog data.                                   ``12.0``
    ``.ForceFilterOrder``                   The filter order used when low pass filtering the force/analog data.                           ``2``
                                            Note: Since the filter is applied as a zero phase filter
                                            (**filtfilt** or forward/backward filter) the effective filter order is the
                                            double of this value.
    ======================================= ============================================================================================== ========================================


```

## More resources

This section contains further documentation on the AnyMoCap framework.

```{toctree}
:maxdepth: 1

grf-prediction
```
