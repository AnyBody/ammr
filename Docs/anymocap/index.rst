.. _anymocap:

######################
The AnyMoCap Framework
######################

The AnyMoCap model is an effort to create a simple and unified framework for
doing any kind of mocap analysis with the `AnyBody Modeling
System <http://anybodytech.com>`__.

.. image:: /_static/anymocap.jpg
    :width: 50%
    :align: center


Features
********
* Adapts to any Mocap protocol 
* Optimization of marker locations and anthropometrics. 
* Support Marker based (C3D) and inertial based (BVH) input.
* Support for standard forceplates: (Types 1-4) plus more.
* Prediction of ground reaction forces
* Easy setup with multiple trials and subjects


Overdeterminate kinematic analysis
**********************************

Musculoskeletal models that use Motion caputure data are different from other
types of models found the AMMR.  Most importantly, MOCAP models usually require
an over-determinate kinematic solver to handle the excess in information that
the optical markers provide. 

The over-determinate solver in AMS works great, but
it can only find velocities and accelerations numerically. That has some
performance issue when running inverse dynamics analysis. To overcome the
problem, the MOCAP analysis is split into a two-step producedure, as illustrated on
the figure below:

.. figure:: /Applications/Mocap/anymocap_flow.png


The overdeterminate kinematic analysis solves the model for positions, and
writes joint angles to a a set of files. These joint angles can then be used
with the determinate kinematic solver in the inverse dynamic analysis.


.. seealso:: The AnyBody tutorials, and the :tutorials:doc:`lesson on using the
    AnyMoCap model <Making_things_move/lesson5>`



AnyMoCap examples:
***********************


.. include:: auto_examples/backreferences/gallery.anymocap.examples
.. raw:: html

    <div style='clear:both'></div>