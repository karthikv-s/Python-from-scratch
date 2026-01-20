# The user will have 3 chances to guess the number correctly.

secret_number=7
chances=3
count=0

while(count<chances):
    guess=int(input("Guess the number: "))
    if(guess==secret_number):
        print("Congragunlations!You guessed it right.")
        break
    else:
        count+=1
        print("Wrong guess.Try again.")
        if(count==chances):
            print("Sorry!You've used all your chances.The correct number will remain a mystery.")