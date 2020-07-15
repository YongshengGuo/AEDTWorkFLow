# coding=utf-8
'''
Created on 2020��7��15��

@author: yguo
'''

import time
import os
from Win32Command import Win32Command


class AEDTCommand(Win32Command):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        Win32Command.__init__(self)
        self.processID = None
        
    def runScript(self,path):
        if not os.path.exists(path):
            print("not found path: " + path)
            return
        
        hwnd = self.hwnd
        self.invokedMenuByID(32822)
        self.waitForValid("self.findWindowEx(self.hwnd.Zero,self.hwnd.Zero, '#32770','Run Script')", 0.1, 5)
        h_runScript = self.findWindowEx(hwnd.Zero,hwnd.Zero, '#32770','Run Script')
        print(h_runScript)
        h_edit = self.findWindowEx(h_runScript,h_runScript.Zero,'ComboBoxEx32', None)
        self.setCompText(h_edit, path)
        self.invokedButtom(h_runScript,0x01)
        
        
if __name__ == "__main__":
    ac = AEDTCommand()
    fp = ac.GetProcessesByName('ansysedt')
    print(fp)
    hwnd = ac.GetHwndFromProcessID(fp[0].Id)    
    hMenu = ac.getMenu(hwnd)
    ac.getMenuIdList(hMenu)
    print(ac.menuIdList)
    ac.runScript(r"D:\Study\Script\Eclipse\Workflow\HBM_workflow\HBM_Workflow\CleanFloatingPython.py")
                