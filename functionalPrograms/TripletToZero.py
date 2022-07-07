'''
    @Author : Priyanka
    @Date : 2022-07-06  19:00:00
    @Last Modified by : Priyanka
    @Last Modified Time : 2022-07-06  19:30:00
    @Title : Finding the distinct triplets.
'''


def findingTriplet():
    """
        Description:
            finding triplet of combination on addition
        Parameter:
            array and size of array
        Return:
            printing triplet if it is in array
    """

    tripletFound = False
    for i in range (0, n-2):
        for j in range (i+1, n-1):
            for k in range (j+1, n):
                if (arr[i] + arr[j] + arr[k]) == 0:
                    print ("Triplet Found: ", end=" ")
                    print (arr[i], arr[j], arr[k])
                    tripletFound = True

    if tripletFound == False:
        print("Triplet is not found")


if __name__ == '__main__':
    arr = [0,1,2,-2,-3,4]
    n = len(arr)
    findingTriplet()

