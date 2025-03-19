class Board:

    def display_board(self):
        tictactoe_board = """
                    _ | _ | _ 
                    _ | _ | _ 
                      |   |   
                """
        print(tictactoe_board)



    def print_score_board(self,score_board):
        print("\t--------------------------------")
        print("\t         SCORE BOARD             ")
        print("\t--------------------------------")
        players = list(score_board.keys())
        print("\t   ", players[0], "\t    ", score_board[players[0]])
        print("\t   ", players[1], "\t    ", score_board[players[1]])
        print("\t--------------------------------\n")
        print("\t Would you like to play again? If Yes continue If No use the door:\n ", end="")

