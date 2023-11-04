import tkinter as tk
from math import sqrt

class Calculator(tk.Tk):
    
    def __init__(self):  
        super().__init__()
        self.title("ماشین حساب")
        self.display = tk.Entry(self, width=50, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        self.buttons = [
            "C", "√", "⌫", "/",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            ".", "0", "^", "="
        ]
        
        self.current_button = ""  
        
        self.create_buttons()
        
    def create_buttons(self):
        row = 1
        column = 0
        for button in self.buttons:
            if button == "C":
                command = self.clear_display
            elif button == "√":
                command = self.calculate_square_root
            elif button == "⌫":
                command = self.delete_last_character
            elif button == "=":
                command = self.calculate_answer
            elif button == "^":
                command = self.calculate_power
            else:
                command = lambda button=button: self.add_to_display(button)  
            tk.Button(self, text=button, width=10, height=5, command=command)\
                .grid(row=row, column=column, padx=5, pady=5)
            if column < 3:
                column += 1
            else:
                column = 0
                row += 1
                
    def add_to_display(self, button):  
        self.current_button = button  
        self.display.insert(tk.END, str(self.current_button))
        
    def clear_display(self):
        self.display.delete(0, tk.END)
        
    def delete_last_character(self):
        self.current_display = self.display.get()[:-1]
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current_display)
        
    def calculate_square_root(self):
        self.current_display = self.display.get()
        self.result = sqrt(float(self.current_display))
        self.display.delete(0, tk.END)
        self.display.insert(0, self.result)
        
    def calculate_answer(self):
        self.current_display = self.display.get()
        self.result = eval(self.current_display)
        self.display.delete(0, tk.END)
        self.display.insert(0, self.result)
        
    def calculate_power(self):
        self.current_display = self.display.get()
        self.result = float(self.current_display) ** 2
        self.display.delete(0, tk.END)
        self.display.insert(0, self.result)

app = Calculator()
app.mainloop()