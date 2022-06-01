# Symmetric Mandible example

Mandible model example.



:::{seealso}
**Main file location in AMMR:**

{menuselection}`Application --> Validation --> MandibleChewingAndClenching --> MandibleChewingAndClenching.main.any`
:::

Model simulating chewing and comparing values to measurements from de Zee et al., J. of Biomechanics 2007.

You can read more about this model and its validation in the following article:

> de Zee, M., M. Dalstra, P.M. Cattaneo, J. Rasmussen, P. Svensson, and B. Melsen. Validation of a
> musculo-skeletal model of the mandible and its application to mandibular distraction osteogenesis.
> J.Biomech. 40: 1192-1201, 2007.

Be aware that this mandible model was a work in progress:

> - The mandibular fossa is modelled as a planar constraint without curvature.

The kinematic data for the chewing case is based on measurements. However, the chewing force
is simulated and might differ a lot from reality. It is only meant as a demonstration.

The work is supported by the Villum Kann Rasmussen Foundation. And I would like to acknowledge my co-workers:
Paolo M. Catteneo, Michel Dalstra, John Rasmussen, Birte Melsen, Peter Svensson

The work was performed at the Department of Orthodontics, School of Dentistry,Faculty of Health Sciences,
University of Aarhus

Do not hesitate to contact the author for questions and/or suggestions.

> Mark de Zee, Ph.D., Post Doc.
> Aalborg University, Denmark
> E-mail: <mailto:mdz@hst.aau.dk>

"""

import sys
sys.path.insert(0, '../../exts')
import gallery

\# dummy call to categorize as certain
\# type for back referencing.
gallery.mandible()

gallery.plot("../images/MandibleChewingAndClenching.jpg")
gallery.show()
