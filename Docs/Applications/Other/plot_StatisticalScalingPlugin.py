# -*- coding: utf-8 -*-
r"""
Statistical Scaling Plugin
===============================

Plugin for scaling subjects based on an anthropometric database.

This example shows how to use the Statistical Scaling Plugin. The plugin is a
small app which allows you to simply specify a few anatomical or functional
parameters when scaling the model. The plugin calculates the remaining (free)
anthropometric variables based on the ANSUR [#f1]_ anthropometrical database. 


.. rst-class:: without-title
.. seealso:: **Main file location in AMMR:** 

  :anylink-ammr:`Application/Examples/StatisticalScalingPlugin/Main.any`


The big advantage is that the correlation between variables are maintained, so
the model will have realistic anthropometrical dimension as long as the
constraints does not conflict (e.g. a very high stature with very short legs )

.. figure:: /Applications/Other/StatisticalScalingPlugin1.png
    :align: center


The algorithm used by the plugin is based on principal component analysis (PCA)
of the correlations between variables in the anthropometric database. An optimization
problem is then solved minimizing the normalized principal component subject to
the anthropometricall constraintsngiven by the user. Please see: 

   Rasmussen, J., Waagepetersen, R. P. & Rasmussen, K. P. 
   Projection of anthropometric correlation for virtual population modelling.
   International Journal of Human Factors Modelling and Simulation 6, 16–30 (2018)


.. warning:: The plugin can not be used to generate subjects which are very
     different from the population of the ANSUR database. For example children. 


Use the plugin in other models
------------------------------

The plugin can be used in any model as long as it uses the
:ammr:bm_constant:`_SCALING_XYZ_` scaling law. It is also necessary to specify into
which file the plugin should write the calculated anthropometrics. This is done
by setting `#path ANSUR_PLUGIN_ANYMAN_FILE` model file which contains the
anthropometrics
. 

.. code:: AnyScriptDoc

    #define BM_SCALING _SCALING_XYZ_

    #include "<ANYBODY_PATH_AMMR>/Tools/Plugins/ANSUR_Plugin.any"
    #path ANSUR_PLUGIN_ANYMAN_FILE "anthropometrics.any"
    
    // Ensure that the generated anthropometrics are
    #include "anthropometrics.any"

.. rubric:: Footnotes

.. [#f1] Gordon, C. C. et al. 1988 Anthropometric Survey of U.S. Army personnel: methods and summary statistics. (US Army Natick Research, Development and Engineering Center, 1989).




"""


import sys
sys.path.insert(0, '../../exts')
import gallery

gallery.plot("../images/StatisticalScalingPlugin.jpg")
gallery.show()
