# class SmartPhone:
#     brand = ""
#     model = ""
#     storage = 0
#     battery = 100
#     is_on = False
#
# phone1 = SmartPhone()
# phone2 = SmartPhone()
# phone3 = SmartPhone()
#
# phone1.brand = "Apple"
# phone1.model = "iPhone 15"
# phone1.storage = 128
# phone1.battery = 85
# phone1.is_on = True
#
#
# phone2.brand = "Samsung"
# phone2.model = "Galaxy S24"
# phone2.storage = 256
# phone2.battery = 92
# phone2.is_on = False
#
#
# phone3.brand = "Xiaomi"
# phone3.model = "Mi 13"
# phone3.storage = 128
# phone3.battery = 67
# phone3.is_on = True
#
# phones = [phone1, phone2, phone3]
# for phone in phones:
#     print(f"{phone.brand} {phone.model} ({phone.storage}) - Заряд: {phone.battery}, Включен {phone.is_on}")
import math
from dataclasses import field
from operator import ifloordiv
from os import remove

from unicodedata import category




# class BankAccount:
#     account_number = ""
#     owner_name = ""
#     balance = 0.0
#     is_active = True
#     transaction_count = 0
#
# account = BankAccount()
# account.account_number = "45326"
# account.owner_name = "Igor"
# account.balance = 10000
# account.is_active = True
# account.transaction_count = 1500
#
# print("=== Начальное состояние ===")
# print(f"Счет: {account.account_number}")
# print(f"Владелец: {account.owner_name}")
# print(f"Баланс: {account.balance}₽")
# print(f"Активен: {account.is_active}")
# print(f"Операций: {account.transaction_count}")
#
# print("\n=== Пополнение счета ===")
# account.balance += 500
# account.transaction_count +=1
# print(account.balance)
# print(f"Operacion: {account.transaction_count}")
#
# print("\n=== Снятие средств ===")
# if account.balance >= 20000:
#     account.balance -= 20000
#     account.transaction_count += 1
#     print(account.balance)
#     print(f"Operacion:{account.transaction_count}")
# else:
#     print("Net sredctv ")


# class Book:
#     title = ""
#     author = ""
#     pages = 0
#     isbn = ""
#
#
#
# book1 = Book()
# book1.title = "Война и мир"
# book1.author = "Толстой"
# book1.pages = 1300
# book1.isbn = "978-5-389-07260-3"
#
# book2 = Book()
# book2.title = "Война и мир"
# book2.author = "Толстой"
# book2.pages = 1300
# book2.isbn = "978-5-389-07260-3"
#
# print("=== Эксперимент 1: Сравнение объектов ===")
# print(f"book1 == book2: {book1 == book2}")
#
# book3 = book1
# print("\n=== Эксперимент 2: Ссылки на объекты ===")
# print(f"book1 is book3: {book1 is book3}")
#
# book3.title = "Анна Каренина"
# print(f"После изменения book3.title:")
# print(f"book1.title: {book1.title}")
# print(f"book3.title: {book3.title}")

# class Product:
#     name = ""
#     price = 0.0
#     category = ""
#     in_stock = True
#     quantity = 0
#
#
# menu_product = Product()
# menu_product.name = "Ноутбук ASUS"
# menu_product.price = 75000.0
# menu_product.category = "Электроника"
# menu_product.in_stock = True
# menu_product.quantity = 3
#
# menu_product1 = Product()
# menu_product1.name = "Мышь Logitech"
# menu_product1.price = 2500.0
# menu_product1.category = "Электроника"
# menu_product1.in_stock = True
# menu_product1.quantity = 15
#
# menu_product2 = Product()
# menu_product2.name = "Книга Python"
# menu_product2.price = 1200.0
# menu_product2.category = "Книги"
# menu_product2.in_stock = False
# menu_product2.quantity = 0
#
# menu_product3 = Product()
# menu_product3.name = "Кофе Арабика"
# menu_product3.price = 800.0
# menu_product3.category = "Продукты"
# menu_product3.in_stock = True
# menu_product3.quantity = 25
#
# menu_product4 = Product()
# menu_product4.name = "Телефон iPhone"
# menu_product4.price = 120000.0
# menu_product4.category = "Электроника"
# menu_product4.in_stock = True
# menu_product4.quantity = 2
#
# products = [menu_product,menu_product1,menu_product2,menu_product3,menu_product4]
# print("=== КАТАЛОГ ТОВАРОВ ===")
# for product in products:
#     print(f"{product.name},{product.price},{product.category},{product.in_stock},{product.quantity}")
# print()
# print("=== КАТАЛОГ ТОВАРОВ категории Электроника ===")
# str_product = "Электроника"
# for product in products:
#  if product.category == str_product:
#     print(f"{product.name},{product.price},{product.category},{product.in_stock},{product.quantity}")
#
#
# print()
# print("=== ДОРОГИЕ ТОВАРЫ (>10000₽) ===")
# for product in products:
#     if product.price > 10000:
#         print(f"{product.name},{product.price},{product.category},{product.in_stock},{product.quantity}")
#
#
# print()
# total_value = 0
# for product in products:
#     if product.in_stock:
#      total_value += product.price * product.quantity
# print(f"\n=== СТАТИСТИКА ===")
# print(f"Общая стоимость товаров в наличии: {total_value}₽")


# class Car:
#     def __init__(self,car_brand,car_model,car_year, car_mileage = 0):
#         self.brand =car_brand
#         self.model =car_model
#         self.year = car_year
#         self.mileage = car_mileage
#
# car1 = Car("Toyota", "Camry", 2020)
# car2 = Car("BMW", "X5", 2022 )
# car3 = Car("Lada", "Granta", 2019)
#
# print(f"Машина 1: {car1.brand} {car1.model} ({car1.year}), пробег: {car1.mileage} км")
# print(f"Машина 2: {car2.brand} {car2.model} ({car2.year}), пробег: {car2.mileage} км")
# print(f"Машина 3: {car3.brand} {car3.model} ({car3.year}), пробег: {car3.mileage} км")


# class Product:
#     def __init__(self, name, price, category):
#         if not name :
#             self.name = "Товар без названия"
#         else:
#             self.name =name
#
#
#         if price < 0 :
#             self.price = 0
#             print(f"Не может быть отрицательм {self.price}")
#         else:
#             self.price = price
#
#
#         if category not in ["Электроника","Одежда","Книги","Продукты"]:
#            self.category = "Разное"
#            print("Предупреждение: категория установлена на 'Разное'.",category)
#         else:
#            self.category = category
#         self.in_stock = True
#         print(f"Создан товар: {self.name} - {self.price}₽ ({self.category})")
#
#
# product1 = Product("iPhone 15", 120000, "Электроника")
# product2 = Product("", 50000, "Электроника")
# product3 = Product("Футболка", -500, "Одежда")
# product4 = Product("Молоток", 1500, "Инструменты")
# product5 = Product("", -100, "Неизвестно")
# product = [product1,product2,product3,product4,product5]
# for prod in product:
#     print(f"{prod.name} - {prod.price}₽ ({prod.category})")

# class Employee:
#     def __init__(self, first_name, last_name, birth_year, department):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.birth_year = birth_year
#         self.department = department
#
#         self.full_name = f"{self.first_name} {self.last_name}"
#         self.age = 2024 -self.birth_year
#         self.employee_id = f"{first_name[:2].upper()}{last_name[:2].upper()}{self.birth_year}"
#         self.email = f"{self.first_name.lower()}.{self.last_name.lower()}@company.ru"
#         self.is_senior = self.age >= 30
#
#         print(f"Зарегистрирован сотрудник: {self.full_name}")
#         print(f"ID: {self.employee_id}, Email: {self.email}")
#         print(f"Возраст: {self.age}, Статус: {'Senior' if self.is_senior else 'Junior'}")
#
# emp1 = Employee("Анна", "Петрова", 1990, "IT")
# emp2 = Employee("Петр", "Иванов", 2000, "HR")
# emp3 = Employee("Мария", "Сидорова", 1985, "Finance")
#
# employees = [emp1, emp2, emp3]
# for emp in employees:
#     print(f"\n{emp.full_name} ({emp.age} лет)")
#     print(f"Отдел: {emp.department}")
#     print(f"Email: {emp.email}")
#     print(f"Статус: {'Senior' if emp.is_senior else 'Junior'}")


# class Calculator:
#     def add(self,a,b):
#         return  a + b
#     def subtract(self,a,b):
#         return  a - b
#     def multiply(self,a,b):
#         return a * b
#     def divide(self,a,b):
#         try:
#             result = a / b
#         except ZeroDivisionError:
#             return print("delit na 0 nelzay")
#         except TypeError:
#             return "nekorektnui tip dannuh"
#         else:
#             return result
#
#
# calc = Calculator()
# print(f"10 + 5 = {calc.add(10, 5)}")           # Должно быть 15
# print(f"10 - 5 = {calc.subtract(10, 5)}")     # Должно быть 5
# print(f"10 * 5 = {calc.multiply(10, 5)}")     # Должно быть 50
# print(f"10 / 5 = {calc.divide(10, 5)}")       # Должно быть 2.0
# print(f"10 / 0 = {calc.divide(10, 0)}")


# class BankAccount:
#     def __init__(self,owner_name,initial_balance = 0):
#         self.owner_name = owner_name
#         self.balance = initial_balance
#         self.transaction_count = 0
#
#
#     def deposit(self,amount):
#         if amount > 0:
#             self.balance += amount
#             self.transaction_count += 1
#             print(f"popolnenie: {self.balance},{self.transaction_count}")
#             return self.balance
#
#     def withdraw(self, amount):
#         if amount <= 0 :
#             print("Сумма должна быть больше 0")
#             return False
#         if amount > self.balance:
#             print("Недостаточно средств на счету")
#             return False
#         self.balance -= amount
#         self.transaction_count += 1
#         print(f"balanc ymenshen: {amount}, ostatock {self.balance}")
#         return True
#
#
#     def get_balance(self):
#         return self.balance
#
#     def get_info(self):
#         return print(f"Счет {self.owner_name}: {self.balance}₽, операций: {self.transaction_count}")
#
#
# account = BankAccount("Иван Петров", 1000)
#
# print("Начальное состояние:")
# print(account.get_info())
# print()
# print("\nПополняем счет:")
# new_balance = account.deposit(500)
# print(f"Новый баланс: {new_balance}₽")
# print()
# print("\nСнимаем деньги:")
# success = account.withdraw(200)
# print(f"Операция {'успешна' if success else 'неуспешна'}")
# print()
# print("\nПытаемся снять больше, чем есть:")
# success = account.withdraw(2000)
# print(f"Операция {'успешна' if success else 'неуспешна'}")
# print()
# print("\nИтоговое состояние:")
# print(account.get_info())

# class Player:
#     def __init__(self, name, health=100, attack_power=20):
#         self.name = name
#         self.health = health
#         self.max_health = health
#         self.attack_power = attack_power
#         self.is_alive = True
#
#     def attack(self, target):
#         if not self.is_alive:
#             print(f"{self.name} не может атаковать, так как мертв.")
#             return False
#         if not target.is_alive:
#             print(f"{target.name} уже мертв и не может быть атакован.")
#             return False
#
#         print(f"{self.name} атакует {target.name}!")
#         target.take_damage(self.attack_power)
#         return True
#
#
#     def take_damage(self,damage):
#         self.health -= damage
#         if self.health <= 0:
#             self.health = 0
#             self.is_alive = False
#             print(f"получен урон {damage},текущее здоровье:{self.health}")
#             if self.max_health == 0:
#                 print(f"Игрок умер: {self.name}")
#
#     def heal(self,amount):
#         if self.health <= self.max_health:
#             self.health += amount
#             print(f"Игрок {self.name} лечится {amount} ")
#
#     def get_status(self):
#         print(f"{self.name}: {self.health}/{self.max_health} HP, {'жив' if self.is_alive else 'мертв'}")

# warrior = Player("Воин", 120, 70)
# mage = Player("Маг", 80, 110)
#
# print("=== Начало боя ===")
# print(warrior.get_status())
# print(mage.get_status())
# print()
# print(f"\n=== Раунд 1 ===")
# warrior.attack(mage)
# print(mage.get_status())
# print()
# print(f"\n=== Раунд 2 ===")
# mage.attack(warrior)
# print(warrior.get_status())
# print()
# print(f"\n=== Маг лечится ===")
# healed = mage.heal(20)
# print(f"Восстановлено {healed} HP")
# print(mage.get_status())
# print()
# print(f"\n=== Раунд 3 ===")
# warrior.attack(mage)
# mage.attack(warrior)
# print()
# print(f"\n=== Итоговые статусы ===")
# print(warrior.get_status())
# print(mage.get_status())


# class Counter:
#     total_counters = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.value = 0
#         Counter.total_counters += 1
#
#     def increment(self):
#         self.value += 1
#     def decrement(self):
#         self.value -= 1
#     def reset(self):
#         self.value = 0
#     def get_value(self):
#         return self.value
#     def get_total_counters(self):
#         return Counter.total_counters
#     def get_info(self):
#         return print(f"Счетчик {self.name}: {self.value} (всего счетчиков: {Counter.total_counters}")
#
#
# print("=== Создаем счетчики ===")
# counter1 = Counter("Первый")
# counter2 = Counter("Второй")
# counter3 = Counter("Третий")
#
# print(f"Всего создано счетчиков: {counter1.get_total_counters()}")
#
#
# print(f"\n=== Работаем с индивидуальными счетчиками ===")
# counter1.increment()
# counter1.increment()
# counter1.increment()
#
#
# counter2.increment()
# counter2.increment()
#
# counter3.increment()
#
# print(counter1.get_info())
# print(counter2.get_info())
# print(counter3.get_info())
#
#
# print(f"\n=== Сбрасываем первый счетчик ===")
# counter1.reset()
# print(counter1.get_info())
# print(counter2.get_info())
#
#
# print(f"\n=== Проверяем общий счетчик ===")
# print(f"Через counter1: {counter1.get_total_counters()}")
# print(f"Через counter2: {counter2.get_total_counters()}")
# print(f"Через класс: {Counter.total_counters}")
# 1. total_counters является атрибутом класса,
# а не экземпляра. Это значит, что он общ для всех объектов класса Counter.
# Когда создается новый объект, значение total_counters увеличивается на 1,
# и это значение остается одинаковым для всех экземпляров,
# так как они ссылаются на один и тот же атрибут.

# 2. Если изменить Counter.total_counters = 100,
# все экземпляры класса Counter будут видеть это новое значение,
# так как они ссылаются на общий атрибут класса.
# Однако это не повлияет на количество фактически созданных счетчиков,
# так как это значение не отслеживает, сколько объектов было создано.
# Это приведет к некорректному отображению количества созданных счетчиков.

# 3. Сброс counter1 не повлиял на counter2,
# потому что каждый экземпляр класса имеет свои собственные атрибуты,
# такие как value. Сброс counter1 устанавливает значение его собственного
# атрибута value в 0, но это не затрагивает атрибут value у counter2,
# который независим и сохраняет свое собственное значение.

# class Product:
#     def __init__(self,name,price,category,stock):
#         self.name = name
#         self.price = price
#         self.category = category
#         self.stock = stock
#
#     def is_available(self):
#        if self.name and self.stock > 0:
#            print("Товар в наличии")
#        else:
#            print("Отсутствует")
#
#     def reduce_stock(self,amount):
#         if self.stock >= amount:
#             self.stock -= amount
#             print(f"Количество товара '{self.name}' уменьшено на {amount}. Остаток: {self.stock}")
#             return True
#         else:
#             print(f"Ошибка: Недостаточно товара '{self.name}'. Запрошено: {amount}, Доступно: {self.stock}")
#             return False
#
#     def add_stock(self,amount):
#          self.stock += amount
#          print(f"Количество товара '{self.name}' увеличено на {amount}. Теперь: {self.stock}")
#
#     def get_info(self):
#         print(
#             f"Наиминование:{self.name},цена товара:{self.price},"
#             f"Категория товара: {self.category},количество товара: {self.stock}")
#
# class ShoppingCart:
#     def __init__(self,customer_name):
#         self.customer_name = customer_name
#         self.items = {}
#         self.total_amount = 0
#
#     def add_item(self,product,quantity):
#         if quantity <=0:
#             print("Ошибка: количество должно быть положительным числом")
#             return False
#         if not product.is_available():
#             print(f"Товар '{product.name}' отсутствует в наличии")
#             return False
#         if product.stock < quantity:
#             print(f"Недостаточно товара '{product.name}'. Доступно: {product.stock}")
#             return False
#
#         if product.name in self.items:
#             self.items[product.name] += quantity
#         else:
#             self.items[product] = quantity
#
#         self.calculate_total()
#         print(f"Добавлено {quantity} шт. товара '{product.name}' в корзину")
#         return True
#
#
#     def remove_iterm(self,product_name):
#         product_to_remove = None
#         for product in self.items.keys():
#             if product.name == product_name:
#                 product_to_remove = product
#                 break
#         if product_to_remove is None:
#             print(f"Товар '{product_name}' не найден в корзине")
#             return False
#         removed_quantity = self.items[product_to_remove]
#         del self.items[product_to_remove]
#         self.calculate_total()
#         print(f"Товар '{product_name}' ({removed_quantity} шт.) удален из корзины")
#         return True
#
#     def calculate_total(self):
#         self.total_amount = 0
#         for product,quantity in self.items.items():
#             self.total_amount += product.price * quantity
#         return self.total_amount
#
#     def get_cart_info(self):
#         if not self.items:
#             return f"Корзина покупателя {self.customer_name} пуста"
#
#         info = f"Корзина покупателя: {self.customer_name}\n"
#         info += "Товары в корзине:\n"
#
#         for product,quantity in self.items.items():
#             item_total = product.price * quantity
#             info += f"- {product.name}: {quantity} шт. × {product.price} руб. = {item_total} руб.\n"
#
#         info += f"Общая стоимость: {self.total_amount} руб."
#         return info
#
#     def checkout(self,):
#         if not self.items:
#             print("Корзина пуста, нечего оформлять")
#             return False
#
#         for product,quantity in self.items.items():
#             if not product.is_available() or product.stock < quantity:
#                 print(f"Товар '{product.name}' недоступен в нужном количестве")
#                 return False
#
#         for product,quantity in self.items.items():
#             success = product.reduce_stock(quantity)
#             if not success:
#                 print(f"Ошибка при списании товара '{product.name}'")
#                 return False
#
#         print(f"Заказ оформлен успешно! Общая сумма: {self.total_amount} руб.")
#         print(f"Списано товаров: {sum(self.items.values())} шт.")
#
#         self.items.clear()
#         self.total_amount = 0
#
#         return True
#
# laptop = Product("Ноутбук", 75000, "Электроника", 5)
# mouse = Product("Мышь", 2500, "Электроника", 20)
# book = Product("Python для начинающих", 1200, "Книги", 10)
#
# cart = ShoppingCart("Анна Петрова")
#
# print("=== Добавляем товары в корзину ===")
# cart.add_item(laptop, 1)
# cart.add_item(mouse, 2)
# cart.add_item(book, 3)
#
# print(cart.get_cart_info())
#
# print(f"\n=== Общая сумма ===")
#
# total = cart.calculate_total()
# print(f"К оплате: {total}₽")
#
# print(f"\n=== Оформляем заказ ===")
# cart.checkout()
#
#
# print(f"\n=== Проверяем остатки на складе ===")
# print(laptop.get_info())
# print(mouse.get_info())
# print(book.get_info())

# from datetime import datetime
# from enum import Enum
#
#
# class TaskStatus(Enum):
#     PENDING = "ожидает"
#     IN_PROGRESS = "в работе"
#     COMPLETED = "завершена"
#
# class Task:
#     def __init__(self,title,description,estimate_hours):
#         self.title = title
#         self.description = description
#         self.estimate_hours = estimate_hours
#         self.status = TaskStatus.PENDING
#         self.assigned_developer = None
#         self.start_time = None
#         self.complete_time = None
#         self.actual_hours = 0
#
#
#     def assign_to(self,developer):
#         if self.assigned_developer:
#             print(f"Задача '{self.title}' уже назначена на {self.assigned_developer.name}")
#             return False
#
#         if developer.take_task(self):
#             self.assigned_developer = developer
#             print(f"Задача '{self.title}' назначена на {developer.name}")
#             return True
#         else:
#             print(f"Не удалось назначить задачу '{self.title}' на {developer.name}")
#             return False
#
#     def start(self):
#         if not self.assigned_developer:
#             print(f"Ошибка: задача '{self.title}' не назначена на разработчика")
#             return False
#
#         if self.status == TaskStatus.IN_PROGRESS:
#             print(f"Задача '{self.title}' уже в работе")
#             return False
#
#         if self.status == TaskStatus.COMPLETED:
#             print(f"Задача '{self.title}' уже завершена")
#             return False
#
#         self.status = TaskStatus.IN_PROGRESS
#         self.start_time = datetime.now()
#         print(f"Задача '{self.title}' начата в {self.start_time.strftime('%H:%M:%S')}")
#         return True
#
#     def complete(self):
#         if self.status != TaskStatus.IN_PROGRESS:
#             print(f"Ошибка: задача '{self.title}' не в работе")
#             return False
#         self.status = TaskStatus.COMPLETED
#         self.complete_time = datetime.now()
#
#         if self.start_time:
#             time_deff = self.complete_time - self.start_time
#             self.actual_hours = round(time_deff.total_seconds()/ 3600,2)
#         if self.assigned_developer:
#             self.assigned_developer.complete_task(self)
#
#         print(f"Задача '{self.title}' завершена за {self.actual_hours} часов")
#         return True
#
#     def get_info(self):
#         info = f"Задача: {self.title}\n"
#         info += f"Описание: {self.description}\n"
#         info += f"Статус: {self.status.value}\n"
#         info += f"Оценка времени: {self.estimate_hours} часов\n"
#
#         if self.assigned_developer:
#             info += f"Исполнитель: {self.assigned_developer.name}\n"
#         else:
#             info += "Исполнитель: не назначен"
#
#         if self.actual_hours > 0:
#             info += f"Фактическое время: {self.actual_hours} часов\n"
#
#         return info
#
#     def __str__(self):
#         return f"Задача: {self.title} ({self.status.value})"
#
# class Project:
#     def __init__(self,name,description):
#         self.name = name
#         self.description = description
#         self.tasks = []
#         self.start_date = datetime.now()
#         self.is_completed = False
#
#     def add_task(self,task):
#         self.tasks.append(task)
#         print(f"Задача '{task.title}' добавлена в проект '{self.name}'")
#
#     def removed_task(self,task_title):
#         for task in self.tasks:
#             if task_title == task_title:
#                 self.tasks.remove(task)
#                 print(f"Задача '{task_title}' удалена из проекта '{self.name}'")
#                 return True
#         print(f"Задача '{task_title}' не найдена в проекте '{self.name}'")
#         return False
#
#     def get_progress(self):
#         total_task = len(self.tasks)
#         if total_task == 0:
#             return {
#                 'total': 0,
#                 'completed': 0,
#                 'in_progress': 0,
#                 'pending': 0,
#                 'completion_percentage': 0
#             }
#         completed = len([t for t in self.tasks if t.status == TaskStatus.COMPLETED])
#         in_progress = len([t for t in self.tasks if t.status == TaskStatus.IN_PROGRESS ])
#         pending = len([t for t in self.tasks if t.status == TaskStatus.PENDING])
#
#         comletion_percentage = round((completed / total_task) * 100 , 1)
#
#         return {
#             "total": total_task,
#             "completed":completed,
#             "in_progress":in_progress,
#             "pending":pending,
#             "completion_percentage": comletion_percentage
#         }
#
#     def assign_task(self,task_title,developer):
#         for task in self.tasks:
#             if task.title == task_title:
#                 return  task.assign_to(developer)
#         print(f"Задача '{task_title}' не найдена в проекте '{self.name}'")
#         return False
#
#     def complete_project(self):
#         progress = self.get_progress()
#         if progress["completed"] == progress["total"] and progress["total"] > 0:
#             self.is_completed = True
#             print(f"Проект '{self.name}' завершен!")
#         else:
#             print(
#                 f"Проект '{self.name}' не может быть завершен. Завершено {progress['completed']} из {progress['total']} задач")
#
#     def get_project_info(self):
#
#         info = f"Проект: {self.name}\n"
#         info += f"Описание: {self.description}\n"
#
#         progress = self.get_progress()
#         info += f"Прогресс: {progress['completion_percentage']}% "
#         info += f"({progress['completed']}/{progress['total']} задач)\n"
#
#         info += f"Статус: {'Завершен' if self.is_completed else 'Активен'}\n"
#         info += "Задачи:\n"
#
#         for task in self.tasks:
#             info += f"  - {task.title} ({task.status.value})\n"
#         return info
#
#     def __str__(self):
#         progress = self.get_progress()
#         return f"Проект: {self.name} ({progress['completion_percentage']}% завершен)"
#
# class Developer:
#     def __init__(self,name,position):
#         self.name = name
#         self.position = position
#         self.assigned_tasks = []
#         self.completed_tasks = []
#         self.max_workload = 3
#
#     def take_task(self,task):
#         if len(self.assigned_tasks) >= self.max_workload:
#             print(f"{self.name} перегружен. Максимум задач: {self.max_workload}")
#             return False
#         if task in self.assigned_tasks:
#             print(f"Задача '{task.title}' уже назначена на {self.name}")
#             return False
#
#         self.assigned_tasks.append(task)
#         print(f"{self.name} взял задачу '{task.title}'")
#         return True
#
#     def complete_task(self,task):
#         if task in self.assigned_tasks:
#             self.assigned_tasks.remove(task)
#             self.completed_tasks.append(task)
#             print(f"{self.name} завершил задачу '{task.title}'")
#         else:
#             print(f"Задача '{task.title}' не назначена на {self.name}")
#
#     def get_workload(self):
#         current_tasks = len(self.assigned_tasks)
#         workload_percentage = round((current_tasks / self.max_workload) * 100 , 1)
#         return {
#             'current_tasks': current_tasks,
#             'max_tasks': self.max_workload,
#             'workload_percentage': workload_percentage,
#             'completed_tasks': len(self.completed_tasks),
#             'is_overloaded': current_tasks >= self.max_workload
#         }
#
#     def start_task(self,task_title):
#         for task in self.assigned_tasks:
#             if task.title == task_title:
#                 return task.start()
#         print(f"Задача '{task_title}' не найдена у {self.name}")
#         return False
#
#     def get_developer_info(self):
#         info = f"Разработчик: {self.name}\n"
#         info += f"Должность: {self.position}\n"
#
#         workload = self.get_workload()
#         info += f"Загрузка: {workload['workload_percentage']}% "
#         info += f"({workload['current_tasks']}/{workload['max_tasks']} задач)\n"
#
#         info += f"Завершено задач: {workload['completed_tasks']}\n"
#         info += "Текущие задачи:\n"
#
#         for task in self.assigned_tasks:
#             info += f"  - {task.title} ({task.status.value})\n"
#         return info
#     def __str__(self):
#         workload = self.get_workload()
#         return f"Разработчик: {self.name} ({workload['current_tasks']} активных задач)"
#
#
# if __name__ ==  "__main__":
#     print("=== СИСТЕМА УПРАВЛЕНИЯ ПРОЕКТАМИ ===\n")
#
#     dev1 = Developer("Алексей Петров", "Senior Developer")
#     dev2 = Developer("Мария Сидорова", "Middle Developer")
#     dev3 = Developer("Иван Козлов", "Junior Developer")
#
#     project = Project("Разработка мобильного приложения", "Создание кроссплатформенного мобильного приложения")
#
#     task1 = Task("Дизайн интерфейса", "Разработать UI/UX дизайн приложения", 40)
#     task2 = Task("Бэкенд API", "Реализовать серверную часть приложения", 60)
#     task3 = Task("Фронтенд разработка", "Создать пользовательский интерфейс", 50)
#     task4 = Task("Тестирование", "Провести полное тестирование приложения", 30)
#     task5 = Task("Документация", "Написать документацию для проекта", 20)
#
#     print("=== ДОБАВЛЕНИЕ ЗАДАЧ В ПРОЕКТ ===")
#     project.add_task(task1)
#     project.add_task(task2)
#     project.add_task(task3)
#     project.add_task(task4)
#     project.add_task(task5)
#
#     print("\n=== НАЗНАЧЕНИЕ ЗАДАЧ РАЗРАБОТЧИКАМ ===")
#     project.assign_task("Дизайн интерфейса", dev1)
#     project.assign_task("Бэкенд API", dev2)
#     project.assign_task("Фронтенд разработка", dev2)
#     project.assign_task("Тестирование", dev3)
#     project.assign_task("Документация", dev3)
#
#     # перегрузка
#     task6 = Task("Дополнительная задача", "Тестовая задача", 10)
#     project.add_task(task6)
#     project.assign_task("Дополнительная задача", dev3)
#
#     print("\n=== ЗАПУСК ВЫПОЛНЕНИЯ ЗАДАЧ ===")
#     dev1.start_task("Дизайн интерфейса")
#     dev2.start_task("Бэкенд API")
#     dev3.start_task("Тестирование")
#
#     print("\n=== ЗАВЕРШЕНИЕ ЗАДАЧ ===")
#     # Имитируем завершение задач
#     task1.complete()
#     task4.complete()
#
#     print("\n=== ИНФОРМАЦИЯ О ПРОЕКТЕ ===")
#     print(project.get_project_info())
#
#     print("\n=== ИНФОРМАЦИЯ О РАЗРАБОТЧИКАХ ===")
#     print(dev1.get_developer_info())
#     print("\n" + dev2.get_developer_info())
#     print("\n" + dev3.get_developer_info())
#
#     print("\n=== ПРОГРЕСС ПРОЕКТА ===")
#     progress = project.get_progress()
#     print(f"Всего задач: {progress['total']}")
#     print(f"Завершено: {progress['completed']}")
#     print(f"В работе: {progress['in_progress']}")
#     print(f"Ожидают: {progress['pending']}")
#     print(f"Процент завершения: {progress['completion_percentage']}%")
#
#     print("\n=== ЗАВЕРШЕНИЕ ПРОЕКТА ===")
#     project.complete_project()

# class Animal:
#     species = []
#     def __init(self,species_name):
#         self.add_species(species_name)
#
#     @classmethod
#     def add_species(cls,species_name):
#         if species_name not in cls.species:
#             cls.species.append(species_name)
#
#     @classmethod
#     def show_species(cls):
#         print(cls.species)
#
# dog = Animal
# print(dog.add_species("Vova"))
# print(dog.show_species())

# class CurrencyConverter:
#     @staticmethod
#     def usd_to_eur(amount):
#        if amount > 100:
#            amount *= 0.85
#        return amount
#     @staticmethod
#     def eur_to_usd(amount):
#         if amount > 1000:
#             amount *= 1.18
#         return amount
#
#
# print(CurrencyConverter.usd_to_eur(123))
# print(CurrencyConverter.eur_to_usd(5000))

# class BankAccount:
#     def __init__(self,balance):
#         self._balance = balance
#     def deposit(self,amount):
#         if amount > 0:
#             self._balance += amount
#         else:
#             print("Сумма депозита должна быть положительной.")
#
#     def withdraw(self,amount):
#         if 0 < amount <= self._balance:
#             self._balance -= amount
#         else:
#             print("Недостаточно средств или некорректная сумма.")
#
#     def get_balance(self):
#         return self._balance
#
# account = BankAccount(1000)
# account.deposit(500)
# account.withdraw(2000)
# print(account.get_balance())
#
# print(account._balance)
#
# account._balance = -1000
# print(account.get_balance())
# account.withdraw(100)
# print(account.get_balance())


# class Rectangle:
#     def __init__(self,width,height):
#         if width > 0 and height > 0:
#          self.width = width
#          self.height = height
#         else:
#             print("должно быть положительным")
#     @property
#     def area(self):
#         return self.width * self.height
#
#     @property
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#     @property
#     def diagonal(self):
#         return math.sqrt(2** self.width + self.height **2)
#
#     @property
#     def dimensions(self):
#         return (self.width, self.height)
#
#     @dimensions.setter
#     def dimensions(self,dimensions):
#         self.width, self.height = dimensions
#
#
# rect = Rectangle(5, 3)
# print(rect.area)         # 15
# print(rect.perimeter)    # 16
# print(rect.diagonal)     # ~5.83
# print(rect.dimensions)   # (5, 3)
#
# rect.dimensions = (10, 6)
# print(rect.area)         # 60
# print(rect.dimensions)


# class Counter:
#     def __init__(self,count):
#         self.count = count
#         self._change_count = 0
#         self._history = [count]
#
#     @property
#     def value(self):
#         return self.count
#
#     @value.setter
#     def value(self, value):
#         if value != self.count:
#            self._history.append(self.count)
#            self.count = value
#            self._change_count +=1
#
#
#     @property
#     def history(self):
#         return self._history
#
#     @property
#     def change_count(self):
#         return self._change_count
#
#
# counter = Counter(10)
# print(counter.value)        # 10
# print(counter.history)      # [10]
# print(counter.change_count) # 0
#
# counter.value = 15
# print(counter.history)
# counter.value = 15
# print(counter.history) # Не должно изменить историю
# counter.value = 20
# print(counter.history)
# print("gg")
# print(counter.history)      # [10, 15, 20]
# print(counter.change_count) #

# class BankAccount:
#     def __init__(self,account_number,owner_name,balance):
#
#
#         self.account_number = account_number
#         self.owner_name = self.set_owner_name(owner_name)
#         self.balance = balance
#         self._balance = 0
#         self._transaction = 0
#         self._transactionHistory = [balance]
#         self.is_active = True
#
#     def set_owner_name(self, name):
#         if isinstance(name, str) and name.strip() and not any(char.isdigit() for char in name):
#             return name
#         else:
#             raise ValueError("Имя владельца должно быть непустой строкой без цифр.")
#
#     @property
#     def formatted_balance(self):
#         return f"{self.balance} ₽"
#
#     @property
#     def balance(self):
#         return self._balance
#
#     @balance.setter
#     def balance(self, value):
#         if value < 0:
#             raise ValueError("Баланс не может быть отрицательным")
#         self._balance = value
#
#
#
#     @property
#     def transaction_history(self):
#         return self._transaction
#
#     @property
#     def account_info(self):
#         return f"на счету у {self.owner_name}:{self.balance} ₽"
#
#     def deposit(self,amount):
#         if not self.is_active:
#             print("ne octiven")
#             return
#         if amount > 0:
#          self.balance += amount
#          self._transaction += 1
#          self._transactionHistory.append(self.balance)
#          print(f"Теперь на счету у {self.owner_name}: {self.balance}")
#          return self.balance
#
#
#     def withdraw(self,amount):
#         if not self.is_active:
#             print("ne octiven")
#             return
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             self._transaction += 1
#             self._transactionHistory.append(self.balance)
#             print(f"Вы сняли {amount} ₽. Теперь на счету: {self.balance} ₽")
#         else:
#             print("не достаточно средств,пополните баланс")
#
#     def check_balance(self):
#         if self.balance < 0:
#             raise ValueError("Баланс не может быть отрицательным")
#
# account = BankAccount("12345", "Иван Петров", 1000)
# print(account.formatted_balance)    # "1000 ₽"
# print(account.account_info)         # Краткая информация
#
#
# account.deposit(500)
# print(account.balance)              # 1500
# print(account.transaction_history)
# print()
# account.withdraw(200)
# print(account.balance)              # 1300
# print(account.transaction_history)
# print()
# account.is_active = False
#
# account.withdraw(400)
# print(account.balance)


# import math
#
# class Shape:
#     def __init__(self,color):
#         self.color = color
#
#     def area(self):
#         return 0
#
#     def describe(self):
#         return f"{self.color} фигура с площадью {self.area()}"
#
# class Rectangle(Shape):
#     def __init__(self, color, width, height):
#         super().__init__(color)
#         self.color = color
#         self.width = width
#         self.height = height
#
#     def area(self):
#        return f" S = {self.width * self.height}"
#
# class Circle(Shape):
#     def __init__(self, color, radius):
#         super().__init__(color)
#         self.color = color
#         self.radius = radius
#
#     def area(self):
#         return f"R = {math.pi * self.radius ** 2}"
#
#
# class Triangle(Shape):
#     def __init__(self, color, base, height):
#         super().__init__(color)
#         self.color = color
#         self.base = base
#         self.height = height
#
#     def area(self):
#         return f"S = {self.base * self.height / 2}"
#
#
# shapes = [
#     Shape("серая"),
#     Rectangle("красный", 5, 3),
#     Circle("синий", 2),
#     Triangle("зеленый", 4, 6)
# ]
# for shape in shapes:
#     print(shape.describe())



# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#
#     def start(self):
#         return f"{self.brand} {self.model} запускается обычным способом"
#
#     def stop(self):
#         return f"{self.brand} {self.model} останавливается"
#
# class Car(Vehicle):
#     def __init__(self,brand,model,fuel_type):
#         super().__init__(brand,model)
#         self.fuel_type = fuel_type
#
#     def start(self):
#         if self.fuel_type == "electric":
#             print(f"{self.brand}-{self.model} запускается бесшумно на электричестве")
#         else:
#             print(f"{self.brand}-{self.model} запускается с рокотом двигателя на {self.fuel_type}")
#
#
# class Motorcycle(Vehicle):
#     def start(self):
#         return f"{self.brand}-{self.model} заводится с характерным звуком мотоцикла"
#
#
# class Bicycle(Vehicle):
#     def start(self):
#            return f"{self.brand}-{self.model} готов к поездке - просто крути педали!"
#
# vehicles = [
#     Vehicle("Generic", "Transport"),
#     Car("Tesla", "Model S", "electric"),
#     Car("Toyota", "Camry", "бензин"),
#     Motorcycle("Harley-Davidson", "Street 750"),
#     Bicycle("Trek", "Mountain Bike")
# ]
#
# print("=== Запуск транспорта ===")
# for vehicle in vehicles:
#     print(vehicle.start())
# print()
# print("\n=== Остановка транспорта ===")
# for vehicle in vehicles:
#     print(vehicle.stop())


# class Notification:
#     def __init__(self,message,recipient):
#         self.message = message
#         self.recipient = recipient
#
#     def send(self):
#         return f"Уведомление {self.message} получил {self.recipient}"
#
# class EmailNotification(Notification):
#     def send(self):
#         return f"Отправка email {self.recipient} {self.message}"
#
#
# class SMSNotification(Notification):
#     def send(self):
#         return f"SMS на номер {self.recipient} {self.message}"
#
#
# class PushNotification(Notification):
#     def send(self):
#         return f"Push уведомление {self.recipient} {self.message}"
#
# notifications = [
#     EmailNotification("Добро пожаловать!", "user@example.com"),
#     SMSNotification("Код подтверждения: 1234", "+7-999-123-45-67"),
#     PushNotification("У вас новое сообщение", "user_123"),
#     Notification("Общее уведомление", "admin")
# ]
#
# for notification in notifications:
#     print(notification.send())


# class BankAccount:
#     def __init__(self,name,balance=0):
#         self.name = name
#         self.balance = balance
#         self.transaction = 0
#
#     def deposit(self):
#         return f"Ваши накопления {self.balance}"
#
#     def account_type(self):
#         return f"Базовый счет: {self.name}, баланс: {self.balance}₽"
#
#     def withdraw(self,amount):
#         if amount <= 0:
#             return "Сумма снятия должна быть положительной"
#         if amount > self.balance:
#            return "Не достаточно средств для снятия "
#
#         else:
#             self.balance -= amount
#             self.transaction += 1
#             return "Транзакция прошла"
#
# class SavingsAccount(BankAccount):
#     def account_type(self):
#         return f"СБЕРЕГАТЕЛЬНЫЙ | {self.name} | Баланс: {self.balance}₽ | Комиссия 1%"
#
#
#     def withdraw(self,amaunt):
#         commission = amaunt * 0.01
#         total_amount = amaunt + commission
#         if total_amount <= self.balance:
#             self.balance -= total_amount
#             self.transaction += 1
#             print(f"комиссия составила 1% {commission} RUB ")
#             print(f"Списано {total_amount}")
#             print(f'Остаток {self.balance}')
#             print(f"транзакция: {self.transaction}")
#             return True
#         else:
#             print(f"Недостаточно средств с учетом комиссии. Нужно: {total_amount}₽, доступно: {self.balance}₽")
#             return False
#
# class CheckingAccount(BankAccount):
#
#     def account_type(self):
#         return f"Расчетный | {self.name} | Баланс: {self.balance}₽ | Комиссия 2% при снятии >1000₽"
#
#     def withdraw(self,amount):
#         if amount > 1000:
#             commission = amount * 0.02
#             total_amount = amount + commission
#         else:
#             commission = 0
#             total_amount = amount
#
#         if total_amount <= self.balance:
#             self.balance -= total_amount
#             self.transaction += 1
#
#             if commission > 0:
#                 print(f"Снятие превысило 1000₽, комиссия составила 2%: {commission}₽")
#             else:
#                 print("Снятие без комиссии")
#
#             print(f"Списано: {total_amount:.2f}₽")
#             print(f"Остаток на балансе: {self.balance:.2f}₽")
#             print(f"Транзакция: {self.transaction}")
#             return True
#
#
#
# class PremiumAccount(BankAccount):
#     def account_type(self):
#         return f"ПРЕМИУМ | {self.name} | Баланс: {self.balance}₽ | Мин.баланс: 10000₽"
#
#     def withdraw(self,amount):
#         if self.balance - amount >= 1000:
#             self.balance -= amount
#             self.transaction += 1
#             return f"Снято: {amount}₽ (без комиссии)"
#         return "Нельзя нарушить минимальный баланс"
#
#
# accounts = [
#     SavingsAccount("Сберегательный", 5000),
#      CheckingAccount("Расчетный", 3000),
#      PremiumAccount("Премиум", 15000)
# ]
# for account in accounts:
#     print(f"\n=== {account.account_type()} ")
#     print(f"Баланс: {account.balance}₽")
#     print(account.withdraw(500))
#     print()
#     print(account.withdraw(1500))
#     print()
#     print(f"Итоговый баланс: {account.balance}₽")

# class Student:
#     def __init__(self,name,grade):
#         self.name = name
#         self.grade = grade
#         self.tasks_completed = 0
#
#     def complete_task(self,task_name,points):
#         self.tasks_completed += 1
#         print(f"{self.name} выполнил задание '{task_name}' за {points} баллов")
#         return points
#
# class HonorStudent(Student):
#     def __init__(self,name,grade,scholarship):
#         super().__init__(name,grade)
#         self.scholarship = scholarship
#         self.bonus_points = 0
#
#     def complete_task(self,task_name,points):
#          base_points = super().complete_task(task_name,points)
#          bonus = int(base_points * 0.1)
#          self.bonus_points += bonus
#          total_points = base_points + bonus
#          print(f"Отличник получает бонус: +{bonus} баллов (всего: {total_points})")
#          return total_points
#
# class TeamLeader(HonorStudent):
#     def __init__(self,name,grade,scholarship,team_size):
#         super().__init__(name,grade,scholarship)
#         self.team_size = team_size
#         self.team_points = 0
#
#     def complete_task(self,task_name,points):
#         personal_points = super().complete_task(task_name,points)
#
#         team_bonus = self.team_size * 5
#         self.team_points += team_bonus
#         total_with_team = personal_points + team_bonus
#
#         print(f"Лидер команды получает командный бонус: +{team_bonus} баллов")
#         print(f"Итого с командным бонусом: {total_with_team} баллов")
#         return total_with_team
#
# team_leader = TeamLeader("Анна", 11, 5000, 4)
# result = team_leader.complete_task("Математика", 100)
#
# print(f"Выполнено заданий: {team_leader.tasks_completed}")
# print(f"Бонусных баллов отличника: {team_leader.bonus_points}")
# print(f"Командных баллов: {team_leader.team_points}")

# class Calculator:
#     def __init__(self,name):
#         self.name = name
#         self.operation_count = 0
#
#     def calculate(self,operation,a,b,precision = 2):
#         self.operation_count += 1
#         if operation == "add":
#             result = a + b
#         elif operation =="subtrect":
#             result = a - b
#         else:
#             result = 0
#         return round(result,precision)
#
# class AdvancedCalculator(Calculator):
#     def __init__(self,name,max_precision):
#         super().__init__(name)
#         self.max_precision = max_precision
#
#     def calculate(self,operation,a,b,precision = 2):
#         precision = min(precision,self.max_precision)
#         result = super().calculate(operation,a,b,precision)
#         print(f"[{self.name}] {operation}({a}, {b}) = {result}")
#         return result
#
# class ScientificCalculator(AdvancedCalculator):
#     def calculate(self,operation,a,b,precision = 2):
#         super().calculate(operation,a,b,precision)
#         try:
#             result = super().calculate(operation,a,b,precision)
#             return result
#         except:
#             if operation == "power":
#                 result = round(a ** b,precision)
#                 print(f"[{self.name}] power({a}, {b}) = {result}")
#                 return result
#             return 0
#
# calc = ScientificCalculator("Sci-Calc", 3)
# print("Результат 1:", calc.calculate("add", 10.12345, 5.67890, 4))       # precision ограничится до 3
# print("Результат 2:", calc.calculate("power", 2, 8, 1))                  # новая операция
# print("Результат 3:", calc.calculate("subtract", 100, 25.5555, 2))       # обычная операция
#
# print(f"Операций выполнено: {calc.operation_count}")

# class BaseValidator:            Цепочка валидации
#     def __init__(self,name):
#         self.name = name
#         self.errors = []
#
#     def validate(self,data):
#         print(f"[{self.name}] Начинаем валидацию: {data}")
#         self.errors.clear()
#         return True
#
# class LengthValidator(BaseValidator):
#     def __init__(self,name,min_length):
#         super().__init__(name)
#         self.min_length = min_length
#
#     def validate(self,data):
#         super().validate(data)
#         if len(str(data)) < self.min_length:
#             self.errors.append(f"Слишком короткое значение (минимум {self.min_length})")
#             return False
#         return True
#
# class FormatValidator(LengthValidator):
#     def __init__(self,name,min_length,required_symbol):
#         super().__init__(name,min_length)
#         self.required_symbol = required_symbol
#
#     def validate(self,data):
#         super().validate(data)
#         if not super().validate(data):
#             return False
#
#         if self.required_symbol not in str(data):
#             self.errors.append(f"Отсутствует обязательный символ '{self.required_symbol}'")
#             return False
#         return True
#
#
# validator = FormatValidator("EmailValidator", 5, "@")
# print("=== Тест 1 ===")
# result1 = validator.validate("user@example.com")
# print(f"Результат: {result1}")
# print(f"Ошибки: {validator.errors}")
# print()
# print("\n=== Тест 2 ===")
# result2 = validator.validate("abc")
# print(f"Результат: {result2}")
# print(f"Ошибки: {validator.errors}")
#
# print("\n=== Тест 3 ===")
# result3 = validator.validate("verylongemail.com")
# print(f"Результат: {result3}")
# print(f"Ошибки: {validator.errors}")

# class A:
#     def method(self):
#         print("Метод A")
#         return "A"
#
# class B(A):
#     def method(self):
#         print("Метод B")
#         result = super().method()
#         return result + " -> B"
#
# class C(A):
#     def method(self):
#         print("Метод C")
#         result = super().method()
#         return result +  " -> C"
#
# class D(B,C):
#     def method(self):
#         print("Метод D")
#         result = super().method()
#         return result + " -> D"
#
# obj = D()
#
# print("MRO класса D:", D.__mro__)
# print("\nВызов obj.method():")
# result = obj.method()
# print(f"Итоговый результат: {result}")

# class Notification:
#     def __init__(self,message):
#         self.message = message
#         self.timestamp = "2025-01-01 12:00:00"
#         self.processed_by = []
#
#     def send(self):
#         self.processed_by.append("BaseNotification")
#         print(f"Базовая обработка: {self.message}")
#         return True
#
# class PriorityNotification(Notification):
#     def __init__(self,message,priority):
#         super().__init__(message)
#         self.priority = priority
#
#     def send(self):
#         super().send()
#         if self.priority == "HIGH":
#             print(f"⚠️ ВЫСОКИЙ ПРИОРИТЕТ: {self.message}")
#         self.processed_by.append(f"PriorityNotification({self.priority})")
#         return True
#
#
# class EncryptedNotification(PriorityNotification):
#     def __init__(self,message,priority,encryption_key):
#         super().__init__(message,priority)
#         self.encryption_key = encryption_key
#
#     def send(self):
#         encrypted_msg = f"[ENCRYPTED:{self.encryption_key}]{self.message}"
#         original_message = self.message
#         self.message = encrypted_msg
#
#         result = super().send()
#
#         self.message = original_message
#         self.processed_by.append("EncryptedNotification")
#         return result
#
# notification = EncryptedNotification(
#     "Секретные данные",
#     "HIGH",
#     "key123"
# )
#
# notification.send()
# print(f"\nОбработано модулями: {notification.processed_by}")

# import logging
#
# logging.basicConfig(level=logging.INFO)
#
#
# class OrderProcessor:
#     def __init__(self, name):
#         self.name = name
#
#
#     def process_order(self,order_data):
#         logging.info(f"[{self.name}]Начинаем проверку заказа {order_data['id']}")
#         return  True
#
#
#
# class PaymentProcessor(OrderProcessor):
#     def process_order(self,order_data):
#         super().process_order(order_data)
#         result = self.check_payment(order_data)
#         return result
#
#
#     def check_payment(self,order_data):
#         logging.info(f"[{self.name}] платеж заказа: {order_data['amount']}обработан успешно")
#         return True
#
# class InventoryProcessor(PaymentProcessor):
#     def process_order(self,order_data):
#         super().process_order(order_data)
#         result = self.check_inventory(order_data)
#         return result
#
#     def check_inventory(self,order_data):
#         logging.info(f"[{self.name}]Товары зарезервированы на складе.")
#         return True
#
#
# class ShippingProcessor(InventoryProcessor):
#     def process_order(self,order_data):
#         super().process_order(order_data)
#         result = self.calculate_shipping(order_data)
#         return result
#
#     def calculate_shipping(self,order_data):
#         logging.info(f"[{self.name}]Расчет доставки заказа: {order_data['address']}")
#         return True
#
# shipping_processor = ShippingProcessor("Полный процессор заказов")
# order = {
#     "id": "12345",
#     "items": ["товар1", "товар2"],
#     "amount": 2500,
#     "address": "Москва, ул. Примерная, 1"
# }
# result = shipping_processor.process_order(order)
# print(f"Заказ обработан: {result}")


# class Animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def eat(self,food,amount):
#         print(f"{self.name} eat {amount}g {food}")
#         return f"Съедено {amount}г"
#
# class Dog(Animal):
#     def __init__(self,name,age,breed):
#         super().__init__(name,age)
#         self.breed = breed
#
#     def eat(self,food,amount):
#         result = super().eat(food,amount)
#         print(f"Собака {self.breed} довольна")
#         return result
#
# class Puppy(Dog):
#     def __init__(self,name,age,breed):
#         super().__init__(name,age,breed)
#
#     def eat(self,food,amount):
#         result = super().eat(food,amount)
#         print("Щенок просит добавки!")
#         return result
#
#
# puppy = Puppy("Бобик", 1, "Лабрадор")
# result = puppy.eat("корм", 100)
# print(f"Результат: {result}")


# class GoblinMerchant:
#     def __init__(self,gold):
#         self.gold = gold
#     @staticmethod
#     def tax_rate():
#         return 0.1
#     @classmethod
#     def from_rich_merchant(cls):
#         rich_merchant = 1000
#         return cls(rich_merchant)
#
#     def buy_item(self,item_name,item_price):
#         if self.gold >= item_price:
#             self.gold -= item_price + item_price * self.tax_rate()
#             return f"Совершена покупка {item_name} остаток {self.gold}"
#         else:
#             return "Недостаточно золота!"
#
# merchant = GoblinMerchant(200)
# print(merchant.buy_item("Амулет удачи", 150))
#
#
# rich_merchant = GoblinMerchant.from_rich_merchant()
# print(rich_merchant.buy_item("Волшебный посох", 500))

# from abc import ABC,abstractmethod
# class Artifact:
#     @abstractmethod
#     def activate(self):
#         pass
#
# class HealingArtifact(Artifact):
#     def activate(self):
#         return "Восстановлено 50 здоровья"
#
# class DamageArtifact(Artifact):
#     def activate(self):
#         return  "Нанесено 30 урона врагу"
#
#
# heal_artifact = HealingArtifact()
# damage_artifact = DamageArtifact()
#
# print(heal_artifact.activate())
# print(damage_artifact.activate())

# class GoblinBank:
#
#     def __init__(self,golds):
#         self.golds = golds
#         if self.golds < 0 :
#             raise Exception ("ошибка количество золота не может быть отрицательным")
#         self.__gold = self.golds
#
#     def get_gold(self):
#         return self.__gold
#
#     def deposit_gold(self,amount):
#         if amount > 0:
#          self.__gold += amount
#          print(f"Добавлено 50 золота.Текущий баланс:{self.__gold}")
#
#     def withdraw_gold(self,amount):
#         if amount <= self.__gold:
#             self.__gold -= amount
#             print(f"Снято 30 золота. Текущий баланс:{self.__gold}")
#         else:
#                 print( "Недостаточно золота!")
#
# bank = GoblinBank(100)
#
# print(bank.get_gold())
# bank.deposit_gold(50)
# bank.withdraw_gold(30)
# bank.withdraw_gold(200)





