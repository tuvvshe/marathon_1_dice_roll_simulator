import random
min_val = 1
max_val = 6
roll_again = "YEAH"

while roll_again == "YEAH" or roll_again == "y":

print("ROLLING THE DICE...")
 
print("THE RESULT IS: ")

print(random.randint(min_val, max_val))
print(random.randrange(min_val, max_val))
roll_again = input("ROLL THE DICE AGAIN?")
