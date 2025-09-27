s = input("Введите строку: ").lower()
glasnye = "аеёиоуыэюя"
count = 0
for ch in s:
    if ch in glasnye:
        count += 1
print("Количество гласных:", count)
