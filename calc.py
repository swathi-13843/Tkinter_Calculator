import tkinter as tk
root=tk.Tk()
root.title("Calculator")
root.geometry("450x600")
root.resizable(True,True)
entry1=tk.Entry(root,font=("bold",20),bg="black",fg="white",bd=0,justify="right")
entry1.grid(row=0,column=0,columnspan=4,padx=12,pady=12,ipady=10)
buttons=["7","8","9","/",
         "4","5","6","*",
         "1","2","3","-",
         "0",".","=","+"]
def press(v):
    entry1.insert(tk.END,v)
def clear():
    entry1.delete(0,tk.END)
def cal():
    try:
        res=eval(entry1.get())
        entry1.delete(0,tk.END)
        entry1.insert(0,res)
    except:
        entry1.delete(0,tk.END)
        entry1.insert(0,"error")
r=1
c=0
for i in buttons:
    cmd=cal if i=="=" else lambda x=i: press(x)
    tk.Button(root,font=("bold",20),text=i,command=cmd,bg="blue" if i in "+-/*=" else "green",bd=0,fg="white",width=5,height=2).grid(row=r,column=c,columnspan=1,padx=2,pady=2)
    c+=1
    if c==4:
        c=0
        r+=1
tk.Button(root,font=("bold",20),text="C",
          command=clear,bg="red",fg="white",bd=0,width=5,height=2).grid(row=r,column=c,columnspan=1,padx=6,pady=6)
          
root.mainloop()

