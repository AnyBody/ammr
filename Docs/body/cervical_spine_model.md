# The Cervical Spine Model

The cervical spine model is the neck of the human model. It is always present
when the human model is used.

The cervical spine model contains **7 vertebrae** with 3 DoF spherical
joints from T1 to C2, a 1 DoF joint between C2 and skull and **136 muscle
fascicles**. The center of rotations is based on Amevo et al. 1991.

The cervical spine model is part of the Trunk model, and the segments,
joints and kinematics are therefore included by default.

The segments of the cervical spine model are always present, but the muscles are
not enabled by default. **Some of the neck muscles are defined by the shoulder
model, so the muscles of the cervical spine model can only be enbled when both
arms with muscles are present.**

```{raw} html
<video width="49%" style="display:block; margin: 0 auto;" controls autoplay loop>
    <source src="../_static/CervicalSpine_rotating_model.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>
<!--<img src="../_static/CervicalSpineCloseupBack.jpg" alt="Smiley face" width="49%">-->
```

## Example Configuration

Enabling muscles from the cervical spine model, requires that the arms
also enabled.

```{code-block} AnyScriptDoc
:emphasize-lines: 4

#define BM_ARM_RIGHT ON
#define BM_ARM_LEFT ON
#define BM_ARM_MUSCLE_BOTH ON
#define BM_TRUNK_CERVICAL_MUSCLES ON
```

```{rst-class} float-right
```

:::{seealso}
The {doc}`Trunk configuration parameters <../bm_config/trunk>` for a
full list of Trunk parmaeters.
:::

## Resources

More details on the cervical spine can be found online at:

- Thesis: Data on which the cervical spine model, described by [Marike van der
  Horst](http://alexandria.tue.nl/extra2/200211336.pdf)
- Webcast: [A detailed rigid-body cervical spine model based on inverse
  dynamics](https://www.anybodytech.com/a-detailed-rigid-body-cervical-spine-model-based-on-inverse-dynamics/)

## References

- de Zee, M., Falla, D., Farina, D. & Rasmussen, J. (2007), "A detailed
  rigid-body cervical spine model based on inverse dynamics", Journal
  of Biomechanics, vol. 40 (2), pp. S284.
