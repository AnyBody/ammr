# Migrating models to AMMR 2.5


## Introduction

Advanced models or models modifying the body models may need to be changed in order to work with the newest version of AnyBody. 

This documents shows some error which may occur and how to fix them.

## Migratin from AMMR 2.4 to 2.5

### Model changes

### MoCap models

#### Pelvic markers

Changes to the pelvic tilt means that markers on the pelvis located directly in
the pelvis Anatomcial frame will have moved slightly. This i most noticable for
markers on the posterior part of the pelvis (i.e. PSIS markers). The Y component
may need to be adjusted to achieve same marker position and joint angle output. 

If markers are placed relative to bony landmarks (using the `PlaceMarkerAt=`
argument) this problem will not occur.

#### Foot markers

Changes to the antomical frame of the foot and talus segment may cause markers
to have moved slightly. The Y component may need to be adjusted to achieve same
frame can casuse marker position and joint angle output.


### Load time errors

#### Unresolved `Scale_Leg_Pelvis`

```
ERROR(SCR.PRS9) :   some-file.any(##)  :   'Scale_Leg_Pelvis'  :  Unresolved object
```

The functions `Scale_Leg_Pelvis` and `Scale_Trunk_Pelvis` on the pelvis segment have been moved inside the `AnatomicalFrame` folder. 
So update code to `AnatomicalFrame.Scale_Leg_Pelvis`.


#### Unresolved `MusPar` folder


```
ERROR(SCR.PRS9) :   some-file.any(##)  :   'MusPar'  :  Unresolved object
```

The `MusPar` folder have been renamed to `MuscleModels`. 

#### Unresolved `PCSAfactor` variable

> ERROR(SCR.PRS9) :   xxx.any(##)  :   'PCSAfactor'  :  Unresolved object

This could be cause by the fact that the `MuscleParameters.Muscles.PCSAfactor` is  now located at `MuscleModels.DefaultMusPar.PCSAfactor`

#### `StringMesh`  :  Error in expression

> ERROR(SCR.EXP0) :   Ligaments.any(18)  :     Defined at :   Class_CreateLigament.any(47)  :   StringMesh  :  Error in expression. Please refer to the following error messages for details ...
> ERROR(SCR.EXP1) :   Ligaments.any(18)  :     Defined at :   Class_CreateLigament.any(47)  :   Operator '='  :  Illegal operation for given argument types  :  'AnyInt[Undefined]' '=' 'AnyFloatVar'

The `StringMesh` variable have changed type from `AnyVar` to `AnyInt`. So if `StringMesh` is assigned from an other variable, make sure that it has the type `AnyInt`.


### Deprecation warnings

#### Deprecated AnyMuscle class names

```
WARNING(SYS3) :  ... :  Deprecated class  :  Class 'AnyViaPointMuscle' was renamed to 'AnyMuscleViaPoint'
WARNING(SYS3) :   ...  :  AnyShortestPathMuscle  :  Deprecated class  :  Class 'AnyShortestPathMuscle' was renamed to 'AnyMuscleShortestPath'
```
Some class names for `AnyMuscle` have been deprecaed. Just rename them. 

*  `AnyViaPointMuscle` --> `AnyMuscleViaPoint`
*  `AnyShortestPathMuscle` --> `AnyMuscleShortestPath`

#### Deprecated use of AnySurf*Fit classes

```
ERROR(OBJ.MCH.SURF4) :   Custom_Seg_Shank.any(114)  :   Surf  :  Deprecated use of AnySurf*Fit classes identified. Compatibility mode entered. 
> 1) Use new concept by remove initializations of sRel and ARel (Recommended). 
> 2) Read the long error description to see how to maintain backwards compatibility of your model. 
```

The class `AnySurfCylinderFit` now inherits directly from `AnyRefNode` and can create a reference frame directly. 
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
The `Outer` class gets the positon and orientation from the inner `AnySurfCylinderFit` class.
This should be changed to: 

```AnyScriptDoc
AnySurfCylinderFit Outer = 
{
    Points = ...; 
    Length = ...;
};

```

In fact, the original would no longer give the correct result given the new properties of `AnySurfCylinderFit` as reference frame.
So AnyBody detects the old usage pattern and reverts to a 'compatability' mode. 




