'''
@Author : Priyanka Salunkhe
@Date : 2022-07-06  11:00:00
@Last Modified by : Priyanka Salunkhe
@Last Modified Time : 2022-07-06  11:35:00
@Title : Compute table of power of two.
'''

import sys


def power_of_two():
    """
       Description:
           Function is used to compute the power of two.
       Parameter:
           None
       Return:
           Returning nothing but print the table of power of two.
    """

    number = 2
    for i in range(exponent):
        value = number ** i
        print(value)


if __name__ == '__main__':

    exponent = int(sys.argv[1])
    if (exponent >= 0) and (exponent < 31):
        power_of_two()
    else:
        print("Enter the exponent between 0 to 31")





