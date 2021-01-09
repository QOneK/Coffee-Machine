def output(water,milk,coffee,cups,money):
    print("")
    print("The coffee machine has:")
    print(str(water) + " of water")
    print(str(milk) + " of milk")
    print(str(coffee) + " of coffee beans")
    print(str(cups) + " of disposable cups")
    print("$" + str(money) + " of money")
    return water, milk, coffee, cups, money

def buy():
    global water, milk, coffee, cups, money
    choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    if choice == "1":
        if water < 250:
            print("Sorry, not enough water!")
        elif coffee < 16:
            print("Sorry, not enough coffee!")
        elif cups < 1:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            water = water - 250
            coffee = coffee - 16
            money = money + 4
            cups -= 1
    elif choice == "2":
        if water < 350:
            print("Sorry, not enough water!")
        elif milk < 75:
            print("Sorry, not enough milk!")
        elif coffee < 20:
            print("Sorry, not enough coffee!")
        elif cups < 1:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            water = water - 350
            milk = milk - 75
            coffee = coffee - 20
            money = money + 7
            cups -= 1
    elif choice == "3":
        if water < 200:
            print("Sorry, not enough water!")
        elif milk < 100:
            print("Sorry, not enough milk!")
        elif coffee < 12:
            print("Sorry, not enough coffee!")
        elif cups < 1:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= 200
            milk -= 100
            coffee -= 12
            money += 6
            cups -= 1
    elif choice == "back":
        main()
    #return output(water, milk, coffee, cups, money)
    return water, milk, coffee, cups, money

def fill():
    global water, milk, coffee, cups, money
    a = int(input("Write how many ml of water do you want to add:"))
    b = int(input("Write how many ml of milk do you want to add:"))
    c = int(input("Write how many grams of coffee beans do you want to add:"))
    d = int(input("Write how many disposable cups of coffee do you want to add:"))

    water += a
    milk += b
    coffee += c
    cups += d

    #return output(water, milk, coffee, cups, money)
    return water, milk, coffee, cups, money

def take():
    global water, milk, coffee, cups, money
    print("I gave you $" + str(money))
    money = 0
    #return output(water, milk, coffee, cups, money)
    return money

def remaining():
    return output(water, milk, coffee, cups, money)
    return water, milk, coffee, cups, money


water = 400
milk = 540
coffee = 120
cups = 9
money = 550
def main():
    global water, milk, coffee, cups, money
    i=0
    while i == 0:
        action = input("Write action (buy, fill, take, remaining, exit):")
        if action == "buy":
            buy()
        elif action == "fill":
            fill()
        elif action == "take":
            take()
        elif action == "remaining":
            remaining()
        elif action == "exit":
            exit()

main()
