'''
Created on 2020-7-14

@author: yguo
'''

import clr
import sys
import re
sys.path.append(r'D:\Study\Script\VSRepos\simpleWinAPI\simpleWinAPI2\bin\Debug')
clr.AddReferenceToFile('simpleWinAPI2.dll')
from simpleWinAPI import winAPI

clr.AddReference("System.Diagnostics.Process")
from System.Diagnostics import Process

class processCommand(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.hwnd = None
        self.hMenu = None
        self.menuIdList = []

    def getProcessesByName(self,name):
        return Process.GetProcessesByName(name)
    
    def getCurrentProcess(self):
        return Process.GetCurrentProcess()

    def getProcesses(self, regName):
        return filter(lambda p:re.match(regName, p.MainWindowTitle),Process.GetProcesses())

    def getMainWindowHandlebyProcess(self,pro):
        return pro.MainWindowHandle
        print(pro.ProcessName)
        print(pro.MainWindowHandle)
        print(pro.SafeHandle)
        print(pro.Handle)
            
        
import time
        
def test1():
    pc = processCommand()
    while(1):
        cpro = pc.getCurrentProcess()
        print(cpro.MainWindowTitle)
        time.sleep(2)

def test2():
    pc = processCommand()
    pro = pc.getProcessesByName('ansysedt')
    print(pro)
    pc.getMainWindowHandlebyProcess(pro[0])                


if __name__ == '__main__':
    test1()

    