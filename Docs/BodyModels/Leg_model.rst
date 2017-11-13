
.. _old_leg_model:

The “Leg” Model
---------------

The “Leg” model was the first leg model to enter the AnyBody model
repository. It includes the pelvis, thigh, shank and a one segment foot.
The hip joint is modeled as a spherical joint, while the knee and ankle
are modeled as hinges. The “Leg” model is equipped with only **35 muscles
elements**, which makes it a far simpler model than the LegTLEM.

.. raw:: html 

    <video width="45%" style="display:block; margin: 0 auto;" controls autoplay loop>
        <source src="../_static/Leg_rotating_model.mp4" type="video/mp4">
    Your browser does not support the video tag.
    </video>


Thanks to *Mark Thompson*, Lund University Hospital, for his help in
developing the lower extremity model. A couple of muscles with broad
insertions (like the m. gluteus maximus) are divided into multiple
individual muscle units to represent the real geometry and the
mechanical actions of the muscle.

The parameters of these muscles are mainly based on the data published
by Delp and Maganaris

.. rubric:: References:

-  S. Delp, Parameters for the lower limb, http://isbweb.org/data/delp/

-  Maganaris, C. N. In vivo measurement-based estimations of the moment
   arm in the human tibialis anterior muscle-tendon unit. Journal of
   Biomechanics, Vol. 33, pp. 375-379, 2000

-  Dostal, W. F. and J. G. Andrews. A three-dimensional biomechanical
   model of hip musculature. Journal of Biomechanics, Vol. 14, pp.
   803-812, 1981.

-  Herzog, W. and L. J. Read. Lines of action and moment arms of the
   major force-carrying structures crossing the human knee joint.
   Journal of Anatomy. Vol. 182:, pp. 213-230, 1993.

-  Hintermann, B., B. M. Nigg, and C. Sommer. Foot movement and tendon
   excursion: an in vitro study. Foot & Ankle International, Vol. 15,
   pp. 386-395, 1994