# update high scores file
# def playerName, game, createFile, newHighScore, highScores, quitGame
import random
number = random.randint(1, 100)
toQuit = {"q", "Q"}

def playerName():
    try:
        name = input("Please enter your first name:\n")
        if name in toQuit:
            quitGame()
        if len(name) > 10:
            return name[:10]
        else:
            return name
    except ValueError:
        print("Invalid selection. Please enter your name.")
        print()
        quitGame()
    except Exception as e:
        print(f"An error has occurred.  Exiting: {e}")
        quitGame()

def game():
    try:
        number = random.randint(1, 100)
        print("Welcome to the Number Guessing Game!")
        print()
        # give the user a way to quit the game

        print("If you would like to exit the game at anytime, press q or Q.")
        print()
        # have user enter a guess
        guess = int(input("Guess an integer between 1 and 100:  "))
        print()
        # keep track of how many guesses
        count = 1

        while number != guess:
            count = count + 1

            if guess > number:
                print(f"Your guess is too high. Please try again.")
                print()
                guess = int(input("Enter an integer between 1 and 100:  "))
                print()

            if guess < number:
                print(f"Your guess is too low. Please try again.")
                print()
                guess = int(input("Enter an integer between 1 and 100:  "))
                print()

        if guess == number:
            print(f'Good job! You won in {count} guesses!')
            return count

    except ValueError:
        print("Please enter an integer.")
    except EOFError:
        print("Ending game.")
        quitGame()
    except Exception as e:
        print(f"Unexpected exception: {e}.")
        exit()

def createFile():
    listOfScores = list()
    with open("topPlayers.txt", "r") as file:
        for line in file:
            listOfScores.append([int(line[0:10]), line[10:].rstrip()])
    return listOfScores

def newHighScore(name, newPlayerCount):
    listOfScores = createFile()
    if newPlayerCount < listOfScores[4][0]:
        del listOfScores[-1]
        listOfScores.append([newPlayerCount, name])
        listOfScores.sort(key=lambda entry:entry[0])
        with open("topPlayers.txt", "w") as file:
            for entry in listOfScores:
                file.write(str(entry[0]).ljust(10) + entry[1] + "\n")

def highScores():
    listOfScores = createFile()
    print(f" FINALLY \n".center(20, "="))
    for each in listOfScores:
        print(str(each[0]).ljust(10) + each[1])

def quitGame():
    print("Thanks for playing!")
    exit()

