(bestpractices-ammr)=

# Best Practices

Once you have installed the demo repository, you are free to work with it as you
please. However, this page describes the best practices to make the most out of
AMMR. This page is especially relevant if you are new to AMMR.

# The libdef file

The libdef.any is an often overlooked but a critical file when you are working 
with the AMMR. So, let's have a look at it together. You can find it in the root 
folder of the AMMR, for example {{AMMR_DEMO_INST_DIR}}.

```{image} _static/best-practices-libdef.png
:alt: Step1
:class: bg-primary
:align: center
:width: 20%
```
If you open this file, you will see several `#path` statements, for example:

```AnyScriptDoc
#path ANYBODY_PATH_AMMR "."
#path ANYBODY_PATH_BODY "Body/AAUHuman/"
#path ANYBODY_PATH_MANDIBLE "Body/Mandible/"
#path ANYBODY_PATH_MODELUTILS "Tools/ModelUtilities/"
#path AMMR_TOOLS "Tools/"
```

These statements define shortcuts that let AnyBody Modeling System know where 
exactly to look for a file when the identifier is used in an `#include` 
statement such as
```AnyScriptDoc
#include "<ANYBODY_PATH_BODY>/HumanModel.any"
```
Once the `#path` statements are correctly defined through the libdef.any file,
it doesn't matter where in your model you use it to `#include` a file, as long 
as it's defined after the path statement. AnyBody Modeling System will know the 
complete path of the file. Please note that sequence matters for statements 
beginning with `#`, such as `#path`, `#include`, `#if`, `#define`, etc. 

:::{note}
In the demo AMMR, you can find several files that are named libdef.any. They only
exist to create a chain up to the libdef.any file in the root folder of the AMMR.
This can be confusing but is convenient as the main files can be several levels
deep into the AMMR.
:::

# Working on your own models

You can either {doc}`create a model from scratch<creating_model_from_scratch>` or 
use one of the {ref}`application examples<example-gallery>` from the AMMR as a 
starting point. In either case, the advice is to keep your demo AMMR as clean as 
possible. Please select another working directory on your machine where you can 
start a new model or copy the folder of the application example that serves you 
the most, and then write all your code over here.

In the main file of your model, write or update the line including the libdef file 
to include the libdef file from the root folder of your demo AMMR. You can copy 
the path of the libdef file from the AMMR and paste the path in the main file 
of your model.

:::{tip}
If you have multiple models in your working directory, you can have a libdef file 
at the root level of your working directory. All your models can point to this
libdef file, which can in turn include the libdef file from your demo AMMR. In 
this way, you can quickly control/update the AMMR version of all your models by 
checking the root libdef file in your working directory.
:::

# Working with the body model

The human model in the AMMR is highly customizable. You can already find several
configurations through the {doc}`body model (BM) statements<bm_config/index>`. 
For example, you can define your own joint for the knee by setting
`#define BM_JOINT_TYPE_KNEE_RIGHT _JOINT_TYPE_USERDEFINED_`. This statement
will exclude the default knee joint from the body model and all the objects that
depends on it. Then, you can simply define a new knee joint without needing to
modify any of the body model files in the AMMR. It is possible to add objects 
to the human model without modifying the body model files. You can open the
scope to the corresponding body model folder through one of your model specific 
file and make additions, for example:
  ```AnyScriptDoc
  Main.HumanModel.BodyModel.Trunk.SegmentsLumbar.L4Seg = {
    AnyRefNode MyNode = {};
  };
  ```

It's possible that the BM statements are not sufficient for your modeling needs.
Depending on your use case, you may need to make some modifications to the body
model. This is possible, and there can be two ways to do it:
- Some parameters in the human model can be overwritten. They are defined using 
  the `??=` operator. Let's say you want to tweak the muscle strength of the 
  biceps. This is defined through `F0` of the corresponding muscle model in
  the body model file defining the parameters for all the muscles in the 
  shoulder-arm group. You can simply overwrite the default value by writing 
  the following line in your Main file or one of the other files of your model:
  ```AnyScriptDoc
  Main.HumanModel.BodyModel.Right.ShoulderArm.MuscleModels.biceps_brachii_caput_longum.F0 = 200;
  ```
  In this way, you can modify the body model parameters without modifying the 
  body model files. This is important so that the modifications only affect
  a specific model and not all the models using your copy of the AMMR.

- For some modifications, you must make changes to the body model files. Let's
  say you need to update the position of a reference node on the human model,
  then you must update the sRel or the model parameters through the corresponding
  body model file. If you change the body model file in your demo AMMR, then you 
  must be aware that the change will affect all the models using that AMMR.
  The best way to do this is to {doc}`install <ammr_installation>` a clean 
  demo AMMR, make a copy of your freshly installed AMMR, mark and use the copied
  version for making changes to the body model. The installed demo AMMR is used
  by the AnyBody Assistant to list the examples on the Demo tab. Therefore, it 
  is recommended not to make any changes in the installed Demo AMMR.

# Version Control

If you are not familiar with version control, then the best advice is perhaps to 
familiarize yourself with version control before you embark on your journey
of making amazing AnyBody models. Building such models takes a lot of time and
version control will make your life easier when you want to look back at the 
changes you have made, whether you want to document your model or debug your 
model. Moreover, version control tools can also make collaborative development
of the model systematic and robust. Since AnyScript is text based, it can be
easily version controlled.

This page can't describe version control in detail. There are several
online resources that explain it better than it can possibly be explained here.
You are encouraged to look for these resources. Meanwhile, here are a couple
of links to help you get started.
[Git](https://git-scm.com/) is a commonly used tool for version control. It is
a command line-based tool, however, there are also several 
[GUI clients](https://git-scm.com/downloads/guis?os=windows) that can make 
version control easier.

# Benefits of best practices

If you follow these practices, you will have several benefits down the line.
- You will be able keep your models separate from your demo AMMR.
- Changes will be introduced through your models and the demo AMMR will remain
  clean.
- You can use the same demo AMMR for several models.
- It will be easier to share models as you won't need to share the entire AMMR.
- You will have a better overview of the changes you will make to your models.

