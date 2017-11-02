import os

TEMPL = """//# Note. Since these tests include main files from other
//# applications they alter the ANYBODY_PATH_MAINFILEDIR and 
//# ANYBODY_PATH_MAINFILE preprocessor flags. 
//#
//# If these flags are important to the model they must be mocked by the
//# test framework. This can be done by adding the following test directives. 
//# path = {{'ANYBODY_PATH_MAINFILEDIR':'{path_mainfiledir}',
//#         'ANYBODY_PATH_MAINFILE':'{path_mainfile}' }}
//#
#include "../libdef.any"

#include "{path_mainfile}"

Main = 
{{
  AnyOperation& RunTest = Main.RunApplication;
}};
"""


mainfiles = g`../../Application/Examples/**.*main.any`
mainfiles = mainfiles + g`../../Application/Validation/**.*main.any`

tests = set()
for mainfile in mainfiles:
    basename = os.path.basename(mainfile)
    name, ext = os.path.splitext(basename)
    maindir = os.path.dirname(mainfile)
    main_dirname = os.path.basename(maindir)
    if name in tests:
        name = main_dirname + '_' + name
    if name in tests:
        print('Already exists: ' + name)
        continue
    tests.add(name)

    
    test_file_name = os.path.join('test_'+ name + '.any')
    test_file_name = test_file_name.replace('.Main','').replace('.main','')
    
    text = TEMPL.format(path_mainfile=mainfile.replace('\\','/'),
                        path_mainfiledir=maindir.replace('\\','/'),
                        name_mainfiledir=main_dirname,
                        name_mainfile=basename)
    if not os.path.exists(test_file_name):
        pass
    with open(test_file_name,'w') as f:
        f.write(text)
        print('Created "{}"'.format(test_file_name))
        
    