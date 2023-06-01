
    # train_options=[0.5 , 0.6 , 0.7 , 0.8]
    # variable= StringVar(lr_screen)
    # variable.set(train_options[2])  # default value
    # OptionMenu(lr_screen, variable, *train_options)



#     def go_to_lr_screen(data):
#         lr_screen = Toplevel()
#         lr_screen.title("Preprocessing Data")
#         lr_screen.geometry("420x300")
#         print(data)
#         # LinearRegression.train_lr(data,lr_screen)
#         button = Button(lr_screen, text="Train" ,font=("bold", 15), width=15, borderwidth=0,bg="#C48189" ,fg="white",
#                     command=lambda: LinearRegression.train_lr(data,lr_screen)).place(x=70 , y=170)
#         test=Label(lr_screen,text="hello world")
#         test.pack()
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from sklearn import metrics

def fourth_win_LR(data):
    lr_screen = Toplevel()
    lr_screen.geometry("500x800")
    lr_screen.title("Linear Regression")


    ## label train size
    Label(lr_screen, text="Train Size  ", fg='#4863A0', font=3).place(x= 120 , y =100)

    w2 =  Scale(lr_screen, from_=0, to=10,
                            orient=HORIZONTAL, command=lambda value_test: value_test)
    w2.set(50)
    w2.place( x= 250 , y = 100)
    ######################## linear regression Code ######################
    def train_lr():
        X = data.iloc[:, :-1].values
        y = data.iloc[:, -1].values
        print(float(w2.get()/10))
        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=float(w2.get()/10), random_state=41)

        regressor = LinearRegression()
        regressor = regressor.fit(X_train, y_train)

        def test_lr():
            y_pred = regressor.predict(X_test)
            Label(lr_screen, text="Mean Squared  Error : ",font=("bold", 15), fg="green").place(x=50, y=230)
            Label(lr_screen, text=metrics.mean_squared_error(y_test, y_pred), font=("bold", 15)).place(x=250, y=230)

            errors = list()
            for i in range(len(y_test)):
                # calculate error
                err = (y_test[i] - y_pred[i]) ** 2
                # store error
                errors.append(err)
            fig = plt.figure(figsize=(5, 4), dpi=100)
            plt.plot(errors)
            plt.xticks(ticks=[i for i in range(len(errors))], labels=y_pred)
            plt.xlabel('Predicted Value')
            plt.ylabel('Mean Squared Error')

            canvas = FigureCanvasTkAgg(fig, lr_screen)
            canvas.draw()
            canvas.get_tk_widget().place(x=10, y=280)


        button = Button(lr_screen, text="Test", font=("bold", 15), width=15, borderwidth=0, bg="green", fg="white",
                        command=test_lr).place(x=260, y=170)

    button = Button(lr_screen, text="Train" ,font=("bold", 15), width=15, borderwidth=0,bg="green" ,fg="white",
                    command=train_lr).place(x=70 , y=170)


    lr_screen.mainloop()