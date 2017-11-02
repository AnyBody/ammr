Tweente Lower Extremity Model
==============================

The AnyBody implementation of a the Tweente lower extremity model (TLEM) consists 
of 159 muscles, and 6 joint degrees. 


.. raw:: html 

    <video width="45%" style="display:block; margin: 0 auto;" controls autoplay loop>
        <source src="../_static/TLEM1_rotating_model.mp4" type="video/mp4">
    Your browser does not support the video tag.
    </video>
    <!--<img src="../_static/TLEM1_closeup.jpg" alt="TLEM model" width="45%">-->

..
    .. centered:: *Tweente Lower Extremity Model (version 1.2)*

The model has been validated against ‘state of the
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



Example Configuration
-----------------------

Short example of how to configure the model with the TLEM model, Hill type
muscle model and only one leg: 

.. code-block:: AnyScriptDoc

    #define BM_LEG_MODEL _LEG_MODEL_TLEM1_
    #define BM_LEG_RIGHT ON
    #define BM_LEG_LEFT OFF
    #define BM_LEG_MUSCLE _MUSCLES_3E_HILL_
    


.. rst-class:: float-right

.. seealso::
   
   See :doc:`Leg configuration parameters <../BM_Config/Leg_configurations>` for a
   full list of configuration parmaeters or :doc:`configuration section <../BM_Config/HumanBody_configurations>`
   for more information on BM parameters.




Resources
------------

More details can be found online:

.. [ESA_cycling_report] Report containing moment arm validation for `ESA:
   report <http://www.anybodytech.com/fileadmin/downloads/Final_Report.pdf>`__

.. [klein-horsman2007] Klein Horsman, M. D., Koopman, H. F. J. M., van der Helm, F. C. T., 
   Prosé, L. P., and Veeger, H. E. J., 2007, “Morphological Muscle and Joint Parameters for
   Musculoskeletal Modelling of the Lower Extremity,” Clin. Biomech. , 22(2), pp. 239–247.
   `link <http://linkinghub.elsevier.com/retrieve/pii/S0268003306001896>`__