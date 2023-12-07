# Lesson 2: Scaling based on External Body Measurements

This tutorial presumes that you have completed {doc}`Scaling tutorial
Lesson 1: Joint to joint scaling methods <lesson1>`. It
covered the methods ScalingStandard, ScalingUniform, ScalingLengthMass
and ScalingLengthMassFat.

This lesson introduces a statistical scaling method based on external measures.

## Statistical Scaling

The scaling laws we discussed in Lesson 1 are using measures for the
segment lengths based on joint-to-joint distances, but some joint
locations cannot be easily palpated. The hip joints are a good example.
They are located deep under the skin and are not easy to measure from
the outside. So to facilitate scaling to individuals, another method of
scaling is provided that use only distances between external
bony landmarks.

Here is where our [Statistical Scaling
PLugin](https://anyscript.org/ammr/beta/Applications/Other/StatisticalScalingPlugin.html)
comes into play. It is a plugin that can be used to scale a model by specifying
a few anatomical or functional anthropometric parameters while calculating the
remaining parameters based on statistical data from the ANSUR [^f1] database.

In order to use the plugin, you need to include it in your model:

```AnyScriptDoc
#define BM_SCALING _SCALING_XYZ_
#include "<ANYBODY_PATH_AMMR>/Tools/Plugins/ANSUR_Plugin.any"
  
// Define a path variable so the plugin knows where to write
// Anthropometric information.
#path ANSUR_PLUGIN_ANYMAN_FILE "AnyMan_ANSUR.any"
#include "<ANSUR_PLUGIN_ANYMAN_FILE>"
```

We are enabling the `_SCALING_XYZ_` law. The plugin is designed to work with this scaling law only.
We will get back to how this law works in a later lesson.

Notice also that we are including the file `AnyMan_ANSUR.any` which we need to
create in order for the plugin to work. The plugin will write the anthropometric
information to this file. Create the file next to the main file of your model
and add the following content:

```AnyScriptDoc
// Anthropometrics file generated based on ANSUR PCA scaling 
Main.HumanModel.Anthropometrics = 
{
 BodyMass = 81.99788166330553;
 BodyHeight = 1.8000000000000007;
};    
    
Main.HumanModel.Anthropometrics.SegmentDimensions = 
{
  HeadDepth = DesignVar(0.19854919694591627);
  HeadHeight = DesignVar(0.13435062679846901);
  HeadWidth = DesignVar(0.15408461276045118);
  Left.FootHeight = DesignVar(0.05346215076533939);
  Left.FootLength = DesignVar(0.26540765594237714);
  Left.FootWidth = DesignVar(0.08057585258177535);
  Left.HandBreadth = DesignVar(0.08836086489212641);
  Left.HandLength = DesignVar(0.18919620482784752);
  Left.LowerArmLength = DesignVar(0.2787988940627688);
  Left.ShankLength = DesignVar(0.44933350273014644);
  Left.ThighLength = DesignVar(0.4329345672323976);
  Left.UpperArmLength = DesignVar(0.31474556404210224);
  NeckLength = DesignVar(0.13339097946419404);
  PelvisDepth = DesignVar(0.14549510408533453);
  PelvisHeight = DesignVar(0.10915196667715318);
  PelvisWidth = DesignVar(0.17734410213497);
  Right.FootHeight = DesignVar(0.05346215076533939);
  Right.FootLength = DesignVar(0.26540765594237714);
  Right.FootWidth = DesignVar(0.08057585258177535);
  Right.HandBreadth = DesignVar(0.08836086489212641);
  Right.HandLength = DesignVar(0.18919620482784752);
  Right.LowerArmLength = DesignVar(0.2787988940627688);
  Right.ShankLength = DesignVar(0.44933350273014644);
  Right.ThighLength = DesignVar(0.4329345672323976);
  Right.UpperArmLength = DesignVar(0.31474556404210224);
  TrunkDepth = DesignVar(0.1943939027626778);
  TrunkHeight = DesignVar(0.6496243660543214);
  TrunkWidth = DesignVar(0.3781679964242773);
};
```

After saving this file, you can load the model and the anthropometrics from the
file will be used to scale the model.

To change the scaling of the model you can start the plugin by clicking the
\ANSUR Configuration\ from the tools line:

```{image} _static/lesson2/ANSUR_plugin_toolbar_icon.jpg
```

This will bring up the plugin window:

```{image} _static/lesson2/ANSUR_plugin_window.jpg
```

The plugin has 4 tabs:

- **Basic Input**: This tab allows you to overwrite *Stature*, *Weight*, *BMI*,
  *Fat percentage* and select gender.
- **Functional Dimensions**: This tab allows you to select a functional
  dimension from a drop down list. It will display a image of the dimension
  applied to the model and allow you to enter a value for the dimension or
  select if the plugin should calculate the value based on the other dimensions.
- **Anatomical Dimensions**: This tab allows you to select a anatomical
  dimension based on the available dimensions of the model. It will display a
  image of the dimension applied to the model and allow you to enter a value for
  the dimension or select if the plugin should calculate the value based on the
  other dimensions.
- **About**: This tab contains information about the plugin.

At the bottom of the window you can see the **Load to AMS** button. This button
will write the selected dimensions to the file `AnyMan_ANSUR.any` and load the
model.

```{rubric} Footnotes
```

[^f1]: Gordon, C. C. et al. 1988 Anthropometric Survey of U.S. Army personnel: methods and summary statistics. (US Army Natick Research, Development and Engineering Center, 1989).

:::{seealso} **Next lesson:**
:class: seealso
{doc}`lesson3`.
:::
