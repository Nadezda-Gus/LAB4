while True:
    try:
        n = int(input("\nВведите искомое количество делителей (n): "))
        if n <= 0:
            print("Ошибка: количество делителей должно быть больше 0.")
        else:
            found_numbers = []
            for num in range(1, 201):
                count = 0
                for divisor in range(1, num + 1):
                    if num % divisor == 0:
                        count += 1
                if count == n:
                    found_numbers.append(num)
            if found_numbers:
                result_str = ", ".join(map(str, found_numbers))
                print(f"Числа от 1 до 200 с количеством делителей {n}: {result_str}")
                print(f"Всего найдено чисел: {len(found_numbers)}")
            else:
                print(f"Среди чисел от 1 до 200 нет чисел с количеством делителей {n}.")
    except ValueError:
        print("Ошибка: введите корректное целое число.")