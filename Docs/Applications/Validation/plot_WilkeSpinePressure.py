# -*- coding: utf-8 -*-
r"""
Wilke Spine Disc Pressure Model
===============================
      
Several models comparing loads in the spine with in vivo measurements
during daily activities from Wilke et al., Spine 1999.

.. figure:: /Applications/Validation/wilke.svg


"""

import sys
sys.path.insert(0, '../../exts')
import gallery

gallery.plot("../images/SpinePressureLyingOnBack.jpg")
gallery.plot("../images/SpinePressureSeatingFlexedNoSupport.jpg")
gallery.plot("../images/SpinePressureSeatingRelaxed.jpg")
gallery.plot("../images/SpinePressureStandingLiftStretchedArms.jpg")
gallery.plot("../images/SpinePressureStandingLiftClose.jpg")
gallery.plot("../images/SpinePressureSeatingStraitNoSupport.jpg")
gallery.plot("../images/SpinePressureStandingLiftFlexed.jpg")
gallery.show()

