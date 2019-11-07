import random
while True:
    usr = input("Please enter 'Yes' to start the game or 'No' to stop the game: ")
    i = usr.upper()
    if i == 'YES':
        x = (random.randrange(1,7))
        g = (input("Guess a no between 1 to 6: "))
        x = str(x)
        if x == g:
            print('congratulations you won the prize')
        else:
            #y = str(x)
            print('The actual no is:', end = str(x))
            print('\nbetter luck')
    else:
        break
