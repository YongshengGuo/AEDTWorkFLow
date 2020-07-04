# coding=utf-8
'''
Created on 2020-7-4

@author: yguo
'''

import clr
import sys
import re
sys.path.append(r'D:\Study\Script\VSRepos\simpleWinAPI\simpleWinAPI2\bin\Debug')
clr.AddReferenceToFile('simpleWinAPI2.dll')
from simpleWinAPI import winAPI

class menuCommand(object):
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
    
    
    def GetHwndFromProcessID(self,processId):
        self.hwnd = winAPI.GetMainWindowHandleFromProcessID(processId)
        
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
                
    def menuClick(self,menuID):
        winAPI.MenuClick(self.hwnd,menuID) 
        
    def invokedMenu(self,name):
        try:
            ind = self.menuIdList.index(name)
            self.menuClick(self.menuIdList[ind+1])
        except:
            print("not fond menu item: " + name)
            
                
if __name__ == "__main__":
    mc = menuCommand()     
    hwnd = winAPI.FindWindow('Notepad',None)
    mc.hwnd = hwnd
    mc.getMenuIdList()
    print(mc.menuIdList)
    #mc.menuClick(3)
    mc.invokedMenu('Save')
        