numbers=[]
size=int(input("Enter the size of he list: "))
for i in range(size):
    num=int(input("Enter the number:"))
    numbers.append(num)
unique=[]
for i in numbers:
    if numbers[i] not in unique:
        unique.append(i)
print(unique)
