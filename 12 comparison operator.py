# temparature=input("Enter the temparature:")
# if int(temparature)>30:
#     print("Its a hot day")
# else:
#     print("Its not a hot day")

name=input("Enter your name:")
if len(name)<3:
    print("Name must be greater than 3 characters")
elif len(name)>50:
    print("Name must be less than 50  characters")
else:
    print("Name is good!")