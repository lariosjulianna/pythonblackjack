import random

class Simulation:
    def __init__(self):
        self.gameInPlay = False

    def startGame(self):
        i_in = input("Dealer: Welcome to Black Jack, do you know how to play?\nPress 1 if you do, 0 if you need instructions.\n")
        print("-----------------------------------")
        if i_in == "1":
            self.deal()
            self.gameInPlay = True
        elif i_in == "0":
            self.gameInPlay = False
            print("Players play against the Dealer. Both will begin with two random cards, the Dealer's first card will be face up. After you look at your two cards, you decide if you want to hit (get another card), or hold (keep your current hand). The goal is to get exactly 21, or a higher number than the dealer -- but you can't go OVER 21, or you lose.")
            i_in2 = input("Ready to play? Press 1 to start.\n")
            print("-----------------------------------")
            if i_in2 == "1":
                print("Dealer: Here we go!")
                print("-----------------------------------")
                self.gameInPlay = True
                self.deal()

    def isGameInPlay(self):
        return self.gameInPlay

    def deal(self):
        d1 = random.randint(1, 13)
        d2 = random.randint(1, 13)
        dealerTotal = d1 + d2

        c1 = random.randint(1, 13)
        c2 = random.randint(1, 13)
        playerTotal = c1 + c2
        print("This is the dealer's first card:", d1)
        print("This is your hand:")
        print("Card 1:", c1)
        print("Card 2:", c2)
        self.playerHit(dealerTotal, playerTotal)

    def playerHit(self, dealerTotal, playerTotal):
        while True:
            h_in = input("Dealer: Would you like to Hit (press 1) or Hold (press 0)?\n")
            if h_in == "1":
                new_c = random.randint(1, 13)
                playerTotal += new_c
                print("New Card:", new_c)
                print("Total:", playerTotal)
                if playerTotal > 21:
                    print("Player busts! Dealer wins.")
                    return
            elif h_in == "0":
                self.hold(dealerTotal, playerTotal)
                return
            else:
                print("Invalid input. Please enter 1 to Hit or 0 to Hold.")

    def hold(self, dealerTotal, playerTotal):
        print("Player holds.")
        self.calcWinner(dealerTotal, playerTotal)

    def calcWinner(self, dealerTotal, playerTotal):
        print("Dealer's total:", dealerTotal)
        print("Player's total:", playerTotal)
        if playerTotal > 21:
            print("Player busts! Dealer wins.")
        elif dealerTotal > 21 or playerTotal > dealerTotal:
            print("Player wins!")
        elif dealerTotal == playerTotal:
            print("It's a tie!")
        else:
            print("Dealer wins!")

# Example usage
if __name__ == "__main__":
    sim = Simulation()
    sim.startGame()
