# -*- coding: utf-8 -*-
r"""
Rehazenter adult walking model
===============================

Fullbody MoCap model with multple subjects and trials based on the 
large dataset by `Schreiber and Moissenet (2019) <https://doi.org/10.1038/s41597-019-0124-4>`__.

The model has 50 subjects and 1145 trials. Subjects walk at five different
speeds (conditions) C1: 0–0.4 m/s, C2: 0.4–0.8 m/s, C3: 0.8–1.2 m/s, C4: a 
self-selected spontaneous speed, C5, self-selected fast speed.

The dataset uses 53 reflective markers and measured ground reaction forces. A 
standing reference trial is used to indentify a number parameters: 

* Segment lengths
* Tibial torsion angle
* Varus-valgus angle
* Unconstrained marker positions

These parameters are then loaded in the matching dynamic trials. 

.. warning:: The model is meant as a starting point for analysing the "Rehazenter adult walking dataset". 
    The model has not been through any kind of validation, and is not likely to produce correct results 
    without futher adjustments.
    
Choises of model parameters are in some cases arbitrary as this model is a work in progress. If you come up 
with improvements to the model please share them back. 


Dataset
----------

The full "Rehazenter adult walking dataset" is not distributed with the model. Schreiber and Moissenet (2009) has
released the data under a Creative Commons license for every one to use. 

You must download it sepearately from:

* `Rehazenter adult walking dataset  <https://figshare.com/articles/A_multimodal_dataset_of_human_gait_at_different_walking_speeds/7734767>`__

After downloading extract the data into the ´C3DFiles` sub folder. 


Model structure
---------------

The files are structured so each trial has its own folder with a main file
(``Main.any``) and a file with trial specific data (``TrialSpecificData.any``).
The C3D files are placed together in a separate folder.

The model is structured as outlined below:

.. code-block:: none

   Application/MocapExamples/Rehazenter-adult-walking-model
    │   libdef.any
    │   C3DSettings.any
    │   BodyModelConfig.any
    │   ExtraDrivers.any
    │   ForcePlates.any
    │   MarkerProtocol.any
    │   LabSpecificData.any
    │
    ├───C3DFiles\
    |   │  
    |   ├───2014001\
    |   |      2014001_C1_01.c3d
    |   |      2014001_C1_02.c3d
    |   |      ..
    |   |      2014001_ST.c3d
    │   |
    |   └───2014002\
    │          ..
    │
    ├───Output\
    │
    └───Subjects\
        │
        ├───2014001\
        │   |   SubjectSpecificData.any
        |   |
        │   ├───2014001_C1_01\
        |   |      Main.any
        |   |      TrialSpecificData.any
        |   :   
        |   |   
        │   └───2014001_ST\
        |          Main.any
        |          TrialSpecificData.any
        │   
        └───2014002\
            |   SubjectSpecificData.any
            |
            ├───2014002_C1_01\
            |      Main.any
            |      TrialSpecificData.any
            : 


Batch processing
----------------
The model also contains a batch processing Python script for running all models autmatically. The script 
``batchprocess.py`` is located in the top-level folder. 

To use the scirpt install the `Anaconda Python Distribution <https://www.anaconda.com/distribution/#download-section>`__. 

The script uses the `AnyPyTools <https://github.com/AnyBody-Research-Group/AnyPyTools>`__ library for working with the
AnyBody Model System (`Lund 2019 <https://doi.org/10.21105/joss.01108>`__). The library can be installed with:

.. code-block:: bash

    conda install -c conda-forge anypytools

Then run the following command in the model folder:

.. code-block:: bash

    python batchprocess.py

.. note:: You may need to modify the script to output the variables you are interested in. It may also 
    be necessary to modify the number parrallel AnyBody instances to match the number of licenses you have. 
    

Bibliography
---------------

Please cite the following paper when using the data. 

> Schreiber, C., Moissenet, F. A multimodal dataset of human gait at different walking speeds established on injury-free adult participants. Sci Data 6, 111 (2019). https://doi.org/10.1038/s41597-019-0124-4


"""


import sys
sys.path.insert(0, '../../exts')
import gallery

# dummy call to categorize as certain 
# type for back referencing.
gallery.anymocap()


gallery.plot("../images/rahazenter-adult-walking-model.jpg")
gallery.show()
