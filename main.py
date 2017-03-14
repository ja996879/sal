# coding=UTF-8
import tkinter as tk
import platform
import tkinter.messagebox as messagebox
#from d_help import *
from tkinter import ttk
from tkinter import *
from con_sql import Sql3
#from export_excel import EXport_excel
from tkinter import Tk, StringVar, ttk

class appMain(Frame):
    
    def __init__(self,master=None):
        Frame.__init__(self,master)
        master.minsize(width=250, height=320)
        self.grid()
        ##################
        
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="功能", menu=filemenu)
        filemenu.add_separator()
        filemenu.add_command(label="登入",command=self.chi_window)
        filemenu.add_command(label="EXIT",command=root.destroy)
        master.config(menu=menubar)
        ##################
        self.createWindow()
    def createWindow(self):
        self.tt = Label(text=" ")
        self.tt.grid(row=0,column=0)
       
        self.notebook = ttk.Notebook(height=250,width=320)
        self.frame1 = ttk.Frame(self.notebook)
        self.frame2 = ttk.Frame(self.notebook)
        self.frame3 = ttk.Frame(self.notebook)
        self.notebook.add(self.frame1, text='UP Data')
        self.notebook.add(self.frame2, text='OFF Data')
        self.notebook.add(self.frame3, text='User Data',state="disabled")
        self.notebook.grid(row=1,column=1)

        ##################### frame1 ############################
        self.block_label = Label(self.frame1, text=" ")
        self.block_label.grid(row=0,column=0,pady=15)
        
        self.onbinput = Entry(self.frame1,width=20)
        self.onbinput.grid(row=1,column=0 , sticky=W ,pady=25,padx=40)

        self.on_button = Button(self.frame1, text="ON", width=8,font=("Courier", 10))
        self.on_button.grid(row=1,column=1 )

        self.upframe = LabelFrame(self.frame1,text="Pane A")
        self.upframe.grid(row=4,column=0 , sticky=W,padx=10, columnspan=2)
        self.message_label = Label(self.upframe , text="off Message!!",width=40,height=6)
        self.message_label.grid(row=4,column=0 , sticky='W')
        ##################### frame2 ############################
        self.block2_label = Label(self.frame2, text=" ")
        self.block2_label.grid(row=0,column=0,pady=15)
        
        self.offbinput = Entry(self.frame2,width=20)
        self.offbinput.grid(row=1,column=0 , sticky=W ,pady=25,padx=40)

        self.off_button = Button(self.frame2, text="DOWN", width=8,font=("Courier", 10))
        self.off_button.grid(row=1,column=1 )

        self.onframe = LabelFrame(self.frame2,text="Pane B")
        self.onframe.grid(row=4,column=0 , sticky=W,padx=10,columnspan=2)
        
        self.message2_label = Label(self.onframe, text="off Message!!",width=40,height=6)
        self.message2_label.grid(row=3,column=0 , sticky=W)
        ##################### frame3 ############################
        
    def chi_window(self):
        c_win = tk.Toplevel()
        c_win.wm_title("admin")
        c_win.minsize(width=400, height=250)
      
        self.notebook.tab(self.frame3, state='normal')
        
        c_win.chipnlab = Label(c_win,text=" account : ")
        c_win.chipnlab.grid(row=0,column=0,sticky=W)
        
        c_win.ac_name = Entry(c_win,width=20)
        c_win.ac_name.grid(row=0,column=1,sticky=W)

        c_win.chipnlab2 = Label(c_win,text=" password : ")
        c_win.chipnlab2.grid(row=1,column=0,sticky=W)
        
        c_win.ac_pass = Entry(c_win,show="*",width=20)
        c_win.ac_pass.grid(row=1,column=1,sticky=W ,pady=5)
        
        ac_login = Button(c_win, text="login", width=8,font=("Courier", 10))
        ac_login.grid(row=2,column=1)
        ac_login['command'] =lambda: self.login_on(c_win) 

        #messagebox.showinfo("wran")
        #######################################Standard Error###################
        
    def login_on(self,cw):
        cbx = Sql3()
        coi = cbx.f_t_login("select Uname,Upass from Suser where Uname='%s' and Upass='%s'" %(cw.ac_name.get(),cw.ac_pass.get()))
        if(coi):
            print("true")
        else:
            print("false")
        cbx.del_con
    def login_off(self):
        pass
if __name__ == '__main__':
   root = Tk() 
   root.wm_title("RPy")
   root.geometry("+150+100")
   app = appMain(master=root)
   root.iconbitmap('PRy.ico')
   app.mainloop()

#s_Help.check_str IS CHECK STR SYMBOL " ' " CHANGE \' FUNCTION
