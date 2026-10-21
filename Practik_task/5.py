while True:
    try:
        n = int(input("\nВведите натуральное число: "))
        if n <= 0:
            print("Ошибка: число должно быть натуральным (больше 0).")
        else:
            total_sum = 0
            for i in range(1, n + 1):
                if n % i == 0 and i % 2 != 0:
                    total_sum += i
            print(f"Сумма нечётных делителей числа {n} равна: {total_sum}")
    except ValueError:
        print("Ошибка: введите корректное целое число.")