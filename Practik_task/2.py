while True:
    try:
        n = int(input("\nВведите целое десятичное число (меньше 256): "))
        if n < 0 or n >= 256:
            print("Ошибка: число должно быть в диапазоне от 0 до 255.")
        else:
            if n == 0:
                binary_str = "0"
            else:
                binary_str = ""
                temp = n
                while temp > 0:
                    remainder = temp % 2
                    binary_str = str(remainder) + binary_str
                    temp = temp // 2
            print(f"Двоичное представление числа {n}: {binary_str}")
    except ValueError:
        print("Ошибка: введите корректное целое число.")