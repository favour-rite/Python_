from tictactoe.Board import Board
from tictactoe.Players import Players

class User:

    @staticmethod
    def main_menu():
        board = Board()
        game_over = False
        try:
            player1 = input("Input your name, player 1: ")
            player2 = input("Input your name, player 2: ")
        except ValueError:
            print("Wrong Input!!! Try Again")

        player_choice = {'X': "", 'O': ""}
        current_player = player1
        options = ['X', 'O']
        score_board = {player1: 0, player2: 0}

        while not game_over:
            print("""Turn to choose for", current_player     
                    Enter 1 for X"
                    Enter 2 for O"
                    Enter 3 to Quit
                """)
            try:
                choice = int(input(" Input your choice: "))
            except ValueError:
                print("Wrong Input!!! Try Again\n")

            if choice == 1:
                board.display_board()
                player_choice['X'] = current_player
                if current_player == player1:
                    player_choice['O'] = player2
                else:
                    player_choice['O'] = player1
            elif choice == 2:
                board.display_board()
                player_choice['O'] = current_player
                if current_player == player1:
                    player_choice['X'] = player2
                else:
                    player_choice['X'] = player1
            elif choice == 3:
                board.print_score_board(score_board)
                print("Final Scores For This Game")
                score_board = {player1: 0, player2: 0}

                break
            else:
                print("Wrong Choice!!!! Try Again\n")

User.main_menu()