# Total Hip Arthroplasty (THA) Model

Model of a total hip replacement using a contact implant model and
force-dependent kinematics (FDK).

**Main file:** `Application/Examples/THA-KneeBendDemo/THA-KneeBendDemo.main.any`

This is a demo model for the simulation of a knee bend for a body model
with a total hip arthroplasty (THA)using:

- either an ideal spherical joint with joint reaction forces
- or force dependent kinematcs and a contact model.

In the body model, the hip joint is excluded from the AnyBodyStudy and a new
force dependent hip joint is included. Therefore, a acetabular cup and a femoral
component [^fn1] are included into the model and a contact force between these
implants is defined. For stabiliy reasons an artifical spring is implemented to
avoid the joint to disconnect.

Please notice that this simulation is only a demo example. The placement of hte
implant is not based on any anatomical data. Further, the implant includes an
artificial spring (in Model/ContactForces.any) element to make the simulation
more robust. For each simulation, the force produced by this artifical spring
should be checked to be aware of the influence of this spring on the results.

```{rubric} Footnotes
```

[^fn1]: The geometry data of the femoral component was kindly provided by
    Edmundo Fuentes via GrabCAD.com <http://edmundofuentes.com>
