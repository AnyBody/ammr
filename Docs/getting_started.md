# Getting Started

The *AnyBody Managed Model Repository* (AMMR) is a comprehensive open library of
musculoskeletal models and examples designed to use with the AnyBody Modeling
System. It allows users to configure and combine different body models, which
can be easily integrated into their own simulations and analyses.

The AnyBody Managed Model Repository (AMMR) is included with the 
[AnyBody Modeling System](https://www.anybodytech.com), 
but it needs to be manually installed or unpacked after installing AnyBody. You
can install the AMMR from the *AnyBody Assistant* dialog that appears when
AnyBody starts. For more information on how to install the AMMR, see the next
lesson {ref}`Installing Latest AMMR Files <installing-ammr>`.

```{toctree}
:hidden: true
:maxdepth: 1

ammr_installation
ammr_best_practices
```

% 1.. rubric:: Before using AMMR

## Opening an AMMR Model

To begin editing AMMR models, first navigate to the 'AMMR' folder in your file
explorer and open the 'Application' folder. Here, you will find all the
available models and examples. Navigate to the model you want to work on and
copy its containing folder and paste it into your working directory. The first
line in the main file of the model includes the 'libdef.any' file from the AMMR
folder. To correctly reference this file, add the following line at the beginning 
of the main file.

```AnyScriptDoc
#include "<ANYBODY_PATH_INSTALLDIR>/AMMR/libdef.any"
```

## Understanding the AnyScript Models

Most examples you will encounter when using the AnyBody Managed Model Repository
use the {ref}`Human Model <the-body-model>`. Regardless of complexity, all
models share a common structure used to set them up.

The models will typically look like this:

```AnyScriptDoc
#include "path_to_AMMR/libdef.any"

Main =
{
  // Configure and include the Human Model
  #define BM_LEG_MODEL _LEG_MODEL_TLEM2_
  #define BM_ARM_LEFT OFF
  #define BM_ARM_RIGHT OFF
  #include "<ANYBODY_PATH_BODY>/HumanModel.any"

  // Compose the model
  AnyFolder Model =
  {
    AnyFolder &BodyModel = .HumanModel.BodyModel;
    AnyFolder Drivers = {...};
    AnyFolder Environment = {...};
  };

  // Configuring the Study
  AnyBodyStudy Study =
  {
    AnyFolder &Model= Main.Model;
    Gravity = {0,-9.81,0}; // Gravity Vector
    nStep = 10; // Number of steps
    tStart = 0; // Start time
    tEnd = 10.0; // End time
  };
};
```

Let us go through the different components to understand how they work.

### Path to AMMR

```AnyScriptDoc
#include "path/to/AMMR/libdef.any"
```

When having multiple versions of AMMR available on your computer, you have to
specify which one will be used by AnyBody. Each AMMR includes a file called
`libdef.any` located at the top-level folder. The AnyScript line, used for
instructing AnyBody which AMMR to use, should be at the very beginning of your
`.any` file.

### Configuring the Human Model

:::{seealso}
:class: margin
{doc}`The documentation on BM configuration </bm_config/index>`
:::

```AnyScriptDoc
Main =
{
  // Configure and include the Human Model
  #define BM_LEG_MODEL _LEG_MODEL_TLEM2_
  #define BM_ARM_LEFT OFF
  #define BM_ARM_RIGHT OFF
```

The Human Body Model is configured through a number of `#define` and `#path`
statements. These statements are all prefixed with `BM_` inside AnyScript, and
they can also be referred to as "bm-statements". They define which parts of the
human body model are included or excluded.

### Including the Human Model

```AnyScriptDoc
#include "<ANYBODY_PATH_BODY>/HumanModel.any"
```

After the configuration statements, the HumanModel is included. It is important
that the configuration statements are placed before this line.

### Composing the Model

```AnyScriptDoc
AnyFolder Model =
{
  AnyFolder &BodyModel = .HumanModel.BodyModel;
  AnyFolder Drivers = {...};
  AnyFolder Environment = {...};
};
```

Most examples have a section where the model is composed. This is where we
combine the `Body` from the HumanModel, and add extra things like drivers,
external loads, and constraints.

It could also be any models of the environment which the body interacts with.

### The Study section

```AnyScriptDoc
AnyBodyStudy Study =
{
  AnyFolder &Model= Main.Model;
  Gravity = {0,-9.81,0}; // Gravity Vector
  nStep = 10; // Number of steps
  tStart = 0; // Start time
  tEnd = 10.0; // End time
};
```

:::{seealso}
:class: margin
{doc}`The full tutorial on how to create a HumanModel from scratch </creating_model_from_scratch>`
:::

The `AnyBodyStudy` is where you configure and define your simulation. It
specifies start and end times of the simulation, and the number of steps. It also
configures which solvers are used.

Only the model elements which are referenced from within the Study will be
included in the simulation. In this case, everything in the `Main.Model` folder is
part of the simulation.

[anybody modelling system]: https://www.anybodytech.com/software/anybodymodelingsystem/ 
[anyscript]: https://anyscript.org/tutorials/A_Getting_started_anyscript/index.html
[human model]: https://anyscript.org/tutorials/A_Getting_started/lesson1.html
