import tkinter as tk

def draw_trees():
    # دریافت تعداد درختان
    how_many_trees = int(entry_trees.get())
    # دریافت ارتفاع درخت
    tall_tree = int(entry_tall.get())

    # حذف محتوای پنجره
    canvas.delete("all")

    # متغیر شمارنده
    tree_count = how_many_trees - 1
    # ساخت فاصله
    spaces = tall_tree - 1

    # تعداد درختان نباید صفر باشد
    while how_many_trees != 0:
        # متغیر برای نمایش درخت
        hashs = 1

        x = 0
        y = 0

        # حلقه شمارنده درختان
        for i in range(tree_count):
            # حلقه شمارنده فاصله
            for j in range(spaces):
                canvas.create_text(x, y, text=" ", anchor="nw")
                x += 10

            # حلقه شمارنده نمایش
            for k in range(hashs):
                canvas.create_text(x, y, text="#", anchor="nw")
                x += 10

            # رفتن به خط بعدی
            x = 0
            y += 20

            # کاهش ارتفاع درخت
            tall_tree -= 1
            # کاهش فاصله
            spaces -= 1
            # افزایش نماد نمایش درخت
            hashs += 2

        # برگشت فاصله خالی به حالت اولیه
        spaces += tree_count

        # ساخت تنه درخت
        for i in range(spaces):
            canvas.create_text(x, y, text=" ", anchor="nw")
            x += 10
        canvas.create_text(x, y, text="#", anchor="nw")
        x = 0
        y += 20

        # کاهش تعداد درختان
        how_many_trees -= 1

    # تغییر اندازه پنجره بر اساس ارتفاع درخت
    window.geometry(f"{tall_tree * 10}x{y}")

# ایجاد پنجره
window = tk.Tk()
window.title("نمایش درختان")
window.geometry("400x200")

# ایجاد برچسب و ورودی برای تعداد درختان
label_trees = tk.Label(window, text=":ارتفاع درخت")
label_trees.pack()
entry_trees = tk.Entry(window)
entry_trees.pack()

# ایجاد برچسب و ورودی برای ارتفاع درخت
label_tall = tk.Label(window, text=":فاصله عرضی")
label_tall.pack()
entry_tall = tk.Entry(window)
entry_tall.pack()

# ایجاد دکمه برای نمایش درختان
button_draw = tk.Button(window, text="نمایش درخت", command=draw_trees)
button_draw.pack()

# ایجاد کانواس برای نمایش درختان
canvas = tk.Canvas(window, width=400, height=200)
canvas.pack()

# نمایش پنجره
window.mainloop()