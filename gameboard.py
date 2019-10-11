class game_board():
    def board(self):
        for i in range(4):
            print("-"*7)
            if(i!=3):
                print("| "*4)
b=game_board()
b.board()
