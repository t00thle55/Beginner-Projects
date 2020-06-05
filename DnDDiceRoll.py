import random


def dice_roll():
    roll = random.randint(1,20)
    return roll

def main():
    while True:
        response = input('Would you like to roll? y/n')
        if response == ('y'):
            print(str(dice_roll()))

        else:
            print('Goodbye')
            break
print(main())
