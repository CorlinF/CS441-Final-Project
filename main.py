from board import Board
def print_board(state):
    for row in state:
        print(" ".join(str(x) for x in row))
    print()

def main():
    board_state = Board.initialize_board()
    board = Board(board_state)
    print_board(board.state)
    print(board.random_game(1))

if __name__ == "__main__":
    main()
    