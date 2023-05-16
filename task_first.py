from tkinter import *
from tkinter import ttk, filedialog, scrolledtext
import Second_Frame

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer


main_form = Tk()
main_form.geometry("700x600")
main_form.title("Machine Learning")
main_form.config(background="white")


def browseFiles():
    # browse file 
    global data, data_info
    filename = filedialog.askopenfilename(initialdir="/Machine Learning",
                                          title="Select a File",
                                          filetypes=(("CSV files", "*.csv*"), ("all files", "*.*")))
    data = pd.read_csv(filename)
    data_info = str(data.describe())
    file.configure(text="File Opened: "+filename)


file = Button(main_form, text="Browse Files",
              command=browseFiles, font="none 10 bold")
file.pack()


tree_data = ttk.Treeview(main_form)
# scrollbar = Scrollbar(main_form)
# scrollbar.pack(side=RIGHT, fill=Y)
text = Text(main_form,width=70, height=15)


def show_data(data):
    # display data
    tree_data["columns"] = list(data.columns)
    for header in data.columns:
        tree_data.column(header, width=10)
        tree_data.heading(header, text=header.title())

    # Add the data to the Treeview
    for index, row in data.iterrows():
        tree_data.insert("", END, values=list(row))
    # delet id column
    tree_data.column("#0", width=0, stretch=NO)


def show_data_info(data_info):
    # display data describtion
    text.delete('1.0',END)
    text.insert(END, data_info)
    text.config(state=DISABLED)


btn = Button(main_form, text='show data', command=lambda: show_data(data))
btn.pack()
tree_data.pack()


btn2 = Button(main_form, text='show data info',
              command=lambda: show_data_info(data_info))
btn2.pack()
text.pack()


# to go to second frame and display algorithm 


btn3 = Button(main_form, text='show details', command=lambda:Second_Frame.second.display(data))
btn3.pack(anchor='sw')


main_form.mainloop()
