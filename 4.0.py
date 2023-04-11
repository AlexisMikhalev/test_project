# n = 4
# for i in range(n):
#     print("*"*i)

# def print_2_add_2():
#     print(2+2)
#
# def hello_world():
#     print("hello, world!")

# def pow_func(base):
#    print(base ** 2)
#
# pow_func(35)  # 9
# pow_func(5)
#
# def pow_func(n, a):
#     if n % a == 0:
#         print(f"Число {n} является делителем числа {a}")
#     else:
#         print(f"Число {n}  ne является делителем числа {a}")
# pow_func(3,3)
# def stars(n):
#     for i in range(n+1):
#         print("*"*i)
#
# stars(10)

# def pow_func(a):
#     c = 0
#     for i in range(1, a + 1):
#         if  a % i == 0:
#             c += 1
#     return c
# print(pow_func(5))
#
# def check_palindrome(text):
#     text = text.lower()  # привели все к нижнему регистру
#     text = text.replace(" ", "")
#     if  text == text[::-1]:
#         return True
#     else:
#         return False
# check_palindrome("Кит на мре не романтик")

# x = 3
# def function():
#     print(x)
#     return x
#
# print(function())

# x = 3


# def func():
#    global x # объявляем, что переменная является глобальной
#    print(x)
#    x = 5
#    x += 5
#    return x
#
#
# func()
# print(x)

# def adder(*nums):
#     sum_ = 1
#     for n in nums:
#         sum_ *= n
#
#     return sum_
#
#
# print(adder(2, 4))
# def rec_fibb(n):
#     print(rec_fibb(n - 1) + rec_fibb(n - 2))
#
# rec_fibb(10)  # 55
# print(rec_fibb(6))

# def nat():
#     a = 0
#     yield a
#     for nums in nat():
#         print(nums)
# nat(3)

# def summ(n):
#     if n == 1:
#         return 1
#     return n + summ(n - 1)
# print(summ(5))

# def fib():
#     a, b = 0, 1
#     yield a
#     yield b
#     while True:
#         a, b = b, a + b
#         yield b

# str_ = "my tst"
# str_iter = iter(str_)
#
# print(type(str_))  # строка
# print(type(str_iter))
#
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))
# print(next(str_iter))

# def my_decorator(fn):
#     print("Этот код будет выведен один раз в момент декорирования функции")
#     def wrapper(*args, **kwargs):
#         print('Этот код будет выполняться перед каждым вызовом функции')
#         result = fn(*args, **kwargs)
#         print('Этот код будет выполняться после каждого вызова функции')
#         return result
#     return wrapper

