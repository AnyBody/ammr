# -*- coding: utf-8 -*-
r"""
Exoskeleton Human Contact
===============================

Exoskeleton Human contact model.



.. rst-class:: without-title
.. seealso:: **Main file location in AMMR:** 

  :menuselection:`Application --> Examples --> ExoskeletonContactElbow --> ExoskeletonContact_Elbow.Main.any`


This example shows a simple exoskeleton and how to use the conditional contact
elements to define the kinetic connections between the human and the exoskeleton.
The example is based on the Standing Model. The mannequin drivers are used to
synthetically drive the arms of the model while it supports external loads at 
the hands. An exoskeleton is added on to the right arm to assist elbow flexion. 


The contact between the human and exoskeleton is set up using custom classes.
It uses a custom contact class template that defines contact elements between 
corresponding nodes on the human and exoskeleton segments. The contact nodes 
are generated using another custom class template that can generate a 
parametrized grid of contact points in an elliptical cylinder shape.





"""


import sys
sys.path.insert(0, '../../exts')
import gallery

gallery.plot("../images/ExoskeletonContact_Elbow.jpg")
gallery.show()
