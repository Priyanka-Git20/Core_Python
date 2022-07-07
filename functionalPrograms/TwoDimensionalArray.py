'''
    @Author : Priyanka
    @Date : 2022-04-06  11:00:00
    @Last Modified by : Priyanka
    @Last Modified Time : 2022-04-06  11:30:00
    @Title : Print the two dimensional array.
'''

arr = []


def add_element_in_array():
    """
        Description:
            adding values in 2D Array
        Parameter:
            None
        Return:
            Returning nothing
    """
    rows = int(input(("Enter the number of rows:\n")))
    columns = int(input(("Enter the number of columns:\n")))

    for i in range(rows):
        row = []
        for j in range(columns):
            num = int(input("Enter the matrix : "))
            row.append(num)
        arr.append(row)


def print_2d_array():
     """
        Description:
            printing the 2D Array
        Parameter:
            None
        Return:
            Returning nothing but printing the array
        """

     for i in arr:
        for j in i:
            print(j, end=" ")
        print()


if __name__ == '__main__':
    add_element_in_array()
    print_2d_array()