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

Documentation for the AnyBody Managed Model Repository - AMMR

```{button-link} ./changelog.html#linkcheck_ignore
:outline:
:color: white
:class: sd-px-4 sd-fs-5

{material-outlined}`timeline;1.5em` New in AMMR {{AMMR_VERSION}}
:::
::::

::::::

Open body models
: All models are open and editable with the AnyScript model language

Configurable Human model
: Configure and combine different body models into a full body model

Lots of Application examples
: Gallery of example models provide a good starting point for modeling

Community effort
: Models are combined effort of many research groups over two decades


The AnyBody Model Repository (AMMR), is an unique open library of
musculoskeletal models and examples ready to be used with the [AnyBody Modeling
System][anybody modeling system]. The AnyBody Managed Model Repository consists of two parts:

<span class="material-symbols-outlined">
</span>

::::{grid} 1 3 2 3
:margin: 2 2 0 0
:gutter: 2

:::{grid-item-card} {material-regular}`settings_accessibility;2em` Body Models
:link: the-body-model
:link-type: ref

The human body models which can be 
customized and scaled to build a specific musculoskeletal model.
+++
{ref}`Learn more » <the-body-model>`
:::

:::{grid-item-card} {material-regular}`fitness_center;2em` Example gallery
:link: example-gallery
:link-type: ref

Lots of applicaiton examples showing how the body models are used.
+++
{ref}`Learn more » <example-gallery>`
:::

:::{grid-item-card} {material-regular}`settings;2em` Model Configuration
:link: bm-config
:link-type: ref

Information on how to configure the body models, and enable or disable various body parts.
+++
{ref}`Learn more » <bm-config>`
:::

::::



The models are developed in research projects at academic institutions or by
AnyBody Technology in collaboration with academic institutions. The models are
maintained by AnyBody Technology who ensure that various body part models can
be used together as full body, scalable musculoskeletal model.


```{admonition} **First time user?**
:class: hint dropdown

If you are a new user check the [AnyBody Tutorials](https://anyscript.org/tutorials/) and the getting started video on AnyBody.

The following {doc}`Getting Started section </getting_started>` on the AMMR provides insight into how AMMR is structured, how to
install it and how to use it.
```

[anybody modeling system]: https://www.anybodytech.com/software/anybodymodelingsystem/



```{toctree}
:caption: Examples and applications
:includehidden: true
:hidden:

getting_started
Example Gallery <Applications/index>

```


```{toctree}
:caption: Body Models
:includehidden: true
:hidden:

Body Models <body/models>
bm_config/index

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


```{toctree}
:caption: ━━━━━━━━
:includehidden: true
:hidden: true
:maxdepth: 2
:titlesonly: true



About the model repository <about>

```