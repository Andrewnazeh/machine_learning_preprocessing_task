from tkinter import *
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import Lasso
import pandas as pd


class second:

    def display(data):
        # second_frame = Tk()
        second_frame = Toplevel()
        second_frame.title("Algorithem Display")
        second_frame.geometry("500x500")

        # replace any nan value to 0
        data = data.fillna(0, inplace=False)

        # delete any object column
        m = (data.dtypes == 'object')
        object_cols = list(m[m].index)
        data = data.drop(object_cols, axis=1)

        def choose_algo(slider_Test, slider_lamda):
            algo_num = algo.get()
            x = data.iloc[:, :-1].values   # featrures
            y = data.iloc[:, -1].values    # traget
            x_train, x_test, y_train, y_test = train_test_split(
                x, y, test_size=(slider_Test.get()/100), random_state=0)
            lam = float(slider_lamda.get())
            ridgereg = Lasso(alpha=lam)
            ridgereg.fit(x_train, y_train)
            y_pred = ridgereg.predict(x_test)
            if algo_num == 1:
                MSE = np.square(np.subtract(y_test, y_pred)).mean()
                mse = str(MSE)
                # print('mse:', mse)
                result.config(text=mse)
            elif algo_num == 3:
                RMSE = np.square(np.subtract(y_test, y_pred)).mean()
                rmse = np.sqrt(RMSE)
                rmsee = str(rmse)
                result.config(text=rmse)
                # print('rmse:', rmsee)
            else:
                MAE = np.mean(np.abs(y_test, y_pred))
                mae = str(MAE)
                # print('mae:', mae)
                result.config(text=mae)

        test = Label(second_frame, text="Test", font=("Arial", 12))
        test.grid(row=0, column=0, padx=10, pady=10)
        slider_Test = Scale(second_frame, from_=0, to=100,
                            orient=HORIZONTAL, command=lambda value_test: value_test)

        slider_Test.set(75)
        slider_Test.grid(row=0, column=2, padx=20, pady=20, columnspan=3)

        lamda = Label(second_frame, text="Lamda ", font=("Arial", 12))
        lamda.grid(row=3, column=0, padx=10, pady=10)
        slider_lamda = Scale(second_frame, from_=0, to=100,
                             orient=HORIZONTAL, command=lambda value: value)

        slider_lamda.set(75)
        slider_lamda.grid(row=3, column=2, padx=20, pady=20, columnspan=3)
        algo = IntVar()

        MSE = Radiobutton(second_frame, text="MSE", variable=algo, value=1)
        MSE.select()
        MAE = Radiobutton(second_frame, text="MAE", variable=algo, value=2)
        RMSE = Radiobutton(second_frame, text="RMSE", variable=algo, value=3)
        btn = Button(second_frame, text='show algo',
                     command=lambda: choose_algo(slider_Test, slider_lamda))
        frame = Frame(second_frame)
        
        result_label = Label(
            frame, text="Result of algorithm", font=("Arial", 12))
        result = Label(frame, font=("Arial", 16))
        MSE.grid(row=5, column=2)
        MAE.grid(row=6, column=2)
        RMSE.grid(row=7, column=2)
        btn.grid(row=8, column=5)
        result_label.grid(row=1, column=1,columnspan=2)
        result.grid(row=1, column=3, columnspan=4)
        frame.grid(row=10, column=1,columnspan=5)
        second_frame.mainloop()


