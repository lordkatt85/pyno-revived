
# main Game Logic

import random
from db import *

numberOfHumanPlayers = 4 # The value just for testing purpose

# cards in each players hand
playerOneHand = []
playerTwoHand = []
playerThreeHand = []
playerFourHand = []

deckCards = [] # the cards in the deck

#Characteristics of a playable character
class Player:
    def __init__(self,Id,Nature,Hand):
        self.id = Id     # Var for identifying player
        self.nature = Nature # =true for human, =false for bot
        self.hand = Hand #List of cards...To be broadcast to and from distributor

    def playCard(self,indexOfCard):
        card = self.hand[indexOfCard] #The card (string) played
        self.hand.remove(card)
        return card
    
    def displayHand(self):
        return self.hand #Can be modified to a func if gui is added

    def drawCard(self,noOfCards):
        for t in range(1,noOfCards):
            self.hand.append(deckCards[0])
            deckCards.remove(deckCards[0])

playerOne = (1, True, playerOneHand)
playerTwo = (2, True, playerTwoHand)
playerThree = (3, True, playerThreeHand)
playerFour = (4, True, playerFourHand)
listOfPlayers = [playerOne, playerTwo, playerThree, playerFour]
