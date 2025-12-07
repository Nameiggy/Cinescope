import copy
import math
import string
from multiprocessing.resource_sharer import stop
from operator import index
from os import remove
from platform import android_ver  # if-else
from tkinter import messagebox
from tkinter.font import names
from turtledemo.penrose import start

import step

# 1
# my_list = [1, 2, 3, 4, 5]
# for number in my_list:
#    if number % 2 == 0:
#     print(f"{number} - Число четное")
# else:
#     print(f"{number} - Не четное число")


                                    #2
# quantity = int(input("Введите количество товара"))
# price_per_unit = float(input("Введите сумму за 1 единицу "))
#
# total_sum = quantity * price_per_unit
#
# if total_sum > 10000:
#     discount = total_sum * 0.20
# elif total_sum < 5000:
#     discount = total_sum * 0.10
# else:
#     discount = 0
# final_sum = total_sum - discount
# print(final_sum)

                                   # 3
# quantity = str(input("Введите пароль "))
# password = "qwerty123"
# if password == quantity:
#     print("Welcome " + quantity)
# else:
#     print("нужен пароль ")


                                    #list

                                  #1

# list1 = [1,2,3,4,5,6,7,8,9,10]
# total_sum = sum(list1)
# print(total_sum)

                                   # 2
# nums =[3,4,11,4,4]
# nums[2]= 100
# print(nums)

                                   # 3
# my_list =list(range(1,101,3))
# print(my_list)
                                # dict

                              # 1
# menu ={"Салат цузарь": 450,
#        "Паста":600,
#        "Ризотто":800,
#        "Стейк":1200,
#        "Десерт":350}
#
# menu["Карпачо"]=1500
# print("Меню ресторана")
# for dish, price in menu.items():
#     print(f"{dish}: {price}")
# menu["Карпачо"]=1100
# print("\nОбновленное меню ресторана:")
# for dish, price in menu.items():
#     print(f"{dish}: {price}")

                               # 2
# products ={"яблоко": 100, "банан": 50, "апельсин": 70}
# order ="яблоко"
# if order in products:
#     print(products[order])
# else:
#     print("net takogo producta")

                               # for

                               # 1
# for i in range(1,6):
#     print(i*2)


                               # 2
# n =5
# sumnubers = sum(range(1,n+1))
# print(sumnubers)

                               # 3
# for i in range(10,0,-1):
#     print(i)

                               # 4
# fruits = ['apple', 'banana', 'orange', 'strawberry']
# for fruit in fruits:
#     print(fruit)

                               # 5
# numbers = [3,8,1,9,4]
# maxnumbers = max(numbers)
# print(maxnumbers)

                               # 6
# products = {"яблоко": 100, "банан": 50, "апельсин": 70}
# sumproducts = sum(products.values())
# print(sumproducts)

                                 # while
#                                  # 1
# i =1
# while i <= 10:
#     print(i)
#     i += 1
                                   # 2
# n=10
# summa =0
# i = 1
# while i <= n:
#     summa += i
#     i += 1
#     print(summa)
                                   # 3
# nums = [2, 7, 4, 9, 6, 5]
# i=0
# while i<len(nums):
#     if nums [i] % 2==0:
#         nums.pop(i)
#     else:
#         i=i+1
# print(nums)
                             # Изменяемые типы данных
# a = [1, 2, 3]
# b = a.copy()
# b[0]=100
# print(a)
# print(b)
# print(id(a))
# print(id(b))
                            # Доп задание (составное)
# time = 7200
# hours = time/3600
# minutes = time%3600/60
# seconds = time%60
# print(hours, "час", minutes, "минута", seconds, "секунда")


# my_list = {
#     "Name":"Igor",
#     "Age":"19",
#     "Mail":"exampl@mail.ru",
# }
# personal ={
#     "Name":"Anthony",
#     "Age":"19",
#     "Mail":"populat@mail.ru",
#     "Number":"8973245523"
# }
# my_list ["Number"] = "79788039204"
# new_list = my_list | personal
# if "Number" in new_list:
#     new_list["Number"] = new_list["Number"][:3] + "*****" +new_list["Number"][-2:]
# if "Mail" in new_list:
#     emai_parts= new_list["Mail"].split("@")
#     new_list["Mail"] = emai_parts[0][:3] +"*****"+emai_parts[1]
# print(new_list)

# residence = {
#     "residence": {
#         "country": "Thailand",
#         "city": "Phuket",
#         "district": "Thalang"
#     }
# }
# my_list = {
#     "Name":"Igor",
#     "Age":"19",
#     "Mail":"exampl@mail.ru",
# }
# new_info = residence |  my_list
# country = residence["residence"]["country"]
# print(country)

# list1= {10, 20, 30, 40, 50}
# list2= {20, 25, 30, 35, 40}
# difference_set = list1.difference(list2)
# difference_set2 = list1.symmetric_difference(list2)
# difference_set3 =list1 & list2
# print(difference_set, "\n" , difference_set2, "\n" , difference_set3)




