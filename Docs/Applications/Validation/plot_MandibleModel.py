# -*- coding: utf-8 -*-
r"""
Mandible Models
===============================
      
Model simulating chewing and comparing 
values to measurements from de Zee et al., J. of Biomechanics 2007.

| **Main file:** 
| :file:`Application/Validation/MandibleChewingAndClenching/MandibleChewingAndClenching.main.any`

    You can read more about this model and its validation in the following article:
    de Zee, M., M. Dalstra, P.M. Cattaneo, J. Rasmussen, P. Svensson, and B. Melsen. Validation of a
    musculo-skeletal model of the mandible and its application to mandibular distraction osteogenesis.
    J.Biomech. 40: 1192-1201, 2007.

    Be aware that the model is work in progress:
    
    - The mandibular fossa is modelled as a planar constraint without curvature.

    The kinematic data for the chewing case is based on measurements. However, the chewing force
    is simulated and might differ a lot from reality. It is only meant as a demonstration.

    The work is supported by the Villum Kann Rasmussen Foundation. And I would like to acknowledge my co-workers:
    Paolo M. Catteneo, Michel Dalstra, John Rasmussen, Birte Melsen, Peter Svensson

    The work was performed at the Department of Orthodontics, School of Dentistry,Faculty of Health Sciences,
    University of Aarhus

    Do not hesitate to contact me for questions and/or suggestions.

    Regards,
    Mark de Zee, Ph.D., Post Doc.
    Aalborg University, Denmark
    E-mail: mdz@hst.aau.dk 



"""

import matplotlib.pyplot as plt
import matplotlib.image as mimg

image = mimg.imread("../images/MandibleChewingAndClenching.jpg")
plt.axis('off')
plt.imshow(image)
plt.show()