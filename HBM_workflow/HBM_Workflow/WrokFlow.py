#coding=utf-8
'''
Created on 2020-06-28
Version 0.8

@author: yongsheng.guo@ansys.com
'''

import clr
import os
import sys

clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')

from System.Windows.Forms import Application
import MainForm

appPath = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(appPath)
MainForm.appPath = appPath


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
MainForm.appPath = appPath


Application.EnableVisualStyles()
form = MainForm.MainForm()
Application.Run(form)
