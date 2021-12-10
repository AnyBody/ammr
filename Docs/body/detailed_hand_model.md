# Detailed hand model

The AnyBody detailed hand model is a model of the carpal bones with 17 DOFs. The model
has no muscles, but the joints are equiped with joint actuators, so the model can
be used for dynamic analysis.

:::{figure} _static/DetailedHandCloseUp.jpg
:width: 50%
:::

## Example Configuration

Short example of how to configure and enable the model:

```AnyScriptDoc
    #define BM_HAND_MODEL  _HAND_MODEL_ANYBODY_ 
```

If you haven't include a custom mannequin file in your model, you can directly specify the posture of the
detailed hand model by setting the values  in `Main.HumanModel.Mannequin`:

```AnyScriptDoc
HumanModel.Mannequin.Posture.Right = {
  Finger1 =
  {
     CMCAbduction = 10;
     CMCFlexion = 40;
     MCPFlexion = 55;
     MCPAbduction = 0.0;
     DIPFlexion = 20;
  };
  Finger2 =
  {
    MCPFlexion = 10;
    PIPFlexion = 10;
    DIPFlexion = 5;
  };
};
```

```{raw} html
<video width="49%" style="display:block; margin: 0 auto;" controls autoplay loop>
    <source src="../_static/DetailedHand_ThumbsUp.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>
```

```{rst-class} float-right
```

:::{seealso}
The {doc}`Arm configuration parameters <../bm_config/arm>` for a
full list of parmaeters.
:::
