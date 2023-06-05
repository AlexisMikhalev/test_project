board = [' ' for _ in range(9)]
# print(board)
# # Функция для отображения игрового поля
def display_board():
    print('---------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('---------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('---------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('---------')

# # Функция для хода игрока
def make_move(symbol):
    while True:
        position = int(input('Выберите позицию (от 1 до 9): ')) - 1
        if position < 0 or position >= 9 or board[position] != ' ':
            print('Некорректный ход. Попробуйте еще раз.')
        else:
            board[position] = symbol
            break
#
# # Функция для проверки победителя
def check_winner(symbol):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # горизонтальные линии
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # вертикальные линии
        [0, 4, 8], [2, 4, 6]              # диагональные линии
    ]
    for combo in winning_combinations:
         if board[combo[0]] == board[combo[1]] == board[combo[2]] == symbol:
             return True
    return False

# # Основной игровой цикл
def play_game():
    display_board()
    while True:
        make_move('X')
        display_board()
        if check_winner('X'):
            print('Игрок X победил!')
            break
        if ' ' not in board:
            print('Ничья!')
            break
        make_move('O')
        display_board()
        if check_winner('O'):
            print('Игрок O победил!')
            break

# Запуск игры
play_game()