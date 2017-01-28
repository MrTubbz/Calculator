def getMenu():
    print("1. Addition:")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
def getChoice():
    valid = False
    while not valid:
        choice = int(input("Please choose an option:"))
        if not choice < 6:
            print("Choice not valid")
        else:
            valid = True
    return choice

def checkDigit(number):
        if number[0]=="-":
            number = int(number)*(-1)
            number= str(number)
        if not number.isdigit():
            valid = False
        else:
            valid = True
        return valid

def getInputs():
    numbers = []
    for num in range (0,2):
        valid = False
        while not valid:
            number = input(("Input a number for the clculation: "))
            if not checkDigit(number):
                print("Input not valid")
            else:
                valid = True
        numbers.append(number)
    return numbers


def addition(numbers):
    print("Adding", numbers[0] ,"with", numbers[1])
    result = int(numbers[0])+int(numbers[1])
    return result

def subtraction(numbers):
    print("Subtracting", numbers[0], "with", numbers[1])
    result = int(numbers[0]) - int(numbers[1])
    return result


def multiplication(numbers):
    print("Multiplying", numbers[0], "with", numbers[1])
    result = int(numbers[0]) * int(numbers[1])
    return result

def division(numbers):
    print("Dividing", numbers[0], "with", numbers[1])
    result = int(numbers[0]) // int(numbers[1])
    remainder = int(numbers[0])% int(numbers[1])
    return result, remainder


def decideCalculation(choice, numbers):
    divide = False
    if choice == 1:
        result = addition(numbers)
    elif choice == 2:
        result = subtraction(numbers)
    elif choice == 3:
        result = multiplication(numbers)
    else:
        result, remainder = division(numbers)
        divide = True
    if not divide:
        return result
    else:
        return result, remainder

def main():
    getMenu()
    choice = getChoice()
    while choice != 5:
        numbers = getInputs()
        if not choice==4:
            result = decideCalculation(choice, numbers)
            print ("Answer is", result)
        else:
            result, remainder = decideCalculation(choice, numbers)
            print ("Answer is",result ,"with remainder",remainder)
        getMenu()
        choice = getChoice()
    print("Thank you for using this calculator")

main()