from itertools import product
from random import shuffle
from os import system
import tkinter as tk


class Player:
    def __init__(self):
        self.name = None
        self.hand = []
        self.pile = []
        self.broom = 0

    def set_name(self, name):
        self.name = name

    def get_name(self):
        print(self.name)

    def set_hand(self, hand):
        self.hand = hand

    def set_broom(self):
        self.broom = self.broom + 1

    def lift_one(self, x, y):
        self.pile.append(x)
        self.hand.remove(x)
        self.pile.append(y)
        table.remove(y)

    def lift_two(self, x, y, z):
        self.pile.append(x)
        self.hand.remove(x)
        self.pile.append(y)
        self.pile.append(z)
        table.remove(y)
        table.remove(z)

    def lift_three(self, x, y, z, a):
        self.pile.append(x)
        self.hand.remove(x)
        self.pile.append(y)
        self.pile.append(z)
        self.pile.append(a)
        table.remove(y)
        table.remove(z)
        table.remove(a)

    def lift_four(self, x, y, z, a, b):
        self.pile.append(x)
        self.hand.remove(x)
        self.pile.append(y)
        self.pile.append(z)
        self.pile.append(a)
        self.pile.append(b)
        table.remove(y)
        table.remove(z)
        table.remove(a)
        table.remove(b)

    def lift_five(self, x, y, z, a, b, c):
        self.pile.append(x)
        self.hand.remove(x)
        self.pile.append(y)
        self.pile.append(z)
        self.pile.append(a)
        self.pile.append(b)
        self.pile.append(c)
        table.remove(y)
        table.remove(z)
        table.remove(a)
        table.remove(b)
        table.remove(c)


def new_deck():
    suit_list = ['Swords', 'Golds', 'Clubs', 'Cups']
    value_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    deck = list(product(suit_list, value_list))
    shuffle(deck)
    return deck


def open_rules():
    root = tk.Tk()
    text = tk.Text(root, height=200, width=200)
    text.pack()
    quote = """'Broom of 15' Rules:

This is a Spanish card game. The Spanish pack has 40 cards distributed in four suits: Golds, Cups, Swords and Clubs, and 
their values go from 1 to 10.

Two players may take part individually at 'Broom of 15'.

The version that I offer is valid for 2 players

Objective:
The objective is to get a 15 Brooms. There must be played as many hands as necessary until some of the players reaches 
that score, but it's possible to finish the game before and still have a winner.

The dynamic of the game entails joining groups of cards whose sum is 15, using a card from our hand, and one of more 
cards from the gaming table. The puntuation of each card is its value.

How the game goes on...

Start
Each player gets 3 cards in its hand and there are 4 cards face up in the table.

Play the cards
Player 1 makes the first move; every move entails in choosing one card from the hand and, if possible, sum 15 with one 
or several of the uncovered cards on the table. If the card used makes possible this kind of action, the player collects 
the used cards in a its Pile that may be increased in following turns. If it´s not possible to add 15 using any card 
from the player's hand and one or any of table cards, the player must choose a card from its hand and throw it to de 
table.

When one of the players lifts all table cards in one move, then it gets a Broom.

Each player uses one of his cards in his turn, and movements are repeated until they discard. Then, each of the players 
gets 3 cards again, and the cycle is repeated until the pack is finished.

When the game finishes (all the cards of the pack are been dealt and moved), the remainding cards in the table will be 
given to each player equitably.

Score count

One point for each Broom obtained by each player.
The player with the 7 of Golds will sum one Broom.
The player with the most number of 7s (included the 7 of oros) sums one point. If both players draw, it will check for 
6s, and it's still drawn, it'll check for 5s. If it's still drawn, none of the players get this Broom.
The player with the most number of Golds will sum one point. If two or more players draw none of them sums one Broom.
The player with the most number of cards will sum one point. If two or more players draw none of them sums one Broom.

When one of the hands is finished and one or more of the players reaches 15 Brooms, the player with the highest score 
wins the game.


    """
    text.insert(tk.END, quote)
    tk.mainloop()


while True:
    print('Lets play Broom of 15...\n')

    need_help = input('Type --help for help or press any key to continue ')
    if need_help == '--help':
        open_rules()
    else:
        pass
    option = input('New game? (y/n)\n')

    if option == 'y':
        player1 = Player()
        player1.set_name(input('Player 1: Please enter your name: '))
        player2 = Player()
        player2.set_name(input('Player 2: Please enter your name: '))
        while not player1.broom >= 15 or player2.broom >= 15:
            playing_deck = new_deck()
            player1.pile = []
            player2.pile = []
            table = []
            turn = 1
            while not (len(playing_deck) == 0 and len(player1.hand) == 0 and len(player2.hand) == 0):
                if len(table) == 0 and len(player2.hand) == 0:
                    for i in range(4 - len(table)):
                        table.append(playing_deck.pop())
                if len(player1.hand) == 0 and len(player2.hand) == 0 and len(playing_deck) != 0:
                    hand1 = [playing_deck.pop() for i in range(3)]
                    player1.set_hand(hand1)
                    hand2 = [playing_deck.pop() for i in range(3)]
                    player2.set_hand(hand2)
                system('cls')

                if turn == 1:

                    print(f'\nIt\'s {player1.name}\'s turn')
                    print('----------------------------')
                    print(f'You have {len(player1.pile)} cards in your Pile and have {player1.broom} Brooms')
                    print(f'\nYour hand: {player1.hand}')
                    print(f'\nTable: {table}\n')
                    need_help = input('Type --help for help or press any key to continue ')
                    if need_help == '--help':
                        open_rules()
                    else:
                        pass

                    option_move = input('Do you want to lift some cards? (y/n)\n')

                    if option_move == 'n':
                        try:
                            throw = int(input('Select the card to throw: '))
                            table.append(player1.hand[throw])
                            player1.hand.remove(player1.hand[throw])
                            turn = 2
                        except IndexError:
                            print('That card is invalid')
                        except ValueError:
                            print('That card is invalid')

                    elif option_move == 'y':
                        print('Make move')
                        try:
                            option_lift = int(input('How many cards do yo want to lift: '))
                            select_card = int(input('Select YOUR card: '))
                            if option_lift == 1:
                                index_table = int(input('Select the card to LIFT '))
                                try:
                                    if player1.hand[select_card][1] + table[index_table][1] == 15:
                                        player1.lift_one(player1.hand[select_card], table[index_table])
                                        if len(table) == 0:
                                            player1.set_broom()
                                        turn = 2
                                except IndexError:
                                    print('That card is invalid')
                                except ValueError:
                                    print('That card is invalid')

                            elif option_lift == 2:
                                table_card_1 = int(input('Select the card to LIFT: '))
                                table_card_2 = int(input('Select the card to LIFT: '))
                                try:
                                    if player1.hand[select_card][1] + table[table_card_1][1] + \
                                            table[table_card_2][1] == 15:
                                        player1.lift_two(player1.hand[select_card], table[table_card_1],
                                                         table[table_card_2])
                                        if len(table) == 0:
                                            player1.set_broom()
                                        turn = 2
                                except IndexError:
                                    print('That card is invalid')
                                except ValueError:
                                    print('That card is invalid')
                            elif option_lift == 3:
                                table_card_1 = int(input('Select the card to LIFT: '))
                                table_card_2 = int(input('Select the card to LIFT: '))
                                table_card_3 = int(input('Select the card to LIFT: '))
                                try:
                                    if player1.hand[select_card][1] + table[table_card_1][1] + table[table_card_2][1] \
                                            + table[table_card_3][1] == 15:
                                        player1.lift_three(player1.hand[select_card], table[table_card_1],
                                                           table[table_card_2], table[table_card_3])
                                        if len(table) == 0:
                                            player1.set_broom()
                                        turn = 2
                                except IndexError:
                                    print('That card is invalid')
                                except ValueError:
                                    print('That card is invalid')
                            elif option_lift == 4:
                                table_card_1 = int(input('Select the card to LIFT: '))
                                table_card_2 = int(input('Select the card to LIFT: '))
                                table_card_3 = int(input('Select the card to LIFT: '))
                                table_card_4 = int(input('Select the card to LIFT: '))
                                try:
                                    if player1.hand[select_card][1] + table[table_card_1][1] + table[table_card_2][1] \
                                            + table[table_card_3][1] + table[table_card_4][1] == 15:
                                        player1.lift_four(player1.hand[select_card], table[table_card_1],
                                                          table[table_card_2], table[table_card_3], table[table_card_4])
                                        if len(table) == 0:
                                            player1.set_broom()
                                        turn = 2
                                except IndexError:
                                    print('That card is invalid')
                                except ValueError:
                                    print('That card is invalid')
                            elif option_lift == 5:
                                table_card_1 = int(input('Select the card to LIFT: '))
                                table_card_2 = int(input('Select the card to LIFT: '))
                                table_card_3 = int(input('Select the card to LIFT: '))
                                table_card_4 = int(input('Select the card to LIFT: '))
                                table_card_5 = int(input('Select the card to LIFT: '))
                                try:
                                    if player1.hand[select_card][1] + table[table_card_1][1] + table[table_card_2][1] \
                                            + table[table_card_3][1] + table[table_card_4][1] + \
                                            table[table_card_5][1] == 15:
                                        player1.lift_five(player1.hand[select_card], table[table_card_1],
                                                          table[table_card_2], table[table_card_3], table[table_card_4],
                                                          table[table_card_5])
                                        if len(table) == 0:
                                            player1.set_broom()
                                        turn = 2
                                except IndexError:
                                    print('That card is invalid')
                                except ValueError:
                                    print('That card is invalid')
                            else:
                                print('Choose again')
                        except IndexError:
                            print('That card is invalid')
                        except ValueError:
                            print('That card is invalid')
                else:

                    system('cls')
                    print(f'\nIt\'s {player2.name}\'s turn')
                    print('----------------------------')
                    print(f'You have {len(player2.pile)} cards in your pile and have {player2.broom} Brooms')
                    print(f'\nYour hand: {player2.hand}')
                    print(f'\nTable: {table}\n')
                    need_help = input('Type --help for help or press any key to continue ')
                    if need_help == '--help':
                        open_rules()
                    else:
                        pass
                    option_move = input('Do you want to lift some cards? (y/n)\n')
                    if option_move == 'n':
                        try:
                            throw = int(input('Select the card to throw: '))
                            table.append(player2.hand[throw])
                            player2.hand.remove(player2.hand[throw])
                            turn = 1
                        except IndexError:
                            print('That card is invalid')
                        except ValueError:
                            print('That card is invalid')
                    elif option_move == 'y':
                        print('Make move')
                        try:
                            option_lift = int(input('How many cards do yo want to lift?: '))
                            select_card = int(input('Select YOUR card: '))
                            if option_lift == 1:
                                index_table = int(input('Select the card to LIFT: '))
                                try:
                                    if player2.hand[select_card][1] + table[index_table][1] == 15:
                                        player2.lift_one(player2.hand[select_card], table[index_table])
                                        if len(table) == 0:
                                            player2.set_broom()
                                        turn = 1
                                except IndexError:
                                    print('That card is invalid')
                                except ValueError:
                                    print('That card is invalid')
                            elif option_lift == 2:
                                table_card_1 = int(input('Select the card to LIFT: '))
                                table_card_2 = int(input('Select the card to LIFT: '))
                                try:
                                    if player2.hand[select_card][1] + table[table_card_1][1] + \
                                            table[table_card_2][1] == 15:
                                        player2.lift_two(player2.hand[select_card], table[table_card_1],
                                                         table[table_card_2])
                                        if len(table) == 0:
                                            player2.set_broom()
                                        turn = 1
                                except IndexError:
                                    print('That card is invalid')
                                except ValueError:
                                    print('That card is invalid')
                            elif option_lift == 3:
                                table_card_1 = int(input('Select the card to LIFT: '))
                                table_card_2 = int(input('Select the card to LIFT: '))
                                table_card_3 = int(input('Select the card to LIFT: '))
                                try:
                                    if player2.hand[select_card][1] + table[table_card_1][1] + table[table_card_2][1] \
                                            + table[table_card_3][1] == 15:
                                        player2.lift_three(player2.hand[select_card], table[table_card_1],
                                                           table[table_card_2], table[table_card_3])
                                        if len(table) == 0:
                                            player2.set_broom()
                                        turn = 1
                                except IndexError:
                                    print('That card is invalid')
                                except ValueError:
                                    print('That card is invalid')
                            elif option_lift == 4:
                                table_card_1 = int(input('Select the card to LIFT: '))
                                table_card_2 = int(input('Select the card to LIFT: '))
                                table_card_3 = int(input('Select the card to LIFT: '))
                                table_card_4 = int(input('Select the card to LIFT: '))
                                try:
                                    if player2.hand[select_card][1] + table[table_card_1][1] + table[table_card_2][1] \
                                            + table[table_card_3][1] + table[table_card_4][1] == 15:
                                        player2.lift_four(player2.hand[select_card], table[table_card_1],
                                                          table[table_card_2], table[table_card_3], table[table_card_4])
                                        if len(table) == 0:
                                            player2.set_broom()
                                        turn = 1
                                except IndexError:
                                    print('That card is invalid')
                                except ValueError:
                                    print('That card is invalid')
                            elif option_lift == 5:
                                table_card_1 = int(input('Select the card to LIFT: '))
                                table_card_2 = int(input('Select the card to LIFT: '))
                                table_card_3 = int(input('Select the card to LIFT: '))
                                table_card_4 = int(input('Select the card to LIFT: '))
                                table_card_5 = int(input('Select the card to LIFT: '))
                                try:
                                    if player2.hand[select_card][1] + table[table_card_1][1] + table[table_card_2][1] \
                                            + table[table_card_3][1] + table[table_card_4][1] \
                                            + table[table_card_5][1] == 15:
                                        player2.lift_five(player2.hand[select_card], table[table_card_1],
                                                          table[table_card_2], table[table_card_3], table[table_card_4],
                                                          table[table_card_5])
                                        if len(table) == 0:
                                            player2.set_broom()
                                        turn = 1
                                except IndexError:
                                    print('That card is invalid')
                                except ValueError:
                                    print('That card is invalid')
                            else:
                                print('Choose again')
                        except IndexError:
                            print('That card is invalid')
                        except ValueError:
                            print('That card is invalid')

            if len(table) != 0:
                number_cards_each = int(len(table) / 2)
                for i in range(number_cards_each):
                    player1.pile.append(table[0])
                    table.remove(table[0])
                for i in range(len(table) - number_cards_each):
                    player2.pile.append(table[0])
                    table.remove(table[0])
            print(f'\n')

            if len(player1.pile) > len(player2.pile):
                player1.set_broom()
                print(f'{player1.name} has lifted more cards!')
            elif len(player1.pile) < len(player2.pile):
                player2.set_broom()
                print(f'{player2.name} has lifted more cards!')
            else:
                pass

            player1_golds = [x for x in player1.pile if x[0] == 'Golds']
            player2_golds = [x for x in player2.pile if x[0] == 'Golds']
            if len(player1_golds) > len(player2_golds):
                player1.set_broom()
                print(f'{player1.name} has lifted more golds!')
            elif len(player1_golds) < len(player2_golds):
                player2.set_broom()
                print(f'{player2.name} has lifted more golds!')
            else:
                pass

            if ('Golds', 7) in player1.pile:
                player1.set_broom()
                print(f'{player1.name} has lifted the 7 of Golds!')
            else:
                player2.set_broom()
                print(f'{player2.name} has lifted the 7 of Golds!')

            player1_sevens = [x for x in player1.pile if x[1] == 7]
            player2_sevens = [x for x in player2.pile if x[1] == 7]
            if len(player1_sevens) > len(player2_sevens):
                player1.set_broom()
                print(f'{player1.name} has lifted more 7s!')
            elif len(player1_sevens) < len(player2_sevens):
                player2.set_broom()
                print(f'{player2.name} has lifted more 7s!')
            else:
                player1_sixes = [x for x in player1.pile if x[1] == 6]
                player2_sixes = [x for x in player2.pile if x[1] == 6]
                if len(player1_sixes) > len(player2_sixes):
                    player1.set_broom()
                    print(f'{player1.name} has lifted more 7s!')
                elif len(player1_sixes) < len(player2_sixes):
                    player2.set_broom()
                    print(f'{player2.name} has lifted more 7s!')
                else:
                    player1_fives = [x for x in player1.pile if x[1] == 5]
                    player2_fives = [x for x in player2.pile if x[1] == 5]
                    if len(player1_fives) > len(player2_fives):
                        player1.set_broom()
                        print(f'{player1.name} has lifted more 7s!')
                    elif len(player1_fives) < len(player2_fives):
                        player2.set_broom()
                        print(f'{player2.name} has lifted more 7s!')
                    else:
                        pass
            print('-------------------------------------')
            print(f'{player1.name} has got {player1.broom} brooms!')
            print(f'{player2.name} has got {player2.broom} brooms!\n')

            rematch = input('Do you want to keep playing? (y/n): ')
            if rematch == 'y':
                continue
            elif rematch == 'n':
                break
            else:
                print(rematch)

        if player1.broom > player2.broom:
            print(f'{player1.name} has won!!')
        elif player1.broom < player2.broom:
            print(f'{player2.name} has won!!')
        else:
            print(f'{player1.name} and {player2.name} have tied...')

        rematch = input('Do you want to keep playing? (y/n): ')
        if rematch == 'y':
            continue
        elif rematch == 'n':
            break
        else:
            print(rematch)
    elif option == 'n':
        break
    else:
        pass



