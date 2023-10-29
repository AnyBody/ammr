# Update models to AMMR 2.5

Models created earlier versions of AnyBody may need to be updated to work with
AnyBody 7.5 and the new model repository (AMMR 2.5).

This document outlines important changes which may break
older models or change results.

:::{tip} 

See the last part of this document for a list of concrete errors and deprecation
warnings and how to fix them. 

:::

## Model changes

### Trunk and pelvis neutral posture

The trunk model in AMMR 2.5 changes which posture is considered
neutral. This was done in preparation for a new [detailed thoracic
model](#thoracic-model) which will be available in [AMMR
3.0](https://github.com/anybody/ammr). Pelvic tilt for the model has been updated as well as the the neutral orientation of the thoracic segment.

::: {warning}
These postural changes will affect older applications. Especially, in models
where trunk joint angles are driven directly and in models where a driver is applied directly on the pelvis segmental reference frame.
:::

### MoCap models

#### Pelvic markers

Changes to the pelvic tilt means that pelvic markers located relative to the
pelvis Anatomical frame will appear to have moved slightly. This is most
noticeable for markers on the posterior part of the pelvis, like the PSIS
markers. The Y component of the marker position may need to be adjusted to achieve same marker position and joint angle output. 

If markers are placed relative to bony landmarks (using the `PlaceMarkerAt=`
argument) this problem will often not occur.

#### Foot markers

Changes to the anatomical frame of the foot and talus segment may cause markers
to have moved slightly. The Y component may need to be adjusted to achieve the
same marker position and joint angle output.


## Load time errors

:::{dropdown} `Scale_Leg_Pelvis  :  Unresolved object`


```
ERROR(SCR.PRS9) :   some-file.any(##)  :   'Scale_Leg_Pelvis'  :  Unresolved object
```

The functions `Scale_Leg_Pelvis` and `Scale_Trunk_Pelvis` on the pelvis segment have been moved inside the `AnatomicalFrame` folder. 
Update your code to `AnatomicalFrame.Scale_Leg_Pelvis`.

:::


:::{dropdown} `MusPar  :  Unresolved object`


```
ERROR(SCR.PRS9) :   some-file.any(##)  :   'MusPar'  :  Unresolved object
```

The `MusPar` folder have been renamed to `MuscleModels`. 

:::



:::{dropdown} `PCSAfactor  :  Unresolved object`

```
ERROR(SCR.PRS9) :   xxx.any(##)  :   'PCSAfactor'  :  Unresolved object
```

This could be cause by the fact that the `MuscleParameters.Muscles.PCSAfactor` is  now located at `MuscleModels.DefaultMusPar.PCSAfactor`

:::


:::{dropdown} `StringMesh  :  Error in expression`

```
ERROR(SCR.EXP0) :   Ligaments.any(18)  :     Defined at :   Class_CreateLigament.any(47)  :   StringMesh  :  Error in expression. Please refer to the following error messages for details ...
ERROR(SCR.EXP1) :   Ligaments.any(18)  :     Defined at :   Class_CreateLigament.any(47)  :   Operator '='  :  Illegal operation for given argument types  :  'AnyInt[Undefined]' '=' 'AnyFloatVar'
```

The `StringMesh` variable have changed type from `AnyVar` to `AnyInt`. So if `StringMesh` is assigned from an other variable, make sure that it has the type `AnyInt`.

:::

## Deprecation warnings

Below is a set of possible errors you may encounter if old models are used with AMMR 2.5. 


:::{dropdown} `AnyViaPointMuscle  :  Deprecated class`

```
WARNING(SYS3) :  ... :  AnyViaPointMuscle : Deprecated class  :  Class 'AnyViaPointMuscle' was renamed to 'AnyMuscleViaPoint'
```
Some class names for `AnyMuscle` have been deprecated. Just rename them. 

*  `AnyViaPointMuscle` --> `AnyMuscleViaPoint`
*  `AnyShortestPathMuscle` --> `AnyMuscleShortestPath`

:::


:::{dropdown} `AnyShortestPathMuscle  :  Deprecated class`

```
WARNING(SYS3) :   ...  :  AnyShortestPathMuscle  :  Deprecated class  :  Class 'AnyShortestPathMuscle' was renamed to 'AnyMuscleShortestPath'
```
Some class names for `AnyMuscle` have been deprecated. Just rename them. 

*  `AnyViaPointMuscle` --> `AnyMuscleViaPoint`
*  `AnyShortestPathMuscle` --> `AnyMuscleShortestPath`

:::



:::{dropdown} `Deprecated use of AnySurf*Fit classes`


```
ERROR(OBJ.MCH.SURF4) :   Custom_Seg_Shank.any(114)  :   Surf  :  Deprecated use of AnySurf*Fit classes identified. Compatibility mode entered. 
> 1) Use new concept by remove initializations of sRel and ARel (Recommended). 
> 2) Read the long error description to see how to maintain backwards compatibility of your model. 
```

The class `AnySurfCylinderFit` now inherits directly from `AnyRefNode` and creates a reference frame directly. 
So they should no longer be nested inside existing reference frames to calculate the position and orientation.

Imagine the following code:

```AnyScriptDoc

AnyRefNode Outer = 
{
    sRel = SurfFit.sRel;
    ARel = SurfFit.ARel;

    AnySurfCylinderFit SurfFit = 
    {
        Points = ...; 
        Length = ...;
    };
};

```
The `Outer` class gets the position and orientation from the inner `AnySurfCylinderFit` class.
This should be changed to: 

```AnyScriptDoc
AnySurfCylinderFit Outer = 
{
    Points = ...; 
    Length = ...;
};

```

In fact, the original would no longer give the correct result given the new properties of `AnySurfCylinderFit` as reference frame.
So AnyBody detects the old usage pattern and reverts to a 'Compatibility' mode. 

:::

