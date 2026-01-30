class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def choose_move(self):
        while True:
            try:
                pos = int(input(f"{self.symbol} : What position do you want to move (1-9)? "))
                if pos < 1 or pos > 9:
                    print("You should use only index (1-9) ")
                    continue
            except ValueError:
                print("You should use only index (1-9) ")
                continue
            return pos
