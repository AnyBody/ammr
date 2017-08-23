
The Shoulder Arm Model
----------------------

This model contains data from two different persons. Most of the data
that has been used in this model comes from the Dutch Shoulder Group and
can be found on the following webpage
http://homepage.tudelft.nl/g6u61/repository/shoulder/overview.htm . The
model is built using data from subject 2 from the VU study and subject 2
from the MAYO study. The files, which contains the name "forearm", are
built on data from the MAYO study

A shoulder rhythm is available in the repository it can be switched on
and off, for full details on its implementation please see this report
`Shoulder Rhythm
Report <https://www.anybodytech.com/download.html?did=publications.files&fname=ShoulderRhythmReport.pdf>`__.

*The model consists of the following joints:*

-  SC SternoClavicular: spherical joint

-  AC AcromioClavicular: spherical joint

-  GH Glenohumeral joint: spherical (normal reactions of the spherical
   joint is not used instead they are created so that they fall within
   the glenoid cavity the file, please see the file GHReactions.any for
   details)

-  AI One dimensional constraint between the scapula and the thorax at
   the bonylandmark AI om scapula

-  AA One dimensional constraint between the scapula and the thorax at
   the bonylandmark AA om scapula

-  ConoideumLigament : the length of this segment is driven to a
   constant length

-  FE Flexion-extension of the elbow: revolute joint

-  PS pronation-supination joint or the forearm: combination of joints
   in distal and proximal end of the radius bone that leaves one dof
   free which is pronation/supination of the forearm

-  Wrist joint: created as two revolute joints where the axis of
   rotations are not coincident

|Image:arm.png|

*Anatomy references:*

-  F.C.T. van der Helm and R. Veenbaas, Modeling the mechanical efect of
   muscles with large attachment sites: aplication to the shoulder
   mechanism. Journal of Biomechanics, vol. 24, no. 12, pp. 1151-1163,
   1991

-  H.E.J. Veeger, F.C.T. van der Helm, L.H.V. van der Woude, G.M. Pronk
   and R.H. Rozendal, Inertia and muscle contraction parameters for
   musculoskeletal modelling of the shoulder mechanism. Journal of
   Biomechanics, vol. 24, no. 7, pp. 615-629, 1991

-  F.C.T. van der Helm, A finite element musculoskeletal model of the
   shoulder mechanism. Journal of Biomechanics, vol. 27, no. 5, pp.
   551-569, 1994

-  R. Happee and F.C.T. Van der Helm, The control of shoulder muscles
   during goal directed movements, an inverse dynamic analysisJ.
   Biomechanics, vol. 28, no. 10, pp. 1179-1191, 1995

-  Van der Helm FC, Veeger HE, Pronk GM, Van der Woude LH, Rozendal RH.
   Geometry parameters for musculoskeletal modeling of the shoulder
   system Journal of biomechanics Vol. 25 no. 2, pp. 129-144, 1992 Note:
   this reference is used for the geometry used for the definition of
   many of the geometries which are used for muscle wrapping

-  DirkJan (H.E.J.) Veeger, Bing Yu, Kai Nan An, Orientation of axes in
   the elbow and forearm for biomechanical modeling Proceedings of the
   first conference of the ISG,1997

-  The segment coordinatesystem are according to the ISB proposal,
   please see
   http://internationalshouldergroup.org/files/standards97.pdf

-  H.E.J. Veeger, Bing Yu, Kai-Nan An and R.H. Rozendal, Parameters for
   modeling the upper extremity, Journal of Biomechanics, Vol. 30, No.
   6, pp. 647-652, 1997

-  H.E.J. Veeger, F.C.T. van der Helm, L.H.V. van der Woude, G.M. Pronk
   and R.H. Rozendal,Inertia and muscle contraction parameters for
   musculoskeletal modelling of the shoulder mechanism. Journal of
   Biomechanics, vol. 24, no. 7, pp. 615-629, 1991

*Muscle references:*

-  Jacobson, M. D., R. Raab, B. M. Fazeli, R. A. Abrams, M. J. Botte,
   and R. L. Lieber. Architectural design of the human intrinsic hand
   muscles. J. Hand Surg. [Am.] 17:804809, 1992.

-  Lieber, R. L., M. D. Jacobson, B. M. Fazeli, R. A. Abrams, and M. J.
   Botte. Architecture of selected muscles of the arm and forearm:
   Anatomy and implications for tendon transfer. J. Hand Surg. [Am.]
   17:787-798, 1992.

-  Lieber, R. L., B. M. Fazeli, and M. J. Botte. Architecture of
   selected wrist flexor and extensor muscles. J. Hand Surg. [Am.]
   15:244-250, 1990.

-  Muray, W.M.,T.S. Buchanan, and S.L. Delp. Scaling of peak moment arms
   with the elbow and forearm position J. Biomech. Vol. 28, pp. 513-525,
   1995