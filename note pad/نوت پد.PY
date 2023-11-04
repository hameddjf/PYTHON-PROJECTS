import tkinter as tk

class Notepad(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Notepad")
        self.text_box = tk.Text(self, height=30, width=80)
        self.text_box.pack()
        
        self.menu_bar = tk.Menu(self)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Cut", command=self.cut)
        self.edit_menu.add_command(label="Copy", command=self.copy)
        self.edit_menu.add_command(label="Paste", command=self.paste)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        
        self.config(menu=self.menu_bar)
        
    def new_file(self):
        self.text_box.delete(1.0, tk.END)
        
    def open_file(self):
        file_path = tk.filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_box.delete(1.0, tk.END)
                self.text_box.insert(tk.END, content)
        
    def save_file(self):
        file_path = tk.filedialog.asksaveasfilename()
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_box.get(1.0, tk.END)
                file.write(content)
        
    def cut(self):
        self.text_box.event_generate("<<Cut>>")
        
    def copy(self):
        self.text_box.event_generate("<<Copy>>")
        
    def paste(self):
        self.text_box.event_generate("<<Paste>>")

app = Notepad()
app.mainloop()