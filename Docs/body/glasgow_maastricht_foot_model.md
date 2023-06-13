# The Glasgow-Maastricht Foot Model (GM Foot)

:::{admonition} **External model:** 
:class: caution 
The model is under development and not yet included in the managed model repository.
You can find this model in a public [repository on GitHub](https://github.com/AnyBody/gm-foot).
:::

AnyBody Technology developed in corporation with Glasgow Caledonian
University and University of Maastricht inside the [AFootprint EU project](https://web.archive.org/web/20190502001603/https://www.afootprint.eu/)
a detailed multisegmental foot model, which is fully dynamic and
contains 26 segments representing all the foot bones, muscles,
ligaments, and joints connecting them.

The model can be used with the
anatomy and recorded motion from different subjects. It has been through
a validation process comparing it with other experimental and computational studies.

:::{admonition} **Complex model:**
:class: warning
The GM Foot model is very complex and not recommended for
beginners in musculoskeletal modeling and AnyBody.
:::

```{raw} html
<video width="45%" style="display:block; margin: 0 auto;" controls autoplay loop>
    <source src="../_static/footgm.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>
```




## Usage:

The model can added to the TLEM 2.0 leg model and requires AMMR 2.0.1 or later.

To use the GM foot model the file GM_Foot_libdef.any must be included before the first Main statement.

```AnyScriptDoc
// Include before the first Main
#include "path/to/GM_Foot/GM_Foot_libdef.any"

Main = {

   // Add body model configuration. E.g.
   #define BM_ARM_RIGHT OFF
   #define BM_ARM_LEFT OFF

   // Include the GM foot model. It handles inlcuding the human model as well.
   #include "<GM_FOOT_PATH>/GM_foot_model.any"
```

## Model structure

The foot model includes 26 rigid segments representing all the bones of
the human foot (except the sesamoid bones), namely:

> Talus, Calcaneus,
> Cuboid, Navicular, Medial cuneiform, Intermediate cuneiform, Lateral
> cuneiform, First metatarsal, Second metatarsal, Third metatarsal, Fourth
> metatarsal, Fifth metatarsal, First proximal phalange, First distal
> phalange, Second proximal phalange, Second medial phalange, Second
> distal phalange, Third proximal phalange, Third medial phalange, Third
> distal phalange, Fourth proximal phalange, Fourth medial phalange,
> Fourth distal phalange, Fifth proximal phalange, Fifth medial phalange,
> Fifth distal phalange.

It includes the following joints and kinematic constraints:

> *Talocrural*  *and Subtalar joint \[20\],*  *Talonavicular joint,*
> *Calcaneocuboid joint,*  *Medialcuneonavicular joint,*
> *Intermediate and lateral cuneonavicular joints,*  *First
> tarsometatarsal joint,*  *Second, third and fourth tarsometatarsal
> joints,*  *Fifth tarsometatarsal joint,*  *Metatarsophalangeal
> joints,*  *Interphalangeal joints,*  *Toe flexion rhythm,*
> *Intertarsal contact,*  *Metatarsal head contact,*  *Metatarsal
> transverse arch,*  *Tarsal transverse arch,*  *Longitudinal medial
> arch,*  *Longitudinal lateral arch.*

The GM-Foot model includes following additional ligaments:

> Collateral
> (tibiotalar anterior, tibiotalar posterior, tibiocalcaneal and
> tibionavicular, and the lateral group constituted of the talofibular
> anterior, talofibular posterior and talocalcaneal), Deep metatarsal
> transverse, Plantar fascia, Long plantar, Calcaneo cuboid plantar,
> Calcaneo navicular plantar, Tarsal ligaments ( Talonavicular dorsal,
> Bifurcate, Calcaneocuboid dorsal, Cuneonavicular dorsal 1, 2 and 3,
> Cuneonavicular plantar 1, 2 and 3, Intercuneiform dorsal 1 and 2,
> Cuneocuboid dorsal, Intercuneiform plantar 1 and 2, Cuneocuboid plantar,
> Cuboideonavicular dorsal, Cuboideonavicular plantar, Tarsometatarsal
> dorsal 1 to 8, Tarsometatarsal plantar 1 to 7, Intermetatarsal dorsal 1,
> 2 and 3, Intermetatarsal plantar 1, 2 and 3) and Phalangeal ligaments

The muscles of the foot can be divided into two groups: the intrinsic
muscles and the extrinsic muscles. All the extrinsic muscles come from
the TLEM leg model of the AMMR. The intrinsic foot musculature is
constituted of the following muscles:

> abductor hallucis (ABDH), flexor hallucis brevis medialis (FHBM) and
> lateralis (FHBL), adductor hallucis transverse (ADHT) and oblique
> (ADHO), abductor digiti minimi (ABDM), flexor digiti minimi brevis
> (FDMB), dorsal interosseous (DI), plantar interosseous (PI), flexor
> digitorum brevis (FDB), lumbricals (LB), quadratus plantar medialis
> (QPM) and lateralis (QPL), extensor hallucis brevis (EHB), extensor
> digitorum brevis (EDB)

More information can be found online:

- **The new Glasgow-Maastricht AnyBody foot model** (Sylvain Carbes,
  20\. September, 2012)

  [Presentation
  (2Mb)](https://www.anybodytech.com/the-new-glasgow-maastricht-anybody-foot-model/?wpdmdl=3101&ind=0),
  [YouTube](https://www.anybodytech.com/download/the-new-glasgow-maastricht-anybody-foot-model/)

  This webcast presents a detailed AnyBody musculoskeletal foot model
  which includes all bones and joints of a real foot. Developed in
  collaboration with Glasgow Caledonian University and University
  Hospital Maastricht and referred to as the "Glasgow-Maastricht foot
  model" this model can be driven by motion capture data and uses
  combined force plate/pressure plate for accurate loading of the
  different joints. Built-in scaling allows the user to reproduce
  principal foot deformities such as flat foot and hallux valgus. The
  high detail level of the model and a built-in scaling protocol allows
  the user to investigate a wide range of parameters like joints motion
  and load, muscles activation, both in healthy and pathologic feet.

References used as input:

- Arampatzis, S. et al., Strain and elongation of the human
  gastrocnemius tendon and aponeurosis during maximal plantarflexion
  effort. J Biomech, 38(4):833–841, Apr 2005.
- Arndt, P. et al., Intrinsic foot kinematics measured in vivo during
  the stance phase of slow running. J Biomech, 40(12):2672–2678, 2007.
- Bandholm, T et al., Foot medial longitudinal-arch deformation during
  quiet standing and gait in subjects with medial tibial stress
  syndrome. J Foot Ankle Surg, 47(2):89–95, 2008.
- Bloome, DM et al., Variations on the insertion of the posterior
  tibialis tendon: a cadaveric study. Foot Ankle Int, 24(10):780–783,
  Oct 2003.
- Cailliet, R. The Illustrated Guide to Functional Anatomy of the
  Musculoskel. Sys.. D J R Evans, 2004.
- Cheung, JT et al., Three-dimensional finite element analysis of the
  foot during standing–a material sensitivity study. J Biomech,
  38(5):1045–1054, May 2005.
- Fernandes, R. et al., Tendons in the plantar aspect of the foot: Mr
  imaging and anatomic correlation in cadavers. Skeletal Radiol,
  36(2):115–122, Feb 2007.
- Funk, JR et al., Linear and quasi-linear viscoelastic
  characterization of ankle ligaments. J Biomech Eng, 122(1):15–22, Feb
  2000\.
- Kanatli, U. et al., Evaluation of the transverse metatarsal arch of
  the foot with gait analysis. Arch Orthop Trauma Surg, 123(4):148–150,
  May 2003.
- Kitaoka, HB, et al., Mat properties of the plantar aponeurosis. Foot
  Ankle Int, 15(10):557–560, 1994.
- Kura, H, et al., Quant. analysis of the intrinsic muscles of the
  foot. Anat Rec, 249(1):143–151,1997.
- Lundberg and O.K. Svensson. The axes of rotation of the talocalcaneal
  and talonavicular joints. The Foot, 3(2):65 – 70, 1993.
- Lundgren, P, et al., Invasive in vivo measurement of rear-, mid- and
  forefoot motion during walking. Gait Posture, 28(1):93–100, Jul 2008.
- MacWilliams, BA, et al., Foot kinematics and kinetics during
  adolescent gait. Gait Posture, 17(3):214–224, Jun 2003.
- Mengiardi, B, et al., Spring ligament complex: Mr imaging-anatomic
  correlation and findings in asymptomatic subjects. Radiology,
  237(1):242–249, Oct 2005.
- Moraes do Carmo, CC, et al., Anatomical features of plantar
  aponeurosis: cadaveric study using ultrasonography and magnetic
  resonance imaging. Skeletal Radiol, 37(10):929–935, Oct 2008.
- Netter, FH. Atlas der Anatomie des Menschen 3nd. Georg Thieme Verlag
  Stuttgart, 2003.
- Pastore, D, et al., Complex distal insertions of the tibialis
  posterior tendon: detailed anatomic and mr imaging investigation in
  cadavers. Skeletal Radiol, 37(9):849–855, Sep 2008.
- Patil, V. et al. Morphometric dimensions of the calcaneonavicular
  (spring) ligament. Foot Ankle Int, 28(8):927–932, Aug 2007.
- Patil, V. et al., Anatomical variations in the insertion of the
  peroneus (fibularis) longus tendon. Foot Ankle Int, 28(11):1179–1182,
  Nov 2007.
- Picard, M et al., orthopedic physical assessment 3rd edition (1997)
  wb saunders company,philadelphia 805 pp. 49.95. Journal of Hand
  Therapy, 11(4):286 –, 1998.
- Siegler, S, et al., Mechanics of the ankle and subtalar joints
  revealed through a 3d quasi-static stress mri technique. J Biomech,
  38(3):567–578, Mar 2005.
- Sooriakumaran, P and Sivananthan, S. Why does man have a quadratus
  plantae? a review of its comparative anatomy. Croat Med J,
  46(1):30–35, Feb 2005.
- Stagni, R., et al., Ligament fibre recruitment at the human ankle
  joint complex in passive flexion. J Biomech, 37(12):1823–1829, Dec
  2004\.
- Taniguchi, A. et al., Anat. of the spring ligament. J Bone Joint Surg
  Am, 85-A(11):2174–2178, 2003.
- Ward, KA and R. W. Soames. Morphology of the plantar calcaneocuboid
  ligaments. Foot Ankle Int, 18(10):649–653, Oct 1997.
- Winson, IC., et al., Metatarsal motion. The Foot, 5(2):91 – 94, 1995.
- Winson, IC., et al., Passive regulation of impact forces in heel-toe
  running. Clin Biomech (Bristol, Avon), 13(7):521–531, Oct 1998.
