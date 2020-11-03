#import libraries
from tkinter import messagebox
import pandas as pd
import list_Disease as l
import numpy as np
from tkinter import *
from sklearn import tree
from sklearn.metrics import accuracy_score
import os


# ---------------------TESTING DATA df -------------------------------------------------------------------------------------

#Read the train set
df = pd.read_csv("Training.csv")

#replace the disease with the interger value
df.replace({'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3,
                          'Peptic ulcer diseae': 4, 'AIDS': 5, 'Diabetes ': 6, 'Gastroenteritis': 7,
                          'Bronchial Asthma': 8, 'Hypertension ': 9,
                          'Migraine': 10, 'Cervical spondylosis': 11,
                          'Paralysis (brain hemorrhage)': 12, 'Jaundice': 13, 'Malaria': 14, 'Chicken pox': 15,
                          'Dengue': 16, 'Typhoid': 17, 'hepatitis A': 18,
                          'Hepatitis B': 19, 'Hepatitis C': 20, 'Hepatitis D': 21, 'Hepatitis E': 22,
                          'Alcoholic hepatitis': 23, 'Tuberculosis': 24,
                          'Common Cold': 25, 'Pneumonia': 26, 'Dimorphic hemmorhoids(piles)': 27, 'Heart attack': 28,
                          'Varicose veins': 29, 'Hypothyroidism': 30,
                          'Hyperthyroidism': 31, 'Hypoglycemia': 32, 'Osteoarthristis': 33, 'Arthritis': 34,
                          '(vertigo) Paroymsal  Positional Vertigo': 35, 'Acne': 36, 'Urinary tract infection': 37,
                          'Psoriasis': 38,
                          'Impetigo': 39}}, inplace=True)

#readt the list of Symptoms
X = df[l.l1]

#read the the progonisis
y = df["prognosis"]

#covert the array in continuous form
np.ravel(y)

# TRAINING DATA  in tr --------------------------------------------------------------------------------
tr = pd.read_csv("Testing.csv")
#replace all diseases in int format
tr.replace({'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3,
                          'Peptic ulcer diseae': 4, 'AIDS': 5, 'Diabetes ': 6, 'Gastroenteritis': 7,
                          'Bronchial Asthma': 8, 'Hypertension ': 9,
                          'Migraine': 10, 'Cervical spondylosis': 11,
                          'Paralysis (brain hemorrhage)': 12, 'Jaundice': 13, 'Malaria': 14, 'Chicken pox': 15,
                          'Dengue': 16, 'Typhoid': 17, 'hepatitis A': 18,
                          'Hepatitis B': 19, 'Hepatitis C': 20, 'Hepatitis D': 21, 'Hepatitis E': 22,
                          'Alcoholic hepatitis': 23, 'Tuberculosis': 24,
                          'Common Cold': 25, 'Pneumonia': 26, 'Dimorphic hemmorhoids(piles)': 27, 'Heart attack': 28,
                          'Varicose veins': 29, 'Hypothyroidism': 30,
                          'Hyperthyroidism': 31, 'Hypoglycemia': 32, 'Osteoarthristis': 33, 'Arthritis': 34,
                          '(vertigo) Paroymsal  Positional Vertigo': 35, 'Acne': 36, 'Urinary tract infection': 37,
                          'Psoriasis': 38,
                          'Impetigo': 39}}, inplace=True)

X_test = tr[l.l1]                               #features in X_test
y_test = tr[["prognosis"]]                      #labels in y_test
np.ravel(y_test)                                #convert the data in continues form

# --------------------------------------Decision tree algorithm------------------------------------------------------

def DecisionTree():

    l2 = []                                 #empty list for prediction
    for x in range(0, len(l.l1)):
        l2.append(0)

    clf3 = tree.DecisionTreeClassifier()
    #clf3 = tree.DecisionTreeClassifier(max_depth=100,min_samples_leaf=20,max_features=38)  # empty model of the decision tree

    clf3 = clf3.fit(X, y)                  #used to train the model

    # calculating accuracy-------------------------------------------------------------------

    #used to predict the class of the input set
    y_pred = clf3.predict(X_test)
    print(y_pred)
    print("accuracy Score: ")
    print(accuracy_score(y_test, y_pred))               #print the accuracy of the classifiaction
    print("Num of values classified: ")
    print(accuracy_score(y_test, y_pred, normalize=False))      #it return how many lables are classified suucessfully


    psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get()]            #contain list of symptoms

    if (Symptom1.get() != 'None' or Symptom2.get() != 'None' or Symptom3.get() != 'None') and NameEn.get():

                #-------------------------------------
                for k in range(0, len(l.l1)):

                    for z in psymptoms:
                        if (z == l.l1[k]):
                            l2[k] = 1

                inputtest = [l2]
                #print(inputtest)

                #predit the value entered by the user
                predictvalue = clf3.predict(inputtest)
                #print("predict =" + str(predictvalue))
                predicted = predictvalue[0]
                #print(predicted)

                h = 'no'
                for a in range(0, len(l.disease)):
                 if predicted == a:
                     #print("predicted ="+str(predicted))
                     h = 'yes'
                     break

                if h == 'yes':
                    t1.delete("1.0", END)
                    t1.insert(END, l.disease[a])
                else:
                    t1.delete("1.0", END)
                    t1.insert(END, "Not Found")
    else:
        msg = "Oops!!\nyou are missing something!!!\n please Enter the Name and Select the Symptoms"
        messagebox.showwarning("Warning!", msg,)

# ---------------------------------------Clear all-----------------------------------

def clear_all():
    # entry variables
    t1.delete(1.0, END)
    NameEn.delete(first=0, last='end')
    Symptom1.set(None)
    Symptom2.set(None)
    Symptom3.set(None)


#----------------------------infor of disease-----------------------------------------
def info():
    #os.system('scrapping.py')
    import scrapping
# ----------------------------------------------------GUI------------------------------

root = Tk()
root.title("Diseases Prediction and analysis")
root.configure(background="gray")
root.geometry("900x600+200+10")


# entry variables
Symptom1 = StringVar()
Symptom1.set(None)
Symptom2 = StringVar()
Symptom2.set(None)
Symptom3 = StringVar()
Symptom3.set(None)
Name = StringVar()



# font description
labelfont = ('times', 20, 'bold')

# Heading
w2 = Label(root, justify=LEFT, text="Disease Predictor using Machine Learning", fg="white", bg="gray")
w2.config(font=("Elephant", 30, 'bold'))
# w2.config(font=("Elephant"))
w2.grid(row=1, column=0, padx=250, pady=2, sticky=W)
# w2.config(font=("Aharoni", 30,'bold'))


# labels
NameLb = Label(root, text="Name of the Patient :", fg="black", bg="gray")
NameLb.grid(row=6, column=0, padx=20, pady=30, sticky=W)
NameLb.config(font=labelfont)

S1Lb = Label(root, text="Symptom 1: ", fg="black", bg="gray")
S1Lb.grid(row=7, column=0, padx=450, pady=20, sticky=W)
S1Lb.config(font=labelfont)

S2Lb = Label(root, text="Symptom 2: ", fg="black", bg="gray")
S2Lb.grid(row=8, column=0, padx=450, pady=20, sticky=W)
S2Lb.config(font=labelfont)

S3Lb = Label(root, text="Symptom 3:", fg="black", bg="gray")
S3Lb.grid(row=9, column=0, padx=450, pady=20, sticky=W)
S3Lb.config(font=labelfont)

# entries
OPTIONS = sorted(l.l1)

NameEn = Entry(root, textvariable=Name, width=40 ,bg="#FFEBEE")
NameEn.grid(row=6, column=0, padx=300, sticky=W)

# drop down options
S1En = OptionMenu(root, Symptom1, *OPTIONS)
S1En.grid(row=7, column=0, padx=650, sticky=W)


S2En = OptionMenu(root, Symptom2, *OPTIONS)
S2En.grid(row=8, column=0, padx=650, sticky=W)

S3En = OptionMenu(root, Symptom3, *OPTIONS)
S3En.grid(row=9, column=0, padx=650, sticky=W)


dst = Button(root, text="Click to Predict", bg="red", fg="white", command=DecisionTree,width="16",height="2",font=("arrial",10,"bold"))
dst.grid(row=19, column=0, padx=450, pady=40, sticky=W)

# ouput textfileds
t1 = Text(root, height=2, width=40, bg="#FFEBEE", fg="black",font=("arrial",13,"bold"))
t1.grid(row=19, column=0, padx=650, pady=40, sticky=W)

# clear all button
cls = Button(root, text="Clear All", command=clear_all, bg="red", fg="white",width="16",height="4",font=("arrial",12,"bold"))
cls.grid(row=24, column=0, padx=500, pady=70, sticky=W)


#---------------scrapping -----------------
# infoButton= Button(root, text="Information about\nDisease", command=info, bg="cyan", fg="black",width="16",height="4",font=("arrial",12,"bold"))
# infoButton.grid(row=24, column=0, padx=700, pady=70, sticky=W)
#

root.mainloop()


