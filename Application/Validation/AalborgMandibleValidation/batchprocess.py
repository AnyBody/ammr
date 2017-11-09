# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 15:34:12 2014

Script to batch process AnyBody models.  Requires the 
package AnyPyTools. 

@author: Michael Skipper Andersen
"""
import os
import time
try:
	from anypytools.abcutils import AnyPyProcess
except ImportError:
	print "The package AnyPyTools needs to be installed. Please contact Morten Enemark Lund mel@m-tech.aau.dk"
	time.sleep(6)

#from anypytools.abcutils import getsubdirs

abp = AnyPyProcess(num_processes = 5,
                   anybodycon_path = 'C:\Program Files\AnyBody Technology\AnyBody.6.0\AnyBodyCon.exe',
                    timeout = 300000,
                     disp = True)

# Macro for the free movement
macroStatic =  ['load "AnalysisFreeMovement.any"', 
         'operation  Main.AnalysisMandible',
         'run']


macroAll =  ['load "AnalysisFreeMovement.any"', 
         'operation  Main.AnalysisMandible',
         'run',
         'load "AnalysisPlanar.main.any"', 
         'operation  Main.AnalysisMandible',
         'run',
         'load "AnalysisFDK.main.any"', 
         'operation  Main.AnalysisMandible',
         'run']
  
#macroAll =  ['load "AnalysisFreeMovement.any"', 
#         'operation  Main.AnalysisMandible',
#         'run',
#         'load "AnalysisPlanar.main.any"', 
#         'operation  Main.AnalysisMandible',
#         'run']

       		  
## Run the static trial first    
abp.start_macro(macrolist=macroStatic,folderlist=[os.getcwd()],search_subdirs = "Static0001.c3d")

## Run all other movement trials
abp.start_macro(macrolist=macroAll,folderlist=[os.getcwd()],search_subdirs = "AnalysisFreeMovement.any")

