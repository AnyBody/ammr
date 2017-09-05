"msxsl.exe" ../BodyModel.define.xml anyxdefs2html_constants.xslt -o ../Documentation/BodyModel.defs.constants.html
"msxsl.exe" ../BodyModel.define.xml anyxdefs2html_parameters.xslt -o ../Documentation/BodyModel.defs.parameters.html
"msxsl.exe" ../BodyModel.define.xml anyxdefs2rst_constants.xslt -o ../../../Docs/bm_constants.rst
"msxsl.exe" ../BodyModel.define.xml anyxdefs2rst_parameters.xslt -o ../../../Docs/bm_statements.rst
"msxsl.exe" ../BodyModel.define.xml anyxdefs2rst_parameter_Table.xslt -o ../../../Docs/bm_tables/LegTable.txt table-type=Leg
"msxsl.exe" ../BodyModel.define.xml anyxdefs2rst_parameter_Table.xslt -o ../../../Docs/bm_tables/TrunkTable.txt table-type=Trunk
"msxsl.exe" ../BodyModel.define.xml anyxdefs2rst_parameter_Table.xslt -o ../../../Docs/bm_tables/ArmTable.txt table-type=Arm
"msxsl.exe" ../BodyModel.define.xml anyxdefs2rst_parameter_Table.xslt -o ../../../Docs/bm_tables/ScalingTable.txt table-type=Scaling
"msxsl.exe" ../BodyModel.define.xml anyxdefs2rst_parameter_Table.xslt -o ../../../Docs/bm_tables/MannequinTable.txt table-type=Mannequin_Driver
"msxsl.exe" ../BodyModel.define.xml anyxdefs2rst_parameter_Table.xslt -o ../../../Docs/bm_tables/OtherTable.txt table-type=Other
"msxsl.exe" ../BodyModel.define.xml anyxdefs2rst_substitutions.xslt -o ../../../Docs/bm_tables/Substitutions.txt
"msxsl.exe" ../BodyModel.define.xml anyxdefs2const.xslt -o ../BodyModels/GenericBodyModel/BodyModel.constants.any
"msxsl.exe" ../BodyModel.define.xml anyxdefs2default.xslt -o ../BodyModels/GenericBodyModel/BodyModel.defaults.any
"msxsl.exe" ../BodyModel.define.xml anyxdefs2define.xslt -o ../Documentation/BodyModel.defs.any
"msxsl.exe" ../BodyModel.define.xml anyxdefs2messages.xslt -o ../BodyModels/GenericBodyModel/BodyModel.config_info.any

cmd /k
