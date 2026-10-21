while True:
    try:
        n = int(input("\nВведите натуральное число для разложения на множители: "))
        if n <= 1:
            print("Ошибка: число должно быть натуральным и больше 1.")
        else:
            original_n = n
            factors = []
            divisor = 2
            while divisor * divisor <= n:
                if n % divisor == 0:
                    factors.append(divisor)
                    n = n // divisor
                else:
                    divisor += 1
            if n > 1:
                factors.append(n)
            result_str = " * ".join(map(str, factors))
            print(f"Разложение числа {original_n} на простые множители: {result_str}")
    except ValueError:
        print("Ошибка: введите корректное целое число.")