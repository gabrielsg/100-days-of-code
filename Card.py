"""
Chapter 17 Inheritance
Think Python 2nd Edition

"""
class Card:
    """
    Represents a playing cards
    """
    #suit_names and rank_names are known as class attributes
    #as they are associated with the class object Card
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spade']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', 
                  '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        # default card is 2 of clubs
        self.suit = suit
        self.rank = rank


    def __str__(self):
        return f'{Card.rank_names[self.rank]} of {Card.suit_names[self.suit]}'

    def __lt__(self, other):
        return (self.suit, self.rank) < (other.suit, other.rank)

class Deck:
    """
    represents a deck of playing cards
    """
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)


    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)








card1 = Card()
print(card1)
card2 = Card(0,1)
print(card2)
print(card1 < card2)
deck = Deck()
print(deck)
