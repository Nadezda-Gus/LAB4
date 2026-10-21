while True:
    try:
        a = int(input("\nВведите первое целое число (A): "))
        b = int(input("Введите второе целое число (B, больше A): "))
        if a >= b:
            print("Ошибка: число A должно быть строго меньше числа B.")
        else:
            print(f"\nЦелые числа между {a} и {b} в порядке убывания:")
            count = 0
            for i in range(b - 1, a, -1):
                print(i, end=" ")
                count += 1
            print()
            print(f"Количество чисел (N): {count}")
    except ValueError:
        print("Ошибка: введите корректные целые числа.")