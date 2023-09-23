import os
import sys

class Prog:
    def __init__(self) -> None:
        self.age = 22
        self.ismaried = 3
        self.result = self.age + self.ismaried
        print(self.result)
        print("############################")

    def mainloop(self):
        pass 


if __name__ == "__main__":
    prog = Prog()
    prog.mainloop()



#-------------------------------------------------------------
class App:
    def __init__(self):
        numbers = int(input())
        if numbers < -5:
            print('low')
        elif -5 <= numbers <= 4:
            print('low')
        else:
            print('hif')

    def mainloop(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()

#----------------------------------------------------
language = str(input())
if language == "english":
    print("hi")
elif language == "german":
    print("hallo")
else:
    print("privet")
#-----------------------------------------------------

age = 22
isMarried = False
result = age > 21 or isMarried
print(result)

message = "ismayil net"
person2 = "ismayil"
print(person2 in message)

#######################################333
from ast import Num
import os
import sys

number = 1

while number < 5:
    print(f"number = {number}")
    number += 1

print("................")

message = "hello"

for c in message:
    print(c)

number = 1
number_2 = 2

while number < 10:
    print(number * number_2, end="\t")
    number_2 += 1

    from tkinter2 import *


# ------------------------------------------
def app(Self):
    Self.root = Tk()
    # root.geometry("500x300")
    Self.root.minsize(500, 250)
    Self.root.maxsize(500, 300)
    Self.root.title("FRİTL")
    Self.root.resizable(False, False)
    Self.root.mainloop()


# -------------------------------------------

import tkinter2 as tk
from tkinter2 import ttk
from tkinter2.messagebox import showinfo


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('My Awesome App')
        self.geometry('300x50')


if __name__ == "__main__":
    app = App()
    app.mainloop()







