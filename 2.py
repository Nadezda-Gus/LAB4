import math

while True:
    try:
        x = float(input("\nВведите значение x (|x| < 1, например 0.5): "))
        eps = float(input("Введите заданную точность e (например 0.0001): "))
        if x <= -1 or x >= 1:
            print("Ошибка: для сходимости ряда необходимо |x| < 1.")
        elif eps <= 0:
            print("Ошибка: точность должна быть положительным числом.")
        else:
            left_part = math.log(1 - x)
            s = 0.0
            term = x
            n = 1
            while abs(term) >= eps:
                s += term
                n += 1
                term = term * x * (n - 1) / n
            right_part = -s
            print(" ")
            print(f"Левая часть (math.log): {left_part:.6f}")
            print(f"Правая часть (сумма ряда): {right_part:.6f}")
            print(f"Разница (погрешность): {abs(left_part - right_part):.6f}")
            print(f"Количество итераций (n): {n - 1}")
    except ValueError:
        print("Ошибка: введите корректные числовые значения.")