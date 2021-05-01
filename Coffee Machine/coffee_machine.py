class CoffeeMachine:
    requirements = {
        '1': [250, 0, 16, 1, 4],
        '2': [350, 75, 20, 1, 7],
        '3': [200, 100, 12, 1, 6]
    }

    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money

    def remaining(self):
        print(f'''The coffee machine has:
                \r{self.water} of water,
                \r{self.milk} of milk,
                \r{self.coffee_beans} of coffee beans,
                \r{self.cups} of disposable cups,
                \r{self.money} of money.''')

    def ingredient_check(self, ingredient):
        absence = False

        if self.water < self.requirements[ingredient][0]:
            absence = True
            print('Sorry, not enough water!')
        if self.milk < self.requirements[ingredient][1]:
            absence = True
            print('Sorry, not enough milk!')
        if self.coffee_beans < self.requirements[ingredient][2]:
            absence = True
            print('Sorry, not enough coffee beans!')
        if self.cups < 1:
            absence = True
            print('Sorry, no cup left!')

        if not absence:
            print('Making your coffee...')
            return True

    def buy(self):
        choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
        if choice == 'back':
            return
        if self.ingredient_check(choice):
            self.water -= self.requirements[choice][0]
            self.milk -= self.requirements[choice][1]
            self.coffee_beans -= self.requirements[choice][2]
            self.cups -= self.requirements[choice][3]
            self.money += self.requirements[choice][4]

    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add: '))
        self.milk += int(input('Write how many ml of milk do you want to add: '))
        self.coffee_beans += int(input('Write how many grams of coffee beans do you want to add: '))
        self.cups += int(input('Write how many disposable cups do you want to add: '))

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0

    def action(self):
        while True:
            choice = input('Write action (buy, fill, take, remaining, exit): ')
            if choice == 'buy':
                self.buy()
            elif choice == 'fill':
                self.fill()
            elif choice == 'take':
                self.take()
            elif choice == 'remaining':
                self.remaining()
            elif choice == 'exit':
                break
            else:
                print('Invalid entry.')


machine = CoffeeMachine(5000, 1000, 900, 130, 30)
machine.action()