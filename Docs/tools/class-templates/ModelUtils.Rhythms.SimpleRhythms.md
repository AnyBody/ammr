(ModelUtils.Rhythms.SimpleRhythms.any)=
# SimpleRhythms



:::{code-block} AnyScriptDoc
:caption: Include this file this file to use
#include "<AMMR_TOOLS>\ModelUtilities\Rhythms\SimpleRhythms.any"`
::: 



(ModelUtils.Rhythms.SimpleRhythms.RhytmDriverLinear)=

## RhytmDriverLinear

:class template type: `AnyKinMotion`{l=AnyScript}

```{code-block} AnyScriptDoc
RhytmDriverLinear <ObjectName>(
  RELATIVE_TO_DOF=RELATIVE_TO_DOF,
  _REDEFINE_VARIABLES=_REDEFINE_VARIABLES,
) = {};
```

Creates a linear rhythm between the DOFs of measure



(ModelUtils.Rhythms.SimpleRhythms.RhytmDriverTwoWayLinear)=

## RhytmDriverTwoWayLinear

:class template type: `AnyKinEq`{l=AnyScript}

```{code-block} AnyScriptDoc
RhytmDriverTwoWayLinear <ObjectName>(
  NDIM=NDIM,
  RELATIVE_TO_DOF=RELATIVE_TO_DOF,
  _REDEFINE_VARIABLES=_REDEFINE_VARIABLES,
) = {};
```

Creates a two way rhythm between the DOFs


