# Create a num-pad from 1 to 9 arranged
# in a 3x3 grid - each digit represented by a button 
import tkinter
from tkinter import messagebox 
from functools import partial

main_win = tkinter.Tk()
number = 1 

def present_number(number):
    messagebox.showinfo("THI", f"Button {number} clicked")

for i in range(3):
    for j in range(3):
        text_label = i*3 + 1 + j
        button = tkinter.Button(main_win, command = partial(present_number, text_label) )
        button.config(width=10, height=5)
        button.grid(row = i, column=j)
        #button.config(text=number)
        button.config(text=text_label)
        number += 1
        
        

main_win.mainloop()