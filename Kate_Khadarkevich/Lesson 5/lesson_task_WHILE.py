# 1. Ряд числе Фибоначчи, начиная с пятого члена ряда и заканчивая двадцатым.
a = 0
b = 1
ab = a + b

i = 0

while i <= 20:
    if i < 4:
        ab = a + b
        a = b
        b = ab
        i = i + 1
    else:
        print(a, end=' ')
        ab = a + b
        a = b
        b = ab
        i = i + 1

# 2. Напишите цикл, выводящий ряд четных чисел от 0 до 20. Затем, каждое третье число в ряде от -1 до -21
i = 0
while i <= 20:
    print(i)
    i += 1

i = -3
while i >= -21:
    print(i)
    i -= 3



