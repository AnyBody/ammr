
The Shoulder Arm Model
======================

The ShoulderArm model contains data from two different persons. Most of this data
comes from the Dutch Shoulder Group and their 
`shoulder model available online 
<http://homepage.tudelft.nl/g6u61/repository/shoulder/overview.htm>`_

.. todo:: What is the VU and MAYO study shown below? Need to add references?

The model is built using data from subject 2 from the VU study and subject 2
from the MAYO study. The files, which contains the name "forearm", are
built on data from the MAYO study

The shoulder is the site of complex, mutually coupled motions of the scapula,
clavicle and the humerus. To balance realism with model simplicity, the model 
defines motions of the scapula and clavicle as mathematical functions of the 
glenohumeral joint angles, also known as a "Shoulder rhythms".

The AnyBody shoulder model's rhythm can be switched on
and off, the full details of which can be seen in this report
`Shoulder Rhythm
Report <https://www.anybodytech.com/download.html?did=publications.files&fname=ShoulderRhythmReport.pdf>`__.


.. raw:: html 

    <video width="45%" style="display:block; margin: 0 auto;" controls autoplay loop>
        <source src="../_static/ShoulderArm_rotating_model.mp4" type="video/mp4">
    Your browser does not support the video tag.
    </video>
    <!--<img src="../_static/ShoulderCloseupBack.jpg" alt="Smiley face" width="45%">-->

..
    .. centered:: *Figure shoulder model*


Example Configuration
-----------------------

Short example of how to configure the Shoulder Arm model: 

.. code-block:: AnyScriptDoc

    #define BM_ARM_RIGHT ON 
    #define BM_ARM_LEFT ON 
    #define BM_ARM_SHOULDER_RHYTHM ON

    #define BM_ARM_MUSCLE _MUSCLES_3E_HILL_
    


.. rst-class:: float-right

.. seealso::
   
   See :doc:`Arm configuration parameters <../BM_Config/Arm_configurations>` for a
   full list of configuration parmaeters or :doc:`configuration section <../BM_Config/index>`
   for more information on BM parameters.



The model consists of the following joints:

.. rst-class:: centered



..
    .. Image:arm.png


Terminology
---------------
.. rst-class:: centered
.. table:: Joints and kinematic contraints of the arm model
    :widths: 1 2 4
    :align: center
    :column-alignment: center left left
    :column-wrapping: false true true
    :column-dividers: none none none none

    ================= ==================== =======================================================
    Name              Description          Joint/Constraint Type
    ================= ==================== =======================================================
    SC                SternoClavicular     Spherical joint
    AC                AcromioClavicular    Spherical joint
    GH                Glenohumeral joint   Spherical joint (The default joint reactions are  
                                           disabled, since they do not automatically ensure that
                                           the net force vector passes through the glenoid cavity. 
                                           The special force elements providing these biofidelic
                                           reaction forces are contained in the file "GHReactions.any")
    AI                                     One DOF constraint requiring the bony landmark
                                           AI on the scapula, to stay in contact with the thorax 
    AA                                     One DOF constraint requiring the bony landmark
                                           AA on the scapula, to stay in contact with the thorax 
    ConoideumLigament                      The length of this ligament is driven
                                           to always remain constant
    FE                Flexion-extension    Revolute joint
                      of the elbow    
    PS                Pronation-supination 
                      joint or the forearm Combination of joints at the distal and
                                           proximal end of the radius bone that
                                           leaves one DOF free which is 
                                           pronation/supination of the forearm
    Wrist joint                            Two successive revolute joints where 
                                           the axes of rotations are not coincident
    ================= ==================== =======================================================


Resources
------------

More details on the ShoulderArm model can be found online:

-  Webcast: `Validation of the AnyBody version of the Dutch Shoulder Model by the in-vivo measurement of GH contact forces by Bergmann et al.
   <https://www.anybodytech.com/downloads/documentation/#2007426>`__




Anatomy References
----------------------

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

Muscle References
----------------------

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


