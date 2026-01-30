class Game:
    def __init__(self):
        self.table = [1,2,3,4,5,6,7,8,9]
        self.game_over = False
        self.players = ["X", "O"]
        self.turn = 0
        self.winner = ""

    def verify_move(self, pos: int):
        if 1 <= pos <= 9:
            if type(self.table[pos-1]) is int:
                return True
        return False

    def apply_move(self, pos: int):
        if not self.verify_move(pos):
            print("Mutare invalida")
            return False
        else:
            self.table[pos-1] = self.players[self.turn]
            if self.check_win():
                self.game_over = True
                self.winner = self.players[self.turn]
                return True
            elif self.check_draw():
                self.game_over = True
                return True
            else:
                self.turn = 1 - self.turn
                return True

    def check_win(self):
        win_condition = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for w in win_condition:
            va = self.table[w[0]]
            vb = self.table[w[1]]
            vc = self.table[w[2]]
            if va == vb == vc and isinstance(va, str):
                return True
        return False

    def check_draw(self):
        for i in self.table:
            if isinstance(i, int):
                return False
        return True