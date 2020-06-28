# ----------------------------------------------
# ----------------------------------------------
import os
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()
oEditor = oDesign.GetActiveEditor()

oEditor.Heal(
	[
		"NAME:Feature",
        "Selection:=", oEditor.FindObjects("Type","poly"), 
		"Type:="		, "FloatingBodies",
		"AntiPads:="		, False,
		"Tol:="			, "1mm2"
	])
