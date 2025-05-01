(Abdominal Pressure Model)=

# Abdominal Pressure Model

This model introduces intra-abdominal and intra-thoracic pressure, along with the diaphragm, which balance pressure balance between them.

The abdominal model consists of five layers connected to L1–L5, and layers connected to the pelvis and the diaphragm. Each layer contains multiple segments, constrained by averaging measures to maintain anatomical accuracy. Multiple nodes are defined on each layer, forming meshes that create volumes. These volumes can hold pressure and transfer forces to surrounding structures. As a result of the layer constraints, the volumes can compress or expand as the body moves. The detailed explanation of the model will be available in the forthcoming paper (Shayestehpour, H., Tørholm, S., Damsgaard, M., Lund, M., Wong, C., Rasmussen, J.: A generic detailed multibody abdominal and diaphragm model. Multibody Syst. Dyn.​).

Here are some examples of different postures of the abdominal pressure model.

```{image} _static/Abdomen_postures.png
```

## Pressure model
The transversus abdominis, obliquus, and rectus abdominis muscles wrap around the abdominal volumes, exerting posterior pressure. The diaphragm muscles support upward pressure transmission to the ribcage, while the pelvic floor absorbs downward pressure. This pressure model generates an extensor moment on the ribcage, integrating detailed muscle configurations.

<!-- This part is commented out for now. But later we can add it to the documentation
## Diaphragm model
Beside holding the pressure and transfering the force to the ribcage, the diaphragm mechanism can move inferosuperiorly according to anatomy and simulate breathing.
 
 ```{raw} html
<video width="60%" style="display:block; margin: 0 auto;" controls autoplay loop>
    <source src="../_static/Diaphragm_Moving_sagittal.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>
```-->

<!-- This part is not ready in the model yet. So the explanation is hidden in the HTML.

    ## Thoracic cavity

    The thoracic cavity can be set to have pressure, which will push or pull the ribcage in and out. This can be used for more detailed simulations if you are interested in thoracic and ribcage forces. Note that the default thoracic cavity pressure is OFF.

    .. image:: _static/Thoracic_Cavity.jpg
        :width: 60%
        :align: center-->





## Muscles configurations
New diaphragm muscles were introduced, and the abdominal muscles were updated. Below are figures of the new muscle configuration.

```{image} _static/Abdomen_muscles.png
```

## Example Configuration

The abdominal pressure model can be controlled using the `BM_*` statements like the rest of the body models. 


```{code-block} AnyScriptDoc
:emphasize-lines: 2

#define BM_TRUNK_CAVITY_MODEL _CAVITY_MODEL_BUCKLE_  //Enables the old buckle model
#define BM_TRUNK_CAVITY_MODEL _CAVITY_MODEL_VOLUME_  //Enables the new abdominal pressure model with the volumes

```


```{rst-class} without-title
```





% .. rst-class:: float-right

% .. seealso::

% The :doc:`Trunk configuration parameters <../bm_config/trunk>` for a

% full list of Trunk parmaeters.

## Resources
- Webcast on the [New AnyBody Thoracic Spine, Ribcage, and Abdominal Model](https://youtu.be/R4kM-ZKc8Gs?t=2)
- Shayestehpour, H., Tørholm, S., Damsgaard, M., Lund, M., Wong, C., Rasmussen, J.: A generic detailed multibody abdominal and diaphragm model. Multibody Syst. Dyn.​

## References
Will be available once the paper is published.
