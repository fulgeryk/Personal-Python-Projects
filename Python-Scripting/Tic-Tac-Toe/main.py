from Game import Game
from Player import Player
from AIPlayer import AIPlayer
new_game = Game()

def show_table(table):
    for i in range(0, len(table), 3):
        print(f"{table[i]} | {table[i+1]} | {table[i+2]}")
        if i != 6:
            print("---------")

human = Player(new_game.players[0])
ai_player = AIPlayer(new_game.players[1])
show_table(new_game.table)
while not new_game.game_over:
    if new_game.turn == 0:
        move = human.choose_move()
        while not new_game.apply_move(move):
            move = human.choose_move()
    else:
        move = ai_player.choose_move(new_game)
        print(f"{ai_player.symbol} choose position {move}")
        while not new_game.apply_move(move):
            move = ai_player.choose_move(new_game)
    show_table(new_game.table)
    if new_game.game_over and new_game.winner == "":
        print("It's a draw")

if new_game.winner:
    print(f"Winner is {new_game.winner}")
