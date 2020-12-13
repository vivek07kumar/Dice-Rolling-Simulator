from random import randrange
from time import sleep
done1 = True
done3 = True
print()
print('               >>>>>>>>>>  Dice Rolling Simulator  <<<<<<<<<<')
print()
print()
while done1 :
    done2 = True
    if done3 :
        input('>> Press ENTER to Begin !')
        print()
    sleep(0.50)
    dice_number = randrange(1,7)
    print('+---------+')
    if dice_number == 1 :
        print('|         |')
        print('|    *    |')
        print('|         |')
    if dice_number == 2 :
        print('| *       |')
        print('|         |')
        print('|       * |')
    if dice_number == 3 :
        print('|       * |')
        print('|    *    |')
        print('| *       |')
    if dice_number == 4 :
        print('| *     * |')
        print('|         |')
        print('| *     * |')
    if dice_number == 5 :
        print('| *     * |')
        print('|    *    |')
        print('| *     * |')
    if dice_number == 6 :
        print('| *  *  * |')
        print('|         |')
        print('| *  *  * |')
    print('+---------+')
    print()
    print('Number : ',dice_number)
    while done2 :
        print()
        choice = input('>> Press R to roll Dice Again ! or Press E to Exit : ')
        if choice == 'R' or choice == 'r' :
            done2 = False
            done3 = False
            print()
        elif choice == 'E' or choice == 'e' :
            done2 = False
            done1 = False
            print()
        else :
            print()
            print('                            >>  Wrong Input !  <<')
