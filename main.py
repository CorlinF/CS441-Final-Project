from board import Board
def print_board(state):
    for row in state:
        print(" ".join(str(x) for x in row))
    print()

def main():
    board_state = Board.initialize_board()
    board = Board(board_state)
    print_board(board.state)
    move=board.random_move(1)
    piece=move[0]
    position=move[1]
    board.make_move(piece,position)
    print_board(board.state)

if __name__ == "__main__":
    main()
    