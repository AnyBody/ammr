# -*- coding: utf-8 -*-
r"""
Simple GRF prediction model
###########################

Example of full body MoCap model using the Plug-in-Gait marker protocol but
without force plates. The external forces are instead predicted using the GRF
algorithms.


.. rst-class:: without-title
.. seealso:: **Main file location in AMMR:** 

  :menuselection:`Application --> MocapExamples --> Plug-in-gait_Simple -->
  FullBody_GRFPrediction.main.any`

Motion capture data is often recorded without force plates. In traditional
inverse dynamics, this would make it impossible to perform a dynamic analysis.
However, AnyBody has the possibility to predict ground reaction forces (GRF), so
you can make inverse dynamics models based on recorded motion without GRF force
measurement (Fluit et al., 2014; Jung et al., 2014). 

More information is available in the :doc:`documentation for the GRF prediction </anymocap/grf-prediction>`.

"""


import sys
sys.path.insert(0, '../../exts')
import gallery

# dummy call to categorize as certain 
# type for back referencing.
gallery.anymocap()


gallery.plot("../images/GRFPrediction-Plug-in-gait.jpg")
gallery.show()