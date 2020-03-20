# This is a small program that solves the collatz sequence and keeps track of how many counts did it take to reach 1
import sys

while True:
    number = input('Enter a positive integer: ')
    count = 0
    try:
        int(number)
        if int(number) < 0:
            print('Sorry, number must be a positive integer, try again')
            continue
    except ValueError:
        print('Invalid Entry! Try Later!')
        print('Quitting program')
        sys.exit(0)
    else:
        number = int(number)
        ORIGINAL = number
    while number != 1:
        count += 1
        if number % 2:  # if this is an ODD number
            number = 3 * number + 1
        elif not number % 2:  # if EVEN number
            number = number // 2  # double slash means integer divison
        print(number)
    print('The number ' + str(ORIGINAL) + ' took ' +
          str(count) + ' counts to reach 1!')
    print('Do you want to try again?')
    answer = input("(Y/N >>>")
    if answer[0].lower() == "n":
        print('program terminated')
        break
input("Press enter to continue")
