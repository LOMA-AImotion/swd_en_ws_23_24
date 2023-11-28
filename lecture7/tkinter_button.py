import tkinter
# although I expect tkinter.messagebox to work, it doesn't
# I have to import it explicitly!
from tkinter import messagebox

main_win = tkinter.Tk()
main_win.title("THI SWD-EGM Class of 23")
label = tkinter.Label(main_win, text="Hi EGM students")
label.grid(row=0, column=0)


button = tkinter.Button(main_win, text="Servus")
button.grid(row=1, column=1)

def say_hi():
    print("Hi, EGM Students")
    tkinter.messagebox.showinfo("Hi", "Hi students")
    button.config(text="OK Goodbye")
    
    #tkinter.messagebox.showerror("Hi", "This was not correct!")
    #tkinter.messagebox.showwarning("Hi", "Beware of the SWD exam!")
button.config(command=say_hi )
# to make it visible - check for IPads
main_win.mainloop()