#coding=utf-8
'''
Created on 2020-06-28
Version 0.8

@author: yongsheng.guo@ansys.com
'''

import clr
import os
import sys

appPath = os.path.realpath(__file__)
appDir = os.path.split(appPath)[0]
sys.path.append(appDir)

clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
clr.AddReferenceToFile('workflowlib.dll')
from System.Windows.Forms import Application,MessageBox
import MainForm

global oDesktop
try:
    import ScriptEnv
    ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
    oDesktop.RestoreWindow()
except ImportError:
    print('Not Run from AEDT')
    oDesktop = None
else:
    print('Running in AEDT environment')
MainForm.oDesktop = oDesktop
MainForm.appDir = appDir

if __name__ == '__main__':
    form = MainForm.MainForm()
    #MessageBox.Show("\n".join(sys.argv))
    htmlPath = appPath.replace('.py','.htm')
    if os.path.exists(htmlPath):
        form.htmlPath = htmlPath
    else:
        MessageBox.Show("Not found setting file: " + htmlPath)
        exit()
        
    if oDesktop:
        form.Show()
    else:
        Application.Run(form)

