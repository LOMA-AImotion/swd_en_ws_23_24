import tkinter

main_win = tkinter.Tk()
main_win.title("THI SWD-EGM Class of 23")
label = tkinter.Label(main_win, text="Hi EGM students")
#label.pack() # actually place the widgeht
label.grid(row=0, column=0)

button = tkinter.Button(main_win, text="Servus")
button.grid(row=1, column=1)
#button.pack()

# to make it visible - check for IPads
main_win.mainloop()