# def greet():
#     print("Hello World")
# greet()

# def greet_user (name):
#     print("Privet", name)
# greet_user("Igor")

# def sum_nambers(a,b):
#     print(a + b)
# sum_nambers(5,3)
# sum_nambers(-1,10)

# def is_even(number):
#     if number % 2 == 0:
#         print("CHetnoe chislo")
#     else:
#         print(" ne chetnoe")
#
# is_even(3)

# def analyze_numbers(numbers):
#     if numbers is not None:
#         average = sum(numbers) / len(numbers)
#         min_value = min(numbers)
#         max_value = max(numbers)
#         even_count = sum(1 for num in numbers if num % 2 == 0)
#         return {
#             "average": average,
#             "min": min_value,
#             "max": max_value,
#             "even_count": even_count
#         }
#     return None
#
# number_list = [5, 10, 2, 4, 20, 1]
# result = analyze_numbers(number_list)
# print(result)
# def filter_list(data, threshold):
#         return [item for item in data if item >= threshold]
# data = [1, 5, 10, 2, 8, 12]
# threshold = 9
# result = filter_list(data,threshold)
# print(result)


# def get_grade(score):
#     if score >= 90:
#         return "A"
#     elif score >=80:
#         return "B"
#     elif score >=70:
#         return "C"
#     else:
#         return "F"
# print(get_grade(7))


# def is_even(x):
#         return x % 2 == 0
# def filter_even_sum(a, b, c):
#     return sum(x for x in (a,b,c) if is_even(x) )
#
# print(filter_even_sum(4,5,6))


# def number_analyzer(num):
#     def is_positive():
#      return num > 0
#     def is_even():
#         return num % 2 == 0
#     analis = {
#             "is_positive()":is_positive(),
#             "is_even()":is_even(),
#             "square": num ** 2,
#             "cube": num ** 3
#     }
#     return analis
# print(number_analyzer(4))
