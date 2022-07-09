'''
   @Author : Priyanka Salunkhe
   @Date : 2022-07-07  12:40:00
   @Last Modified by : Priyanka Salunkhe
   @Last Modified Time : 2022-07-07  12:30:00
   @Title : Generate distinct coupon number.
'''


import random


if __name__=='__main__':

    coupon=int(input("How many coupon numbers do you want:"))
    digits=int(input("How many digits of coupon number would you prefer:"))
    created=0
    list1=[]
    counter=0
    while created<coupon:
        special=''
        for x in range(digits):
            number=str(random.randint(0,9))
            counter=counter+1
            special=special+number
        if special in list1:
            continue
        else:
            list1.append(special)
            created=created+1
    print("The distinct coupon numbers are:")
    for y in list1:
        print(y)
    print("Total random number needed to have all coupons numbers:")
    print(counter)

