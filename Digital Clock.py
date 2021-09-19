#clock in python
from tkinter import *
from tkinter.ttk import *
from time import strftime

def clocktime1():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,clocktime1)
    

root=Tk()

Clock1 = Label(root, text = " India Standard Time Clock")
Clock1.pack()
Clock1.config(font =( 14))

root.title("Digital Clock")
label =Label(root,font=("ds-digital",100),background ="black",foreground="cyan")
label.pack(anchor='center')
clocktime1()


mainloop()

  

  




  

  
