from random import choice

def game(user, com, elements, way):
    index = elements.index(user)
    half = len(elements) // 2
    if index > half:
        elements = elements[index - half:] + elements[:index - half]
    elif index < half:
        elements = elements[index + half:] + elements[:index + half + 1]
    idx_user, idx_com = elements.index(user), elements.index(com)
    if way and (idx_user < idx_com) or not way and (idx_com < idx_user):
        print(f'Sorry, but the computer chose {com}')
        return 'l'
    elif way and (idx_com < idx_user) or not way and (idx_user < idx_com):
        print(f'Well done! The computer chose {com} and failed.')
        return 'w'
    else:
        print('There is a draw.')
        return 'd'


def elements():
    elements = input()
    print("Okay, let's start...")
    if elements:
        elements = elements.split(',')
        if elements.index('rock') < elements.index('paper'):
            return elements, True
        else:
            return elements, False
    else:
        return ['rock', 'paper', 'scissors'], True


def play(score, gestures, way):
    while True:
        user = input()
        if user == '!exit':
            print('Bye!')
            break
        elif user == '!rating':
            print('Your rating:', score)
        elif user in gestures:
            result = game(user, choice(gestures), gestures, way)
            if result == 'w':
                score += 100
            if result == 'd':
                score += 50
        else:
            print('Invalid input.')
    return score


def initialize():
    name = input('Enter your name: ')
    print('Hello,', name)
    try:
        rating = open('rating.txt')
        for line in rating:
            if line.split()[0] == name:
                score = int(line.split()[1])
                break
        else:
            score = 0
        rating.close()
        return score
    except FileNotFoundError:
        return 0


def main():
    score = initialize()
    gestures, way = elements()
    play(score, gestures, way)


main()
