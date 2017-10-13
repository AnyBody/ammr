Introduction to Scaling
=======================

Musculoskeletal models must be scalable to sizes of different
individuals to be useful for product design. This is very challenging,
because scaling pertains not only to the overall geometry, but also to
properties like muscle insertion points, muscle parameters and wrapping
surfaces. A general method for scaling musculoskeletal models has been
implemented into the AnyBody Respository models. The scaling procedure
is implemented in a generic manner and allows the usage of user-defined
scaling laws. For details on the theory behind please take a look at the
scaling introduction presented by AnyBody researchers in cooperation
with researchers from Ford:
`*Abstract* <https://www.anybodytech.com/downloads/publications/#rasmussen2005e>`__.

The models in the `AnyBody Managed Model
Repository <http://www.anybodytech.com/anybody.html?fwd=modelrepository>`__
have been made scalable by building generalized parameters into all the
numbers in the model. Just about everywhere, numbers in the models have
been replaced by calls to a scaling law. This means that all body models
expect such a scaling law to be present, but it is up to the user to
choose the actual law. This decoupling of the scaling laws from the body
parts makes it possible for the user to choose between the laws that are
supplied with the models or perhaps define a new law, without making any
changes in the body models.

Currently there are seven scaling laws available in AnyBody

-  ScalingStandard  (do not scale; i.e. use standard model size)

-  ScalingUniform  (scale equally in all directions; input is joint to
   joint distances)

-  ScalingLengthMass (scale taking mass into account; input is joint to
   joint distances and mass)

-  ScalingLengthMassFat (scale taking mass and fat into account; input
   is joint to joint distances)

-  ScalingUniformExt (scale equally in all directions; input is external
   measurements)

-  ScalingLengthMassExt (scale taking mass into account; input is
   external measurement)

-  ScalingLengthMassFatExt (scale taking mass and fat into account;
   input is external measurements).

The parameters of the scaling laws are controlled by the mean of the
AnyMan.any file. Several versions of this file are available the choice
depending on the scaling strategy chosen.  More details about how to use
this file are given along the tutorial.

Please also notice that each scaling law scales the strength of the
muscles, in addition to the size and mass of the bone. This strength
scaling is done automatically in most cases. We will come back to it
when needed. Users who need a more comprehensive introduction can view
this recorded previous webcast entitled `“Anthropometrical Scaling of
Musculoskeletal
Models” <http://www.anybodytech.com/downloads/documentation/#20090319>`__.

The first four scaling methods are covered in Lesson 1. They are often
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
