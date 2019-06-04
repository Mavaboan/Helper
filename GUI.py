import wx

#TODO Make basic UI

class myFrame(wx.Frame):

    def __init__(self, parent, id):

        wx.Frame.__init__(self, parent, id, 'Helper Chan69', size=(800, 800))

        # Creates the panel inside the frame it's where everything the user is gonna use
        # for example the button
        panel = wx.Panel(self)

        # Adds an statusbar to GUI
        # Makes a variable called status using wxPythons function CreateStatusBar
        # which creates an status bar
        status = self.CreateStatusBar()

        # Creates a menu bar at the top of the window stored in the variable
        menubar = wx.MenuBar()
        # Adds a menu to menubar called first and second
        first = wx.Menu()
        second = wx.Menu()

        # Adds a option in the first menu called new window which has a text in the status bar
        first.Append(wx.NewId(), "New Window", "This feature will come in a future version")
        # Adds another option to the first menu with other name but same text
        first.Append(wx.NewId(), "Open...", "This feature will come in a future version")
        # Tells what the first and second menu is gonna be called which is file and edit
        menubar.Append(first, "File")
        menubar.Append(second, "Edit")
        # Does so the menubar actual shows
        self.SetMenuBar(menubar)
    def closeWindow(self, event):
        self.Destroy()

    def income(self, event):



if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = myFrame(parent = None, id = -1)
    frame.Show()
    app.MainLoop()




#TODO Make input for salary

#TODO Make how much spent on stuff
