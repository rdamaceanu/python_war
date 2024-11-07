# a deck is an object containing a list of card objects
import cards
from random import shuffle

suits = ('♣️','❤️','🔶','♠')
ranks = ('2','3','4','5','6','7','8','9','10','J','Q','K','A')
values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':12,'Q':13,'K':14,'A':15}

class Deck():
    
    
    
    def __init__(self):
        self.deck = []
        self.deck_str=''
        for suit in suits:
            for rank in ranks:
                self.deck.append(cards.Cards(rank,suit))
    
    def draw_card(self):
        return self.deck.pop()
        
    def shuffle(self):
        shuffle(self.deck)


    def __str__(self):
        self.deck_str
        for card in self.deck:
            self.deck_str = self.deck_str + ' ' + card.__str__()
        return self.deck_str

if __name__=='__main__':
    deck = Deck()
    print(deck)
    deck.shuffle()
    drawn_card = deck.draw_card() 
    print(drawn_card)

    print(deck)