from tkinter import *
from sklearn.preprocessing import LabelEncoder,MinMaxScaler,StandardScaler
import pandas as pd
import SVM
import Linearregression,KNN




class Preprocessing:
    def label_encoder(column, dataset):
        label = LabelEncoder()
        for item in column:
            dataset[item] = label.fit_transform(dataset[item])
        return dataset
    
        
    #minmax    
    def minmax(data_set):
        minmax=MinMaxScaler()
        data_set=pd.DataFrame(minmax.fit_transform(data_set),columns=data_set.columns)
        return data_set

        # print(data_set)
        

    # standerd scaler
    def standar(data_set):
        st=StandardScaler()
        data_set=pd.DataFrame(st.fit_transform(data_set),columns=data_set.columns)
        return data_set

        # print(data_set)
        


    def go_to_second_screen(data):
        Preprocess_screen = Toplevel()
        Preprocess_screen.title("Preprocessing Data")
        Preprocess_screen.geometry("420x300")
        copydata=data
        # --------------preprocesssing----------

        data = data.fillna(0, inplace=False)
        column = (data.dtypes == 'object')
        object_cols = list(column[column].index)

        data = Preprocessing.label_encoder(object_cols, data)

        data=Preprocessing.standar(data)
        data = Preprocessing.minmax(data)

        



        txt=Text(Preprocess_screen,height=10,width=50)
        txt.insert(END, "applied preproccessing\nmissing value 0\nstring value Labelencoder\nstander and minmax algorithm")
        txt.config(state=DISABLED)
        txt.pack()
        # print(data)
        svm = Button(Preprocess_screen, text="Support Vector Machine",command=lambda: SVM.fourth_win_svm(copydata),background='green',fg="white")
        svm.pack(side=LEFT,anchor="s",padx=5,pady=10)
        knn = Button(Preprocess_screen, text="K-Nearest Neighbors",command=lambda: KNN.fourth_win_knn(data),background='green',fg="white")
        knn.pack(side=LEFT,anchor="sw",padx=5,pady=10)
        lr = Button(Preprocess_screen, text="Linear Regression",command=lambda: Linearregression.fourth_win_LR(data),background='green',fg="white")
        lr.pack(side=LEFT,anchor="se",padx=5,pady=10)
