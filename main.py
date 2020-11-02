from tkinter import *
from recognizer import *
root= Tk()
root.title('face recognizer')
b=Label(root,text='Finds_Who')
b.config(font=("Courier", 22))
b.grid(row=0,column=0)
for i in range(2):
    s1=Label(root,text='\n')
    s1.grid(row=i+1,column=0)

def click():
    global lb
    recognizer()
    lb.pack_forget()
    l=Label(status, text='scan completed')
    l.grid(row=0, column=0)
    inverse = {v: k for k, v in names.items()}
    h = 0
    for i in names.values():
        if h < i:
            h = i
    for i in range(1):
        s1 = Label(root, text='\n')
        s1.grid(row=i + 7, column=0)
    result = LabelFrame(root, text='result', padx=100, pady=50)
    result.grid(row=8, column=0, padx=5, pady=5)
    l = Label(result, text='you are '+inverse[h])
    l.config(font=("Courier", 12))
    l.grid(row=0, column=0)

b = Button(root, text='click to find who', command=click, padx=60, pady=40)
b.grid(row=3, column=0, padx=20)

status = LabelFrame(root, text='status', padx=100, pady=50)
status.grid(row=6, column=0, padx=5, pady=5)
m='READY FOR YOUR COMMAND!!!'
lb=Label(status, text=m)
lb.grid(row=0, column=0)


for i in range(2):
    s1=Label(root,text='\n')
    s1.grid(row=i+4,column=0)
mainloop()