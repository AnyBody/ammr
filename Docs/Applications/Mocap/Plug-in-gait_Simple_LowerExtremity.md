---
gallery_title: "Simple Lower extremity model"
gallery_image: "/Applications/images/LowerExtremity-Plug-in-gait.jpg"
---

(sphx_glr_auto_examples_Mocap_plot_Plug-in-gait_Simple_LowerExtremity)=

# Simple Lower extremity model


````{sidebar}
<img src="/Applications/images/LowerExtremity-Plug-in-gait.jpg" width="70%" align="center">
````

Example of lower body MoCap model using the Plug-in-Gait marker protocol,
and walking on three typ4 force platforms. The model is fairly simple and a
good starting point for new users. If you plan to have many trials/subjects,
take a look at the example which better support multiple trails.



:::{seealso}
**Main file location in AMMR:**

{menuselection}`Application --> MocapExamples --> Plug-in-gait_Simple -->
LowerExtremity.main.any`
:::

"""

import sys
sys.path.insert(0, '../../exts')
import gallery

\# dummy call to categorize as certain
\# type for back referencing.
gallery.anymocap()

gallery.plot("../images/LowerExtremity-Plug-in-gait.jpg")
gallery.show()
