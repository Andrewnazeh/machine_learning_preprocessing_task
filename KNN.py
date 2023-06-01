from tkinter import*



# class Knn:
#     def go_to_knn_screen(data):
#         svm_screen = Toplevel()
#         svm_screen.title("Preprocessing Data")
#         svm_screen.geometry("420x300")
#         print(data)

#         test=Label(svm_screen,text="hello world")
#         test.pack()


from tkinter import *
def fourth_win_knn(data):
    root = Tk()
    root.geometry("900x650")
    root.title("KNN")
    ## label 1 entry
    Label(root, text="n_neighbors", fg='#4863A0', font=3).place(x= 220 , y =20)
    entry = Entry(root, bg="white")
    entry.place( x= 350 , y = 20)
    ## label 2 option
    Label(root, text="Distance Metric", fg='#4863A0', font=3).place(x= 150 , y =60)
    options=['euclidean','manhattan','minkowski']
    variable_1 = StringVar(root)
    variable_1.set(options[0])  # default value
    w1 = OptionMenu(root, variable_1, *options)
    w1.place( x= 350 , y = 60)
    ## label 3 train size
    Label(root, text="Train Size  ", fg='#4863A0', font=3).place(x= 220 , y =100)
    train_options=[0.5 , 0.6 , 0.7 , 0.8]
    variable_2= StringVar(root)
    variable_2.set(train_options[2])  # default value
    w2 = OptionMenu(root, variable_2, *train_options)
    w2.place( x= 350 , y = 100)

    ######################## KNN Code ######################
    def train_knn():
        ## check if the user didn't enter the n_neighbour
        if not entry.get() or int(entry.get()) == 0:
            label = Label(root, text='Input Required', fg='red')
            label.place(x=250, y=65)
            root.after(5000, lambda: label.destroy())
        else:               ## KNN
            import pandas as pd
            from sklearn.neighbors import KNeighborsClassifier

            # data = pd.read_csv(datapath)
            x = data.drop(['outcome'], axis=1)
            y = data['outcome']

            from sklearn.model_selection import train_test_split
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=float(variable_2.get()), random_state=1)
            knn = KNeighborsClassifier(n_neighbors=int(entry.get()), metric=variable_1.get())
            knn.fit(x_train, y_train)
            y_pred = knn.predict(x_test)
            def test_knn():
                # confusion matrix
                from sklearn.metrics import confusion_matrix
                Label(root, text="Confusion Matrix : ", font=("bold", 15), fg="green").place(x=50, y=250)
                Label(root, text=confusion_matrix(y_pred, y_test), font=("bold", 15)).place(x=230, y=250)
                # Import scikit-learn metrics module for accuracy calculation
                from sklearn import metrics
                Label(root, text="Accuracy : ", font=("bold", 15), fg="green").place(x=50, y=320)
                Label(root, text=metrics.accuracy_score(y_test, y_pred), font=("bold", 15)).place(x=170, y=320)
                Label(root, text="Precition : ", font=("bold", 15), fg="green").place(x=50, y=370)
                Label(root, text=metrics.precision_score(y_test, y_pred), font=("bold", 15)).place(x=170, y=370)
                Label(root, text="F1 score : ", font=("bold", 15), fg="green").place(x=50, y=420)
                Label(root, text=metrics.f1_score(y_test, y_pred), font=("bold", 15)).place(x=170, y=420)
                Label(root, text="Recall    : ", font=("bold", 15), fg="green").place(x=50, y=470)
                Label(root, text=metrics.recall_score(y_test, y_pred), font=("bold", 15)).place(x=170, y=470)
                ### Error Rate PLot
                import numpy as np
                import matplotlib.pyplot as plt
                from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
                error_rate = []
                for i in range(1, 40):
                    knn = KNeighborsClassifier(n_neighbors=i)
                    knn.fit(x_train, y_train)
                    pred_i = knn.predict(x_test)

                    error_rate.append(np.mean(pred_i != y_test))

                fig=plt.figure(figsize=(5,4), dpi=100)
                plt.plot(range(1, 40), error_rate, color='blue', linestyle='--', markersize=10, markerfacecolor='red',
                         marker='o')
                plt.title('k versus Error rate')
                plt.xlabel('k')
                plt.ylabel('Error rate')

                canvas = FigureCanvasTkAgg(fig, root)
                canvas.draw()
                canvas.get_tk_widget().place(x=420, y=220)


            button = Button(root, text="Test", font=("bold", 15), width=15, borderwidth=0, bg="green", fg="white",
                            command=test_knn).place(x=360, y=170)

    button = Button(root, text="Train", font=("bold", 15), width=15, borderwidth=0, bg="green", fg="white",
                        command=train_knn).place(x=170, y=170)

    root.mainloop()

