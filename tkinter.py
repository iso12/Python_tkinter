import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('IQ')
        self.geometry('500x300')

        self.Label = ttk.Label(self, text='uran')
        self.Button_1 = ttk.Button(self, text='run')
        self.Button_2 = ttk.Button(self, text='stop')
        self.Button_1['command'] = self.button_clicked
        self.Button_2['command'] = self.button_clicked_2

        self.Label.pack()
        self.Button_1.pack()
        self.Button_2.pack()

    def button_clicked(self):
        showinfo(title='info', message='-------')

    def button_clicked_2(self):
        showinfo(title='info', message='########')

if __name__=="__main__":
    app = App()
    app.mainloop()
