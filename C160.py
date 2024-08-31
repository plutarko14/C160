from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.minsize(500, 500)
root.maxsize(1000, 1000)
open=ImageTk.PhotoImage(Image.open("open.jpg"))
save=ImageTk.PhotoImage(Image.open("save.jpg"))
exit=ImageTk.PhotoImage(Image.open("exit.jpg"))

btn1=Button(root, image=open)
btn2=Button(root, image=save)
btn3=Button(root, image=exit)
btn1.place(relx=0.1, rely=0.1, anchor=CENTER)
btn2.place(relx=0.3, rely=0.1, anchor=CENTER)
btn3.place(relx=0.5, rely=0.1, anchor=CENTER)

root.mainloop()