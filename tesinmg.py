import tkinter as tk
from tkinter import simpledialog


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.withdraw()  # Hide the main Tkinter window
        self.amount = None
        self.popup()

    def popup(self):
        self.amount = simpledialog.askfloat("Input", "Enter the amount", minvalue=0)
        self.quit()

    def get_amount(self):
        return self.amount

app = Application()
app.mainloop()  # mainloop must be called to handle events
number = app.get_amount()
print(number)
