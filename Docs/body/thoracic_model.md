(Ribcage and Thoracic Spine Model)=

# Ribcage and Thoracic Spine Model

The present generic ribcage and thoracic model has been published in [Shayestehpour, H., Tørholm, S., Damsgaard, M., Lund, M., Wong, C., Rasmussen, J.: A generic detailed multibody thoracic spine and ribcage model](https://dx.doi.org/10.1007/s11044-024-10034-0). This model extends the state-of-the-art by introducing a kinematically determinate rigid-body model controlled by full spine DOFs, enabling the simulation of activities such as curved spine motions (e.g., scoliosis) with detailed ribcage kinematics. Designed for improved usability in clinical and motion capture applications, the model has a wide Range of Motion (ROM) and accommodates severe deformities without locking, thanks to nonlinear constraints and redundancy handling. The model supports direct and inverse kinematics, offering flexibility in input options.

The new model builds on a previously developed thoracic spine model [1](https://doi.org/10.1007/s11044-021-09787-9). This thoracic spine model consists of the thoracic vertebral column (12 vertebrae) and the ribcage, including individual ribs (24 ribs) and a two-part sternum. The multiple segments interconnected by joints replicate the physiological connections and load transfer mechanisms.

Here is a full view of the flexible thoracic model together with the new {doc}`abdominal pressure model <abdominal_model>`.
<video width="100%" style="display:block; margin: 0 auto;" controls autoplay loop>
    <source src="../_static/ThoracicSpine_rotating_model.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>

## Kinematics
The kinematic constraints of the thorax are summarized as follows:

- **Vertebra constraints:** The intervertebral joints of the spine, adopted from previous work, are modeled as spherical joints. These joint angles can be adjusted to set the model’s posture.
- **Rib constraints:** The costovertebral (CV) connections between the vertebrae and ribs are also defined as spherical joints. For each rib, three rotational Averaging measure (AvgM) constraints were established. Detailed information is provided in the [paper](https://dx.doi.org/10.1007/s11044-024-10034-0).
- **Sternum constraints:** A revolute joint was defined between the manubrium and the sternal body, allowing rotation around the mediolateral axis. This DOF enables ribcage movements independent of spinal posture. Additionally, three linear and three rotational AvgM constraints were defined for the entire sternum, with further details provided in the [paper](https://dx.doi.org/10.1007/s11044-024-10034-0).

```{image} _static/Ribcage_Constraints.jpg 
    :width: 60%
    :align: center  
```

## Spine rhythms 
To drive the thoracic model, only the thoracic spine needs to be controlled, while the ribcage follows the spine as it is kinematically determinate due to the constraints. However, the thoracic spine consists of 12 vertebrae, each requiring three rotational drivers. To simplify usage, we introduced rhythms, which are constraints that link the rotational DOFs of the intervertebral joints. As a result, all vertebrae are linked with rhythm drivers, requiring input for only three spine rotational DOFs (flexion/extension, lateral bending, and axial rotation). Below is a video demonstrating how the rhythms work.

```{raw} html
<video width="100%" style="display:block; margin: 0 auto;" controls autoplay loop>
    <source src="../_static/rhythms.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>
```

:::{admonition} See the [Spine rhythm](spine-rhythm)
:class: seealso
for more information on how the spine rhythm is implemented, the coefficient and how to overwrite it with your own data.
:::

## Example of the model
Here are some examples of the new thoracic model.

<div style="display: flex; justify-content: center; gap: 10px;">
    <video width="45%" controls autoplay loop>
        <source src="../_static/Thoracic_AR.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    <video width="45%" controls autoplay loop>
        <source src="../_static/Thoracic_LB.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</div>

<div style="display: flex; justify-content: center; gap: 10px;">
    <video width="45%" controls autoplay loop>
        <source src="../_static/Thoracic_FE.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    <video width="45%" controls autoplay loop>
        <source src="../_static/Thoracic_Scoliosis_PA.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</div>



## Muscles configurations
The muscle configuration of the model has been greatly expanded in both the spine and abdominal regions, with a total of 1,222 muscle fascicles for the thoracic spine.


<div style="display: flex; justify-content: center; gap: 10px;">
    <img src="../_static/Thoracic_muscle_front.png" width="20%" alt="Thoracic Muscle Front">
    <img src="../_static/Thoracic_muscle_back.png" width="20%" alt="Thoracic Muscle Back">
    <img src="../_static/Thoracic_muscle_iso.png" width="20%" alt="Thoracic Muscle Iso">
</div>


## Example Configuration

The detailed thoracic model can be controlled using the `BM_*` statements like the rest of the body models. 


```{code-block} AnyScriptDoc
:emphasize-lines: 2

#define BM_TRUNK_THORACIC_MODEL _THORACIC_MODEL_RIGID_
#define BM_TRUNK_THORACIC_MODEL _THORACIC_MODEL_FLEXIBLE_
#define BM_TRUNK_THORACIC_MODEL _THORACIC_MODEL_USERDEFINED_

model

```


```{rst-class} without-title
```





% .. rst-class:: float-right

% .. seealso::

% The :doc:`Trunk configuration parameters <../bm_config/trunk>` for a

% full list of Trunk parmaeters.

## Resources
- Webcast on the [New AnyBody Thoracic Spine, Ribcage, and Abdominal Model](https://youtu.be/R4kM-ZKc8Gs?t=2)
- Webcast on the [Spine Rhythms](https://youtu.be/-kWxr_UDvjo?t=1451)
- Paper: [Shayestehpour, H., Tørholm, S., Damsgaard, M., Lund, M.E., Wong, C., Rasmussen, J.: A generic detailed multibody model for simulating thoracic spine and ribcage kinematics. Multibody Syst. Dyn. (2024)](https://doi.org/10.1007/s11044-024-10034-0)

## References
- 1. Previous version of ribcage and thoracic model: [Shayestehpour, H., Rasmussen, J., Galibarov, P., Wong, C.: An articulated spine and ribcage kinematic model for simulation of scoliosis deformities. Multibody Syst. Dyn. 53, 115–134 (2021).](https://doi.org/10.1007/s11044-021-09787-9)
- 2. Lee, D.: Biomechanics of the thorax: a clinical model of in vivo function. J. Man. Manip. Ther. 1, 13–21 (1993). https://doi.org/10.1179/106698193791069771
- 3. Watkins, R. IV, Watkins, R., Williams, L., Ahlbrand, S., Garcia, R., Karamanian, A., Sharp, L., Vo, C., Hedman, T.: Stability provided by the sternum and rib cage in the thoracic spine. Spine 30, 1283–1286 (2005). https://doi.org/10.1097/01.brs.0000164257.69354.bb
- 4. Stokes, I.A.F., Gardner-Morse, M.: Lumbar spine maximum efforts and muscle recruitment patterns predicted by a model with multijoint muscles and joints with stiffness. J. Biomech. 28, 173–186 (1995). https://doi.org/10.1016/0021-9290(94)E0040-A
- 5. Keller, T.S., Colloca, C.J., Harrison, D.E., Harrison, D.D., Janik, T.J.: Influence of spine morphology on intervertebral disc loads and stresses in asymptomatic adults: implications for the ideal spine. Spine J. 5, 297–309 (2005). https://doi.org/10.1016/j.spinee.2004.10.050
- 6. Briggs, A.M., van Dieën, J.H., Wrigley, T.V., Greig, A.M., Phillips, B., Lo, S.K., Bennell, K.L.: Thoracic kyphosis affects spinal loads and trunk muscle force. Phys. Ther. 87, 595–607 (2007). https://doi.org/10. 2522/ptj.20060119
- 7. de Zee, M., Hansen, L., Wong, C., Rasmussen, J., Simonsen, E.B.: A generic detailed rigid-body lumbar spine model. J. Biomech. 40, 1219–1227 (2007). https://doi.org/10.1016/j.jbiomech.2006.05.030
- 8. Christophy, M., Faruk Senan, N.A., Lotz, J.C., O’Reilly, O.M.: A musculoskeletal model for the lumbar spine. Biomech. Model. Mechanobiol. 11, 19–34 (2012). https://doi.org/10.1007/s10237-011-0290-6
- 9. Galbusera, F., Wilke, H.-J., Brayda-Bruno, M., Costa, F., Fornari, M.: Influence of sagittal balance on spinal lumbar loads: a numerical approach. Clin. Biomech. 28, 370–377 (2013). https://doi.org/10.1016/ J.CLINBIOMECH.2013.02.006
- 10. Arshad, R., Zander, T., Dreischarf, M., Schmidt, H.: Influence of lumbar spine rhythms and intra- abdominal pressure on spinal loads and trunk muscle forces during upper body inclination. Med. Eng. Phys. 38, 333–338 (2016). https://doi.org/10.1016/j.medengphy.2016.01.013
- 11. Raabe, M.E., Chaudhari, A.M.W.: An investigation of jogging biomechanics using the full-body lumbar spine model: model development and validation. J. Biomech. 49, 1238–1243 (2016). https://doi.org/10. 1016/j.jbiomech.2016.02.046
- 12. Arjmand, N., Shirazi-Adl, A.: Model and in vivo studies on human trunk load partitioning and stability in isometric forward flexions. J. Biomech. 39, 510–521 (2006). https://doi.org/10.1016/J.JBIOMECH. 2004.11.030
- 13. Jalalian, A., Tay, F.E.H., Arastehfar, S., Liu, G.: A patient-specific multibody kinematic model for repre- sentation of the scoliotic spine movement in frontal plane of the human body. Multibody Syst. Dyn. 39, 197–220 (2017). https://doi.org/10.1007/s11044-016-9556-1
- 14. Harrison, D.E., Colloca, C.J., Harrison, D.D., Janik, T.J., Haas, J.W., Keller, T.S.: Anterior thoracic posture increases thoracolumbar disc loading. Eur. Spine J. 14, 234–242 (2005). https://doi.org/10.1007/ s00586-004-0734-0
- 15. Brasiliense, L.B.C., Lazaro, B.C.R., Reyes, P.M., Dogan, S., Theodore, N., Crawford, N.R.: Biomechan- ical contribution of the rib cage to thoracic stability. Spine 36, E1686-93 (2011). https://doi.org/10.1097/ BRS.0b013e318219ce84
- 16. Sham, M.L., Zander, T., Rohlmann, A., Bergmann, G.: Effects of the rib cage on thoracic spine flexibil- ity/Einfluss des Brustkorbs auf die Flexibilität der Brustwirbelsäule. Biomed. Tech. Eng. 50, 361–365 (2005). https://doi.org/10.1515/BMT.2005.051
- 17. Bayoglu, R., Galibarov, P.E., Verdonschot, N., Koopman, B., Homminga, J.: Twente spine model: a thorough investigation of the spinal loads in a complete and coherent musculoskeletal model of the human spine. Med. Eng. Phys. 68, 35–45 (2019). https://doi.org/10.1016/j.medengphy.2019.03.015
- 18. Bruno, A.G., Bouxsein, M.L., Anderson, D.E.: Development and validation of a musculoskeletal model of the fully articulated thoracolumbar spine and rib cage. J. Biomech. Eng. 137, 081003 (2015). https:// doi.org/10.1115/1.4030408
- 19. Higuchi, R., Komatsu, A., Iida, J., Iwami, T., Shimada, Y.: Construction and validation under dynamic conditions of a novel thoracolumbar spine model with defined muscle paths using the wrapping method. J. Biomech. Sci. Eng. 14, 18–00432 (2019). https://doi.org/10.1299/jbse.18-00432
- 20. Ignasiak, D., Dendorfer, S., Ferguson, S.J.: Thoracolumbar spine model with articulated ribcage for the prediction of dynamic spinal loading. J. Biomech. 49, 959–966 (2016). https://doi.org/10.1016/j. jbiomech.2015.10.010
- 21. Khurelbaatar, T., Kim, K., Kim, Y.H.: A cervico-thoraco-lumbar multibody dynamic model for the es- timation of joint loads and muscle forces. J. Biomech. Eng. 137, 1–8 (2015). https://doi.org/10.1115/1. 4031351
- 22. Schmid, S., Burkhart, K.A., Allaire, B.T., Grindle, D., Bassani, T., Galbusera, F., Anderson, D.E.: Spinal Compressive Forces in Adolescent Idiopathic Scoliosis with and Without Carrying Loads: a Muscu- loskeletal Modeling Study. 8, 1–12 (2020). https://doi.org/10.3389/fbioe.2020.00159
- 23. Iyer, S., Christiansen, B.A., Roberts, B.J., Valentine, M.J., Manoharan, R.K., Bouxsein, M.L.: A biome- chanical model for estimating loads on thoracic and lumbar vertebrae. Clin. Biomech. 25, 853–858 (2010). https://doi.org/10.1016/J.CLINBIOMECH.2010.06.010
- 24. Barba, N., Ignasiak, D., Villa, T.M.T., Galbusera, F., Bassani, T.: Assessment of trunk muscle activa- tion and intervertebral load in adolescent idiopathic scoliosis by musculoskeletal modelling approach. J. Biomech. 114, 110154 (2021). https://doi.org/10.1016/j.jbiomech.2020.110154
- 25. Schmid, S., Burkhart, K.A., Allaire, B.T., Grindle, D., Anderson, D.E.: Musculoskeletal full-body mod- els including a detailed thoracolumbar spine for children and adolescents aged 6–18 years. J. Biomech. 102, 109305 (2020). https://doi.org/10.1016/j.jbiomech.2019.07.049
- 26. Kamal, Z., Rouhi, G., Arjmand, N., Adeeb, S.: A stability-based model of a growing spine with ado- lescent idiopathic scoliosis: a combination of musculoskeletal and finite element approaches. Med. Eng. Phys. 64, 46–55 (2019). https://doi.org/10.1016/j.medengphy.2018.12.015
- 27. Shayestehpour, H., Tørholm, S., Damsgaard, M., Lund, M.: AnyBody Managed Model Repository (AMMR4_Beta). https://doi.org/10.5281/zenodo.10849365
- 28. Damsgaard, M., Rasmussen, J., Christensen, S.T., Surma, E., de Zee, M.: Analysis of musculoskeletal systems in the AnyBody modeling system. Simul. Model. Pract. Theory 14, 1100–1111 (2006). https:// doi.org/10.1016/j.simpat.2006.09.001
- 29. Nikravesh, P.E.: Planar Multibody Dynamics: Formulation, Programming and Applications. CRC Press, Boca Raton (2007)
- 30. de Zee, M., Falla, D., Farina, D., Rasmussen, J.: A detailed rigid-body cervical spine model based on inverse dynamics. J. Biomech. 40, S284 (2007). https://doi.org/10.1016/S0021-9290(07)70280-4
- 31. Schultz, A.B., Benson, D.R., Hirsch, C.: Force-deformation properties of human costo-sternal and costo- vertebral articulations. J. Biomech. 7, 311–318 (1974). https://doi.org/10.1016/0021-9290(74)90024-4
- 32. Lebschy, C.: Biomechanical Modelling of a Human Thorax using the Finite Element Method. Diploma Thesis, Tech. Univ. Wien. 01652328 (2021). https://doi.org/10.34726/hss.2021.65203
- 33. Lemosse, D., Le Rue, O., Diop, A., Skalli, W., Marec, P., Lavaste, F.: Characterization of the mechanical behaviour parameters of the costo- vertebral joint. Eur. Spine J. 7, 16–23 (1998). https://doi.org/10.1007/ s005860050021
- 34. Andriacchi, T., Schultz, A., Belytschko, T., Galante, J.: A model for studies of mechanical interactions between the human spine and rib cage. J. Biomech. 7, 497–507 (1974). https://doi.org/10.1016/0021- 9290(74)90084-0
- 35. Liebsch, C., Graf, N., Wilke, H.: In vitro analysis of kinematics and elastostatics of the human rib cage during thoracic spinal movement for the validation of numerical models. J. Biomech. 94, 147–157 (2019). https://doi.org/10.1016/j.jbiomech.2019.07.041
- 36. Liebsch, C., Graf, N., Wilke, H.J.: The effect of follower load on the intersegmental coupled motion characteristics of the human thoracic spine: an in vitro study using entire rib cage specimens. J. Biomech. 78, 36–44 (2018). https://doi.org/10.1016/j.jbiomech.2018.06.025
- 37. Wong, C.: Mechanism of right thoracic adolescent idiopathic scoliosis at risk for progression; a unifying pathway of development by normal growth and imbalance. Scoliosis 10, 1–5 (2015). https://doi.org/10. 1186/s13013-015-0030-2
- 38. Duprey, S., Subit, D., Guillemot, H., Kent, R.W.: Biomechanical properties of the costovertebral joint. Med. Eng. Phys. 32, 222–227 (2010). https://doi.org/10.1016/j.medengphy.2009.12.001
- 39. Shayestehpour, H., Shayestehpour, M.A., Koutras, C., Tierp-Wong, C.N.E., Rasmussen, J.: Musculoskeletal Modeling of Scoliosis Patients with Acceptable Kinematic Accuracy. Abstr. From 13th Annu. Meet. Danish Soc. Biomech. Kgs. Lyngby, Denmark (2021)
- 40. Mehta, M.H.: The rib-vertebra angle in the early diagnosis between resolving and progressive infantile scoliosis. J. Bone Jt. Surg., Br. 54–B, 230–243 (1972). https://doi.org/10.1302/0301-620X.54B2.230
