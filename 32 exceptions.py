try:
    age=int(input("Enter the age: "))
    risk=100/age
    print("Risk is:",risk)
    print("Age is: ",age)
except ZeroDivisionError:
    print("Age cannot be zero")
except ValueError:
    print("Invalid entry")

