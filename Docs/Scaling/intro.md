(scaling-intro)=

# Introduction to Scaling

:::{sidebar} Scaling Tutorials

The three tutorials covers the different scaling 
methods shown in the table below:

```{toctree}
:maxdepth: 1

lesson1
lesson2
lesson3

```
:::

Musculoskeletal models must be scalable to sizes of different
individuals to be useful for product design. Scaling pertains not only to the overall geometry,
but also muscle insertion points, muscle parameters, wrapping
surfaces etc. AnyBody has a both generic and user-define scaling laws for models in the repository.

For details on scaling theory behind please take a look at [Rasmussen 2005](https://paperpile.com/shared/4znHWd).

Size related parameters of models in the {doc}`AMMR </index>`
are seldom defined as constant numbers, but instead computed from global measurements
(e.g., total height, weight of human) based on a scaling law. Thus all body models
expect the definition of a scaling law, although user can
choose the actual law.

Currently there are nine pre-defined scaling laws available in AnyBody



```{eval-rst}
.. list-table::
   :widths: 3 7
   :header-rows: 1

   * - Scaling law
     - Description
   * - :any:`ScalingStandard <_SCALING_STANDARD_>`
     - scale to a standard size; i.e. use 50th percentile sizes for a European male
   * - :any:`ScalingNone <_SCALING_NONE_>`
     - do not scale; i.e. use underlying cadaveric dataset as is
   * - :any:`ScalingUniform  <_SCALING_UNIFORM_>`
     - cale segments equally in all directions; input is joint to
       joint distances
   * - :any:`ScalingLengthMass <_SCALING_LENGTHMASS_>`
     - scale taking mass into account; input is joint to
       joint distances and mass
   * - :any:`ScalingLengthMassFat <_SCALING_LENGTHMASSFAT_>`
     - scale taking mass and fat into account; input
       is joint to joint distances
   * - :any:`ScalingXYZ  <_SCALING_XYZ_>`
     - scale taking mass and fat into account; scale segments along X, Y, Z axes;
       input is scale factors along X, Y, Z axes.
```

**Input parameters of scaling laws are specified in a file that is always named
AnyMan.any.** Several versions of this file are available, each for a different scaling law.
More details can be found the in the tutorial below.

**Please also notice that each scaling law scales the strength of the
muscles, in addition to the size and mass of the bone.** This strength
scaling is done automatically in most cases. We will come back to it
when needed. Users who need a more comprehensive introduction can view
this recorded previous webcast titled [“Anthropometrical Scaling of
Musculoskeletal
Models”](https://www.anybodytech.com/download/anthropometrical-scaling-of-musculoskeletal-models).




:::{admonition} **Next lesson:**
:class: seealso
Now head for {doc}`lesson1`.
:::

% ..  image:: _static/intro/image1.jpeg
%     :width: 80%
