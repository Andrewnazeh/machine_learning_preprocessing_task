from tkinter import*
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# class Svm:
#     def go_to_svm_screen(data):
#         svm_screen = Toplevel()
#         svm_screen.title("Preprocessing Data")
#         svm_screen.geometry("420x300")
#         print(data)

#         test=Label(svm_screen,text="hello world")
#         test.pack()

def fourth_win_svm(data):
    root = Toplevel()
    root.geometry("500x500")
    root.title("SVM")
    print(data)
    ## label 1 option
    Label(root, text="Kernal", fg='#4863A0', font=3).place(x= 150 , y =30)
    options=["linear","rbf"]
    variable_1 = StringVar(root)
    variable_1.set(options[0])  # default value
    w1 = OptionMenu(root, variable_1, *options)
    w1.place( x= 250 , y = 30)

    ## label 2 train size
    Label(root, text="Train Size  ", fg='#4863A0', font=3).place(x= 120 , y =100)
    train_options=[0.5 , 0.6 , 0.7 , 0.8]
    variable_2= StringVar(root)
    variable_2.set(train_options[2])  # default value
    w2 = OptionMenu(root, variable_2, *train_options)
    w2.place( x= 250 , y = 100)
    ######################## SVM Code ######################
    def train_svm():
       

        # data = pd.read_csv(datapath)
        X = data.iloc[:, :-1].values
        y = data.iloc[:, -1].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=float(variable_2.get()), random_state=41)
        clf = SVC(kernel=variable_1.get())
        clf = clf.fit(X_train, y_train)
        def test_svm():
            y_pred = clf.predict(X_test)
            # confusion matrix
            from sklearn.metrics import confusion_matrix
            Label(root, text="Confusion Matrix : ", font=("bold", 15), fg="green").place(x=50, y=220)
            Label(root, text=confusion_matrix(y_pred, y_test), font=("bold", 15)).place(x=230, y=220)
            # Import scikit-learn metrics module for accuracy calculation
            from sklearn import metrics
            Label(root, text="Accuracy : ",font=("bold", 15), fg="green").place(x=50, y=300)
            Label(root, text=metrics.accuracy_score(y_test, y_pred), font=("bold", 15)).place(x=170, y=300)
            Label(root, text="Precition : ", font=("bold", 15), fg="green").place(x=50, y=350)
            Label(root, text=metrics.precision_score(y_test, y_pred), font=("bold", 15)).place(x=170, y=350)
            Label(root, text="F1 score : ", font=("bold", 15), fg="green").place(x=50, y=400)
            Label(root, text=metrics.f1_score(y_test, y_pred), font=("bold", 15)).place(x=170, y=400)
            Label(root, text="Recall    : ", font=("bold", 15), fg="green").place(x=50, y=450)
            Label(root, text=metrics.recall_score(y_test, y_pred), font=("bold", 15)).place(x=170, y=450)


        button = Button(root, text="Test", font=("bold", 15), width=15, borderwidth=0, bg="green", fg="white",
                        command=test_svm).place(x=260, y=170)

    button = Button(root, text="Train" ,font=("bold", 15), width=15, borderwidth=0,bg="green" ,fg="white",
                    command=train_svm).place(x=70 , y=170)


    root.mainloop()


