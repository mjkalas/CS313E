#File: Eights.py
#Description: This program simulates a blackjack game.
#Student's Name: Minal Kalas
#Student's UT EID: mjk863
#Course Name: CS 313E 
#Unique Number: 50945 
#Date Created: 03/12/16
#Date Last Modified: 03/14/16

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

class Player (object):
  # cards is a list of card objects
  def __init__ (self, cards):
    self.cards = cards

#get points for each player's hand
  def get_points (self):
    count = 0
    for card in self.cards:
      if card.rank > 9:
        count += 10
      elif card.rank == 8:
        count += 50
      else:
        count += card.rank
    return count

  def __str__ (self):
    hand = ""
    points = self.get_points()
    for card in self.cards:
      hand = hand + " " + str(card)
    points_string = " - " + str(points) + " points."
    return hand + points_string

class Eights (object):
  def __init__ (self, num_players = 2):
    self.deck = Deck()
    self.deck.shuffle()
    self.num_players = num_players
    self.player_list = []

    # create the number of players specified
    for i in range (self.num_players):
      self.player_list.append (Player (sorted([self.deck.deal(), self.deck.deal(), self.deck.deal(), self.deck.deal(), self.deck.deal()])))

  def play (self):
    pile = Player ([self.deck.deal()])
    discard = 0
    print ("Pile: " + str(pile))

    for i in range (self.num_players):
      print ('Player ' + str (i + 1) + " : " + str(self.player_list[i]))

    Game_round = 0
    '''for i in range (self.num_players):
      for j in range (i):
        if (self.player_list[i][j]).rank == pile.rank:
          pile = self.player_list[i][j]
    Keep getting error "TypeError: 'Player' object does not support indexing"
    
    for i in range (self.num_players):
      if self.player_list[i].rank == pile[i].rank:
        pile[i] = self.player_list[i].rank
        print (pile)
    '''
    winner_point = 0
    point_list = []

    for i in range (self.num_players):
      points = (self.player_list[i]).get_points()
      point_list.append(points)
      point_list = sorted(point_list)

    for i in range(self.num_players):  
      points = (self.player_list[i]).get_points()
      if point_list[0] == points:
        print ("Winner: Player " + str(i+1) + " - " + str(point_list[0]) + " points")
    print ("Discard: " + str(discard))

def main():
  num_players = eval (input ('Enter number of players: '))
  while (num_players < 2 or num_players > 6):
    num_players = eval (input ('Enter number of players: '))
  print ()

  # create a game object
  game = Eights (num_players)

  # star the game
  game.play()

main()