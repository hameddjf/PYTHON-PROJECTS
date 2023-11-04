from tkinter import *
import random

class ColorPaletteGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title('Color Palette Generator')
        self.master.geometry('400x400')

        self.color_canvas = Canvas(self.master, bg='#FFFFFF', height=300, width=300)
        self.color_canvas.pack(pady=20)

        self.color_palette_button = Button(self.master, text='Generate', command=self.generate_palette)
        self.color_palette_button.pack(pady=10)

        self.palette_label = Label(self.master, text='Click "Generate" to create your own color palette')
        self.palette_label.pack()

        self.color_palette = None

    def generate_palette(self):
        palette = []
        for i in range(5):
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            palette.append(f'#{red:02x}{green:02x}{blue:02x}')

        self.color_palette = palette
        self.draw_palette()

    def draw_palette(self):
        self.color_canvas.delete('all')
        x = 0
        y = 0
        for color in self.color_palette:
            self.color_canvas.create_rectangle(x, y, x + 60, y + 60, fill=color)
            x += 70

        self.palette_label.config(text=f'Your color palette: {self.color_palette}')

if __name__ == '__main__':
    root = Tk()
    app = ColorPaletteGenerator(root)
    root.mainloop()