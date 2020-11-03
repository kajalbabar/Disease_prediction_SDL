import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox



#TAKE TWO EMPTY STRINGS
str1=""
str2 =""

try:
    url = "https://en.wikipedia.org/wiki/Gastroesophageal_reflux_disease"
    page = requests.get(url)
    print(page.status_code)
    soup = BeautifulSoup(page.content, 'html.parser')

    tb = soup.find('div', class_='mw-parser-output')

    for link in tb.find_all('p'):
        str1 = str1 + link.get_text()
        #print(name.get_text('title'))
        #print(str1)

    i=1
    while str1[i] != '\n':
        str2 = str2 +str1[i];
        i +=1

    #user interface----------
    root = Tk()
    root.title("Diseases Prediction and analysis")
    root.geometry("500x200+200+10")
    # info = Text(root, fg='black', height=200, width=500, font=('arrial', 12, "bold"))
    # info.insert(END, str2)
    # info.pack()
    t1 = Text(root, height=200, bg="#FFEBEE", fg="black", font=("arrial", 13, "bold"))
    t1.grid(row=19, column=0)
    t1.insert(1.0,str2)
    root.mainloop()



except requests.exceptions.ConnectionError:
        errMsg= "Please check your internet connection"
        messagebox.showerror("ERROR", errMsg)

#
