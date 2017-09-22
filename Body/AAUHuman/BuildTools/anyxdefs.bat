
"msxsl.exe" ../BodyModel.define.xml reST_constants.xslt -o ../../../Docs/BM_Config/bm_constants.rst
"msxsl.exe" ../BodyModel.define.xml reST_parameters.xslt -o ../../../Docs/BM_Config/bm_statements.rst
"msxsl.exe" ../BodyModel.define.xml reST_parameter_tables.xslt -o ../../../Docs/BM_Config/LegTable.txt table-type=Leg
"msxsl.exe" ../BodyModel.define.xml reST_parameter_tables.xslt -o ../../../Docs/BM_Config/TrunkTable.txt table-type=Trunk
"msxsl.exe" ../BodyModel.define.xml reST_parameter_tables.xslt -o ../../../Docs/BM_Config/ArmTable.txt table-type=Arm
"msxsl.exe" ../BodyModel.define.xml reST_parameter_tables.xslt -o ../../../Docs/BM_Config/ScalingTable.txt table-type=Scaling
"msxsl.exe" ../BodyModel.define.xml reST_parameter_tables.xslt -o ../../../Docs/BM_Config/MannequinTable.txt table-type=Mannequin_Driver
"msxsl.exe" ../BodyModel.define.xml reST_parameter_tables.xslt -o ../../../Docs/BM_Config/OtherTable.txt table-type=Other
"msxsl.exe" ../BodyModel.define.xml reST_description_substitutions.xslt -o ../../../Docs/BM_Config/Substitutions.txt
"msxsl.exe" ../BodyModel.define.xml anyxdefs2const.xslt -o ../BodyModels/GenericBodyModel/BodyModel.constants.any
"msxsl.exe" ../BodyModel.define.xml anyxdefs2default.xslt -o ../BodyModels/GenericBodyModel/BodyModel.defaults.any
"msxsl.exe" ../BodyModel.define.xml anyxdefs2define.xslt -o ../Documentation/BodyModel.parameters.any
"msxsl.exe" ../BodyModel.define.xml anyxdefs2messages.xslt -o ../BodyModels/GenericBodyModel/BodyModel.config_info.any
"msxsl.exe" ../BodyModel.define.xml BM_ConstantsMap.xslt -o ../BodyModels/bm_constants.py

cmd /k