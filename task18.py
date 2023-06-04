n = int(input("Введите количество элементов массива: "))
import random
numbers = [random.randint(1,5) for i in range(n)]
print (numbers)

X = int(input("Введите число, к которому будем искать близкий по значению элемент в массиве: "))
for i in numbers:
    if i == X:
        print('В массиве есть искомое число!')
        break
    else:
        m = min(numbers, key=lambda i: abs(i - X))
print(f"Близкий по величине элемент {m} ")