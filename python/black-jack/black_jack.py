"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""
from typing import Tuple


def value_of_card(card: str) -> int | str:
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card in ['J', 'Q', 'K']:
        return 10
    if card == 'A':
        return 1
    if card.isnumeric() and int(card) in range(2, 11):
        return int(card)

    return 'Invalid input'

def higher_card(card_one: str, card_two: str) -> str | Tuple[str, str]:
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    # Return both cards if they have the same value, otherwise return the card with the bigger value
    return (card_one, card_two) if card_one_value == card_two_value else (card_one if value_of_card(card_one) > value_of_card(card_two) else card_two)


def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    if card_one == 'A' or card_two == 'A':
        return 1

    sum_cards_values = value_of_card(card_one) + value_of_card(card_two)

    if sum_cards_values <= 10:
        return 11
    return 1

def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    return ('A' in (card_one, card_two)) and (card_one in ['10', 'J', 'Q', 'K'] or card_two in ['10', 'J', 'Q', 'K'])


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    return value_of_card(card_one) == value_of_card(card_two)

def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    return value_of_card(card_one) + value_of_card(card_two) in range(9, 12)