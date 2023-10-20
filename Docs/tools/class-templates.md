# Class templates

Class templates are a way to encapsulate and reuse AnyScript code. Class templates are used 
in many parts of the model repository to make the code more readable and easier to maintain.

A simple class template which creates a reference frame which is visible by default:
```{code-block} AnyScriptDoc
#class_template MyClassTemplate(__CLASS__=AnyRefNode, DRAW_NODE = Off) 
{
   #var sRel = {0,0,0};
   #var ARel = eye(3);    
   viewRefFrame = {
      #var Visible = On;
   };
   #if DRAW_NODE == On
   AnyDrawNode DrawNode = {};
   #endif
};
```

The class template can then be used to create a `AnyRefNode`:

```{code-block} AnyScriptDoc
MyClassTemplate MyNode(DRAW_NODE=On) = {
   sRel = {1,1,0};
};
```

Many of the class templates in the model repository are also useful for the users when building
models. 

This page contain a list of all the documented class templates in the model repository.

## List of class templates

```{toctree}
:includehidden: true
:maxdepth: 0
:glob:

*-toc
```

