'''
@Author : Priyanka Salunkhe
@Date : 2022-07-06  11:50:00
@Last Modified by : Priyanka Salunkhe
@Last Modified Time : 2022-07-06  12:10:00
@Title : Comupte the Nth harmonic value.
'''


def harmonic_value():
    """
        Description:
            Prints the harmonic sum
        Parameter:
             none
        Return:
            Return the sum of nth harmonic number
    """

    harmonicSum = 0

    for i in range(1,harmonicValue+1):
        if (harmonicValue != 0):
            harmonicSum += 1/i
    print("Harmonic sum is ",harmonicSum)


if __name__ == '__main__':

    harmonicValue = int(input(("Enter the harmonic value:\n")))
    (harmonic_value())