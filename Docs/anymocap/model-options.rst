
Overview of AnyMoCap options
#############################


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



.. table:: ``#define`` settings for AnyMoCap. 

    ============================================== ============================================================================================== ========================================
    Setting                                        Description                                                                                    Default value
    ============================================== ============================================================================================== ========================================
    ``MOCAP_INPUT_DATA_TYPE``                      Data type ("C3D", "BVH") used by the AnyMoCap application.                                     "C3D"
    ``MOCAP_CREATE_PARAMETER_ID_SHORTCUT``         Setting for creating the ``Main.RunParameterIdentification`` shortcut operation  .             ON
    ``MOCAP_OUTPUT_FILENAME_PREFIX``               Prefix added to all output files from the model.                                               ""
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

