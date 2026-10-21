found_numbers = []
for num in range(1000, 10000):
    a = num // 1000
    b = (num // 100) % 10
    c = (num // 10) % 10
    d = num % 10
    if (a + d) == (b + c):
        found_numbers.append(str(num))
print(f"Найдено чисел: {len(found_numbers)}")
print("Сами числа:")
for i in range(0, len(found_numbers), 10):
    print(", ".join(found_numbers[i:i+10]))