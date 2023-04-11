# a = 5
# print(id(a))
#
# b = 3 + 2
# print(id(b))
# a = 0
# b = 0
#
# while id(a) == id(b):
#     a -= 1
#     b -= 1
#
# print(a)

# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
# list_id_before = id(shopping_center[-1])
#
# shopping_center[-1].append("Uniqlo")
# list_id_after = id(shopping_center[-1])
# print(list_id_before is list_id_after)

# L = [1,1,2,3,2]
#
# b = set(L)
#
# print(b)

# text = input("Введите текст:")
#
# unique = set(text)
#
# print("Количество уникальных символов: ", len(unique))

# a = {1, 2, 3, 4, 5, 6, 7, 8}
# b = {2, 4, 6, 8, 10, 12}
#
# a_set, b_set = set(a), set(b) # используем множественное присваивание
#
# a_and_b = a_set.symmetric_difference(b_set)
#
# print(a_and_b)

# some_var = (2,)
# if some_var is None:
#     print("NoneType")
# else:
#     print(type(some_var))
# a = None # пустая строка
# b = a or 1
# print(b)
# a = ""
# b = "bar"
#
# print(1 and a or b)
# a = ""
# b = "bar"
# if a and b:
#     print("Обе переменные истинные")
#     print(a,b)
# elif a or b:
#     print("Одна из переменных истинная")
#     print(a or b)
# else:
#     print("Обе переменные ложные")

# a = int(input())
# if type(a) == int and 100 <= a and a <= 999 and a % 2 == 0 and a % 3 == 0:
#     print("Ok!")
# else:
#     print("Ne ok")
# if type(a) == int:
#     if 100 <= a <= 999:
#         if a % 2 == 0:
#             if a % 3 == 0:
#                 print("Число удовлетворяет условиям")
# print(type(a))

# L = list(map(int, input().split()))
#
# print(all(L))

# M = [[(i, i*j) for j in range(1, 10)] for i in range(1, 10)]
# for n in M:
#     print(n)

# # L = [input(f"Введите {i+1} элемент") for i in range(5)]
# # print(L)
# L = [int(input()) % 2 == 0 for i in range(5)]
# print(L)
# L = [i for i in range(10)]
# # # 0 1 2 3 4 5 6 7 8 9
# M = [i for i in range(10,0,-1)]
# #
# # for a, b in zip(L,M):
# #     print('a =', a, 'b =', b, "proizvedenie=", a*b)
# N = [a*b for a, b in zip (L, M)]
# print(N)

# text = input()  # получаем строку

# last = text[0]  # сохраняем первый символ
# count = 0  # заводим счетчик
# result = ''  # и результирующую строку
#
# for c in text:
#     if c == last:  # если символ совпадает с сохраненным,
#         count += 1  # то увеличиваем счетчик
#     else:
#         result += last + str(count)  # иначе - записываем в результат
#         last = c  # и обновляем сохраненный символ с его счетчиком
#         count = 1
#
# result += last + str(count)  # и добавляем в результат последний символ
# print(result)

# def linear_solve(a, b):
#     return b / a
# print(linear_solve(0, 1))

# M = {'a': 1,
#      'b': 0,
#      'c': -1}
# def D(**M):
#     return b**2 - 4*a*c
#
# def squad(*M):
#     if D() < 0:
#         return "not resheniy"
#     elif D() == 0:
#         return -b/(2*a)
#     else:
#         return (-b - D()**0.5)/(2*a), (-b + D()**0.5)/(2*a)
# print(D())
# print(squad())
# print(type(squad()))

# def equal(N, S):
#     if S < 0:
#         return False
#     if N < 10:
#         return N == S
#     else:
#         return equal(N // 10, S - N % 10)
# print(equal(13,40))

# iter_obj = iter("Hello!")
#
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))

# L = ['THIS', 'IS', 'LOWER', 'STRING']
# print(list(map(str.lower, L)))
# print(M)

# def positive(x):
#     return x % 2 == 0  # функция возвращает только True или False
#
#
# result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])
#
# # Возвращается итератор, т.е. перечисляйте или приводите к списку
# print(list(result))
# some_list = [i - 10 for i in range(20)]
# def pow2(x): return x**2
# def positive(x): return x > 0
#
# print(some_list)
# print(list(map(pow2, filter(positive, some_list))))

# d = {2 : "c", 1 : "d", 4 : "a", 3 : "b"}
# print(dict(sorted(d.items())))
# print(sorted(d.items(), key=lambda x: x[0]))

# data = [
#    (82, 1.91),
#    (68, 1.74),
#    (90, 1.89)
#    (73, 1.79),
#    (76, 1.84)
# ]
# print(sorted(data, key=lambda x: x[0]))

# a = ["asd", "bbd", "ddfa", "mcsa"]
#
# print(list(map(len, a)))

a = ["это", "маленький", "текст", "обидно"]

print("Love wife")