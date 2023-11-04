# دریافت تعداد درختان
how_many_trees = int(input('تعداد درختان را وارد کنید: '))
# دریافت ارتفاع درخت
tall_tree = int(input('ارتفاع درخت را وارد کنید: '))

# متغیر شمارنده
tree_count = how_many_trees - 1
# ساخت فاصله
spaces = tall_tree - 1

# تعداد درختان نباید صفر باشد
while how_many_trees != 0:
    # متغیر برای نمایش درخت
    hashs = 1
    
    # حلقه شمارنده درختان
    for i in range(tree_count):
        # حلقه شمارنده فاصله
        for j in range(spaces):
            print(' ', end='')

        # حلقه شمارنده نمایش
        for k in range(hashs):
            print('#', end='')
        
        # رفتن به خط بعدی
        print()
        
        # کاهش ارتفاع درخت
        tall_tree -= 1
        # کاهش فاصله
        spaces -= 1
        # افزایش نماد نمایش درخت
        hashs += 2 
    
    # برگشت فاصله خالی به حالت اولیه
    spaces += tree_count
    # کاهش تعداد درختان
    how_many_trees -= 1
    
    # ساخت تنه درخت
    for i in range(spaces):
        print(' ', end='')
    print('#')
    print()