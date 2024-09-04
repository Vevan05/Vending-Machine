#Vending Machine

#Using while loop to make a menu based program
while True:
    #Printing Items Available
    print("----------------------Welcome to the Vending Machine----------------------")
    print("Items Available:\n1. Item A: $2\n2. Item B: $3\n3. Item C: $5\n")

    #Asking user which option they will choose by defining variable choice
    choice = input("Enter which item to choose(A/B/C/quit): ")

    #Variable amount defines the amount to be paid
    amount = 0

    #Using if-elif-else to see which option the user chose and then, set the amount accordingly
    if choice.lower() == "a":
        amount = 2
    elif choice.lower() == "b":
        amount = 3
    elif choice.lower() == "c":
        amount = 5
    elif choice.lower() == "quit":
        print("Exiting vending machine...")
        break
    else:
        print("Enter Valid Value")
        print()
        continue

    print()

    #Asking user to insert money
    print(f"Amount to be paid: {amount}$")
    money = int(input("Insert money: "))

    #Using if-else
    if money >= amount:
        #Dispensing amount and giving the user the change if sufficient amount is given
        print(f"Dispensing Item {choice.upper()}")
        print(f"Your change is ${money - amount}")
    else:
        #Asking user to cancel order if insufficient amount
        print("Money is less than the required amount")
        cancel = input("Do you want to cancel transaction? (y/n): ")
        if cancel.lower() == "y":
            print("Cancelling Transaction")
            break
        elif cancel.lower() == "n":
            additional = int(input(f"Insert additional ${amount - money}: "))
            if additional >= (amount - money):
                print(f"Dispensing Item {choice.upper()}")
                print(f"Your change is ${money + additional - amount}")
            else:
                print("Invalid value: Exiting...")
                break

    print()
