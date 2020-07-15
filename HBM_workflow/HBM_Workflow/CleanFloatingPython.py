# ----------------------------------------------
# ----------------------------------------------
# import os
# import ScriptEnv
# ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
# oDesktop.RestoreWindow()

global oDesktop
try:
    if 'oDesktop' not in dir():
        import ScriptEnv
        ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
        oDesktop.RestoreWindow()
except ImportError:
    print('Not Run from AEDT')
    oDesktop = None
else:
    print('Running in AEDT environment')

oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()
oEditor = oDesign.GetActiveEditor()
print("cleanFloating....................................")
oEditor.Heal(
	[
		"NAME:Feature",
        "Selection:=", oEditor.FindObjects("Type","poly"), 
		"Type:="		, "FloatingBodies",
		"AntiPads:="		, False,
		"Tol:="			, "1mm2"
	])
