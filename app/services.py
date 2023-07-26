moves = { "queen"   : [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)],
          "bishop"  : [(1, 1), (1, -1), (-1, 1), (-1, -1)],
          "rook"    : [(0, 1), (0, -1), (1, 0), (-1, 0)],
          "knight"  : [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]}

ATTACK_POS = 1
PLACED_PIECE = 2
PROTECTED_PIECE = 3

def is_within_chessboard(i,j):
    """ Validates boundary of chessboard"""
    if(i >= 0 and i <=7 and j >= 0 and j <= 7):
        return True
    return False

def fill_valid_pos(chess_piece, chess_board, bottom_index, left_index, directions, index):
    next_bottom = bottom_index + directions[index][0]
    next_left   = left_index + directions[index][1]

    if(is_within_chessboard(next_bottom, next_left)):
        if(chess_board[next_bottom][next_left] == PLACED_PIECE or chess_board[next_bottom][next_left] == PROTECTED_PIECE):
            chess_board[next_bottom][next_left] = PROTECTED_PIECE
            return
        chess_board[next_bottom][next_left] = ATTACK_POS
        fill_valid_pos(chess_piece, chess_board, next_bottom, next_left, directions, index)
    else:
        return

def fill_valid_pos_knight(chess_piece, chess_board, bottom_index, left_index, directions, index):
    next_bottom = bottom_index + directions[index][0]
    next_left   = left_index + directions[index][1]
    if is_within_chessboard(next_bottom, next_left) :
        if(chess_board[next_bottom][next_left] == PLACED_PIECE):
            chess_board[next_bottom][next_left] = PROTECTED_PIECE
        else:
            chess_board[next_bottom][next_left] = ATTACK_POS

def get_valid_pos(chess_piece, chess_board, bottom_index, left_index, directions, index):
    list_of_moves =[]
    next_bottom = bottom_index + directions[index][0]
    next_left   = left_index + directions[index][1]

    if(is_within_chessboard(next_bottom, next_left)):
        # Unprotected so kill and return
        if chess_board[next_bottom][next_left] == PLACED_PIECE :
            list_of_moves.append([next_bottom,next_left])
            return list_of_moves
        # Protected so only return
        elif chess_board[next_bottom][next_left] == PROTECTED_PIECE:
            return list_of_moves
        # Another piece is attacking this location so recurssively check next location in same direction
        elif chess_board[next_bottom][next_left] == ATTACK_POS:
            list_of_moves.extend(get_valid_pos(chess_piece, chess_board, next_bottom, next_left, directions, index))
            return list_of_moves
        # Valid position
        else :
            list_of_moves.append([next_bottom,next_left])
            list_of_moves.extend(get_valid_pos(chess_piece, chess_board, next_bottom, next_left, directions, index))
            return list_of_moves
    else:
        return list_of_moves

def get_valid_pos_knight(chess_piece, chess_board, bottom_index, left_index, directions, index):
    list_of_moves = []
    next_bottom = bottom_index + directions[index][0]
    next_left   = left_index + directions[index][1]
    if(is_within_chessboard(next_bottom, next_left)):
        if chess_board[next_bottom][next_left] not in [ATTACK_POS,PROTECTED_PIECE] :
            list_of_moves.append([next_bottom,next_left])
    return list_of_moves


def get_valid_moves(positions) -> 'List' :
    chess_board = [[0 for i in range(8)] for j in range(8)]
    for piece, pos in positions.items():
        bottom_index = ord(list(pos)[0]) - ord('A')
        left_index   = int(list(pos)[1]) - 1
        chess_board[bottom_index][left_index] = PLACED_PIECE #Original positions of all the chess pieces

    for piece, pos in positions.items():
        bottom_index = ord(list(pos)[0]) - ord('A')
        left_index   = int(list(pos)[1]) - 1
        if(piece.lower() in ["queen", "bishop", "rook"]):
            for dir in range(len(moves[piece.lower()])):
                fill_valid_pos(piece, chess_board, bottom_index, left_index, moves[piece.lower()], dir)
        elif(piece.lower() == "knight"):
            for dir in range(len(moves[piece.lower()])):
                fill_valid_pos_knight(piece, chess_board, bottom_index, left_index, moves[piece.lower()], dir)
        else:
            print("Invalid Chess Piece")
    return chess_board
           
def get_moves_for_slug(chess_board,piece,pos):
    bottom_index = ord(list(pos)[0]) - ord('A')
    left_index   = int(list(pos)[1]) - 1
    list_of_moves = []
    if(piece.lower() in ["queen", "bishop", "rook"]):
        for dir in range(len(moves[piece.lower()])):
            list_of_moves.extend(get_valid_pos(piece, chess_board, bottom_index, left_index, moves[piece.lower()], dir))
    elif(piece.lower() == "knight"):
        for dir in range(len(moves[piece.lower()])):
            list_of_moves.extend(get_valid_pos_knight(piece, chess_board, bottom_index, left_index, moves[piece.lower()], dir))
    else:
        print("Invalid Chess Piece")
    return list_of_moves

