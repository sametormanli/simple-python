class ChattyBot:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def greet(self):
        print(f'Hello! My name is {self.name}.')
        print(f'I was created in {self.birth_year}.')

    def remind_name(self):
        print('Please, remind me your name:')
        self.username = input()
        print(f'What a great name you have, {self.username}!')

    def age_guess(self):
        print('Let me guess your age.\n'
              'Enter remainders of dividing your age by 3, 5 and 7.')
        rem_3 = int(input())
        rem_5 = int(input())
        rem_7 = int(input())
        self.age = (rem_3 * 70 + rem_5 * 21 + rem_7 * 15) % 105
        print(f'Your age is {self.age}; that\'s a good time to start programming!')

    def count(self):
        print('Now I will prove to you that I can count to any number you want.')
        number = int(input())
        counter = 1
        while counter <= number:
            print(f'{counter}!')
            counter += 1

    def test(self):
        print("Let's test your programming knowledge.")
        print('Why do we use methods?\n'
              '1. To repeat a statement multiple times.\n'
              '2. To decompose a program into several small subroutines.\n'
              '3. To determine the execution time of a program.\n'
              '4. To interrupt the execution of a program.')
        while True:
            answer = input()
            if answer == '2':
                break
            print('Please, try again.')
        print('Correct, you are a genious!')

    def end(self):
        print('Have a nice day!')

    def main(self):
        self.greet()
        self.remind_name()
        self.age_guess()
        self.count()
        self.test()
        self.end()


bot = ChattyBot('R2-D2', 1977)
bot.main()