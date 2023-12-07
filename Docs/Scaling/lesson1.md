# Lesson 1: Joint to Joint Scaling Methods

This lesson covers five of the scaling laws available in AnyBody:

- `_SCALING_STANDARD_` (scale to a standard size)
- `_SCALING_NONE_` (do not scale)
- `_SCALING_UNIFORM_` (scale equally in all directions; input is joint to
  joint distances)
- `_SCALING_LENGTHMASS_` (scale taking mass into account; input is joint to
  joint distances and mass)
- `_SCALING_LENGTHMASSFAT_` (scale taking mass and fat into account; input
  is joint to joint distances)

## ScalingStandard

This scaling law produces a model with the default parameters for mass and
size (corresponding roughly to the 50th percentile European male). It is
used by default for non-specific models, or when there is no data
available about the modeled subject. This law does not use the AnyMan
file because there is no parameter to modify.

With the AnyBody Modeling System you already have a repository of models
available; for details please see the AnyBody Assistant available from
the menu. Let us practice, as a starting point for this tutorial, please
find this model:

```{image} _static/lesson1/ScalingDisplayHelp.png
```

To use this law you do not need to do anything at all; however, for
demonstration purposes the scaling law configuration parameter (BM_SCALING)
will be set to use the default value:

```AnyScriptDoc
/*------------- SCALING CONFIGURATION SECTION --------------------*/

// Scaling laws using joint to joint measures
   §#define BM_SCALING _SCALING_STANDARD_§
//  #define BM_SCALING _SCALING_NONE_
//  #define BM_SCALING _SCALING_UNIFORM_
//  #define BM_SCALING _SCALING_LENGTHMASS_
//  #define BM_SCALING _SCALING_LENGTHMASSFAT_
//  #define BM_SCALING _SCALING_XYZ_

//--------------- END OF SCALING CONFIGURATION -------------------
```

Now load the model and open a Model View window. You will see the
standing model with the standard size.

```{image} _static/lesson1/ScalingStandardFront.jpg
:width: 49%
```

```{image} _static/lesson1/ScalingStandardBack.jpg
:width: 49%
```

## ScalingNone

This particular scaling law can be used for the studies, which require the unscaled cadaveric
datasets, which were used for the construction of the body parts. Please enable the \_SCALING_NONE\_
option in order to switch to this scaling law.

```AnyScriptDoc
/*------------- SCALING CONFIGURATION SECTION --------------------*/

// Scaling laws using joint to joint measures
§#define BM_SCALING _SCALING_NONE_§
//  #define BM_SCALING _SCALING_UNIFORM_
//  #define BM_SCALING _SCALING_LENGTHMASS_
//  #define BM_SCALING _SCALING_LENGTHMASSFAT_
//  #define BM_SCALING _SCALING_XYZ_

```

The result will not noticeably change as compared to the ScalingStandard, but minor differences
can be observed when looking at the actual locations of the muscle attachment sites and so on.

## Working with known body part dimensions

When modelling a specific person with known anthropometric factors, e.g. weight,
height, body part lengths, etc., these details need to be incorporated into the model.
In this case \_SCALING_STANDARD\_ and \_SCALING_NONE\_ are not applicable, since they
correspond to predetermined human sizes and weights, which cannot be overwritten.

For these purposes a number of additional scaling laws were implemented, which
all share an input mechanism for subject-specific measurements. This mechanism
lets the user overwrite the height, weight, fat percentage, and individual
segmental measurements or scale factors. This is done like below:

```AnyScriptDoc
/*------------- SCALING CONFIGURATION SECTION --------------------*/

// Scaling laws using joint to joint measures
§//  #define BM_SCALING _SCALING_NONE_§
§    #define BM_SCALING _SCALING_UNIFORM_§
//  #define BM_SCALING _SCALING_LENGTHMASS_
...
// Example of how to overwrite the default values
§//  Main.HumanModel.Anthropometrics.BodyHeight = 1.8;§
§//  Main.HumanModel.Anthropometrics.BodyMass = 80;§
```

The above line shows how it can be overwritten from, say, the Main folder.
We have now succesfully personalized the model using anthropometric measurements.

## ScalingUniform

This law allows you to define the total weight of the model and the
individual sizes of the bones. The length of each bone is defined as a
joint to joint distance and the bone is then scaled in three dimensions
proportionally to its length. To use this law you must change the
scaling parameter to be \_SCALING_UNIFORM\_.

In the previous section we showed how this can be done. Please now load the
model and have a look at the Model View window. Notice that the body size did
not change from the standard scaling version. This is because the default values
for segment masses and sizes in this file are the same as the standard values.
But if you change them, the model will scale according to your specifications.

Let us try to change the mass of the body. First, inspect the *BodyMass* variable in the Model Tree window.
You can find it at `Main.HumanModel.Anthropometrics.BodyMass`.
The default value is 75 kg.

Try changing it to 90 kg by adding the following to your main file:

```AnyScriptDoc
§Main.HumanModel.Anthropometrics.BodyMass = 90;§
```

Now load the model again. Once again the size
of the body did not change. In the ScalingUniform law, the `BodyMass`
parameter controls the mass of the segments but not their sizes. As shown
previously the overall body mass is distributed to each segment.

So the `BodyMass` parameter only controls the segment masses. The size
of the model is controlled by another list of variables defining the
lengths of the different bones. The length of each segment can be set
independently, for example we can increase the length of the thigh
by adding the following line to the main file:

```AnyScriptDoc
§Main.HumanModel.Anthropometrics.SegmentDimensions.Right.ThighLength = 0.626§;
```

Load the model again and have a look at the Model View window. The
femur bone is now bigger. It has been scaled uniformly in 3 directions
according to the defined length. Notice that we only changed the size
of the femur and not the other bones, so the femur looks unreasonably
big compared to the rest of the body. To avoid results such as this,
it is important to feed those variables with consistent data rooted in
real anthropometry.

```{image} _static/lesson1/LargeFemurFront.jpg
:width: 49%
```

Let us apply a more reasonable size. Please change the default values
to the following set of consistent measures:

```AnyScriptDoc
§Main.HumanModel.Anthropometrics.SegmentDimensions.PelvisWidth = 0.180§;
§Main.HumanModel.Anthropometrics.SegmentDimensions.HeadHeight = 0.169§;
§Main.HumanModel.Anthropometrics.SegmentDimensions.TrunkHeight = 0.754§;

§Main.HumanModel.Anthropometrics.SegmentDimensions.Right.UpperArmLength = 0.405§;
§Main.HumanModel.Anthropometrics.SegmentDimensions.Right.LowerArmLength =0.316§;
Main.HumanModel.Anthropometrics.SegmentDimensions.Right.ThighLength = §0.548§;
§Main.HumanModel.Anthropometrics.SegmentDimensions.Right.ShankLength = 0.551§;
§Main.HumanModel.Anthropometrics.SegmentDimensions.Right.FootLength = 0.243§;

§Main.HumanModel.Anthropometrics.SegmentDimensions.Left.UpperArmLength = 0.405§;
§Main.HumanModel.Anthropometrics.SegmentDimensions.Left.LowerArmLength =0.316§;
§Main.HumanModel.Anthropometrics.SegmentDimensions.Left.ThighLength = 0.548§;
§Main.HumanModel.Anthropometrics.SegmentDimensions.Left.ShankLength = 0.551§;
§Main.HumanModel.Anthropometrics.SegmentDimensions.Left.FootLength = 0.243§;

```

```{image} _static/lesson1/ScalingUniformFront.jpg
:width: 49%
```

When you reload the model you should see a tall body and with
proportionate sizes of the segments. If you can't see the difference
from the standard size model, notice how the feet are now sticking down
below the reference frame.

It should be obvious that this type of scaling requires good anthropometric data
to give reasonable results. But such data is not always easily available. To
help with this, the default values of the `_SCALING_UNIFORM_` law is implemented
in a way that it only takes as input the body mass and the body height and
subsequently scales all the segment lengths uniformly according to the defined
body height. This may not give you a model where each bone matches a given
subject, but it can be a reasonable estimate in cases where only the overall
mass and height of the body is known. Try to comment out these lines again:

```AnyScriptDoc
§//Main.HumanModel.Anthropometrics.SegmentDimensions.PelvisWidth = 0.180§;
§//Main.HumanModel.Anthropometrics.SegmentDimensions.HeadHeight = 0.169§;
§//Main.HumanModel.Anthropometrics.SegmentDimensions.TrunkHeight = 0.754§;

§//Main.HumanModel.Anthropometrics.SegmentDimensions.Right.UpperArmLength = 0.405§;
§//Main.HumanModel.Anthropometrics.SegmentDimensions.Right.LowerArmLength =0.316§;
§//Main.HumanModel.Anthropometrics.SegmentDimensions.Right.ThighLength = 0.548§;
§//Main.HumanModel.Anthropometrics.SegmentDimensions.Right.ShankLength = 0.551§;
§//Main.HumanModel.Anthropometrics.SegmentDimensions.Right.FootLength = 0.243§;

§//Main.HumanModel.Anthropometrics.SegmentDimensions.Left.UpperArmLength = 0.405§;
§//Main.HumanModel.Anthropometrics.SegmentDimensions.Left.LowerArmLength =0.316§;
§//Main.HumanModel.Anthropometrics.SegmentDimensions.Left.ThighLength = 0.548§;
§//Main.HumanModel.Anthropometrics.SegmentDimensions.Left.ShankLength = 0.551§;
§//Main.HumanModel.Anthropometrics.SegmentDimensions.Left.FootLength = 0.243§;

```

Now it is easy to scale the body down to represent a small person.
Use thefollowing line to set the body height to 1.65 m and the body mass to 60 kg:

```AnyScriptDoc
§Main.HumanModel.Anthropometrics.BodyHeight = 1.65;§
§Main.HumanModel.Anthropometrics.BodyMass = 60;§
```

When you load the model you will see all the segments automatically
scaling down. The mass is also scaled, but as we said previously this is
not visible graphically with this scaling law.

## Scaling based on length and mass

This law scales the size of the body according not only to the segment
lengths but also to the segments masses, so unlike the ScalingUniform
law it provides the opportunity to define tall and skinny people or
small and squat people. Like in the ScalingUniform law, the total body
mass is defined by the variable `BodyMass`. Just as previously, this
total mass is then divided between the segments by means of
coefficients, but the size scaling is different. Let us investigate it.
In the main file, please choose the ScalingLengthMass law and switch
back to the AnyMan file:

```AnyScriptDoc
// Scaling laws using joint to joint measures
§//#define BM_SCALING _SCALING_UNIFORM_
  #define BM_SCALING _SCALING_LENGTHMASS_§
//  #define BM_SCALING _SCALING_LENGTHMASSFAT_
...
```

In the Main file, switch back the segment length values to the initial
ones (by outcommenting the added lines) and increase the body mass to 110 kg:

```AnyScriptDoc
Main.HumanModel.Anthropometrics.BodyMass = §110§;
```

Load the model and look at the Model View. Our model looks strange!
The body is deformed and looks a bit like a Neanderthal.

```{image} _static/lesson1/ScalingLengthMassFront.jpg
:width: 49%
```

```{image} _static/lesson1/ScalingLengthMassBack.jpg
:width: 49%
```

What really happens is that the ScalingLengthMass law scales the sizes
of the segments according to their masses, but only in two directions.
The third scaling direction is controlled by the segment length
variables. Unlike in the ScalingUniform law, the segment length
variables just control one scaling direction and not the two others.

So to have a normal-looking model we have to adjust segment mass and
length simultaneously. As the mass we defined is 110 kg, a height of
1.98 m could be reasonable:
  
```AnyScriptDoc
§Main.HumanModel.Anthropometrics.BodyHeight = 1.98§;
```

```{image} _static/lesson1/ScalingLengthMassCorrectFront.jpg
:width: 49%
```

```{image} _static/lesson1/ScalingLengthMassCorrectBack.jpg
:width: 49%
```

When you load the model you will see a more *Homo sapiens*-looking
figure corresponding to a large 110kg and 1.98 m person.

We mentioned at the beginning of the tutorial that the muscle strength
is also scaled. It is time to have a look at it and compare muscle
forces from different scaled models. To do so we need a body with
muscles. Please add the muscles by commenting out the following section
of the general configuration block in the `BodyModelConfiguration.any` file:

```AnyScriptDoc
§//#ifndef BM_LEG_MUSCLES_BOTH
//  #define BM_LEG_MUSCLES_BOTH OFF
//#endif
//#ifndef BM_ARM_MUSCLES_BOTH
//  #define BM_ARM_MUSCLES_BOTH OFF
//#endif
//#ifndef BM_TRUNK_MUSCLES
//  #define BM_TRUNK_MUSCLES OFF
//#endif
    §
```

We also need to add some forces to the model in order to make it react
and see muscle activity. This can be done by adding the following lines
to the Environment.any file. This piece of code creates a force of 50 N
on each hand and displays it in the model view:

```AnyScriptDoc
AnyFolder Environment = {
  AnyFixedRefFrame GlobalRef = {Origin = {0.0,0.0,0.0};};
};
 §
AnyForce3D RightHandLoad = {
    F = {0, -50, 0};
 AnyRefFrame &Hand = Main.HumanModel.BodyModel.Right.ShoulderArm.Seg.Glove;
};

  AnyForce3D LeftHandLoad = {
    F = {0, -50, 0};
    AnyRefFrame &Hand = Main.HumanModel.BodyModel.Left.ShoulderArm.Seg.Glove;
  };

  AnyDrawVector DrawRightLoad = {
    Vec = .RightHandLoad.F*0.015;
    PointAway = On;
    GlobalCoord = On;
    Line = {
      Style = Line3DStyleFull;
      Thickness = 0.01;
      RGB = {0, 0, 0};
      End = {
        Style = Line3DCapStyleArrow;
        RGB = {0, 0, 0};
        Thickness = 0.025;
        Length = 0.025;
      };
    };
    AnyRefFrame &Hand = .RightHandLoad.Hand;
  };

  AnyDrawVector DrawLeftLoad = {
    Vec = .LeftHandLoad.F*0.015;
    PointAway = On;
    GlobalCoord = On;
    Line = {
      Style = Line3DStyleFull;
      Thickness = 0.01;
      RGB = {0, 0, 0};
      End = {
        Style = Line3DCapStyleArrow;
        RGB = {0, 0, 0};
        Thickness = 0.025;
        Length = 0.025;
      };
    };
    AnyRefFrame &Hand = .LeftHandLoad.Hand;
  };§
```

```{image} _static/lesson1/AppliedForcesFront.jpg
:width: 49%
```

We are now ready to run an inverse dynamic analysis with our large 110kg
model. Please load the model and run the RunApplication operation from
the Operations tab. Then open a chart window to investigate the
results. By browsing your way to the MaxMuscleActivity in Main.Study you
should get the following value:

```{image} _static/lesson1/MaxMuscleActivity198cm110kg.jpg
```

We will now try to model a small person to compare his muscle activity
with the one we have just plotted. Let us enter the
parameters for a 65kg and 1.70 m person:

```AnyScriptDoc
Main.HumanModel.Anthropometrics.BodyHeight = §1.70§;
Main.HumanModel.Anthropometrics.BodyMass = §65§;
```

We can load the model, run the inverse dynamics analysis and check the
resultant value.

```{image} _static/lesson1/MaxMuscleActivity170cm65kg.jpg
```

For the same load on the hands (50 N) the tall heavy model has a muscle
activity of 44.9 %, whereas the short model reaches 59.6 % of muscle
activity. So our small model is definitely weaker than the tall one.

## ScalingLengthMassFat

Most scaled models used for practical investigations use the
ScalingLengthMassFat law. It works exactly like the ScalingLengthMass
but with an additional parameter: It takes the fat percentage of the
body into account. The argument is that the fat percentage adds to the
mass of each segment and in the ScalingLengthMass law would lead an
estimation of more muscle tissue rather than fat tissue. So the fat
percentage in this scaling model does not modify the mass or the size
of the body. It is only used to calculate the strength of the muscles.
Between two persons of similar segment masses, the one with higher fat
percentage will have less muscle strength, because the volume
otherwise occupied by the muscles is replaced by inactive fat.

So the mass and size scales are controlled as in the ScalingLengthMass
model by the `BodyMass` variable and all the segment length variables
respectively. The fat percentage is controlled in concert by the
variables `BodyHeight` and `BodyMass`. These two variables are used to
calculate the BMI (Body-Mass Index), and the BMI is used to calculate
the fat percentage of the body according to Frankenfield, D. C.; Rowe,
W. A.; Cooney, R. N.; Smith, J. S. & Becker, D. (2001): Limits of body
mass index to detect obesity and predict body composition, Nutrition
17(1), 26-30.

```AnyScriptDoc
// Default values for the fat percentage found in (ammr\Body\AAUHuman\Scaling\DefaultAnthropometrics.any)
AnyVar BMI = AnthroData.Body_Mass/(AnthroData.body_height*AnthroData.body_height);
AnyVar FatPercent = (-0.09 + 0.0149*BMI - 0.00009 *BMI*BMI)*100; //Estimation from Frankenfield et al. (2001) valid for men
```

Obviously it is important to input the correct height
of the body when using this law. Please notice, however, that it is
very easy for the user to substitute the formula for the fat
percentage by another equation or possibly by a fixed number for
modeling of a particular individual for whom the fat percentage has
been measured directly.

The resultant value for the fat percentage is then directly used to
compute an estimate of the strength of each muscle in the model.

This advanced strength scaling makes a significant difference for the
model that is short and heavy. The ScalingLengthMass law tends to
over-estimate the strength of those models, because they often have a
high fat percentage that is not taken into account by the law.

We will try to illustrate this by plotting the muscle activity of the
same short and heavy model with both ScalingLengthMass and
ScalingLengthMassFat laws. We will begin by adjusting the anthropometrics
to match a 90kg and 1.70 m person:

```AnyScriptDoc
Main.HumanModel.Anthropometrics.BodyMass = §90§;
```

Then please load the model and re-run the application. Notice that we
should still be using the ScalingLengthMass law. You should now get
the following value for the maximum muscle activity.

```{image} _static/lesson1/MaxMuscleActivity170cm90kgLM.jpg
```

The next step is to run an analysis with the same body but with the
ScalingLengthMassFat law:

```AnyScriptDoc
// Scaling laws using joint to joint measures
//  #define BM_SCALING _SCALING_UNIFORM_
§//  #define BM_SCALING _SCALING_LENGTHMASS_
#define BM_SCALING _SCALING_LENGTHMASSFAT_§
```

Once again load the model and run the inverse dynamics
analysis by executing the RunApplication operation. We should get the
following results:

```{image} _static/lesson1/MaxMuscleActivity170cm90kgLMF.jpg
```

If we compare these two activity values, the difference is clear. The
ScalingLengthMassFat law is increasing the muscle activity by
approximately 13 % in this case, from 46 % to 59 %. This shows the
limits of the ScalingLengthMass law for extreme cases.
ScalingLengthMassFat is able to cover a wider range of cases while
keeping its accuracy.

This completes scaling Lesson 1: Joint to joint scaling methods.

:::{admonition} **Next lesson:**
:class: seealso
{doc}`lesson2`.
:::
