
# try:
#     value = int(input("Введите число: "))  # Попытка преобразовать ввод пользователя в число
#     result = 10 / value
# except ValueError:  # Если введено не число
#     print("Ошибка: нужно вводить только числа!")
# except ZeroDivisionError:  # Деление на ноль
#     print("Ошибка: деление на ноль!")
# except Exception as e:  # Общее исключение для любых других ошибок
#     print("Произошла ошибка:", e)
# else:  # Блок выполнится, если исключений не было
#     print(f"Результат: {result}")
# finally:  # Этот блок выполнится в любом случае
#     print("Завершение программы.")


                        # Объяснение кода:
                        # 1.except ValueError — перехватывает ошибки преобразования ввода в число.
                        # 2.except ZeroDivisionError — ловит деление на ноль.
                        # 3.except Exception — перехватывает все остальные ошибки.
                        # 4.else — выполняется, если не возникло исключений.
                        # 5.finally — выполняется всегда, независимо от того,
                        #             возникло исключение или нет. Часто используется для освобождения ресурсов
                        #             (например, закрытия файлов или соединений).


# def safe_divide (a,b):
#     if b == 0:
#         raise ZeroDivisionError ('na 0 delit nelza')
#     return a / b
# try:
#     print(safe_divide(10,0))
# except ZeroDivisionError as e:
#     print("Error",e)

# def divide_numbers(a, b):
#     try:
#         result = a / b
#     except ZeroDivisionError:
#         return "Ошибка: Деление на ноль."
#     except TypeError:
#         return "Ошибка: Некорректный тип данных."
#     else:
#         return result

# def safe_file (filename):
#     if not filename :
#         print("Error")
#     try:
#       with open(filename,"r")as file:
#           content = file.read()
#       return content
#     except FileNotFoundError:
#         return "Is not file"
# print(safe_file("r"))

# def list_number (numbers):
#     results = []
#     for num in numbers:
#         try:
#             result = 100 / num
#             results.append(result)
#         except ZeroDivisionError:
#             continue
#         except TypeError:
#            continue
#     return results
#
#
# print(list_number([2,0,6,0,5,10,]))


