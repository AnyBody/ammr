Introduction to Scaling
=======================

Musculoskeletal models must be scalable to sizes of different
individuals to be useful for product design. Scaling pertains not only to the overall geometry, 
but also muscle insertion points, muscle parameters, wrapping
surfaces etc. AnyBody has a both generic and user-define scaling laws for models in the repository.

For details on scaling theory behind please take a look at the
following resource:
`*Abstract* <https://www.anybodytech.com/downloads/publications/#rasmussen2005e>`__.

Size related parameters of models in the `AMMR <../index.html>`__
are seldom defined as constant numbers, but instead computed from global measurements 
(e.g., total height, weight of human) based on a scaling law. Thus all body models
expect the definition of a scaling law, although user can 
choose the actual law. 

Scaling laws
-----------------------

Users to choose to use pre-defined laws that are built into AnyBody 
or perhaps define a custom scaling law. Currently there are seven inbuilt scaling laws in AnyBody.

-  ScalingStandard  (does not scale; i.e. use standard model size)

-  ScalingUniform  (scales equally in all directions; input is joint to
   joint distances)

-  ScalingLengthMass (scales taking mass into account; input is joint to
   joint distances and mass)

-  ScalingLengthMassFat (scales taking mass and fat into account; input
   is joint to joint distances)

-  ScalingUniformExt (scales equally in all directions; input is external
   measurements)

-  ScalingLengthMassExt (scales taking mass into account; input is
   external measurement)

-  ScalingLengthMassFatExt (scales taking mass and fat into account;
   input is external measurements).

**Input parameters of scaling laws are specified in a file that must always be named
AnyMan.any.** Several versions of this file are available, each for a different scaling law. 
More details can be found the in the tutorial below.

**Please also notice that each scaling law scales the strength of the
muscles, in addition to the size and mass of the bone.** This strength
scaling is done automatically in most cases. We will come back to it
when needed. Users who need a more comprehensive introduction can view
this recorded previous webcast titled `“Anthropometrical Scaling of
Musculoskeletal
Models” <http://www.anybodytech.com/downloads/documentation/#20090319>`__.

Tutorial
-----------------------

The first four scaling laws are covered in Lesson 1. They are often
referred to as Joint to joint scaling methods. Lesson 2 covers the
latter three which are based on external body measurement. 

With the AnyBody Modeling System you already have a repository of models
available, for details please see the AnyBody Assistant available from
the menu. As a starting point for this tutorial please find the model
StandingModelScalingDisplay. This model can be found in the folder
Applications/Examples.


.. toctree::
    :maxdepth: 1

    lesson1
    lesson2


.. rst-class:: without-title
.. seealso::
    **Next lesson:** Now head for :doc:`lesson1`.


|http://www.anybodytech.com/fileadmin/images/AnyFamily.JPG|

.. |http://www.anybodytech.com/fileadmin/images/AnyFamily.JPG| image:: _static/intro/image1.jpeg
   :width: 4.15625in
