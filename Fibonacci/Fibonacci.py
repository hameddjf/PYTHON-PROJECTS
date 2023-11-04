def fib_list(max):
    num = []
    a, b = 0, 1
    while len(num) < max:
        num.append(b)
        a, b = b, a + b
    return num


print(fib_list(10))  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def fib_generator(max):
    x = 0
    y = 1
    count = 0
    while count < max:
        x, y = y, x + y
        yield y
        count += 1


for num1 in fib_generator(10):
    print(num1)