from tkinter import (Frame, Label, Entry, StringVar, Toplevel, Tk, Button)


class main(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.minsize(width=250, height=250)
        self.master.title("main window")
        self.grid()
        self.children_dict = dict()

        newWindowButton = Button(self,
                                 text="open new window",
                                 command=self.newWindowOpen)
        newWindowButton.grid(row=0, column=0)

    def newWindowOpen(self):
        childWindow = Toplevel()
        childWindow.wm_title("child window")

        childWindow.itemLabel = Label(childWindow, text="Test Value")
        childWindow.itemVar = StringVar()
        childWindow.itemEntry = Entry(childWindow,
                                      textvariable=childWindow.itemVar)

        self.children_dict[childWindow] = childWindow.itemVar
        childWindow.itemLabel.grid(row=0, column=0)
        childWindow.itemEntry.grid(row=0, column=1)

        childWindow.submitButton = Button(childWindow,
                                          text="submit",
                                          command=lambda: self.submitTest(childWindow))

        childWindow.submitButton.grid(row=1, column=0)

    def submitTest(self, childWindow):
        value = self.children_dict[childWindow].get()
        print(value)

root = Tk()
main_menu = main()
main_menu.mainloop()
