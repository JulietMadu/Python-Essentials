#The secret_number
secret_number = 777
#print welcome message
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
#ask the user for their first guess
number=int(input("Guess the secret number:"))
#keep looping WHILE the guess is NOT equal to the secret_number
while number !=secret_number:
    print("Ha ha! You're stuck in my loop!" )
    #Ask the user to guess again
    number=int(input("Guess the secret number:"))
    #this line only runs AFTER the loop stops
print(number)
print("Well done, muggle! You are free now")
