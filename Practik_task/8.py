print("Двузначные числа, удовлетворяющие условию:")
found_numbers = []
for num in range(10, 100):
    if (num * 2) % 10 == 8 and (num * 3) % 10 == 4:
        found_numbers.append(num)
        print(f"Число: {num} -> {num} * 2 = {num * 2}, {num} * 3 = {num * 3}")
if not found_numbers:
    print("Таких чисел не найдено.")
else:
    print(f"\nВсего найдено чисел: {len(found_numbers)}")