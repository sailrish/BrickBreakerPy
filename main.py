# pygame
from tkinter import *
import tkinter.messagebox
root=Tk()
root.title("Tic Tac Toe")
click=True
def check(buttons):
    global click
    if buttons["text"]=="" and click==True:
        buttons["text"]="X"
        click=False
    elif buttons["text"]=="" and click==False:
        buttons["text"]="O"
        click=True
    elif(button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X"
         or button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X"
         or button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X"
         or button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X"
         or button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X"
         or button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X"
         or button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X"
         or button7["text"]=="X" and button5["text"]=="X" and button3["text"]=="X"):
         tkinter.messagebox.showinfo("WINNER X","YOU WON")
    elif(button1["text"]=="O" and button2["text"]=="" and button3["text"]=="O"
         or button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O"
         or button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O"
         or button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O"
         or button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O"
         or button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O"
         or button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O"
         or button7["text"]=="O" and button5["text"]=="O" and button3["text"]=="O"):
         tkinter.messagebox.showinfo("WINNER 0","YOU WON")
buttons=StringVar()
button1=Button(root,text="",font=("arial",40,"bold"),height=2,width=4,command=lambda:check(button1))
button1.grid(row=0,column=0,stick=W)
button2=Button(root,text="",font=("arial",40,"bold"),height=2,width=4,command=lambda:check(button2))
button2.grid(row=0,column=1,stick=W)
button3=Button(root,text="",font=("arial",40,"bold"),height=2,width=4,command=lambda:check(button3))
button3.grid(row=0,column=2,stick=W)
button4=Button(root,text="",font=("arial",40,"bold"),height=2,width=4,command=lambda:check(button4))
button4.grid(row=1,column=0,stick=W)
button5=Button(root,text="",font=("arial",40,"bold"),height=2,width=4,command=lambda:check(button5))
button5.grid(row=1,column=1,stick=W)
button6=Button(root,text="",font=("arial",40,"bold"),height=2,width=4,command=lambda:check(button6))
button6.grid(row=1,column=2,stick=W)
button7=Button(root,text="",font=("arial",40,"bold"),height=2,width=4,command=lambda:check(button7))
button7.grid(row=2,column=0,stick=W)
button8=Button(root,text="",font=("arial",40,"bold"),height=2,width=4,command=lambda:check(button8))
button8.grid(row=2,column=1,stick=W)
button9=Button(root,text="",font=("arial",40,"bold"),height=2,width=4,command=lambda:check(button9))
button9.grid(row=2,column=2,stick=W)
root.mainloop()


    
