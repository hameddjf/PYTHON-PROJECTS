from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # display
        self.display = Entry(master, width=25, justify=RIGHT, font=('Arial', 14))
        self.display.grid(row=0, column=0, columnspan=4, pady=5)

        # Buttons
        buttons = {
            '7': (1, 0), '8': (1, 1), '9': (1, 2), '/': (1, 3),
            '4': (2, 0), '5': (2, 1), '6': (2, 2), '*': (2, 3),
            '1': (3, 0), '2': (3, 1), '3': (3, 2), '-': (3, 3),
            'C': (4, 0), '0': (4, 1), '=': (4, 2), '+': (4, 3)
        }

        # create button in GUI
        for button in buttons:
            # looping for all buttons in 'buttons' and Assigned them to row , col
            row, col = buttons[button] 
            # created btn by Button class                                        # for any btn is defined command when they push are called
            btn = Button(master, text=button, width=5, height=2, font=('Arial', 14), command=lambda x=button:self.button_click(x))
            # added the btn with grid
            btn.grid(row=row, column=col, padx=3, pady=3)

    # when clicked(pushed) buttons = changed them
    def button_click(self, text):
        if text == 'C':
            self.display.delete(0, END)
        elif text == '=':
            try: #try Perform mathematical operations = by result
                result = eval(self.display.get())
                self.display.delete(0, END)
                self.display.insert(0, str(result))
            except: # Error display / displaying Error
                self.display.delete(0, END)
                self.display.insert(0, 'Error')
        else:
            self.display.insert(END, text)

root = Tk()
calculator = Calculator(root)
root.mainloop()