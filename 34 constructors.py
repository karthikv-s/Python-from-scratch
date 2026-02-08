# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def move(self):
#         print("Move")
#     def draw(sef):
#         print("Draw")

# point=Point(10,20)
# point.x=11
# print(point.x)

class Person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f"Hi,I am {self.name}")

karthik=Person("Karthik")
print(karthik.name)
karthik.talk()

vaishnav=Person("Vaishnav")
vaishnav.talk()