board = list(range(1, 10))

jek_pots = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def draw_board():
    print('-------------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
    print('-------------')


def take_input(player_token):
    while True:
        player_answer = input('Вводим:' + player_token + " ")
        if not (player_answer in '123456789'):
            print('Будбте внимательнее! Попробуйте еще раз!')
            continue
        player_answer = int(player_answer)
        if str(board[player_answer - 1]) in 'XO':
            print('Уууупс! Занято! Еще раз')
            continue
        board[player_answer - 1] = player_token
        break


def chek_win():
    for each in jek_pots:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return True
    else:
        return False


def main():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if counter > 3:
            winner = chek_win()
            if winner:
                draw_board()
                print("Победааа!!")
                break
        counter += 1
        if counter > 8:
            draw_board()
            print("И ничья не взяла!")
            break


main()
