#!/usr/bin/env python3

# Created by: Izza Khalid
# Created on: November 2019
# This program finds the L.C.M. of two input number
# with user input


def main():
    # This function finds the L.C.M. of two input number

    # input
    print("Enter 2 positive integers to find their L.C.M!")

    # process & output
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if num1 > num2:
            greater = num1
        else:
            greater = num2

        while(True):
            if((greater % num1 == 0) and (greater % num2 == 0)):
                print("")
                print("The L.C.M. of {0} and {1} = {2}".format(num1, num2,
                      greater))
                break
            greater = greater + 1

    except Exception:
        print("")
        print("You did not sub in integers!")


if __name__ == "__main__":
    main()
