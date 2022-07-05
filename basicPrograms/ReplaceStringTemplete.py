'''
@Author : Priyanka Salunkhe
@Date : 2022-07-05  9:00:00
@Last Modified by : Priyanka Salunkhe
@Last Modified Time : 2022-07-05  9:20:00
@Title : Replace String Template  .
'''


def replace_string():
    """
       Description:
           Function is used to replace the string
       Parameter:
           None
       Return:
           Returning nothing but print the message.
    """

    oldTemplete = "Hello name How are you!"
    userName = input(("Enter the user name:\n"))

    if len(userName) < 3:
         print("Please enter the string with more than three characters.")
    else:
         newTemplete = oldTemplete.replace("name",userName)
         print(newTemplete)

replace_string()