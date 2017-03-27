###This is a simplified Blackjack game with OOP; written in python

#include random library
import random

#values found on a deck of cards
SUIT = ['Clubs','Hearts', 'Spades', 'Diamonds']
FACE = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

#Card object
#A card  has a suit and a face. The face correspond to the card value
#In blackjack JQK count as 10 and A can either be 1 or 11
#For simplicity A will be defaulted to 11
class Card(object):
    def __init__(self, suit, face):
        self.suit = suit
        self.face = face
        if face in ['J', 'Q', 'K']:
            self.value = 10
        elif face == 'A':
            self.value = 11
        else:
            self.value = int(face)

    #prints out card value
    def __str__(self):
        return '[' + self.face + ' ' + self.suit + ']'


#Defines a deck of cards.
#Constructed useing SUITS and FACE array creatinga deck of 52
class Deck(object):
    def __init__(self):
        self.cards = [Card(i, j) for i in SUIT for j in FACE]
        self.shuffle()

    #shuffles the deck of cards
    def shuffle(self):
        random.shuffle(self.cards)
    #deals a card from the top of the deck
    def deal(self):
        card = self.cards.pop(0)
        return card

#A hand is a set of cards.
#initializes an empty hand and
class Hand(object):
    def __init__(self):
        self.hand = []
        self.action = ''

    #resets hand to empty
    def clear_hand(self):
        self.hand = []

    #adds cards to hand and tracks hit action
    def hit(self, card):
        self.hand.append(card)
        self.action = 'h'
        return self.hand

    #stands and keeps hand and track stand action
    def stand(self):
        self.action = 's'

    #returns total of all cards in hand
    #optimized to make A to count as 1 to prevent busts
    def total(self):
        ace_count = 0
        hand_sum = 0
        for card in self.hand:
            if card.face =='A':
                ace_count += 1
            hand_sum += card.value
        while (hand_sum > 21) and (ace_count > 0):
            hand_sum -= 10
            ace_count -= 1
        return  hand_sum

    #returns whether or not hand is a bust
    def is_bust(self):
        if self.total() > 21:
            return True
        else:
            return False
    #prints out cards in hand and total
    def show_hand(self):
        for card in self.hand:
            print(card, end="")
        print("\n and a total of ", self.total(), ".")

#A player is type of hand with new attributes like name and
#deck manipulation
#initializes with name and used deck.
class Player(Hand):
    def __init__(self, name, deck):
        Hand.__init__(self)
        self.name = name
        self.deck = deck

    #resets deck
    def new_deck(self, deck):
        self.deck = deck

    #get input for new name
    def enter_name(self):
            self.name = input("Enter player name: ")
            print("Hi ", self.name, "!\n")

    #print/play a stand move
    def play_stand(self):
        print (self.name, " stands on ", self.total(), "." )

    #print/play a hit move and take a card and add to hand
    def play_hit(self):
        self.hit(deck.deal())
        print(self.name, "hits. ", self.name, " gets ")
        print(self.hand[-1],". ", self.name, " has ")
        self.show_hand()

    #the player hits 21 and so there is an auto stand.
    def hit_21(self):
        if self.total() == 21:
            print(self.name, "hits 21!")
            self.action = 's'
            return True
        else:
            return False

    #get a play for the hand
    def get_play(self):
        move = input('Do you hit (h) or stand (s)? Enter h or s\n')
        while (move != 'h' and move != 's'):
            move = input("I don't understand. Enter h or s\n" )
        self.action = move
        if self.action == 'h':
            self.play_hit()
        elif self.action == 's':
            self.play_stand()

    #reset for a new round
    def new_round(self, deck):
        self.new_deck(deck)
        self.clear_hand()

#Dealer is a specific type of Player
#that can only show one card initially and has the same name
class Dealer(Player):
    def __init__(self, deck):
        Player.__init__(self, 'Dealer', deck)

    #shows only one card
    def show_dealer(self):
        print("Dealer shows ", self.hand[0], "\n")

    #dealer always stands on soft 17
    def play(self):
        if self.total() > 16:
            self.action = 's'
            self.play_stand()
        else:
            self.action = 'h'
            self.play_hit()


if __name__ == '__main__':
    #initialize deck and players
    deck = Deck()
    dealer = Dealer(deck)
    player = Player('Player', deck)
    player.enter_name()

    #start game loop
    while True:
        print("Let's play super simple BlackJack!!!! Dealer stands on soft 17.")

        #deal 2 cards each
        for i in range(2):
            player.hit(deck.deal())
        for i in range(2):
            dealer.hit(deck.deal())

        #dealer shows one card
        dealer.show_dealer
        #show player's hand
        print ("Player shows ")
        player.show_hand()
        #start hand play
        while (player.action != 's' and not player.is_bust() and not player.hit_21()):
            player.get_play()
        #player has not busted so the dealer plays their hand
        if not player.is_bust():
            print("Dealer's turn. Shows hand:")
            dealer.show_hand()
            dealer.play()
            while (dealer.action != 's' and not dealer.is_bust()):
                dealer.play()
            #Game win outcomes
            if dealer.is_bust():
                print("Dealer busts! ", player.name, " wins!")
            elif dealer.total() > player.total():
                print("Dealer has ", dealer.total(), ". ", player.name, " has ", player.total(), ". Dealer wins!\n")
            elif dealer.total() < player.total():
                print("Dealer has ", dealer.total(), ". ", player.name, " has ", player.total(), ". ", player.name, " wins!\n")
            elif dealer.total() == player.total():
                print("Dealer has ", dealer.total(), ". ", player.name, " has ", player.total(), ". It's a tie!\n")
        #player has busted so dealer wins
        else:
            print(player.name, " busts! Dealer wins!")
        #check to play new round again
        move = input('Play again (y/n)?\n')
        while (move != 'y' and move != 'n'):
            move = input("I don't understand. Enter y or n\n" )
        if move == 'n':
            break
        #initialize new round
        else:
            deck = Deck()
            dealer.new_round(deck)
            player.new_round(deck)
