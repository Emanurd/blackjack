"""Functions to help play and score a game of blackjack.
"""


def value_of_card(card: str):
    """Determine the scoring value of a card.
    """
    if card in ["J", "Q", "K"]:
        return 10
    if card == "A":
        return 1
    return int(card)


def higher_card(card_one:str or tuple, card_two: str or tuple):
    """Determine which card has a higher value in the hand.
    """
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    if value_of_card(card_one) < value_of_card(card_two):
        return card_two
    return (card_one, card_two)
    
    
def value_of_ace(card_one: str, card_two: str):
    """Calculate the most advantageous value for the ace card.
    """
    if value_of_card(card_one) + value_of_card(card_two) + 11 > 21:
        return 1
    if value_of_card(card_one) + value_of_card(card_two) + 1 == 21:
        return 1
    if (card_one) == "A" or (card_two) == "A":
        return 1
    return 11
        


def is_blackjack(card_one: str, card_two:str):
    """Determine if the hand is a 'natural' or 'blackjack'.
    """

    
    if (card_one == "A" and card_two in ["10", "K", "Q", "J"]) or (card_two == "A" and card_one in ["10", "K", "Q", "J"]):
        return True
    return False




def can_split_pairs(card_one:str, card_two:str):
    """Determine if a player can split their hand into two hands.
    """
    
    pares = value_of_card(card_one) == value_of_card(card_two)
    return pares

def can_double_down(card_one: str, card_two:str):
    """Determine if a blackjack player can place a double down bet.
    """
    total_value = value_of_card(card_one) + value_of_card(card_two)
    
    if total_value in [9, 10, 11]:
        return True
    
    return False
