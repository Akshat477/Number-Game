import random

list = [1,2,3,4,5,6,7,8,9]
number = random.choice(list)

guess = input("ENTER YOUR GUESS FROM 1-9")

if guess == number : 
  print("CONGRATULATION YOU HAVE WON")

if guess == number-1 or number+1 : 
    print("U WERE CLOSE")

chances = 5 

if guess == list[:] : 
    chances-1 

if chances == 0 :
    print("U LOOSE THE NUMBER WAS",number)
