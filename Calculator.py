while True:
    select = input("""This is a calculator
Type in what u would like it to perform or Type exit to close the calculator""")


    if select == "exit".lower():
        print("Calculator Closed")
        break

    elif select == "addition".lower():
        x = int(input("Type your first number here"))
        y = int(input("Type your second number here"))
        addition = x + y
        print(addition)

    elif select == "subtraction".lower():
        x = int(input("Type your first number here"))
        y = int(input("Type your second number here"))
        subtraction = x - y
        print(subtraction)

    elif select == "multiplication".lower():
        x = int(input("Type your first number here"))
        y = int(input("Type your second number here"))
        multiplication = x * y
        print(multiplication)

    elif select == "division".lower():
        x = int(input("Type your first number here"))
        y = int(input("Type your second number here"))
        division = x / y
        print(division)

    elif select == "modulus".lower():
        x = int(input("Type your first number here"))
        y = int(input("Type your second number here"))
        modulus = x % y
        print(modulus)


