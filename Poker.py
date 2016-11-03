#  File: Poker.py
#  Description: This program simulates a game of poker given a number of players.
#  Student's Name: Minal Kalas
#  Student's UT EID: mjk863
#  Course Name: CS 313E 
#  Unique Number: 50945
#  Date Created: 02/08/16
#  Date Last Modified: 02/15/16

import random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12
    
    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  def __eq__ (self, other):
    return (self.rank == other.rank)

  def __ne__ (self, other):
    return (self.rank != other.rank)

  def __lt__ (self, other):
    return (self.rank < other.rank)

  def __le__ (self, other):
    return (self.rank <= other.rank)

  def __gt__ (self, other):
    return (self.rank > other.rank)

  def __ge__ (self, other):
    return (self.rank >= other.rank)

class Deck (object):
  def __init__ (self):
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append (card)

  def shuffle (self):
    random.shuffle (self.deck)

  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Poker (object):
  def __init__ (self, num_players):
    self.deck = Deck()
    self.deck.shuffle()
    self.players = []
    numcards_in_hand = 5

    for i in range (num_players):
      self.players.append([])

    for j in range (numcards_in_hand):
      for i in range (num_players):
        self.players[i].append(self.deck.deal())

  def play (self):
    points_hand = []
    rank_hand =[]

    # sort the hands of each player and print
    for i in range (len(self.players)):
      sortedHand = sorted (self.players[i], reverse = True)
      self.players[i] = sortedHand
      hand = ""
      for card in sortedHand:
        hand = hand + str (card) + " "
      print ('Player ' + str (i + 1) + " : " + hand)

      if self.is_royal(self.players[i]) > 0:
        points_hand.append (self.is_royal(self.players[i]))
        rank_hand.append("Player " + str(i + 1) + ": " + "Royal Flush")
        continue

      elif self.is_straight_flush(self.players[i]) > 0:
        points_hand.append (self.is_straight_flush(self.players[i]))  
        rank_hand.append("Player " + str(i + 1) + ": " + "Straight Flush")
        continue

      elif self.is_four_kind(self.players[i]) > 0:
        points_hand.append (self.is_four_kind(self.players[i]))
        rank_hand.append("Player " + str(i + 1) + ": " + "Four of a Kind")
        continue

      elif self.is_full_house(self.players[i]) > 0:
        points_hand.append (self.is_full_house(self.players[i]))
        rank_hand.append("Player " + str(i + 1) + ": " + "Full House")
        continue

      elif self.is_flush(self.players[i]) > 0:
        points_hand.append (self.is_flush(self.players[i]))
        rank_hand.append("Player " + str(i + 1) + ": " + "Flush")
        continue

      elif self.is_straight(self.players[i]) > 0:
        points_hand.append (self.is_straight(self.players[i]))
        rank_hand.append("Player " + str(i + 1) + ": " + "Straight")
        continue

      elif self.is_three_kind(self.players[i]) > 0:
        points_hand.append (self.is_three_kind(self.players[i]))
        rank_hand.append("Player " + str(i + 1) + ": " + "Three of a Kind")
        continue

      elif self.is_two_pair(self.players[i]) > 0:
        points_hand.append (self.is_two_pair(self.players[i]))
        rank_hand.append("Player " + str(i + 1) + ": " + "Two Pair")
        continue

      elif self.is_one_pair(self.players[i]) > 0:
        points_hand.append (self.is_one_pair(self.players[i]))
        rank_hand.append("Player " + str(i + 1) + ": " + "One Pair")
        continue

      else:
        points_hand.append (self.is_high_card(self.players[i]))
        rank_hand.append("Player " + str(i + 1) + ": " + "High Card")
        continue

    print()
    for i in range(len(self.players)):
      print(rank_hand[i])
    print()

    winner = max(points_hand)
    ranks = []

    for i in range(len(points_hand)):
      if points_hand[i] == winner:
        ranks.append(i+1)

    if len(ranks) > 1:
      for i in range (len(ranks)):
        print("Player " + str(i +1) + " ties.")
    else:
      print("Player " + str(ranks[0]) + " wins.")

  # determine if a hand is a royal flush
  def is_royal (self, hand):
    h = 10
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)
    if (not same_suit):
      return 0

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)
    if (not rank_order):
      return 0
  
    return (h * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[2].rank * 13**2 + hand[3].rank * 13 + hand[4].rank)


  def is_straight_flush (self, hand):
    h = 9
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[1 + i].suit)
    if (not same_suit):
      return 0
    return True

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == hand[i+1].rank + 1)
    if (not rank_order):
      return 0
    
    return (h * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[2].rank * 13**2 + hand[3].rank * 13 + hand[4].rank)

  def is_four_kind (self, hand):
    h = 8
    if (hand[0].rank == hand[1].rank == hand[2].rank == hand[3].rank):
      return (h * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[2].rank * 13**2 + hand[3].rank * 13 + hand[4].rank)
    elif (hand[1].rank == hand[2].rank == hand[3].rank == hand[4].rank):
      return (h * 13**5 + hand[1].rank * 13**4 + hand[2].rank * 13**3 + hand[3].rank * 13**2 + hand[4].rank * 13 + hand[0].rank)
    return 0

  def is_full_house (self, hand):
    h = 7
    if (hand[0].rank == hand[1].rank == hand[2].rank) and (hand[3].rank == hand[4].rank):
      return (h * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[2].rank * 13**2 + hand[3].rank * 13 + hand[4].rank)
    elif (hand[0].rank == hand[1].rank) and (hand[2].rank == hand[3].rank == hand[4].rank):
      return (h * 13**5 + hand[2].rank * 13**4 + hand[3].rank * 13**3 + hand[4].rank * 13**2 + hand[0].rank * 13 + hand[1].rank)
    return 0

  def is_flush (self, hand):
    h = 6
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[1 + i].suit)
    if (not same_suit):
      return 0
    return True

  def is_straight (self, hand):
    h = 5
    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == hand[i+1].rank + 1)
    if (not rank_order):
      return 0
    
    return (h * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[2].rank * 13**2 + hand[3].rank * 13 + hand[4].rank)

  def is_three_kind (self, hand):
    h = 4
    if (hand[0].rank == hand[1].rank == hand[2].rank):
      return (h * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[2].rank * 13**2 + hand[3].rank * 13 + hand[4].rank)
    elif (hand[1].rank == hand[2].rank == hand[3].rank):
      return (h * 13**5 + hand[1].rank * 13**4 + hand[2].rank * 13**3 + hand[3].rank * 13**2 + hand[0].rank * 13 + hand[4].rank)
    elif (hand[2].rank == hand[3].rank == hand[4].rank):
      return (h * 13**5 + hand[2].rank * 13**4 + hand[3].rank * 13**3 + hand[4].rank * 13**2 + hand[0].rank * 13 + hand[1].rank)
    return 0

  def is_two_pair (self, hand):
    h = 3
    if (hand[0].rank == hand[1].rank) and (hand[2].rank == hand[3].rank):
      return (h * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[2].rank * 13**2 + hand[3].rank * 13 + hand[4].rank)
    elif (hand[0].rank == hand[1].rank) and (hand[3].rank == hand[4].rank):
      return (h * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[3].rank * 13**2 + hand[4].rank * 13 + hand[2].rank)
    elif (hand[1].rank == hand[2].rank) and (hand[3].rank == hand[4].rank):
      return (h * 13**5 + hand[1].rank * 13**4 + hand[2].rank * 13**3 + hand[3].rank * 13**2 + hand[4].rank * 13 + hand[0].rank)
    return 0

  # determine if a hand is one pair
  def is_one_pair (self, hand):
    h = 2
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        return (h * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[2].rank * 13**2 + hand[3].rank * 13 + hand[4].rank)
    return 0

  def is_high_card (self, hand):
    h = 1
    return (h * 13**5 + hand[0].rank * 13**4 + hand[1].rank * 13**3 + hand[2].rank * 13**2 + hand[3].rank * 13 + hand[4].rank)

def main():
  # prompt user to enter the number of players
  num_players = int (input ('Enter number of players: '))
  while (num_players < 2 or num_players > 6):
    num_players = int (input ('Enter number of players: '))

  # create the Poker object
  game = Poker (num_players)

  # play the game (poker)
  game.play()

main()