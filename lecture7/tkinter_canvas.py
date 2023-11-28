import tkinter
main_win = tkinter.Tk()
canvas = tkinter.Canvas(main_win, width=800, height=600)
canvas.grid(columnspan=3, rowspan=5)

label = tkinter.Label(main_win, text="Hi EGM students")
#label.pack() # actually place the widgeht
label.grid(row=2, column=1)

main_win.mainloop()