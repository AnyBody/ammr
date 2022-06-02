---
sd_hide_title: true
---

# AMMR documentation!

::::::{div} landing-title
:style: "padding: 0.1rem 0.5rem 0.6rem 0; background-image: linear-gradient(315deg, #9e3f49 0%, #953337 74%); clip-path: polygon(0px 0px, 100% 0%, 100% 100%, 0% calc(100% - 1.5rem)); -webkit-clip-path: polygon(0px 0px, 100% 0%, 100% 100%, 0% calc(100% - 1.5rem));"

::::{grid}
:reverse:
:gutter: 2 3 3 3
:margin: 4 4 1 2

:::{grid-item}
:columns: 12 4 4 4

```{image} ./_static/ammr_bodyparts2.png
:width: 180px
:class: sd-m-auto sd-animate-grow50-rot20
```
:::

:::{grid-item}
:columns: 12 8 8 8
:child-align: justify
:class: sd-text-white sd-fs-3

Documentation for the AnyBody Managed Model Repository.

```{button-link} changelog.html
:outline:
:color: white
:class: sd-px-4 sd-fs-5

{material-outlined}`timeline;1.5em` New in AMMR {{AMMR_VERSION}}
:::
::::

::::::


The AnyBody Model Repository (AMMR), is an open library of
musculoskeletal models and examples ready to be used with the [AnyBody Modeling
System][anybody modeling system].



The AnyBody Managed Model Repository consists of two parts:

- {ref}`Body Models <the-body-model>`: The human body models which can be
  customized and scaled to build a specific musculoskeletal model;
- {ref}`Application examples <example-gallery>`: in which the body models are
  utilized in specific applications (from common daily activities,
  like pushing the acceleration or brake pedals of a car, to workplace
  specific scenarios).

The models are developed in research projects at academic institutions or by
AnyBody Technology in collaboration with academic institutions. The models are
maintained by AnyBody Technology who ensure that various body part models can
be used together as full body, scalable musculoskeletal model.

```{rubric} First time you're using AMMR?
```

If you are a new user check the [AnyBody Tutorials](https://anyscript.org/tutorials) and the getting started video on AnyBody.

The following {doc}`Getting Started section </getting_started>` on the AMMR provides insight into how AMMR is structured, how to
install it and how to use it.


[anybody modeling system]: https://www.anybodytech.com/software/anybodymodelingsystem/


```{toctree}
:includehidden: true
:hidden:

getting_started
about
```

```{toctree}
:caption: Reference
:includehidden: true
:hidden:
:maxdepth: 2
:titlesonly:

bm_config/index
body/models
Applications/index

```

```{toctree}
:caption: Guides
:includehidden: true
:hidden:
:maxdepth: 2
:titlesonly:

creating_model_from_scratch
Scaling/intro
anymocap/index
```
