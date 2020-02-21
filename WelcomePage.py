from Tkinter import *
root = Tk()
Label(root,text="Project Title : Phonebook",font=("Comic Sans MS", "24", "bold"),fg="black").grid(row=0,column=100)
Label(root,text="Project of Python and Database",font=("Comic Sans MS", "24", "bold"),fg="black").grid(row=1,column=100)
Label(root,text="Developed by : Harshit Purwar",font=("Comic Sans MS", "24", "bold"),fg="blue").grid(row=2,column=100)
def close(e=1):
    root.destroy()
root.bind("<Motion>",close)
root.mainloop()
