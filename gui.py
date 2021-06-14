from tkinter import *
from tkinter import messagebox
import tkinter as tk
from regex import reg

root = Tk()
root.geometry("800x500")
root.title("regex tool")

def clear():
    data.delete("1.0","end")
    regex.delete("1.0","end")

def email():
    regex.delete("1.0","end")
    email_regx = "[a-zA-Z0-9-_.]+[@][a-zA-Z]+[.][a-zA-Z]+"
    regex.insert(END, email_regx)
def number():
    regex.delete("1.0","end")
    number_regx = "[789]\d{9}" # for india only
    regex.insert(END,number_regx)

def welcomeMessage():
    return messagebox.showinfo('message',"Please check your regular expression again!")

def run():
    try:
        obj_reg = regex.get("1.0","end - 1c")
        obj_data = data.get("1.0","end - 1c")
        obj = reg(obj_reg,obj_data)
        ret = obj.find_all()
        out.delete("1.0","end")
        out.insert(END, ret)
    except Exception as e:
        welcomeMessage()
        print(e)

emailButton = Button(root,text = "Email",padx = 25,pady = 5,command = email)
emailButton.grid(row = 0,column = 1,pady = 5)
mobileButton = Button(root,text = "Mobile-No",padx = 25,pady = 5,command = number)
mobileButton.grid(row = 0,column = 2,pady = 5)


regex_label = Label(root,text = "Regular Expression:")
regex_label.grid(row = 1,column = 0,pady = 5)
regex = Text(root, height = 1,width = 50,font=("Times", 14))
regex.grid(row = 1,column = 1,columnspan=2,pady = 5)


data_label = Label(root,text = "Texts:")
data_label.grid(row = 2,column = 0,pady = 5)
data = Text(root, height = 8, width = 50,font=("Times", 14))
data.grid(row = 2,column = 1,columnspan=2,pady = 5)
# def demo():
#    T.insert(END, regex.get())
#    print(T.get("1.0","end - 1c"))



runButton = Button(root,text = "Run",padx = 25,pady = 5,command = run)
runButton.grid(row = 3,column = 1)
clearButton = Button(root,text = "Clear",padx = 25,pady = 5,command = clear)
clearButton.grid(row = 3,column = 2)

out_label = Label(root,text = "Output:")
out_label.grid(row = 4,column = 0,pady = 5)
out = Text(root, height = 8, width = 50,font=("Times", 14))
out.grid(row = 4,column = 1,columnspan=2,pady = 5)

# def save():
#     pass
# save = Text(root,height = 1, width = 20)
# save.grid(row = 5,column = 0)
# save_button = Button(root,text = "Save",padx = 25,pady = 5,command = save)
# save_button.grid(row = 5,column = 1)
root.mainloop()