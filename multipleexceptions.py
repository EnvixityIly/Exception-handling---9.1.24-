try:
    num1 = int(input("enter a number: "))
    num2 = int(input("enter a number: "))

    result = num1/num2

    print("Result is" , result)
    print("Result is" , result1)

except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("please enter a numerical value")
except NameError as ex:
    print(f"the exception is {ex}")

finally: 
    print("English or spanish")
    print("First to move is gay")