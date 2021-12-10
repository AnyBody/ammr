# The Lumbar Spine Model

The Lumbar spine contains **5 vertebrae** with 3 DoF spherical joints in
between, **188 muscle fascicles** and a model of intra-abdominal pressure.

```{raw} html
<!--<img src="../_static/LumbarSpineBack.jpg" alt="Smiley face" width="32%">
<img src="../_static/LumbarSpineFront.jpg" alt="Smiley face" width="32%">-->
<video width="32%" style="display:block; margin: 0 auto;" controls autoplay loop>
    <source src="../_static/LumbarSpine_rotating_model.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>
```

Since it is impractical to measure or specify the motions of individual segments within the spine
(termed functional spinal units or FSU), these motions are prescribed by default as a function of overall lumbar curvature.
These functions are known as kinematic rhythms.

Facet joints are also not employed by default, since most applications do not focus on the lumbar spine
section. However, several examples in `AMMR/Applications` folder demonstrate possible mechanisms of
facet joint incorporation and detailed modeling of the lumbar spine.

The spinal muscles do not include the force-length-velocity relations (i.e.
we use the so-called simple muscle model). The only input parameter in
the muscle model is the cross-sectional area multiplied by a factor.
Daggfeldt and Thorstensson (J.Biomech. 2003, 36: 815-825) didn't include
the force-length-velocity relations either.

The inclusion of the lumbar spine ligaments is optional and can be defined as a cumulative stiffness of
FSUs or as separate elastic elements. Similarly, the intervertebral disc
(IVD) stiffness can be defined as a single cumulative value for a FSU or as
linear and nonlinear functions for the disc alone. This, however, is
mostly utilized for the spine specific applications, where such a level of
detail is important.

In other cases, it has been shown that the torque
production from ligaments might not be very important (Cholewicki and
McGill, J.Biomech. 1992, 25: 17-28). The data of vertebrae dimensions
and whole body parameters is taken from: Nissan and Gilad (J.Biomech.
19: 753-758, 1986) and mechanical properties of ligaments were taken
from: Pintar et al. (J.Biomech. 25(11): 1351-1356, 1992).

The spine model contains a preliminary model of the Intra Abdominal
pressure (IAP). In short the abdomen is modeled as constant volume, which,
when squeezed from the side by the transversus muscles extends the spine
by pushing on the rib thorax and the pelvic floor.

From the mathematical
point-of-view, this lets the abdominal muscles function as spine
extensors, and they become part of the whole recruitment problem. The
limit of the IAP was set to 26600 Pa, which was based on measurements on
well-trained subjects (Essendrop, M., 2003. Significance of
intra-abdominal pressure in work related trunk-loading. Ph.D. Thesis,
National Institute of Occupational Health, Denmark.) and using
geometric/anatomical estimates of pressure surface area and area
centroids, which in turn determines the effective moment arm of the
resulting forces.

## Example Configuration

The lumbar spine model is always part of the AnyBody Human model. The muscles can
be enabled/disabled, and the lumbar disc stiffness can be controlled.

```AnyScriptDoc
#define BM_TRUNK_MUSCLES ON
#define BM_TRUNK_DISC_STIFNESS _DISC_STIFFNESS_LINEAR_
```

```{rst-class} float-right
```

:::{seealso}
The {doc}`Trunk configuration parameters <../bm_config/trunk>` for a
full list of Trunk parameters.
:::

## Resources

More details on the lumbar spine model can be found online:

- Presentation about the [Abdominal pressure
  Presentation](https://www.anybodytech.com/download.html?did=publications.files&fname=AbdominalPressureModel.pdf)
- Webcast: [A lumbar spine model with facets joints and a dynamic stabilization device](https://www.anybodytech.com/downloads/documentation/#20101221)
- Webcast: [Implementation of facet joints in a lumbar spine model](https://www.anybodytech.com/downloads/documentation/#2008925)
- Webcast [A detailed rigid-body cervical spine model based on inverse
  dynamics](https://www.anybodytech.com/anybody.html?fwd=webcasts#2007918)
- Webcast [A generic detailed rigid-body lumbar spine model](https://www.anybodytech.com/anybody.html?fwd=webcasts#2006124)
- PowerPoint presentation [Spine Rhythm Presentation (PDF with videos click to activate
  them)](https://www.anybodytech.com/download.html?did=publications.files&fname=Spinerhythm.pdf)

You can read more about this lumbar spine model and some preliminary
validation in the following article:

- de Zee, M., L. Hansen, C. Wong, J. Rasmussen, and E.B. Simonsen. A
  generic detailed rigid-body lumbar spine model. J.Biomech. 40:
  1219-1227, 2007.

## References

- Andersson,E., Oddsson,L., Grundstrom,H.,Thorstensson,A., The role of
  the psoas and iliacus muscles for stability and movement of the
  lumbar spine, pelvis and hip, Scand. J. Med. Sci. Sports,5 (1995)
  10-16.
- Bogduk,N., Clinical anatomy of the lumbar spine and sacrum, Churchill
  Livingstone, Edinburgh, 1997.
- Bogduk,N., Macintosh,J.E., Pearcy,M.J., A universal model of the
  lumbar back muscles in the upright position, Spine, 17 (1992)
  897-913.
- Bogduk,N., Pearcy,M.J., Hadfield,G., Anatomy and biomechanics of
  psoas major, Clin. Biomech., 7 (1992) 109-119.
- Daggfeldt,K., Thorstensson,A., The role of intraabdominal pressure in
  spinal unloading, J. Biomech., 30 (1997) 1149-1155.
- Daggfeldt,K., Thorstensson,A., The mechanics of back-extensor torque
  production about the lumbar spine, J. Biomech., 36 (2003) 815-825.
- Heylings,D.J.A., Supraspinous and interspinous ligaments of the human
  lumbar spine, J. Anat., 125 (1978) 127-131.
- Hodges,P.W., Cresswell,A.G., Daggfeldt,K., Thorstensson,A., In vivo
  measurement of the effect of intra-abdominal pressure on the human
  spine, J. Biomech., 34 (2001) 347-353.
- Macintosh,J.E., Bogduk,N., The biomechanics of the lumbar multifidus,
  Clin. Biomech., 1 (1986) 205-213.
- Macintosh,J.E., Bogduk,N., 1987 Volvo award in basic science. The
  morphology of the lumbar erector spinae, Spine, 12 (1987) 658-668.
- Macintosh,J.E., Bogduk,N., The attachments of the lumbar erector
  spinae, Spine, 16 (1991) 783-792.
- Macintosh,J.E., Bogduk,N., Munro,R.R., The morphology of the human
  lumbar multifidus, Clin. Biomech., 1 (1986) 196-204.
- McGill,S.M., Norman,R.W., Effects of an anatomically detailed erector
  spinae model on L4/L5 disc compression and shear, J. Biomech., 20
  (1987) 591-600.
- Pearcy,M.J., Bogduk,N., Instantaneous axes of rotation of the lumbar
  intervertebral joints, Spine, 13 (1988) 1033-1041.
- Penning,L., Psoas muscle and lumbar spine stability: a concept
  uniting existing controversies. Critical review and hypothesis, Eur.
  Spine J., 9 (2000) 577-585.
- Prestar,F.J., Putz,R., Das Ligamentum longitudinale posterius -
  morphologie und Funktion, Morphol. Med., 2 (1982) 181-189.
- Prilutsky,B.I., Zatsiorsky,V.M., Optimizationbased models of muscle
  coordination, Exerc. Sport Sci. Rev., 30 (2002) 32-38.
- Stokes,I.A., Gardner-Morse,M., Lumbar spine maximum efforts and
  muscle recruitment patterns predicted by a model with multijoint
  muscles and joints with stiffness, J. Biomech., 28 (1995) 173-186.
- Stokes,I.A., Gardner-Morse,M., Quantitative anatomy of the lumbar
  musculature, J. Biomech., 32 (1999) 311-316.
- Pintar et al., “Biomechanical properties of human lumbar spine
  ligaments”, J Biomech, Vol. 25(11), 1992, pp.1351-1356.
