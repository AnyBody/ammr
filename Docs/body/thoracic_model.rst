Thoracic spine model
=============================

.. rst-class:: without-title

.. caution:: **Unreleased model:** The model is under development and not yet included in the managed model repository. 
   The model is used in various research projects and access to the model can be given on request. Please 
   `contact us <sales@anybodytech.com>`_ if you are interested in this work. 

The thoracic spine model consists of the thoracic vertebral column and the
ribcage, including individual ribs and sternum. It can be used as a single
segment or as a collection of several segments interconnected by joints
replicating physiological connection and load transfer mechanisms.

.. raw:: html 

    <video width="70%" style="display:block; margin: 0 auto;" controls autoplay loop>
        <source src="../_static/thoracic1.mp4" type="video/mp4">
    Your browser does not support the video tag.
    </video>

The thoracic vertebral column contains 12 vertebrae with 3 DoF spherical joints
in between each 2 vertebrae, connecting to the cervical spine through a
spherical joint at T1C7 levels, and a spherical joint to the lumbar spine at
T12L1 levels. Costovertebral and sternocostal joint are also represented through
kinematic joints. The majority of the muscle fascicles are defined for the
thoracic column and ribcage region. 

.. rst-class:: without-title
.. warning:: **Complex model:** The Thoracic model is a high complexity model and not recommended for
    beginners in musculoskeletal modeling and AnyBody.



.. .. image:: _static/thoracic.png
..    :width: 100%


Example Configuration
-----------------------

The thoracic column and ribcage model comes with several different configurations: 

.. code-block:: AnyScriptDoc
    :emphasize-lines: 3

    #define BM_TRUNK_RIGCAGE_MODE _RIBCAGE_RIGID_
    #define BM_TRUNK_RIGCAGE_MODE _RIBCAGE_SEMI_RIGID_
    #define BM_TRUNK_RIGCAGE_MODE _RIBCAGE_POTENTIAL_ENERGY_


.. .. rst-class:: float-right

.. .. seealso::
   
..    The :doc:`Trunk configuration parameters <../bm_config/trunk>` for a
..    full list of Trunk parmaeters.
   
References
----------------

-  Ignasiak, D., Dendorfer, S., Fergusson, S.J. (2016), "Thoracolumbar spine model with 
   articulated ribcage for the prediction of dynamic spinal loading", 
   Journal of Biomechanics, vol. 49 (6), pp. 959-966.
