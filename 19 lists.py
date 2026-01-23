size=int(input("Enter the number of elements"))
lists=[]
for i in range (size):
    num=int(input("Enter the number:"))
    lists.append(num)
largest=lists[0]
for i in range(len(lists)):
    if(lists[i]>largest):
        largest=lists[i]

print(f"Largest number is: {largest}")