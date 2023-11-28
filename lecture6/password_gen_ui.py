import tkinter
from password_gen import generate_password

main_win = tkinter.Tk()
label = tkinter.Label(main_win)
label.pack()

def gen_new_password():
    password = generate_password()
    label.config(text=password)

next_pw_button = tkinter.Button(main_win,
                                text="Another password?",
                                command=gen_new_password)
next_pw_button.pack()

main_win.mainloop()
