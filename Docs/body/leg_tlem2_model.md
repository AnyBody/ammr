(tlem2)=

# Twente Lower Extremity Model v.2.2

The Twente lower extremity model version 2 (TLEM2) is a successor to the {doc}`TLEM 1
model <leg_tlem_model>`. It contains **6 DOF** and **169
muscles**.

```{raw} html
<video width="45%" style="display:block; margin: 0 auto;" controls autoplay loop>
    <source src="../_static/TLEM2_rotating_model.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>
```


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


## Background

The model is based on published anatomical data produced from a cadaver study in
the [TLEMsafe EU project](https://tlemsafe.eu/). The first implementation of
the musculoskeletal model was created by Vincenzo Carbone and René Fluit from
the University of Twente [^cite_cfpk15].

The key feature of TLEM 2 compared to older TLEM 1 model is a consistent
dataset, where both muscle attachment and bone surface scans are from the same
subject. This makes TLEM2 the more anatomically consistent model. Bone contact
at joints such as the knee thus consists of naturally congruent surfaces, making
it easier to implement Force Dependent Kinematics on joint movements ({doc}`see
tutorial <tutorials:ForceDependentKinematics/index>`)

The model was refined during the [Life Long Joints
project](https://web.archive.org/web/20230323035759/https://lifelongjoints.eu/) where its anatomical fidelity and joint
force prediction accuracy were improved by De Pieri et al. [^cite_dlgr17], 
mainly, by implementing better a wrapping surfaces for the muscles ([TLEM
v2.1](#TLEM2-v2.1)). 


::::{figure} _static/Wrapping_TLEM2.png
:width: 80%

New wrapping surfaces for (clockwise) Gluteus Maximus, Ilio-Psoas, Gluteus
Medius & Minimus, Hamstrings & Gastrocnemius. All figures are
from the publication by De Pieri et al. [^cite_dlgr17]

::::


Subsequently, the model has been updated again (currently [TLEM
v2.2](#TLEM2-v2.2)) with muscle wrapping for the Achilles tendon, as well as
updates to the implementation of the ankle complex in preparation for new multi
segment foot models. 







## Resources

More details on the TLEM2 model can be found online:

- Webcast: [TLEMsafe: Personalization of musculoskeletal models and prediction of functional outcome](https://www.anybodytech.com/download/tlemsafe-personalization-of-musculoskeletal-models-and-prediction-of-functional-outcome/)
- Webcast: [TLEMsafe: An integrated system to improve predictability of functional recovery of patients requiring musculoskeletal surgery](https://www.anybodytech.com/download/tlemsafe-an-integrated-system-to-improve-predictability-of-functional-recovery-of-patients-requiring-musculoskeletal-surgery/)





## History and changes:

(TLEM2-v2.2)=

TLEM v2.2 (Released in AMMR 3.0.0)
: Wrapping surfaces have been added to the Achilles tendon around the ankle in
  the TLEM 2 leg model (now designated TLEM 2.2). This ensures an even ratio of moment arms between
  the soleus and gastrocnemius muscles. Hence, gastrocnemius is recruited less, 
  especially during downhill walking and stair descent, solving the tendency of the model 
  to overpredict the knee contact forces at toe off. 
  This is the first of a number of improvements to the leg model by Dr. Enrico De Pieri, 
  who is working on a publication on improvements and validation of the TLEM 2 leg model.
: The ankle complex has been redefined to compensate for the non-neutral position in which the 
  cadaver was scanned. The method described in Stolle et al.[^cite_slnbrmv22] was adapted to 
  identify coordinate systems at the tibia, talus, and calcaneus using their respective 
  bone surfaces. The coordinate systems were then used to reposition the bone surfaces using 
  the average values provided in Stolle et al.[^cite_slnbrmv22] for talus-calcaneus and 
  calcaneus-tibia. These values are based on weight-bearing scans in neutral, bilateral 
  standing position of 95 healthy adult subjects. This improves the alignment of the tibia, 
  talus, and calcaneus bones.
  
  With the redefined alignment of the ankle complex, the ankle joint axis was updated using 
  the method described in Montefiori et al.[^cite_mmmmmprhdww19] The joint axis was defined 
  as the axis of a cylinder fitted to the talar trochlea. The ankle joint centre was defined 
  at the midpoint of the medial and lateral malleoli projected on the ankle axis.

  The knee joint was also updated to compensate for the non-neutral scan of the cadaver. The
  updated joint ensures that the patella tendon is straight in the neutral position. 
  The net effect is rotation of the tibia about its long axis with the feet still pointing in 
  the same direction in the neutral position. 
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
    on heel, fifth metatarsal, and medial sesamoid on first metatarsal. This will update 
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

The following video compares TLEM v2.2 with TLEM v2.1 (in gray). The knee and
and ankle joint axes in blue belong to TLEM v2.2 while the ankle joint axes in
gray belongs to TLEM v2.1
```{raw} html
<video width="45%" style="display:block; margin: 0 auto;" controls autoplay loop>
    <source src="../_static/TLEM22_TLEM21_rotating_model.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>
```
::::{figure} _static/TLEM22_TLEM21_closeup.jpg
:width: 80%

Comparison of TLEM v2.2 with TLEM v2.1 (in gray). Please note the patella tendon in
gray inserts in TLEM v2.1 shank. It depicts the rotational offset of the tibia along
its axis.

::::
(TLEM2-v2.1)=

TLEM v2.1 (Released in AMMR 2.0.0)
: Wrapping surfaces for several muscles were updated. These changes were engineered to
  result in realistic muscle coordination and hip contact forces as documented
  in the publication by De Pieri et al. [^cite_dlgr17]

## Citing and references

If you need to cite the model use the following references [^cite_dlgr17], [^cite_cfpk15]. Other useful papers using or related to the TLEM2 model are: [^cite_ca16] and [^cite_ckkv16]. 


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

[^cite_slnbrmv22]: Stolle,J., Lintz,F., de Cesar Netto,C., Bernasconi,A., Rincon,MR., Mathew,R., Vispute,D., Siegler,S. 
    "Three-dimensional ankle, subtalar, and hindfoot alignment of the normal, weightbearing hindfoot, in bilateral 
    posture", J. Orthop. Res., 40(10) (2022) 2430-2439 ([link](https://onlinelibrary.wiley.com/doi/10.1002/jor.25267)).

[^cite_mmmmmprhdww19]: Montefiori,E., Modenese,L., Di Marco,R., Magni-Manzoni,S., Malattia,C., Petrarca,M., 
    Ronchetti,A., de Horatio,LT., van Dijkhuizen,P., Wang,A., Wesarg,S., "An image-based kinematic model of 
    the tibiotalar and subtalar joints and its application to gait analysis in children with Juvenile 
    Idiopathic Arthritis", J. Biomech., 85 (2019), 27-36. ([link](https://doi.org/10.1016/j.jbiomech.2018.12.041)).