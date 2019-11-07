import random
while True:
    usr = input("Please enter 'Yes' to Roll the dies or 'No' to stop the game: ")
    i = usr.upper()
    if i == 'YES':
        x = (random.randrange(1,7))
        print(x)
        
    else:
        break
