random_matrix = [
   [9, 2, 1],
   [2, 5, 3],
   [4, 8, 5]
]
min_value_rows = []
min_index_rows = []
max_value_rows = []
max_index_rows = []
for row in random_matrix:
    min_index = 0
    min_value = row[min_index]
    max_index = 0
    max_value = row[max_index]
    for index_col in range(len(row)):
        if row[index_col] < min_value:
            min_value = row[index_col]
            min_index = index_col
        if row[index_col] > max_value:
            max_value = row[index_col]
            max_index = index_col
    min_value_rows.append(min_value)
    min_index_rows.append(min_index)
    max_value_rows.append(max_value)
    max_index_rows.append(max_index)
print("Minimal elements:", min_value_rows) # минимальные элементы
print("Their indices:", min_index_rows) # их индексы
print("Maximal elements:", max_value_rows) # максимальные элементы
print("Their indices:", max_index_rows) # их индексы








# n = 20
# for i in range(n, 1, -1):
#     print("*" * i, ' ' * (n - i) * 2, '*' * i),
# for i in range(1, n + 1):
#     print("*" * i, ' ' * (n - i) * 2, '*' * i),

# inttemp = int(input("Insert temperature:"))
# temperaturerain = None
# realRain = None
#
# if temp > 0:
#     rain = input("Rainy?") == "yes"
#     if rain:
#         realRain = input("Really Rainy?") == "yes"
# if 40 >= temp >= 20:
#     if rain:
#       decision = str("Futbolka shorti dojdevik")
#     else:
#       decision = "Futbolka shorti"
# elif 20 > temp >= 0:
#     if rain:
#         if  realRain:
#             decision = "Palto rezinovie sapogi i zont"
#         else:
#             decision = "palto i dojdevik"
#     else:
#         decision = "palto"
# else:
#     decision = "puhovik"
# print(decision)


# temp = input("Insert temperature: ")
# rain = input("Insert rain if rainy insert 1 and if no insert 0:")
# if 20 <= int(temp) <=30:
#     if  int(rain) == 0:
#         print("Oden futbolku")
#     else:
#         print("Dojevik")
# elif 20 > int(temp) >= 0:
#     if  int(rain) == 0:
#         print("palto")
#     elif int(rain) > 2:
#         print("palto zont sapogi")
#     else:
#         print("palto dojdevik")
# else:
#     print("Puhovik")

# temperature = int(input("Input temperature: "))
#
# #для указания начальных статусов дождливости воспользуемся False или None
# rainy = None
# heavyRain = None
#
# #если температура <0 то про дождь спрашивать бессмысленно
# if temperature > 0:
#    rainy = input("Is rainy: ") == "yes", "да"
# #если идет дождь спросим насколько он серьезный
#    if rainy:
#        heavyRain = input("Is heavy rain: ") == "yes", "да"
#
#
# #реализуем логику по схеме
# decision = "Не решил что брать. Останусь дома."
# if (temperature) > 20 and (temperature < 30) :
#    if rainy:
#        decision = "Взять футболку шорты и дождевик"
#    else:
#        decision = "Взять футболку и шорты"
# elif temperature > 0:
#    if rainy:
#        if heavyRain:
#            decision = "Взять пальто, резиновые сапоги и зонт"
#        else:
#            decision = "Взять пальто и дождевик"
#    else:
#        decision = "Взять пальто"
# else:
#    decision = "Взять пуховик"
#
#
# #Выведем наше решение на экран
# print(decision)
