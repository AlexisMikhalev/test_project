# random_matrix = [
#    [9, 2, 1],
#    [2, 5, 3],
#    [4, 8, 5]
# ]
# min_value_rows = []
# min_index_rows = []
# max_value_rows = []
# max_index_rows = []
# for row in random_matrix:
#     min_index = 0
#     min_value = row[min_index]
#     max_index = 0
#     max_value = row[max_index]
#     for index_col in range(len(row)):
#         if row[index_col] < min_value:
#             min_value = row[index_col]
#             min_index = index_col
#             print('изменили мин')
#         if row[index_col] > max_value:
#             max_value = row[index_col]
#             max_index = index_col
#             print('изменили макс')
#     min_value_rows.append(min_value)
#     min_index_rows.append(min_index)
#     max_value_rows.append(max_value)
#     max_index_rows.append(max_index)
# print("Minimal elements:", min_value_rows) # минимальные элементы
# print("Their indices:", min_index_rows) # их индексы
# print("Maximal elements:", max_value_rows) # максимальные элементы
# print("Their indices:", max_index_rows) # их индексы
#
#
# lists = [[1, 2, 3],
#                [7, 1, 1],
#                [123, 2, -1]]

# max_value = []
# isKva = None
# for row in lists:
#     if len(row) == len(lists):
#         isKva = True
#         max_value.append(True)
#     else:
#         max_value.append(False)
#
#
# if all(max_value):
#     print('kvadrat')
# else:
#     print('me kvadr')
test_matrix = [[1, 2, 3],
               [7, -1, 2],
               [123, 2, -1]]
max_value = None
for row in test_matrix:
    max_value = row[0]
    for index_col in range(len(row)):
        if row[index_col] > max_value:
            max_value = row[index_col]
print("Maximal elements:", max_value)




