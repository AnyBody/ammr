
"msxsl.exe" ../BodyModel.define.xml reST_constants.xslt -o ../../../Docs/bm_config/bm_constants.rst
"msxsl.exe" ../BodyModel.define.xml reST_parameters.xslt -o ../../../Docs/bm_config/bm_statements.rst
"msxsl.exe" ../BodyModel.define.xml reST_parameter_tables.xslt -o ../../../Docs/bm_config/LegTable.txt table-type=Leg
"msxsl.exe" ../BodyModel.define.xml reST_parameter_tables.xslt -o ../../../Docs/bm_config/TrunkTable.txt table-type=Trunk
"msxsl.exe" ../BodyModel.define.xml reST_parameter_tables.xslt -o ../../../Docs/bm_config/ArmTable.txt table-type=Arm
"msxsl.exe" ../BodyModel.define.xml reST_parameter_tables.xslt -o ../../../Docs/bm_config/ScalingTable.txt table-type=Scaling
"msxsl.exe" ../BodyModel.define.xml reST_parameter_tables.xslt -o ../../../Docs/bm_config/MannequinTable.txt table-type=Mannequin_Driver
"msxsl.exe" ../BodyModel.define.xml reST_parameter_tables.xslt -o ../../../Docs/bm_config/JointTypeTable.txt table-type=Joint_type
"msxsl.exe" ../BodyModel.define.xml reST_parameter_tables.xslt -o ../../../Docs/bm_config/OtherTable.txt table-type=Other
"msxsl.exe" ../BodyModel.define.xml reST_description_substitutions.xslt -o ../../../Docs/bm_config/Substitutions.txt
"msxsl.exe" ../BodyModel.define.xml ifdef_BM_param.xslt -o ../BodyModels/GenericBodyModel/Ifdef_BM_param.any
"msxsl.exe" ../BodyModel.define.xml anyxdefs2const.xslt -o ../BodyModels/GenericBodyModel/BodyModel.constants.any
"msxsl.exe" ../BodyModel.define.xml anyxdefs2default.xslt -o ../BodyModels/GenericBodyModel/BodyModel.defaults.any
"msxsl.exe" ../BodyModel.define.xml anyxdefs2define.xslt -o ../Documentation/BodyModel.parameters.any
"msxsl.exe" ../BodyModel.define.xml anyxdefs2messages.xslt -o ../BodyModels/GenericBodyModel/BodyModel.config_info.any
"msxsl.exe" ../BodyModel.define.xml BM_ConstantsMap.xslt -o ../Documentation/bm_constants.py

cmd /k