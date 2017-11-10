.. _anymocap:

######################
The AnyMoCap Framework
######################

The AnyMoCap model is an effort to create a simple and unified framework for
doing any kind of mocap analysis with the [AnyBody Modeling
System](http://anybodytech.com).

Musculoskeletal models that use Motion caputure data are releative complex and quite
difficult to understand for new users.

The reason is that the MoCap models are different from the other examples models
in the AMMR. Most importantly, MOCAP models usually require an over-determinate
kinematic solver to handle the excess in information that the optical markers
provide. The over-determinate solver in AMS works great, but it can only find
velocities and accelerations numerically. That has some performance issue when
running inverse dynamics analysis. To overcome the problem, the MOCAP analysis
is split into a two-step producedure.

.. figure:: /Applications/Mocap/anymocap_flow.png

The overdeterminate kinematic analysis solves the model for positions, and
writes joint angles to a a set of files. These joint angles can then be used
with the determinate kinematic solver in the inverse dynamic analysis.


AnyMocap examples:
***********************


.. include:: auto_examples/backreferences/gallery.anymocap.examples
.. raw:: html

    <div style='clear:both'></div>