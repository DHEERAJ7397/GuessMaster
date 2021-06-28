import random
#Defining the range of numbers 
a = int(input("Enter the range of numbers\nstarting from the range : "))
b = int(input("ending till the range : "))
#deciding chances
decision=abs(max(a,b))*0.05
decision=int(decision)+1
if decision<1:
    chance=1
else:
    chance=decision
while chance>0:#executing the loop 
    c = random.randint(a, b) #generating random number
    print("chances remaining : {}".format(chance)) #displaying chances
    d = int(input("Guess the number : ")) #asking user to guess the number
    chance=chance-1 #decrementing chances
    if c==d:  #checks if guessed number is equal to generated random number
        print("Yeah! You identified the number")
        break #breaks the loop
    elif c<d: #checks if guessed number is greater than random number
        print("Please try again! The number you guessed is too high")
    else:     #checks if guessed number is lesser than random number by default
        print("Please try again! The number you guessed is too small")
else : #after 5 chances this condition is executed
    print("Ooops! All you chances are finished. Better luck next time")
