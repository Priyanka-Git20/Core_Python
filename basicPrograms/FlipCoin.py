'''
@Author : Priyanka Salunkhe
@Date : 2022-07-05  9:30:00
@Last Modified by : Priyanka Salunkhe
@Last Modified Time : 2022-07-05  10:00:00
@Title : Flip Coin and print percentage of Heads and Tails.
'''

import random


def flip_percentage():
    """
        Description:
            Calculate the percentage of heads and tails
        Parameter:
             none
        Return:
            Return the printing message
    """

    numberOfFlip = int(input("Enter the how many times want to flip the coin:\n"))
    tail = 0
    head = 0
    for i in range(1,numberOfFlip+1):
        flipCheck = random.uniform(0,1)
        if flipCheck < 0.5:
            tail += 1
        else:
            head += 1
    tailPercentage = (tail/numberOfFlip)*100
    print("Tail percentage is",tailPercentage)
    headPercentage = 100 - tailPercentage
    print("Head percentage is",headPercentage)


flip_percentage()