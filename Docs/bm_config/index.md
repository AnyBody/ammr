(bm-config)=

# Configuring the Body Model

The body model can be configured in multiple ways. This include what limb
segments are include, the type of muscles, scaling etc.

All these choises are controlled through a number of switches called Body Model
(BM) parameters. BM parameters are always prefixed with `BM_` and written in
uppercase.

## Simple example

The example below configures a model with no arms and enables the 3-element Hill
muscles model on the legs.

:::{note}
:class: margin
Some parameters have simple {ammr:bm_constant}`ON`/{ammr:bm_constant}`OFF`
options, while others have more options. 
:::

```{code-block} AnyScriptDoc
:emphasize-lines: 1-3

#define BM_ARM_LEFT OFF
#define BM_ARM_RIGHT OFF
#define BM_LEG_MUSCLES_BOTH _MUSCLES_3E_HILL_

// Now include the HumanModel
#include "<ANYBODY_PATH_BODY>\HumanModel.any"
```



The next section shows an overview of what BM statements are available for the different body parts.

## BM parameters

:::{tip}
:class: margin
Most models can also be configured using the
{doc}`BM plugin </bm_config/bm_plugin>`.
:::

There are body model parameters for configuring each body part, controlling scaling, controlling the default
mannequin drivers (click to see tutorial on {ref}`modelling from scratch <MannequinDriver>`), as well as other global options for the model.

See the following links for details on BM parameters related to different body parts and modelling options:

```{toctree}
:maxdepth: 1

leg
arm
trunk
mannequin
scaling
joint_type
other
bm_plugin
```

## All Parameters and constants

The full list of all the parameter and their options is available in the links below:

```{toctree}
:maxdepth: 1

bm_statements
bm_constants
```
