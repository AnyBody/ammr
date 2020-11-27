.. _ruhm:

Regensburg Ulm Hand Model (RUHM)
==================================

The Regensburg-Ulm hand model (RUHM) is full detailed hand model for the AMS
including all extrinsic and intrinsic muscles using data
by the University of West Bohemia gained through an anatomical study by Fiala et al. (???) 
of ten cadaver hands.


.. figure:: _static/RUHMHandCloseUp.jpg
    :width: 50%


The hand model consists of 22 hand segments
(including ulna and radius) modelled as rigid bodies
linked by physiological idealized joints giving a total of 31 DOF.
For the sake of reduced complexity the carpal bones where treated as one rigid body.

The Regensburg-Ulm-Hand-Model was developed by Lucas Engelhardt and Maximilian Melzner
from Ulm University and OTH Regensburg respectively. 

.. EMBED a rotatable 3D version of the hand model.
.. .. raw:: html 

..     <video width="45%" style="display:block; margin: 0 auto;" controls autoplay loop>
..         <source src="../_static/TLEM2_rotating_model.mp4" type="video/mp4">
..     Your browser does not support the video tag.
..     </video>

.. The model was Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
.. eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
.. veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
.. consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
.. dolore



.. Example Configuration
.. -----------------------

.. Short example of how to enable the the model:  

.. .. code-block:: AnyScriptDoc

..     #define BM_HAND_MODEL  _HAND_MODEL_RUHM_ 

.. You can directly specify the posture of the 
.. detailed hand model by setting the values  in ``Main.HumanModel.Mannequin``:


.. .. code-block:: AnyScriptDoc

..     HumanModel.Mannequin.Posture.Right = {
..       Finger1 = 
..       {
..          CMCAbduction = 10;
..          CMCFlexion = 40;
..          MCPFlexion = 55;
..          MCPAbduction = 0.0;
..          DIPFlexion = 20;
..       };
..       Finger2 =
..       {
..         MCPFlexion = 10;
..         PIPFlexion = 10;
..         DIPFlexion = 5;
..       }; 
..     };


.. .. rst-class:: float-right

.. .. seealso::
   
..    The :doc:`Leg configuration parameters <../bm_config/leg>` for a
..    full list of configuration parameters.


References
-----------------------

If you need to cite the model use the following references: 

.. [ENME20] Engelhardt,L. and Melzner,M. “Cool title for the RUHM paper”
   Nature (2020) ( `link <https://nature.com>`__ ) 

