arr = list(map(int, input("Введите числа через пробел: ").split()))
x = int(input("Введите число для поиска: "))
if x in arr:
    print("Число найдено в массиве")
else:
    print("Число не найдено")
