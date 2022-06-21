from random import choice

def main():
    # values = ("'R' for 'rock'","'P' for 'paper'","'S' for 'scissors'")
    values = ["R","P","S"]

    computer = choice(values)
    player = False

    print( """
                        Hello Gamer. Welcome to play the Rock-Paper-Scissors game. 
                        INFO => 'R' for 'rock',
                                'P' for 'paper',
                                'S' for 'scissors'
                        Pick one option from the following - 'R', 'P' and 'S' to play 
                        
                        """)

    while player == False:
        player = input("Pick one option from the following - 'R', 'P' and 'S' to play ===> \n")
        player = player.upper()
        if player == computer:
            print(" Player (",player, "): CPU (",computer, "). It's a tie  ")
        elif player == "R":
            if computer == "P":
                print(" Player (",player, "): CPU (",computer, "). You lose ")
            else:
                print(" Player (",player, "): CPU (",computer, "). You win ")
                return
        elif player == "P":
            if computer == "S":
                print(" Player (",player, "): CPU (",computer, "). You lose ")
            else:
                print(" Player (",player, "): CPU (",computer, "). You win ")
                return
        elif player == "S":
            if computer == "R":
                print(" Player (",player, "): CPU (",computer, "). You lose ")
            else:
                print(" Player (",player, "): CPU (",computer, "). You win ")
                return
        else:
            print('Invalid option, try again using the letter options provided') 

        player = False
        computer = choice(values)


main()