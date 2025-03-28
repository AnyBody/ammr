# Howto: Update old models

Models created in earlier versions of AnyBody may need to be updated to work with
newest version of AnyBody and the new model repository (AMMR).

If you are upgrading a model from AMMR version 3. 
Please see this migration guide: [Update models to AMMR 4](migration3to4.md).

If you are upgrading a model from AMMR version 2, please also consult this migration guide: [Update models to AMMR 3](migration2to3.md).

### Shank markers

The coordinate system used for scaling shank have been changed slightly. Scaling no longer takes place 
in the shank anatomical frame, but in a frame that is aligned with the femur scaling frame. 
This may affect markers placed on the shank segment, which is not set releative to some bony landmark. 


```{toctree}
:includehidden: true
:maxdepth: 1

migration3to4
migration2to3
```
