'''
@Author : Priyanka Salunkhe
@Date : 2022-07-05  10:30:00
@Last Modified by : Priyanka Salunkhe
@Last Modified Time : 2022-07-05  11:00:00
@Title : Check the year is leap or not  .
'''


def check_leap_year():
    """
       Description:
           Function is used to check year is leap or not.
       Parameter:
           None
       Return:
           Returning nothing but print the message.
    """

    if (year % 400 == 0) and (year % 100 == 0) :
        print("{} is leap year".format(year))
    elif (year % 4 == 0) and (year % 100 != 0):
        print("{} is a leap year".format(year))
    else:
        print("{} is not a leap year".format(year))


if __name__ == '__main__':
     year = int(input(("Enter the year you want to check is it leap or not:\n")))

     if (year > 9999) or (year < 1000):
          print("Enter the year with 4 digit number")
     else:
          check_leap_year()
