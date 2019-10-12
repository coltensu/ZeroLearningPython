"""
CRAPS赌博游戏
"""
import random


def toss_dice():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    print('A:', a, 'B:', b)
    toss_sum = a + b
    return toss_sum


if __name__ == '__main__':
    first_sum = toss_dice()
    if first_sum == 7 or first_sum == 11:
        print('Player win.')
    elif first_sum == 2 or first_sum == 3 or first_sum == 12:
        print('Boss win.')
    else:
        while True:
            print('continue.')
            next_sum = toss_dice()
            if next_sum == first_sum:
                print('Player win.')
                break
            elif next_sum == 7:
                print('Boss win.')
                break
            else:
                print('continue.')
    print('Done')
