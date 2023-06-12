(tlem2)=

# Twente Lower Extremity Model v.2.2
:::{versionadded} 2.5.0
TLEM 2.2 is introduced.
:::
The Twente lower extremity model version 2 (TLEM2) is a successor to the {doc}`TLEM
model <leg_tlem_model>`. It contains **6 DOF** and **169
muscles**.

```{raw} html
<video width="45%" style="display:block; margin: 0 auto;" controls autoplay loop>
    <source src="../_static/TLEM2_rotating_model.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>
```

The model is based on published anatomical data produced from a cadaver study in
the [TLEMsafe EU project](https://tlemsafe.eu/) (see the study by Carbone
et al. at the University of Twente, The Netherlands). The first implmentation of
the musculoskeletal model was created by Vincenzo Carbone and René Fluit from
the University of Twente [^cite_cfpk15].

The key feature of the TLEM 2 model is consistent database:
: Unlike the old TLEM model, the dataset consisted of muscle attachment data &
  bone surface scans from the same subject. This makes TLEM2 the more
  anatomically consistent model. Bone contact at joints such as the knee thus
  consists of naturally congruent surfaces, making it easier to implement
  Force Dependent Kinematics on joint movements ({doc}`see tutorial <tutorials:ForceDependentKinematics/index>`)

## Updates to the TLEM2 model:

:::{admonition} Introduced in
:class: margin
 AMMR 2.5.0. See {doc}`Changelog <../changelog>` 
:::
TLEM v2.2
: The foot and talus models have several updates in preparation for the 
  release of advanced multi-segment foot models in the future:  
  - The talus coordinate system is updated to be coincident with the foot 
    coordinate system in the neutral position. This facilitates scaling
    of subject-specific foot models that would normally include the foot 
    and talus in the same coordinate system. For backwards compatibility,
    a new reference node, `TalusCompatibilityFrameAMMR24`, is created in the 
    talus segment. This reference node has the same position and orientation 
    as the previous coordinate system of talus.
  - The update of the talus coordinate system allows reusing some of the 
    parameters from the foot model and simplifies the code. The talus now uses the
    subtalar joint parameters from the foot model. The ankle joint parameters 
    have been updated to be expressed in the new coordinate system. However, 
    both joints are consistent with the previous implementation. 
  - The anatomical frames of the foot and the talus are now defined using bony 
    landmarks on the foot and the lateral and medial malleoli. The vertical axis 
    is defined as the perpendicular to three coplanar points that can be considered 
    parallel to the ground. In the new implementation, these are the lowermost points
    on heel, metatarsal 5, and medial sesamoid on metatarsal 1. This will update 
    the neutral position of the foot and talus. Moreover, this will also affect the 
    ankle plantarflexion and subtalar joint angles.
    :::{warning}
    Ankle and Subtalar joint angle measures are updated. Please
    run `MarkerTracking` again for mocap models if using TLEM 2.2.
    :::
  - The malleoli coordinates in the foot coordinate system have been fixed to 
    match the malleoli on the shank in the neutral position.
  - The model tree has been updated. The talus segment is moved inside the 
    foot segment. For backwards compatibility, a pointer to the talus segment 
    still exists outside the foot segment.

:::{admonition} Introduced in 
:class: margin
AMMR 2.0.0. See {doc}`Changelog <../changelog>`
:::
TLEM v2.1
: After the TLEM*safe* project the model was further refined
  in the [Life
Long Joints project](https://lifelongjoints.eu/) where its anatomical
fidelity and joint force prediction accuracy were improved by De Pieri et al.
[^cite_dlgr17], resulting the version 2.1 which was integrated here in the AMMR.




: Wrapping surfaces for several muscles were updated. These changes were engineered to
  result in realistic muscle coordination and hip contact forces as documented
  in the publication by De Pieri et al. [^cite_dlgr17]

:::{figure} _static/Wrapping_TLEM2.png
:width: 80%

*New wrapping surfaces for (clockwise) Gluteus maximus, Ilio-Psoas, Gluteus
medius & minimus, Hamstrings & Gastrocnemius (version 1.2). All figures are
from the publication by De Pieri et al.* [^cite_dlgr17]
:::

## Example Configuration

Short example of how to configure the model with the TLEM model, Hill type
muscle model and only one leg:

:::{seealso}
:class: margin
The {doc}`Leg configuration parameters <../bm_config/leg>` for a
full list of configuration parameters.
:::

```AnyScriptDoc
#define BM_LEG_MODEL _LEG_MODEL_TLEM2_
#define BM_LEG_RIGHT ON
#define BM_LEG_LEFT OFF
#define BM_LEG_MUSCLE _MUSCLES_3E_HILL_
```




## Resources

More details on the TLEM2 model can be found online:

- Webcast: [TLEMsafe: Personalization of musculoskeletal models and prediction of functional outcome](https://www.anybodytech.com/tlemsafe-personalization-of-musculoskeletal-models-and-prediction-of-functional-outcome/)
- Webcast: [TLEMsafe: An integrated system to improve predictability of functional recovery of patients requiring musculoskeletal surgery](https://www.anybodytech.com/tlemsafe-an-integrated-system-to-improve-predictability-of-functional-recovery-of-patients-requiring-musculoskeletal-surgery/)

## Citing and references

If you need to cite the model use the following references [^cite_dlgr17], [^cite_cfpk15]. Other usefull papers using or related to the TLEM2 model are: [^cite_ca16] and [^cite_ckkv16]. 


[^cite_dlgr17]: De Pieri,E., Lund,ME., Gopalakrishnan, A, Rasmussen, KP., Lunn, DE., Ferguson, SJ.
    “Refining muscle geometry and wrapping in the TLEM 2 model for improved hip contact force prediction”
    PloS One 13 (2018) ( [link](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0204109) )

[^cite_cfpk15]: Carbone,V., Fluit,R., Pellikaan,P., van der Krogt,MM., Jansen,D., Damsgaard,M.,
    Vigneron,L.,Feilkas,T., Koopman,HF., Verdonschot,N.,
    "Tlem 2.0–A comprehensive musculoskeletal geometry dataset for subject-specific
    modeling of lower extremity", J. Biomech.,48(5) (2015) 734-741.


[^cite_ca16]: Carbone,V., "Subject-specific lower extremity modeling: personalization of
    musculoskeletal models using medical imaging and functional measurements",
    PhD thesis, University of Twente, Netherlands (2016).

[^cite_ckkv16]: Carbone,V., van der Krogt,MM., Koopman,HF., Verdonschot,N., "Sensitivity of subject-specific
    models to Hill muscle-tendon model parameters in simulations of gait",
    J. Biomech.,49 (2016) 1953-1960.
