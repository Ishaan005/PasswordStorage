import tkinter as tk
from tkinter import *
from tkinter import messagebox
import csv
import sys

def readFile():
    with open("passwords.csv", "r") as f:
        passwordFile = f.readlines()
        list1 = []
        for item in passwordFile[1:]:
            item = item.strip().split(",")
            list1.append(item)
        #print(list1)
        
    passwords = {}
    
    for list in list1:
        passwords.update({list[0]:list[1]})
    return passwords

print("passwordsDict: ", readFile())

def search():
    userInput = input("Enter App name: ")
    passwordDict = readFile()
    if userInput in passwordDict:
        return passwordDict[userInput]
    else:
        return ("Password not found")
    
#print(search())

def storeNew():
    appInput = input("Enter App name: ")
    passwordInput = input("ENter password")
    

    with open("passwords.csv", "a", newline = "") as f:
        writer = csv.writer(f)
        writer.writerow([appInput, passwordInput])
        
#storeNew()
#print(readFile())

#print(search())

##        Pasword Entry Window        ##
password = "123"
def check_password():
    entered_password = password_entry.get()

    # You can perform your password validation logic here
    # For example, you can compare the entered password with a predefined one
    if entered_password == password:
        messagebox.showinfo("Success", "Access granted!")
        
        next_window = tk.Toplevel()
        next_window.title("Next Page")

        #window.withdraw()
    else:
        messagebox.showerror("Error", "Incorrect password!")
        
        
# Create the main window
window = Tk()
window.title("Password Entry")
window.config(bg = "#D6D6D6")
window.geometry("300x300")
window.pack_propagate(0)


#Initialise frame
frame = Frame(window, width = 400, height = 25, bg = "#02699C")
frame.grid(row = 0, column = 1, padx = 10, pady = 10)
frame.pack_propagate(0)
frame.pack()

# Create a label widget
label = Label(frame, text="Password Storage!", bg = "#02699C",fg ="white" )

label.pack()

pass_frame = Frame(window)
pass_frame.pack()

#Password field
password_entry = Entry(pass_frame)
password_entry.pack()

# Create a button to check the password
check_button = Button(pass_frame, text="Check Password", command=check_password)
check_button.pack()

# Start the Tkinter event loop
window.mainloop()

        

        
        

    
    



