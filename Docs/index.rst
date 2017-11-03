.. AMMR documentation master file, created by
   sphinx-quickstart on Wed Aug 23 14:56:19 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the AMMR documentation!
=======================================

The AnyBody Model Repository (AMMR) [#f1]_, is an open library of
musculoskeletal models and examples ready to be used with the `AnyBody Modeling
System`_. 

.. figure:: _static/ammr_bodyparts.png
   :align: center
   :figwidth: 85 %
   :width: 70 %
   :alt: The AnyBody Model Repository

   *The AnyBody Model Repository is a unique open collection of human body parts*.


The models are developed in research projects at academic institutions or by
AnyBody Technology in collaboration with academic institutions. The models are
maintained by AnyBody Technology who ensure that various body part models can
be used together as full body, scalable musculosketeal model.

.. _AnyBody Modeling System: https://www.anybodytech.com/software/ams/

Using the AMMR
--------------
.. toctree::
    :maxdepth: 1

    Installation
    Understanding_the_models
    BM_Config/HumanBody_configurations


Model Overview
--------------

The Model Repository consist of two parts. The **Body Models** which can be
customized and scaled to build a subject specific musculoskeletal model, and **Application examples** in which the body models are utlizied in specific
applications.

.. toctree::
    :maxdepth: 2

    BodyModels/BodyParts_and_models
    Applications/overview


Guides
---------------
.. toctree::
    :maxdepth: 1

    Creating_model_from_scratch
    Scaling/intro



Development
-----------

.. toctree::
    :maxdepth: 2

    Contribute


Indices and tables
------------------

* :ref:`genindex`
* :ref:`search`

.. rubric:: Footnotes


.. [#f1] The double *M* in the *AMMR* comes from the repository sometimes
    beeing refered to as the "AnyBody Managed Model Repository". 
    You may call it what you like. 