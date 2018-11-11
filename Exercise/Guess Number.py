from random import randint

print('In this game. you have 5 times to try this game, ')
print('and after 5times, the game will stop')
x = randint(0,300)
for count in range(0,5):
    print('please input a number between 0~300:')
    digit=int(input())
    if digit == x:
        print('HaHa, NICE WORK!')
    elif digit>x:
        print('Emmmm, meybe you should try a small one.')
    else:
        print('Ok, you should try a large one.')
