print("Введите колличество элементов в списке")
l = int(input())
list_1 = []

print("Введите элементы списка")
for i in range(l):
    k = input()
    list_1.append(k)

print("введите число для поиска")
x = input()

n = 0

for i in list_1:
    if x == i:
        n += 1

print("Число повторений = ", n)