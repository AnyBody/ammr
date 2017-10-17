
Tweente Lower Extremity Model version 2
=======================================

The cervical spine model contains 7 vertebrae with 3 DoF spherical
joints from T1 to C2, a 1 DoF joint between C2 and skull and 136 muscle
fascicles. The center of rotations is based on Amevo et al. 1991.


More details can be found online at:

-  Data based on a neck model described by `Marike van der
   Horst <http://alexandria.tue.nl/extra2/200211336.pdf>`__

-  Webcast `A detailed rigid-body cervical spine model based on inverse
   dynamics (Dr. Mark de Zee, 18. September,
   2007) <https://www.anybodytech.com/anybody.html?fwd=webcasts#2007918>`__
   This webcast presents a detailed model of the cervical spine, which
   was presented at the ISB Congress in Taipei. We will go through the
   model and its assumptions including the muscles and preliminary
   validation. Moreover, an application will be presented where we try
   to predict neuromuscular adaptation of experimentally induced neck
   pain using the cervical spine model. (The webcast is available for
   playback.)

References:

-  de Zee, M., Falla, D., Farina, D. & Rasmussen, J. (2007), "A detailed
   rigid-body cervical spine model based on inverse dynamics", Journal
   of Biomechanics, vol. 40 (2), pp. S284.

The “LegTLEM” Model
-------------------

Implementation of a new lower extremity model labeled the Twente Lower
Extremity Model (TLEM) consisting of 159 muscles, and 6 joint degrees of
freedom is almost completed. It has been validated against ‘state of the
art’ literature with respect to its biomechanical performance and first
applications in gait and cycling deliver very convincing results.

The model is based on published morphological consistent anatomical
dataset on muscle and joint parameters by Martijn Klein-Horsman from the
University of Twente, The Netherlands. The implementation of the model
was started by Karin Gorter, a Master Student, also from the University
of Twente, during a three-month stay at Aalborg University and has been
finished by the AnyBody Technology.

The current version has been updated several times and is still being
maintained in collaboration with The AnyBody Research Group at Aalborg
University (DK) (www.anybody.aau.dk) and University of Twente (NL) under
the TLEMsafe project (`www.tlemsafe.eu <http://www.tlemsafe.eu>`__).
Currently, new cadaver datasets are recorded within the TLEMsafe
project.


More details can be found online:

-  Report containing moment arm validation for `ESA:
   report <http://www.anybodytech.com/fileadmin/downloads/Final_Report.pdf>`__

-  Link to publication of the dataset: `Klein-Horsman et al.
   Morphological muscle and joint parameters for musculoskeletal
   modelling of the lower extremity. Clin Biomech, 2007, 22,
   239-247 <http://linkinghub.elsevier.com/retrieve/pii/S0268003306001896>`__