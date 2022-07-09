'''
   @Author : Priyanka Salunkhe
   @Date : 2022-07-07  10:20:00
   @Last Modified by : Priyanka Salunkhe
   @Last Modified Time : 2022-07-07  12:30:00
   @Title : Tic tac toe game.
'''
import random

board = {
    'A1': '', 'A2': '', 'A3': '',
    'B1': '', 'B2': '', 'B3': '',
    'C1': '', 'C2': '', 'C3': ''
}

totalMoves = 0
endCheck = 1


def gameBoardCreation():
    """
       Description:
            Create the board with key values.
       Parameter:
            None
       Return:
            Printing the board with key.
    """

    print('A1|A2|A3')
    print('-- ++ --')
    print('B1|B2|B3')
    print('-- ++ --')
    print('C1|C2|C3')
    print('*************************')


def winConditionCheck():
    """
        Description:
            Checking winning condition for player 1 and player 2.
        Parameter:
            None
        Return:
            Return the value 1.
    """

    if(board['A1'] == 'X') and (board['A2'] == 'X') and (board['A3'] == 'X'):
        print("Player1 won the game")
        return 1
    if (board['B1'] == 'X') and (board['B2'] == 'X') and (board['B3'] == 'X'):
        print("Player1 won the game")
        return 1
    if (board['C1'] == 'X') and (board['C2'] == 'X') and (board['C3'] == 'X'):
        print("Player1 won the game")
        return 1
    if (board['A1'] == 'X') and (board['B1'] == 'X') and (board['C1'] == 'X'):
        print("Player1 won the game")
        return 1
    if (board['A2'] == 'X') and (board['B2'] == 'X') and (board['C2'] == 'X'):
        print("Player1 won the game")
        return 1
    if (board['A3'] == 'X') and (board['B3'] == 'X') and (board['C3'] == 'X'):
        print("Player1 won the game")
        return 1
    if (board['A1'] == 'X') and (board['B2'] == 'X') and (board['C3'] == 'X'):
        print("Player1 won the game")
        return 1
    if (board['A3'] == 'X') and (board['B2'] == 'X') and (board['C1'] == 'X'):
        print("Player1 won the game")
        return 1
    if (board['A1'] == 'O') and (board['A2'] == 'O') and (board['A3'] == 'O'):
        print("Player2 won the game")
        return 1
    if (board['B1'] == 'O') and (board['B2'] == 'O') and (board['B3'] == 'O'):
        print("Player2 won the game")
        return 1
    if (board['C1'] == 'O') and (board['C2'] == 'O') and (board['C3'] == 'O'):
        print("Player2 won the game")
        return 1
    if (board['A1'] == 'O') and (board['B1'] == 'O') and (board['C1'] == 'O'):
        print("Player2 won the game")
        return 1
    if (board['A2'] == 'O') and (board['B2'] == 'O') and (board['C3'] == 'O'):
        print("Player2 won the game")
        return 1
    if (board['A3'] == 'O') and (board['B3'] == 'O') and (board['C3'] == 'O'):
        print("Player2 won the game")
        return 1
    if (board['A1'] == 'O') and (board['B2'] == 'O') and (board['C3'] == 'O'):
        print("Player2 won the game")
        return 1
    if (board['A3'] == 'O') and (board['B2'] == 'O') and (board['C1'] == 'O'):
        print("Player2 won the game")
        return 1
    return 0


def inputFromPlayer():
    """
        Description:
            Take a input from plaayer and print on the board and display this board.
        Parameter:
            None
        Return:
            Return nothing but printing the board
    """

    totalMoves = 0
    player = 1
    while True:
        print(board['A1'] + ' | ' + board['A2'] + ' | ' + board['A3'])
        print('-+-+-')
        print(board['B1'] + ' | ' + board['B2'] + ' | ' + board['B3'])
        print('-+-+-')
        print(board['C1'] + ' | ' + board['C2'] + ' | ' + board['C3'])
        print('-+-+-')

        endCheck = winConditionCheck()

        if totalMoves == 9 or endCheck == 1:
           break

        while True:
           if player == 1:
               p1_input = input("player one")
               if p1_input.upper() in board and board[p1_input.upper()] == '':
                   board[p1_input.upper()]='X'
                   player = 2
                   break
               else:
                   print("Invalid input, please try again")
                   continue
           else:
               list1 = ["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
               p2_input = random.choice(list1)
               if p2_input.upper() in board and board[p2_input.upper()] == '':
                   board[p2_input] = 'O'
                   player = 1
                   break
               else:
                    print("Invalid input, please try again")
                    continue
        totalMoves += 1
        print('*****************************')
        print()


if __name__ == '__main__':
    gameBoardCreation()
    inputFromPlayer()
