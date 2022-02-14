(the-body-model)=

# The Body Models

Each body part is implemented utilizing data from detailed cadaver/anatomy
studies, thus ensuring high accuracy and anatomical fidelity.

See the section below for a more detailed description of the models and the underlying anatomical data.

```{rubric} Background
```

The body models live in the `Body/` subfolder within your AMMR directory. The folder names and organization here depend on
the origin of the models.

By far the most important folder is the `Body/AAUHuman`, which
contains the AnyBody full body model. It was originally developed at Aalborg
University, Denmark (with the acronym AAU) but also consists of body-parts (trunk
and extremities) that were either developed elsewhere or based on data sets
from elsewhere.

Two mandible models have also been developed but are yet to be assembled with
the AAUHuman. These two mandible models can be found in `Body/Mandible`

The `Body/Beta` folder contains less developed and tested models.

The different body parts included in the full body model are derived from
various anatomical databases from literature.

The segmental coordinate systems are constructed using the original data. To ensure having a well defined coordinate system for all segments an anatomical frame has been defined, the anatomical frame is constructed using well defined bony landmark locations on the bone.

The full body model
contains shoulder/arm, trunk, foot and multiple leg models
which can be assembled into the full human in many combinations.

:::{note}
Parts of the AAUHuman (except the
mandible) are by default assembled together into a full body model.
See {doc}`/bm_config/index` for re-configuring the model to for example, only represent the trunk, or use a different leg/muscle model.
:::

```{rubric} Models
```

```{toctree}
:caption: Trunk
:maxdepth: 1

lumbar_spine_model
cervical_spine_model
thoracic_model
```

```{toctree}
:caption: Upper extremity
:maxdepth: 1

shoulder_arm_model
detailed_hand_model
Regensburg-Ulm hand model <regensburg_ulm_hand_model>
```

```{toctree}
:caption: Lower extremity
:maxdepth: 1

leg_model
leg_tlem_model
leg_tlem2_model
GM Foot model <glasgow_maastricht_foot_model>
```

```{toctree}
:caption: other
:maxdepth: 1

symmetric_mandible_model
aalborg_mandible
```
