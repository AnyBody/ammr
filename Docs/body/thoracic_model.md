(thoracic-model)=

# Thoracic spine model

:::{admonition} **Unreleased model:** 
:class: caution
The model is under development and not yet included in the managed model repository.
The model is used in various research projects and access to the model can be given on request. Please
[contact us](mailto:sales@anybodytech.com) if you are interested in this work.
:::


```{image} _static/Detailed-thorax.png
```

The thoracic spine model consists of the thoracic vertebral column and the
ribcage, including individual ribs and a two part sternum. The many segments interconnected by joints
replicates the physiological connection and load transfer mechanisms.



## Kinematics and spine rhythms 

The thoracic vertebral column contains 12 vertebrae with 3 DoF spherical joints
in between each 2 vertebrae, connecting to the cervical spine through a
spherical joint at T1C7 levels, and a spherical joint to the lumbar spine at
T12L1 levels. Costovertebral and sternocostal joint are also represented through
kinematic joints. All vertebra are linked with rhythm drivers to allow easy use. 


```{raw} html
<video width="100%" style="display:block; margin: 0 auto;" controls autoplay loop>
    <source src="../_static/rhythms.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>
```

## Muscles configurations

The majority of the muscle fascicles are defined for the thoracic column, ribcage region 
as well as a diaphragm muscles to simulatate breathing and abdominal volume pressure. 


```{image} _static/Detailed-thorax2.png
```


% .. image:: _static/thoracic.png

% :width: 100%

## Example Configuration

The detailed thoracic model can be controlled using the `BM_*` statements like the rest of the body models. 


```{code-block} AnyScriptDoc
:emphasize-lines: 3

  #define BM_TRUNK_THORACIC_MODEL _THORACIC_MODEL_FLEXIBLE_   //Enables the detailed thoracic model

  #define BM_TRUNK_CAVITY_MODEL _CAVITY_MODEL_VOLUME_  //Enables the new abdominal volume model

```


```{rst-class} without-title
```

:::{note}
**Planned for AMMR 4.0:** The model is scheduled to be released together with AMMR 4.0. But a beta release will be available on GitHub when AMMR 3.0 comes out.
Otherwise, for early access please [contact us](mailto:sales@anybodytech.com).
:::



% .. rst-class:: float-right

% .. seealso::

% The :doc:`Trunk configuration parameters <../bm_config/trunk>` for a

% full list of Trunk parmaeters.

## References

- Ignasiak, D., Dendorfer, S., Fergusson, S.J. (2016), "Thoracolumbar spine model with
  articulated ribcage for the prediction of dynamic spinal loading",
  Journal of Biomechanics, vol. 49 (6), pp. 959-966.
- Shayestehpour, H., Toerholm, S.,  Lund, M.E., Rasmussen, J. (To be submitted), "A generic detailed multibody thoracic spine and ribcage model."
  Journal of Multibody system dynamics.