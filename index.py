from tkinter import *
from tkinter import ttk, filedialog, scrolledtext
import pandas as pd
import preprocessing


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
    file.configure(text="File Opened: "+filename,background='green',foreground="white")


file = Button(main_form, text="Browse Files",
              command=browseFiles, font="none 10 bold")
file.pack()
tree_data = ttk.Treeview(main_form)
text = Text(main_form,width=110, height=20)

def show_data():    
    tree_data["columns"] = list(data.columns)
    for header in data.columns:
            tree_data.column(header, width=10)
            tree_data.heading(header, text=header.title())

        # Add the data to the Treeview
    for index, row in data.iterrows():
            tree_data.insert("", END, values=list(row))
        # delet id column
    tree_data.column("#0", width=0, stretch=NO)


    text.delete('1.0',END)
    text.insert(END, data_info)
    text.config(state=DISABLED)

showData=Button(main_form,text="Show Data",command=lambda: show_data())

showData.pack(pady=10)
tree_data.pack()
text.pack()



        
showAlgorithm=Button(main_form,text="Show Algorithm",command=lambda:preprocessing.Preprocessing.go_to_second_screen(data))
showAlgorithm.pack(side=RIGHT)


main_form.mainloop()
