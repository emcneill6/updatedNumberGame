# Emma McNeill
# Purpose: the purpose of this program is to play a numbers guessing game
# and keep track of the top 5 scores

import updates as u

while True:

    name = u.playerName()
    newPlayerCount = u.game()

    u.newHighScore(name, newPlayerCount)

    print("Thanks for playing!")
