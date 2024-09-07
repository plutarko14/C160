from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox
import os

root=Tk()
root.minsize(500, 500)
root.maxsize(1000, 1000)
openimg=ImageTk.PhotoImage(Image.open("open.jpg"))
save=ImageTk.PhotoImage(Image.open("save.jpg"))
exitimg=ImageTk.PhotoImage(Image.open("exit.jpg"))



labelfilename=Label(root, text="archivo")
labelfilename.place(relx=0.3, rely=0.2, anchor=CENTER)
inputfilename=Entry(root)
inputfilename.place(relx=0.5, rely=0.2, anchor=CENTER)
mytext=Text(root, height=30, width=80)
mytext.place(relx=0.5, rely=0.6, anchor=CENTER)
name=""
def abrir():
    global name
    mytext.delete(1.0, END)
    inputfilename.delete(0, END) 
    text_file = filedialog.askopenfilename(title = "Abrir el archivo de texto", filetypes=(("Archivos de texto", "*.txt*"),))
    print(text_file)
    name = os.path.basename(text_file)
    formatted_name = name.split('.')[0] 
    inputfilename.insert(END, formatted_name)
    root.title(formatted_name) 
    text_file = open(name, 'r') 
    paragraph = text_file.read() 
    mytext.insert(END, paragraph) 
    text_file.close()

def guardar():
    inputname=inputfilename.get()
    file=open(inputname+".txt", "w")
    data=mytext.get("1.0",END)
    print(data)
    file.write(data)
    inputfilename.delete(0,END)
    mytext.delete(1.0, END)
    messagebox.showinfo("Actualizacion","Exitosa")
    
def salir():
   root.destroy()    
   
btn1=Button(root, image=openimg, command=abrir)
btn2=Button(root, image=save, command=guardar)
btn3=Button(root, image=exitimg, command=salir)
btn1.place(relx=0.1, rely=0.1, anchor=CENTER)
btn2.place(relx=0.3, rely=0.1, anchor=CENTER)
btn3.place(relx=0.5, rely=0.1, anchor=CENTER)
    
root.mainloop()