while True:
    try:
        s1 = float(input("\nВведите дистанцию в первый день (км): "))
        k = int(input("Введите номер дня (k): "))
        if k < 1:
            print("Ошибка: номер дня должен быть больше или равен 1.")
        else:
            distance = s1
            for day in range(1, k):
                distance = distance * 1.1
            print(f"Дистанция в {k}-й день составит: {distance:.2f} км")
    except ValueError:
        print("Ошибка: введите корректные числовые значения.")