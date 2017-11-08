
#########
Changelog
#########


AMMR 2.0.0 (2017-10-30)
=============================

Major changes:
---------------------------

* New lower extremity model (TLEM2.1)

   * The `Tweente Lower Extremity Model version 2.0 dataset
     <http://dx.doi.org/10.1016/j.jbiomech.2014.12.034>`_, developed in the
     TLEMSafe EU project was implmented in the AMMR repostory. The model is not
     the default model, but can be enabled with the :ref:`BM parameter
     <bm-config>` ``#define BM_LEG_MODEL _LEG_MODEL_TLEM2_``
   * The model is versioned TLEM 2.1, to indicate the number of changes and
     correction which has been added in process. The changes and updates to the
     TLEM2 dataset was done in the `Life Long Joints
     <https://lifelongjoints.eu/>`_ EU research project (paper submitted for publication). 
   * The most important changes to the TLEM 2 dataset include the following: 
     
        * Updated wrapping for the Gluteus Maximus, Iliacus, Psoas around the hip.
        * Reworked muscle topology for Gluteus Medius and Gluetus Minimus
        * Updated wrapping for Hamstring muscles, and Gastrocnemius around the knee. 
        * Redfinened revolute knee axis (thanks to Marco Antonio Marra (Radboudumc)
          for this improvement)

    * See the :doc:`TLEM2.1 documenation </Appl>` page for more information.


* Updates to the TLEM 1 model

    * The exisitng implementaion of the Twente Lower Extremity model has also been updated. 
      The version of is now called 1.2. Changes include the following: 

        *   See the TLEM2.1 documenation page for more information.
  

* New topology for the Trunk Pelvis


* 






Minor Changes: 
------------------------




Fixed:
------------------------




Removed:
-----------------------






New Tweente Lower Eximity Model V. 2.1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* 



Tweente Lower Eximity Model V. 1.1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^






Fixed:
--------------------------------





Removed:
-------------------------


Deprecated:
------------------------


