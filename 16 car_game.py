option=""
started=False

while(True):
    option=input("Enter the choice: ").lower()
    if(option=="start"):
        if started:
            print("Car is already started!")
            continue
        else:
            started=True
            print("Car started succesfully,letsgo!")
        
    elif(option=="stop"):
        if not started:
            print("Car is already stopped!")
            continue
        else:
            started=False
            print("Car stopped succesfully.")
    elif(option=="quit"):
        print("You have exited the game.")
        break
    elif option=="help":
        print("""
        start- to start the car.
        stop- to stop the car.
        quit- to exit the game.
        """)
    else:
        print("Oops!Sorry,you have entered the wrong choice.")
    
