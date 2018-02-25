from appJar import gui

def press(button):
	app.addButtons(["Enter", "Cancel"], press)
	if button == "Cancel":
		app.stop()
	else:
		usr = app.getEntry("Login")
		pwd = app.getEntry("Pass")
		print("User: ", usr, "Pass: ", pwd)
app = gui()
app.setLabelBg("title", "green")
app.label("title", "Welcome")
app.setLabelEntry("Login")
app.setSecrentEntry("Password")
press()

app.go()
