num=int(input("Enter a number: "))
num2=0
while num>0:
    digit=num%10
    num2=num2*10+digit
    num=num//10
print("Reversed number is :",num2)