#coding=utf-8
'''
Created on 2020-06-28
Version 0.8

@author: yongsheng.guo@ansys.com
'''
import System.Drawing
import System.Windows.Forms
import os,sys

from System.Drawing import *
from System.Windows.Forms import *
global appPath
global oDesktop



class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._webBrowser1 = System.Windows.Forms.WebBrowser()
        self.SuspendLayout()
        # 
        # webBrowser1
        # 
        self._webBrowser1.Anchor = System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left | System.Windows.Forms.AnchorStyles.Right
        self._webBrowser1.Location = System.Drawing.Point(0, 0)
        self._webBrowser1.MinimumSize = System.Drawing.Size(20, 20)
        self._webBrowser1.Name = "webBrowser1"
        self._webBrowser1.Size = System.Drawing.Size(286, 525)
        self._webBrowser1.TabIndex = 0
        self._webBrowser1.DocumentCompleted += self.WebBrowser1DocumentCompleted
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(286, 525)
        self.Controls.Add(self._webBrowser1)
        self.Name = "MainForm"
        self.Text = "Workflow"
        self.Shown += self.MainFormShown
        self.ResumeLayout(False)


    def WebBrowser1DocumentCompleted(self, sender, e):
#         clearFloatCopper = self._webBrowser1.Document.GetElementById("clearFloatCopper")
#         print(dir(clearFloatCopper))
#         clearFloatCopper.Click += HtmlElementEventHandler(self.element_click)
        document = self._webBrowser1.Document
        a = document.GetElementsByTagName('li')[0]
        print(dir(a))
        for li in document.GetElementsByTagName('li'):
            li.Click += HtmlElementEventHandler(self.element_click)
        
        #MessageBox.Show(document.Title)
        self.Text = document.Title
        
    def element_click(self, sender, e):
        
        if sender.DomElement.hasAttribute('event'):
            event = sender.DomElement.getAttribute('event')
            eventSplit = event.split(':')
            if len(eventSplit) == 2:
                typ,action = eventSplit
            else:
                MessageBox.Show("Event error on " + sender.InnerText)
                return
            
            if 'script' in typ:
                if oDesktop:
                    scriptPath = os.path.join(appPath,action.strip())
                    if os.path.exists(scriptPath):
                        oDesktop.RunScript(scriptPath)
                    else:
                        MessageBox.Show("Not exist script file: " + scriptPath) 
                else:
                    MessageBox.Show("Please run the application from AEDT")
                    
            elif 'function' in typ:
                exec(action.strip())
            else:
                MessageBox.Show("Event error on " + sender.InnerText)
                
        else:
            MessageBox.Show("Manual check " + sender.InnerText)
            

    def MainFormShown(self, sender, e):
        self._webBrowser1.Navigate(os.path.join(appPath,"HBM_workflow.htm"))
        self.TopMost = True