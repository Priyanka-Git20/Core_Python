'''
@Author : Priyanka Salunkhe
@Date : 2022-07-06  12:20:00
@Last Modified by : Priyanka Salunkhe
@Last Modified Time : 2022-07-06  12:40:00
@Title : Computes the prime factor of number.
'''

import math


def compute_prime_factor():
    """
       Description:
           Function is used to compute the prime factors of the number.
       Parameter:
           None
       Return:
           Returning nothing but print the message.
    """

    number =int(input("Enter the number for calculating the prime factor \n"))
    print("Prime factors of {} are".format(number))
    while number % 2 == 0:
        print(2),
        number = number / 2

    for i in range(3, int(math.sqrt(number))+ 1):

        while (number % i == 0):
            print(i)
            number = number / i

    if number > 2:
        print(number)


if __name__ == '__main__':
    compute_prime_factor()
