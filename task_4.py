number = input("Введите пятизначное число: ")

a = int(number[0])
b = int(number[1])
c = int(number[2])
d = int(number[3])
e = int(number[4])

result = ((d ** e) * c) / (a - b)

print(f"Результат: {result}")