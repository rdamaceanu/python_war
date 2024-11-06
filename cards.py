# CARD
# SUIT, RANK, VALUE
# value will be calculated from the rank, based on a dictionary 
# ♣️,❤️,🔶,♠

values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':12,'Q':13,'K':14,'A':15}

class Cards:

    def __init__(self,rank,suit):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + self.suit

        