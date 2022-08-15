---
gallery_title: "Arm curl"
gallery_image: "/Applications/images/ArmCurl.jpg"
---

(sphx_glr_auto_examples_Sports_plot_ArmCurl.py)=

# Arm curl

````{sidebar} **Example**
<img src="/Applications/images/ArmCurl.jpg" width="70%" align="center">
````

Example of an Arm Curl fitness machine.



:::{seealso}
**Main file location in AMMR:**

{menuselection}`Application --> Examples --> ArmCurl --> ArmCurl.main.any`
:::

The objective of this example is to adjust the eccentricity of the cable wheel
such that the arm muscles experience a constant effort throughout the elbow
flexion taking the change of moment arms of the muscles into account.

It is not possible to obtain a completely constant muscle effort with only the
eccentricity as parameter. However, if more parameters were introduced into an
actual design optimization, then it is likely that an almost completely uniform
effort profile could be obtained.

By chaning between the files "EnvironmentOptimized.any" and "Environment.any" it
is possible to to see the machine with adjusted eccentricity and the one with
zero eccentricity
