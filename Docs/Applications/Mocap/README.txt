.. _mocap_examples:

Motion Capture and gait analysis
----------------------------------

..
        All MoCap examples here uses the base *AnyMoCap* model, which is a new framework for 
        making MoCap models in the AMMR.

        The AnyMoCap model is an effort to create a simple and unified framework for
        doing any kind of MoCap analysis.

        Motion capture model were previously relatively complex and quite difficult to
        understand for new users. The reason is that the MoCap models are different from
        the other examples models in the AMMR. 

        Most importantly, MOCAP models usually require an over-determinate
        kinematic solver to handle the excess in information that the optical markers
        provide. The over-determinate solver in AMS works great, but it can only find
        velocities and accelerations numerically. That has some performance issue when
        running inverse dynamics analysis. To overcome the problem, the MOCAP analysis
        is split into a two-step procedure.

        .. figure:: /Applications/Mocap/anymocap_flow.png

        The over-determinate kinematic analysis solves the model for positions, and
        writes joint angles to a a set of files. These joint angles can then be used
        with the determinate kinematic solver in the inverse dynamic analysis.

        A number of examples are available as starting point for your application. 