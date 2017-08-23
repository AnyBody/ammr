The Lumbar Spine Model
----------------------

The Lumbar spine contains 5 vertebrae with 3 DoF spherical joints in
between, 188 muscle fascicles and intra-abdominal pressure.

|Image:spine.png|

The functional spinal units (FSU) are driven using a prescribed
kinematic rhythm, and by default, facet joints are not employed due to
the fact that most of the application do not focus on the lumbar spine
section. However, several examples demonstrate possible mechanisms of
facet joint incorporation and detailed modeling of the lumbar spine. The
spinal muscles do not include the force-length-velocity relations (i.e.
we use the so-called simple muscle model). The only input parameter in
the muscle model is the cross-sectional area multiplied by a factor.
Daggfeldt and Thorstensson (J.Biomech. 2003, 36: 815-825) didn't include
the force-length-velocity relations either. The inclusion of the lumbar
spine ligaments is optional and can be done as cumulative stiffness of
FSU or as separate elastic elements. Similarly, the intervertebral disc
(IVD) stiffness can be used as a single cumulative value for a FSU or as
linear and nonlinear functions for the disc only. This, however, is
mostly utilized for the spine specific applications, where the level of
detail is important. In other cases, it has been shown that the torque
production from ligaments might not be very important (Cholewicki and
McGill, J.Biomech. 1992, 25: 17-28). The data of vertebrae dimensions
and whole body parameters is taken from: Nissan and Gilad (J.Biomech.
19: 753-758, 1986) and mechanical properties of ligaments were taken
from: Pintar et al. (J.Biomech. 25(11): 1351-1356, 1992).

The spine model contains a preliminary model of the Intra Abdominal
pressure (IAP). In short the IAP is modeled as constant volume, which,
when squeezed from the side by the transversus muscles extends the spine
by pushing on the rib thorax and the pelvic floor. From the mathematical
point-of-view, this lets the abdominal muscles function as spine
extensors, and they become part of the whole recruitment problem. The
limit of the IAP was set to 26600 Pa, which was based on measurements on
well-trained subjects (Essendrop, M., 2003. Significance of
intra-abdominal pressure in work related trunk-loading. Ph.D. Thesis,
National Institute of Occupational Health, Denmark.) and using
geometric/anatomic estimates of pressure surface area and area
centroids, which in turn determines the effective moment arm of the
pressure.

More details on the lumbar spine model can be found online:

-  Presentation about the `Abdominal pressure
   Presentation <https://www.anybodytech.com/download.html?did=publications.files&fname=AbdominalPressureModel.pdf>`__

-  **Webcast `A lumbar spine model with facets joints and a dynamic
   stabilization
   device  <https://www.anybodytech.com/anybody.html?fwd=webcasts#20101221>`__**\ (Sebastian
   Dendorfer, 21. December, 2010). This presentation will bring an
   insight to added features and methods available in Anybody Modelling
   System using a lumbar spine example. First, we will shown a
   computational prediction of spine curvature and show the effect of
   the muscles on human posture. Secondly, this approach will be
   employed to highlight the effect of different designs of spinal
   fixation devices. Moreover, an overview of how to apply this
   modelling strategy in conjunction with two different formulations of
   the facet joints will be given.

-  Webcast `Implementation of facet joints in a lumbar spine model (Mark
   de Zee, 25. September,
   2008). <https://www.anybodytech.com/downloads/documentation/#2008925>`__
   This work presents a new methodology for implementation of facet
   joints in the lumbar spine model developed by De Zee et al. (2007: J
   Biomech. 40, 1219-1227). It enables the facet joint forces to become
   part of a redundant system of equilibrium equations for the entire
   system including the muscles. This redundant system is subsequently
   solved uniquely thereby making it possible to analyze the effect of
   whole body movements and loads on facet joint loading for the whole
   lumbar spine together with its muscles.

-  Webcast `A detailed rigid-body cervical spine model based on inverse
   dynamics (Dr. Mark de Zee, 18. September,
   2007) <https://www.anybodytech.com/anybody.html?fwd=webcasts#2007918>`__
   This webcast presents a detailed model of the cervical spine, which
   was presented at the ISB congress in Taipei. We will go through the
   model and its assumptions including the muscles and a preliminary
   validation. Moreover an application will be presented where we try to
   predict neuromuscular adaptation of experimentally induced neck pain
   using the cervical spine model. (The webcast is available for
   playback.)

-  Webcast `A generic detailed rigid-body lumbar spine model (Dr. Mark
   de Zee, 4. December,
   2006) <https://www.anybodytech.com/anybody.html?fwd=webcasts#2006124>`__
   This webcast presents a detailed model of the lumbar spine, which has
   been published in the Journal of Biomechanics. We will go through the
   model and its assumptions including the muscles, intra-abdominal
   pressure and validation. With the presented model it will be possible
   to investigate a range of research questions, because the model is
   relatively easy to share and modify, available in the public domain
   repository. (The webcast is available for playback.)

-  PowerPoint presentation `Spine Rhythm Presentation (PDF with videos
   click to activate
   them) <https://www.anybodytech.com/download.html?did=publications.files&fname=Spinerhythm.pdf>`__

You can read more about this lumbar spine model and some preliminary
validation in the following article:

-  de Zee, M., L. Hansen, C. Wong, J. Rasmussen, and E.B. Simonsen. A
   generic detailed rigid-body lumbar spine model. J.Biomech. 40:
   1219-1227, 2007.

*References:*

-  Andersson,E., Oddsson,L., Grundstrom,H.,Thorstensson,A., The role of
   the psoas and iliacus muscles for stability and movement of the
   lumbar spine, pelvis and hip, Scand. J. Med. Sci. Sports,5 (1995)
   10-16.

-  Bogduk,N., Clinical anatomy of the lumbar spine and sacrum, Churchill
   Livingstone, Edinburgh, 1997.

-  Bogduk,N., Macintosh,J.E., Pearcy,M.J., A universal model of the
   lumbar back muscles in the upright position, Spine, 17 (1992)
   897-913.

-  Bogduk,N., Pearcy,M.J., Hadfield,G., Anatomy and biomechanics of
   psoas major, Clin. Biomech., 7 (1992) 109-119.

-  Daggfeldt,K., Thorstensson,A., The role of intraabdominal pressure in
   spinal unloading, J. Biomech., 30 (1997) 1149-1155.

-  Daggfeldt,K., Thorstensson,A., The mechanics of back-extensor torque
   production about the lumbar spine, J. Biomech., 36 (2003) 815-825.

-  Heylings,D.J.A., Supraspinous and interspinous ligaments of the human
   lumbar spine, J. Anat., 125 (1978) 127-131.

-  Hodges,P.W., Cresswell,A.G., Daggfeldt,K., Thorstensson,A., In vivo
   measurement of the effect of intra-abdominal pressure on the human
   spine, J. Biomech., 34 (2001) 347-353.

-  Macintosh,J.E., Bogduk,N., The biomechanics of the lumbar multifidus,
   Clin. Biomech., 1 (1986) 205-213.

-  Macintosh,J.E., Bogduk,N., 1987 Volvo award in basic science. The
   morphology of the lumbar erector spinae, Spine, 12 (1987) 658-668.

-  Macintosh,J.E., Bogduk,N., The attachments of the lumbar erector
   spinae, Spine, 16 (1991) 783-792.

-  Macintosh,J.E., Bogduk,N., Munro,R.R., The morphology of the human
   lumbar multifidus, Clin. Biomech., 1 (1986) 196-204.

-  McGill,S.M., Norman,R.W., Effects of an anatomically detailed erector
   spinae model on L4/L5 disc compression and shear, J. Biomech., 20
   (1987) 591-600.

-  Pearcy,M.J., Bogduk,N., Instantaneous axes of rotation of the lumbar
   intervertebral joints, Spine, 13 (1988) 1033-1041.

-  Penning,L., Psoas muscle and lumbar spine stability: a concept
   uniting existing controversies. Critical review and hypothesis, Eur.
   Spine J., 9 (2000) 577-585.

-  Prestar,F.J., Putz,R., Das Ligamentum longitudinale posterius -
   morphologie und Funktion, Morphol. Med., 2 (1982) 181-189.

-  Prilutsky,B.I., Zatsiorsky,V.M., Optimizationbased models of muscle
   coordination, Exerc. Sport Sci. Rev., 30 (2002) 32-38.

-  Stokes,I.A., Gardner-Morse,M., Lumbar spine maximum efforts and
   muscle recruitment patterns predicted by a model with multijoint
   muscles and joints with stiffness, J. Biomech., 28 (1995) 173-186.

-  Stokes,I.A., Gardner-Morse,M., Quantitative anatomy of the lumbar
   musculature, J. Biomech., 32 (1999) 311-316.

-  Pintar et al., “Biomechanical properties of human lumbar spine
   ligaments”, J Biomech, Vol. 25(11), 1992, pp.1351-1356.