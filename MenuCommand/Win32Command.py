# coding=utf-8
'''
Created on 2020-7-4

@author: yguo
'''

import clr
import sys
import re
import time
sys.path.append(r'D:\Study\Script\VSRepos\simpleWinAPI\simpleWinAPI2\bin\Debug')
clr.AddReferenceToFile('simpleWinAPI2.dll')
from simpleWinAPI import winAPI

clr.AddReference("System.Diagnostics.Process")
from System.Diagnostics import Process



class Win32Command(object):
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
    
    
    def GetProcessesByTitle(self, regName):
        return filter(lambda p:re.match(regName, p.MainWindowTitle),Process.GetProcesses())

    def GetProcessesByName(self,name):
        return Process.GetProcessesByName(name)

    def GetHwndFromProcessID(self,processId):
        self.hwnd = winAPI.GetMainWindowHandleFromProcessID(processId)
        return self.hwnd
    
    def findWindowEx(self,hwndParent,hwndChildAfter,lpszClass=None,lpszWindow=None):   
        return winAPI.FindWindowEx(hwndParent,hwndChildAfter,lpszClass,lpszWindow)

    def setWindowText(self, hWnd, text):
        #return winAPI.SendMessage(hWnd,winAPI.WM_SETTEXT,0,text)
        return winAPI.SetWindowText(hwnd, text)

    def getWidowText(self, hWnd):
        return winAPI.GetWidowText(hWnd) 

    def getCompText(self,hWnd, text):
        return winAPI.SendMessage(hWnd,winAPI.WM_SETTEXT,0,text)

    def setCompText(self,hComp, text):
        return winAPI.SendMessage(hComp,winAPI.WM_SETTEXT,0,text)        
        
    def getMenu(self,hwnd = None):
        hwnd = hwnd or self.hwnd  
        print(hwnd)
        if hwnd:      
            self.hMenu = winAPI.GetMenu(hwnd)            
            return self.hMenu
        else:
            print("Bad hwnd handle")
    

    #弹出式菜单，就返回-1, 分隔符则返回0
    def getMenuIdList(self,hmenu = None):
        hmenu = hmenu or self.hMenu or self.getMenu()
        if not hmenu:
            print("Bad hmenu handle")
            return
            
        count = winAPI.GetMenuItemCount(hmenu)
        #print(count)
        if count == -1:
            return
        for i in range(count):
            menuStr = winAPI.GetMenuString(hmenu,i).replace("&","")
            menuStr = re.sub(r'\t.*','',menuStr)
            menuID = winAPI.GetMenuItemID(hmenu,i)
            #hSubmenu = winAPI.GetSubMenu(hmenu,i)
            self.menuIdList +=[menuStr,menuID] 
            #print(i,menuStr,menuID)
            if menuID == -1:
                hSubmenu = winAPI.GetSubMenu(hmenu,i)
                self.getMenuIdList(hSubmenu)
                
    def invokedMenuByID(self,menuID):
        #return winAPI.SendMessage(self.hwnd, winAPI.WM_COMMAND, menuID, None)
        return winAPI.PostMessage(self.hwnd, winAPI.WM_COMMAND, menuID, None)
        
    def invokedMenuByName(self,name):
        try:
            ind = self.menuIdList.index(name)
            self.invokedMenuByID(self.menuIdList[ind+1])
        except:
            print("not fond menu item: " + name)
    
    def invokedButtom(self,hWnd,ID):
        winAPI.SendMessage(hWnd,winAPI.WM_COMMAND,ID,None)

    def waitForValid(self,cmd,interval,timeout):
        timeElapse = 0
        while timeElapse < timeout:
            rst = eval(cmd)
            if rst:
                return rst
            time.sleep(interval)
            timeElapse += interval
            print(timeElapse)

                
if __name__ == "__main__":
    mc = Win32Command()     
#     hwnd = winAPI.FindWindow('Notepad',None)
#     mc.hwnd = hwnd
#     mc.getMenuIdList()
#     print(mc.menuIdList)
    #mc.menuClick(3)
    #mc.invokedMenuByName('Save')
    fp = mc.GetProcessesByName('ansysedt')
    print(fp)
    hwnd = mc.GetHwndFromProcessID(fp[0].Id)
    hMenu = mc.getMenu(hwnd)
    mc.getMenuIdList(hMenu)
    print(mc.menuIdList)
    h_runScript = mc.findWindowEx(hwnd.Zero,hwnd.Zero, '#32770','Run Script')
    print(h_runScript)
    h_edit = mc.findWindowEx(h_runScript,h_runScript.Zero,'ComboBoxEx32', None)
    #h_open = mc.findWindowEx(h_runScript,h_runScript.Zero,'Button', "&Open")
    print(h_edit)
    #mc.setWindowText(h_edit, "test11112222.py")
    mc.setCompText(h_edit, "test11112222.py")
    mc.invokedButtom(h_runScript,1)
    
        