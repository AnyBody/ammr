# Updating from AMMR 3

Models created in earlier versions of AnyBody may need to be updated to work with
AnyBody 8.1 and the new model repository (AMMR 4.0).

This document outlines important changes which may break
older models or change results.

<!-- :::{tip} 

See the last part of this document for a list of concrete errors and deprecation
warnings and how to fix them. 

::: -->

## Model changes

### Default pelvis

The default pelvis morphology is now the one from the trunk model, as oposed to
the pelvis belonging to whatever leg model has been selected. This was done to
get a consistent trunk model and considering all the recent improvements to the
trunk. This option can be controlled with:

```AnyScriptDoc
#define BM_LEG_TRUNK_INTERFACE _MORPH_LEG_TO_TRUNK_
```

In practice, this means that the morphology of the leg pelvis is moprhed to
match the Trunk pelvis. Using `_MORPH_TRUNK_TO_LEG_` instead will revert to the
old behaviour.

### Trunk changes

The trunk model in AMMR 4.0 is completly new, and many parts of the model structure has changed. 

::: {warning}
These postural changes will affect older applications. Especially, in models
where trunk joint angles are driven directly and in models where a driver is applied directly on the pelvis segmental reference frame.
:::

### Muscle groups in the model tree

Muscles elements are now grouped into folders representing the physiological muscles. 

References to their old locations may there break. You can enable backwards compatibility by setting:

```AnyScriptDoc
#define BM_COMPATIBILITY_MUSCLE_STRUCTURE ON
```

This add the old strucuture in addition to the new one, and should make it easier to update the model.


### MoCap models


## Load time errors


## Deprecation warnings
