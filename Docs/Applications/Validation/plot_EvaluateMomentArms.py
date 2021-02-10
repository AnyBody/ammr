# -*- coding: utf-8 -*-
r"""
Evaluate moment arms
=============================

This model shows how to enable the built-in moment arm evaluation studies.
The studies can be enabled by setting the switch: ``#define EVALUATE_MOMENT_ARMS 1``

The studies will appear in the ``HumanModel.EvaluateMomentArms``
folder. 


.. figure:: /Applications/Validation/EvalMomentArms_plot.png
    :align: center

    The figure shows the moment arms (in meters) for Iliacus and GluteusMaximus inferior) during the hip flexion.
    Agonists muscles (Iliacus) have positive moment arms, and anatagonist (GluetusMaximus) have negative moment arms. 

.. note:: This  will include a lot of studies (one per DOF) so they will 
          affect performance when loading and switching between tabs/operations.



.. rst-class:: without-title
.. seealso:: **Main file location in AMMR:** 

  :anylink-ammr:`Application/Validation/EvaluateMomentArms/EvaluateMomentArms.main.any`


"""

import sys
sys.path.insert(0, '../../exts')
import gallery

gallery.plot("../images/EvaluateMomentArms.jpg")
gallery.show()
