Body Model Plugin (BM-Plugin)
=============================

The Body Model Plugin is a piece of software meant to be used as a
high level interface on top of AnyScript, particularly for setting
BM statements. 

The example below configures a model with no arms and sets the
"TLEM Leg v2" legs model.

.. image:: /_static/bm_plugin_1.png
    :width: 500
    :align: center

The BM-Plugin is available with models that make use of the
Human Model:

.. code-block:: AnyScriptDoc

    // Include the HumanModel to configure it using BM-Plugin
    #include "<ANYBODY_PATH_BODY>\HumanModel.any"

To start BM-Plugin, a button comes available in AMS in order to
launch it:

.. image:: /_static/bm_plugin_2.png
    :width: 700
    :align: center

The BM statements are classified in five tabs which are providing
instantaneous visual feedback: ``Body``, ``Legs``, ``Arms``,
``Trunk``, ``Mannequin Drivers``.

The complete configurable list of BM statements can be found in the
``Advanced`` tab:

.. image:: /_static/bm_plugin_3.png
    :width: 500
    :align: center

The BM statements are stored in a dedicated file located in the
``Model`` folder next to the ``.main.any`` file of the model.
For the BM statements set in this file to take effect, the file
needs to be included in the model:

.. code-block:: AnyScriptDoc

    // Include the file containing the BM statements. 
    #include "Model/BodyModelConfiguration.any"

This structure of for the model's files is encouraged regardless
if the BM-Plugin is used or not. The content of the configuration
file can be seen in the ``Script File`` tab of the plugin:

.. image:: /_static/bm_plugin_4.png
    :width: 500
    :align: center


