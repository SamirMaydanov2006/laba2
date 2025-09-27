n = int(input("Введите число N: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Факториал числа", n, "=", fact)
