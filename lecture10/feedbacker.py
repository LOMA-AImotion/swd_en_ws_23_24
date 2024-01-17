class Feedbacker: 
    def __init__(self) -> None:
        pass

    def positive(self):
        pass

    def negative(self):
        pass 

class PrintFeedbacker(Feedbacker):
    def positive(self):
        print("You did great!")

    def negative(self):
        print("Try again")

from tkinter import messagebox
class TkinterFeedbacker(Feedbacker):
    def positive(self):
        messagebox.showinfo("THI", "Great job!")

    def negative(self):
        messagebox.showerror("THI", "Try again!")

# this code is only executed when feedbacker.py is run directly, not
# when feedbacker is imported from another module
if __name__ == "__main__":
    if input("Use tkinter? (y|n)") == "y":
        my_feedbacker = TkinterFeedbacker()
    else:
        my_feedbacker = PrintFeedbacker()
        
    answer = int(input("What is 2+2?"))
    if answer == 4:
        my_feedbacker.positive()
    else:
        my_feedbacker.negative() 