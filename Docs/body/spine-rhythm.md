# Spine rhythm

The spine rhythm is a set of drivers which can be used to reduces the degrees of
fredom of the spine and makes the spine model easier to use without the need to
specify how every vertebra should move.

The spine rhythms is also a set of coefficients which speficies how the spine
should move as function of the overall spine motion. The spine rhythm
coefficients are documented on this page which also show how to overwrite the
default coefficients with your own data.


## Spine rhytmn class templates

The model repository comes with two class templates which makes it easy to
create kinematic rhytms between joints. The two class templates are
`RhythmDriverLinear` and `RhythmDriverBiLinear` which can be used to create
linear and rhythms with different coefficients for the positive and negative
direction.

Here is an example of simple linear rhythm between two joints:

```AnyScriptDoc
RhythmDriverLinear Rhythm = {
   RhythmCoefficients = {0.2, 0.8};
   Measures.Input = {
       AnyJoint& ref1 = Main.HumanModel.BodyModel.Interface.Arm.Right.ShoulderElevation;
       AnyJoint& ref2 = Main.HumanModel.BodyModel.Interface.Arm.Right.GHElevation;
   };
 };
```
In the example the rhythm constrains two DOFs of the arm to move in a 1:4 ratio.
The use of `RhythmDriverBiLinear` is quite similar, and the use of both class
templates are [documented here](Rhythms.Linear.SimpleRhythms.any).

The class templates encapsulates the complex rhytnm implementation which uses
classes `AnyKinFunComb` and `AnyKinMeasureFunComb1` to combine and transform
kinematic measures into a single kinematic measure. It is easy to see the
underlying code by right-clicking the class template in the AnyScript editor and
select `Go to definition`.

## Spine rhythm coefficients

The rhythm coefficients were
derived from a review of spine literature. The values for spine and vertebra
range-of-motion vary significantly in published studies, and no single complete
dataset was found. Consequently, the rhythm presented here is a composite,
designed to provide the most consistent and average set of rhythm coefficients.
The papers used to derive the coefficients are listed at the bottom of the page.

:::{figure-md} 
:align: center

<img src="_static/spine-rhythm-axial-rotation.svg" width="50%">
<img src="_static/spine-rhythm-lateral-bending.svg" width="50%">
<img src="/_static/spine-rhythm-flexsion-extension.svg" width="50%">

Coeffients for axial rotation, lateral bending and flexion/extension.
:::

spine-rhythm-axial-rotation.svg


## Overwriting the spine rhythm coefficients




## References

The rhythm coefficients were derived from the following papers:

### Thoracic Region

#### Flexion/extension
- Narimani, M., & Arjmand, N. (2018). https://doi.org/10.1016/j.jbiomech.2018.01.017
- Madinei, S. S., & Arjmand, N. (2018).  https://doi.org/10.24200/sci.2018.20503
- Ignasiak, D., Rüeger, A., & Ferguson, S. J. (2017).  https://doi.org/10.1016/j.humov.2017.05.011
- Alqhtani, R. S., Jones, M. D., Theobald, P. S., & Williams, J. M. (2015). https://doi.org/10.1016/j.jmpt.2014.12.007

#### Lateral-bending:
- Narimani, M., & Arjmand, N. (2018). https://doi.org/10.1016/j.jbiomech.2018.01.017
- Alqhtani, R. S., Jones, M. D., Theobald, P. S., & Williams, J. M. (2015).  https://doi.org/10.1016/j.jmpt.2014.12.007
- Schinkel-Ivy, A., Pardisnia, S., & Drake, J. D. M. (2014). https://doi.org/10.1123/jab.2013-0247

#### Rotation:
- Fujimori, T., Iwasaki, M., Nagamoto, Y., Matsuo, Y., Ishii, T., Sugiura, T., Kashii, M., Murase, T., Sugamoto, K., & Yoshikawa, H. (2014). https://doi.org/10.1016/j.spinee.2013.11.054
- Narimani, M., & Arjmand, N. (2018). https://doi.org/10.1016/j.jbiomech.2018.01.017
- Alqhtani, R. S., Jones, M. D., Theobald, P. S., & Williams, J. M. (2015). https://doi.org/10.1016/j.jmpt.2014.12.007


### Lumbar region:

#### Flexion/extension:
- Eberhardt, K., Ganslandt, O., & Stadlbauer, A. (2014). https://doi.org/10.1007/s00234-014-1433-0
- Dvorák, J., Panjabi, M. M., Chang, D. G., Theiler, R., & Grob, D. (1991). https://journals.lww.com/spinejournal/abstract/1991/05000/functional_radiographic_diagnosis_of_the_lumbar.14.aspx

#### Lateral bending:
- Dvorák, J., Panjabi, M. M., Chang, D. G., Theiler, R., & Grob, D. (1991).  https://journals.lww.com/spinejournal/abstract/1991/05000/functional_radiographic_diagnosis_of_the_lumbar.14.aspx
- Rozumalski, A., Schwartz, M. H., Wervey, R., Swanson, A., Dykes, D. C., & Novacheck, T. (2008). https://doi.org/10.1016/j.gaitpost.2008.05.005

#### Rotation:
- Fujii, R., Sakaura, H., Mukai, Y., Hosono, N., Ishii, T., Iwasaki, M., Yoshikawa, H., & Sugamoto, K. (2007). https://doi.org/10.1007/s00586-007-0373-3
- Rozumalski, https://doi.org/10.1016/j.gaitpost.2008.05.005
- Pearcy, M. J. (1985). https://doi.org/10.3109/17453678509154154


### Neck:
#### Flexion/extension - Lateral bending -rotation
- Anderst, W. J., Donaldson, W. F., 3rd, Lee, J. Y., & Kang, J. D. (2015). https://doi.org/10.1016/j.jbiomech.2015.02.049
- Dvorak, J., Antinnes, J. A., Panjabi, M., Loustalot, D., & Bonomo, M. (1992).  https://doi.org/10.1097/00007632-199210001-00009
- Yu, Y., Li, J.-S., Guo, T., Lang, Z., Kang, J. D., Cheng, L., Li, G., & Cha, T. D. (2019). https://doi.org/10.1016/j.jot.2018.12.002
- Zhou, C., Wang, H., Wang, C., Tsai, T.-Y., Yu, Y., Ostergaard, P., Li, G., & Cha, T. (2020). https://doi.org/10.1016/j.jbiomech.2019.109418

