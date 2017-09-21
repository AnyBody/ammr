"msxsl.exe" ../BodyModel.define.xml anyxdefs2html_constants.xslt -o ../Documentation/BodyModel.defs.constants.html
"msxsl.exe" ../BodyModel.define.xml anyxdefs2html_parameters.xslt -o ../Documentation/BodyModel.defs.parameters.html
"msxsl.exe" ../BodyModel.define.xml anyxdefs2const.xslt -o ../BodyModels/GenericBodyModel/BodyModel.constants.any
"msxsl.exe" ../BodyModel.define.xml anyxdefs2default.xslt -o ../BodyModels/GenericBodyModel/BodyModel.defaults.any
"msxsl.exe" ../BodyModel.define.xml anyxdefs2define.xslt -o ../Documentation/BodyModel.defs.any
"msxsl.exe" ../BodyModel.define.xml anyxdefs2messages.xslt -o ../BodyModels/GenericBodyModel/BodyModel.config_info.any
"msxsl.exe" ../BodyModel.define.xml anyxdefs2constants_python.xslt -o ../Documentation/bm_constants.py

cmd /k
