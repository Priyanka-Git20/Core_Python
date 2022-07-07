'''
    @Author : Priyanka Salunkhe
    @Date : 2022-07-06  23:20:00
    @Last Modified by : Priyanka Salunkhe
    @Last Modified Time : 2022-07-06  23:30:00
    @Title : Find the roots of the Quadratic equation.
'''

import math


def compute_roots():
    delta = math.pow(b, 2) - 4.0 * a * c

    if (delta > 0):
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        print("The roots are ", root1, root2)
    elif (delta == 0):
        root1 = -b / (2 * a)
        print("The root is ", root1)
    else:
        print("Roots are imaginary.")


if __name__ == '__main__':
    a = int(input(("Enter Value Of a:\n")))
    b = int(input(("Enter Value Of b:\n")))
    c = int(input(("Enter Value Of c:\n")))
    compute_roots()