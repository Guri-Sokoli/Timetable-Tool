import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
import csv
from tkinter import filedialog

class Courses():

    def __init__(self, root):
        FilePathLbl = Label(root, width=15)
        FilePathLbl.config(text="Provide data path", bg="white")
        FilePathLbl.grid(row=0, column=0, padx=(5, 10), pady=(20, 0))

        self.PathEntry = Entry(root)
        self.PathEntry.grid(row=0, column=1, padx=(0, 0), pady=(20, 0), columnspan=2, sticky=W + E)
        self.PathEntry.insert(END, 'C:\\Users\\PC\\Downloads\\sampledata (1).csv')

        YrLbl = Label(root, width=15)
        YrLbl.config(text="Year", bg="white")
        YrLbl.grid(row=1, column=0, padx=(5, 10), pady=(20, 0), sticky=W + E)
        n = tk.StringVar()

        self.YrBox = ttk.Combobox(root, width=5, textvariable=n)
        self.YrBox['values'] = ('1', '2', '3', '4', '5')
        self.YrBox.grid(column=1, row=1, padx=(5, 10), pady=(20, 0), sticky=W + E)
        self.YrBox.current()

        DepLbl = Label(root)
        DepLbl.config(text="Department", bg="white")
        DepLbl.grid(row=1, column=3, padx=(5, 10), pady=(20, 0), sticky=W + E)

        self.DpEntry = Entry(root)
        self.DpEntry.grid(row=1, column=4, padx=(5, 10), pady=(20, 0), sticky=W)

        DspBtn = Button(root, command=lambda:[self.enter_file_dir(), self.enter_year(), self.enter_dep()])
        DspBtn.config(text="Display", bg="white")
        DspBtn.grid(row=2, column=0, sticky=E, padx=(0, 10), pady=(50, 0))

        ClrBtn = Button(root, command=self.clear_file_dir)
        ClrBtn.config(text="Clear", bg="white")
        ClrBtn.grid(row=2, column=1, sticky=W + E, padx=(0, 10), pady=(50, 0))

        SvBtn = Button(root)
        SvBtn.config(text="Save", bg="white")
        SvBtn.grid(row=2, column=2, sticky=W + E, padx=(0, 10), pady=(50, 0))

        SelCrsLbl = Label(root)
        SelCrsLbl.config(text="Selected courses: ", bg="white")
        SelCrsLbl.grid(row=5, column=0, columnspan=5, padx=(10, 0), pady=(50, 0), ipadx=5, sticky=W)

        self.SelCrsLbx = Listbox(root, width=20)
        self.SelCrsLbx.grid(row=6, column=0, columnspan=5, padx=(10, 0), pady=(15, 0), sticky=W)

        CrsLbl = Label(root)
        CrsLbl.config(text="Courses", bg="white")
        CrsLbl.grid(row=5, column=2, columnspan=10, padx=(0, 0), pady=(50, 0), sticky=W + E)

        self.CrsLbx = Listbox(root, width=50)
        self.CrsLbx.grid(row=6, column=2, columnspan=10, padx=(0, 0), pady=(15, 0), sticky=W + E)
        self.CrsLbx.bind('<Double-1>')
# C:\\Users\\PC\\Downloads\\sampledata (1).csv
    def enter_file_dir(self):
        filepath = self.PathEntry.get()
        year = self.YrBox.get()
        department = self.DpEntry.get()
        if year=='' or department=='':
            print('kah je nis')
        else:
            with open('sampledata (1).csv', mode='r') as file:
                sd = csv.reader(file)
                for lines in sd:
                    self.CrsLbx.insert(END, lines)

    def enter_year(self):
        year = self.YrBox.get()
        print(year)

    def enter_dep(self):
        list_dp = ['','']
        department = self.DpEntry.get()
        print(department)

    def clear_file_dir(self):
        self.SelCrsLbx.delete(0, END)






root = Tk()
root.resizable(0, 0)  # disable window size
root.geometry("520x500+400+200")  # size of the window
root.wm_title(" " * 50 + "Course Tool")  # to set a title of the window
root.configure(background='dimgray')  # backgournd color
Courses(root)
root.mainloop()
