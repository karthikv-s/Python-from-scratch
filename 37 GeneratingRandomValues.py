#we will use random module
import random
for i in range(3):
    print(random.random())

#random.random()#will generate a random number between 0 to 1
for i in range(3):
    print(random.randint(10,20))

members=["Karthik","Suresh","Ramesh"]
leader=random.choice(members)
print(leader)