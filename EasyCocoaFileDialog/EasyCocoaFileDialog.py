import Cocoa

def chooseFileToOpen(prompt="Select the file to open"):
	"""Show a Cocoa open file dialog box and return the filename the user chooses."""
	openDlg = Cocoa.NSOpenPanel.openPanel()

	# set characteristics of the open file dialog
	openDlg.setMessage_(prompt)
	openDlg.setCanChooseFiles_(True)
	openDlg.setCanChooseDirectories_(False)
	openDlg.setAllowsMultipleSelection_(False)

	buttonClicked = openDlg.runModal()
	if buttonClicked == Cocoa.NSFileHandlingPanelOKButton:
		return openDlg.URL().fileSystemRepresentation()
	return None

def chooseFileToSave(prompt="Select the file to save"):
	"""Show a Cocoa save file dialog box and return the filename the user chooses."""
	saveDlg = Cocoa.NSSavePanel.savePanel()

	# set characteristics of the save file dialog
	saveDlg.setMessage_(prompt)

	buttonClicked = saveDlg.runModal()
	if buttonClicked == Cocoa.NSFileHandlingPanelOKButton:
		return saveDlg.URL().fileSystemRepresentation()
	return None

def main():
	prompt = "Please pick the input data file."
	filename = chooseFileToOpen(prompt)
	if filename is None:
		print "The user clicked Cancel."
	else:
		print "The user picked: %s" % filename
	prompt = "Please pick the output data file."
	filename = chooseFileToSave(prompt)
	if filename is None:
		print "The user clicked Cancel."
	else:
		print "The user picked: %s" % filename



if __name__ == '__main__':
	main()