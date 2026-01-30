import random

class AIPlayer:
    def __init__(self, symbol):
        self.symbol = symbol


    def choose_move(self, game):
        ai_table = []
        for i in game.table:
            if isinstance(i, int):
                ai_table.append(i)
        pos = random.choice(ai_table)
        return pos
