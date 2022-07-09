'''
   @Author : Priyanka Salunkhe
   @Date : 2022-07-07  13:20:00
   @Last Modified by : Priyanka Salunkhe
   @Last Modified Time : 2022-07-07  13:55:00
   @Title : Gambler Simulation.
'''


import random


def gambler_game():
    """
        Description:
            Printing the number of Wins and Percentage of Win and Loss.
        Parameter:
            None
        Return:
            Returning nothing printing the percentage of win and loss.
    """

    AmountOfBet = 1
    wins = 0

    for i in range(numOfTimes):
        cashOfThePlayer = stake

        while (cashOfThePlayer > 0) and (cashOfThePlayer < goal):
            betCheck = random.randint(0,1)
            if betCheck == 1 :
                cashOfThePlayer += AmountOfBet
            else:
                cashOfThePlayer -= AmountOfBet

        if cashOfThePlayer == goal:
            wins += 1

    print("{} wins out of {} trials".format(wins,numOfTimes))
    winPercentage = (wins/numOfTimes)*100
    print("Percentage of win: ", winPercentage)
    print("Percentage of loss: ", 100 - winPercentage)


if __name__ == '__main__':
    stake = int(input("Enter Stake: "))
    goal = int(input("Enter Goal You Want Achieve: "))
    numOfTimes = int(input("Enter Number Of Times You Want To Try: "))
    gambler_game()

