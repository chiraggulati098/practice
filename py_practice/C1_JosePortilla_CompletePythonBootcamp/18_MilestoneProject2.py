import random   #importing random to use shuffle to shuffle the deck

'''
Setting up global variable to initialize the deck and also give values to the cards as per the game rules
'''
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True  #playing = True till you enter that you don't want to play again

class Card():
    
    '''
    Card class is used to give every card a suit and rank and it prints the card in the format - "<rank> of <suit>"
    '''

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck():
    
    '''
    The constructor of the Deck class uses suits and ranks to create a full deck
    Shuffle is added as a member function to shuffle the deck
    Deal is a function made to return a card that's removed from the deck, this will be used to give one card to the player
    '''

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand():

    '''
    Hand class is used here to operate on the cards in the hands of the player
    Add cards is used to add cards to the hand
    Adjust for aces makes sure that when value of hand goes over 21 and the player has an ace, the ace adjusts the value to 1 instead of 11
    '''
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips():
    
    '''
    The Chips class is working on the operations on the chips in cases of winning and loosing
    '''

    def __init__(self,total = 100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet?"))
        except:
            print("Sorry please provide an integer")
        else:
            if chips.bet > chips.total:
                print(f'Sorry, you do know have enough chips! You have: {chips.total}')
            else:
                break

def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input('Hit or Stand? Enter h or s:')
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            playing = False
        else:
            print("Sorry, I did not understand that, Please enter h or s only")
            continue
        break

def show_some(player,dealer):
    print("\nDealer's Hand:  ")
    print("First card hidden!")
    print(dealer.cards[1])
    print("\nPlayer's Hand:  ")
    for card in player.cards:
        print(card)
    print(f"Value of Players's hand is: {player.value}")

def show_all(player,dealer):
    print("\nDealer's Hand:  ")
    for card in dealer.cards:
        print(card)
    print(f"Value of Dealer's hand is: {dealer.value}")
    print("\nPlayer's Hand:  ")
    for card in player.cards:
        print(card)
    print(f"Value of Players's hand is: {player.value}")

def player_busts(player,dealer,chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("PLAYER WINS! DEALER BUSTED!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("DEALER WINS!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player tie! PUSH")

while True:
    print("WELCOME TO BLACKJACK")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()
    take_bet(player_chips)
    
    show_some(player_hand,dealer_hand)

    while playing:

        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
        
        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
    
    print(f"\nPlayer total chips are at: {player_chips.total}")

    new_game = input("Would you like to play another hand? ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank You for playing!")
        break
