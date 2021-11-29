import random 
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':10}


class Card:

    def __init__(self,rank,suit):

        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):

        return f'{self.rank} of {self.suit}'


class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:

                self.all_cards.append(Card(rank,suit))

    def shuffle_deck(self):

        return random.shuffle(self.all_cards)

    def deal_one(self):

        return self.all_cards.pop()

class Player:

    def __init__(self,name):

        self.name = name

        self.player_hand = []
        
        self.hand_value = 0
        
        self.player_funds = 1000

        self.stake = 0

    def add_card(self,new_cards):

        if type(new_cards) == type([]):

            self.all_cards.extend(new_cards)

        else:

            self.player_hand.append(new_cards)

    def bet(self):

        while True:
            try:
                self.stake = int(input('How much are you staking? \n'))
                break
            except ValueError:
                print("Oops that wasn't a number")


        while self.stake > self.player_funds:

            print('Insufficent Balance')
            self.stake = int(input('How much are you staking? \n'))

        self.player_funds -= self.stake

    def winning(self,amount):

        self.player_funds += amount   
        
    def clear_hand(self):
        
        self.player_hand = []


    def __str__(self):

        return f'{self.name} has {self.player_funds} left'



class Dealer:

    def __init__(self):

        self.dealer_hand = []

    def add_card(self,new_cards):

        self.dealer_hand.append(new_cards)

    def deal_card(self,destination):   
        return destination.append(self.dealer_hand.pop())

    def deal_two(self,destination):
        
        for num in range(2):
            destination.append(self.dealer_hand.pop())
    


    


        #####################
        ####GAME LOGIC#######



new_deck = Deck()

new_deck.shuffle_deck()


player_1 = Player('Mulero')

dealer = Dealer()


for x in range(52):
    dealer.add_card(new_deck.deal_one())

game_on = True    

value_table = 0
value_player = 0
table = []

while game_on == True:
    

    print('BLACKJACK \n \n ')
    #Initaial card share
    dealer.deal_two(table)
    dealer.deal_two(player_1.player_hand)
   
    #Stake time
    print(player_1)
    player_1.bet()
    
    stake = player_1.stake

    #show player cards

    print('\nPLAYER')
    for obj in player_1.player_hand:
        print(obj)
    #show dealer first card
    print('DEALER')
    print(table[-1])       
    

    #Value cal
   
    for obj in table:
        value_table += obj.value
    for obj in player_1.player_hand:
        value_player += obj.value
   
    #Choice
    options = {'S':'stand','H':'hit'}
    choice = ''
    print('\n \nDo you want to stand(S) or hit(H)?\n')
    
    while choice not in options.keys():
        
        choice = input('Stand(S) or hit(H)?\n')
        
    if choice == 'H':
        dealer.deal_card(player_1.player_hand)
        for obj in player_1.player_hand:
            print(obj)
    
    if choice == 'S':
        pass
    #Show dealer second card
    for obj in table:
        print(obj)
    
    #Dealers hit
    if value_table < value_player:
        
        dealer.add_card(table)
        
        print(len(table))
        for obj in table:
            print(obj)
    
    #Comparison time
    
    if value_table ==21:
        
        print('Dealer won\nBlackjack')
    
    elif value_player == 21:
        player_1.winning((stake*2))
        print('Blackjack')
        
    elif value_table > 21:
        player_1.winning((stake*2))
        
        print(f'Dealer bust player won {(stake*2)}')
    
    elif value_player > 21:
        
        
        print('Player bust dealer wins')
              
        
    elif value_table > value_player:
        
        print(f'player lost {(stake)}\nDealer > player')
   
    elif value_table < value_player:
        
        player_1.winning((stake*2))
        print(f'Player won {(stake*2)}\nDealer < Player')
    
    elif value_table == value_player:
        print('Draw')
        player_1.winning((stake))
        
    elif player_1.player_funds == 0:
        
        print('Game Over\nNo more funds to play with')
        game_on == False
    
        
    
    #Continue Game?
    
    answer = ['Y','N']
    
    choice2 = []
    
    while choice2 not in answer:
        
        choice2 = input('Do you want to play another round?\nYes(Y) of No(N)\n')
        
    if choice2 == 'Y':
        
        player_1.clear_hand()
        table = 0
        value_player = 0
        value_table = 0
        
        continue
    
    if choice2 == 'N':
        
        game_on == False
        
        break
    
    
    















    






