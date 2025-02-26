import numpy as np
from utils.constants import Color, Piece, Rank, File
from square import Square
from move.move import Move

# ekvivalent med "state"
class ChessBoard:
  def __init__(self):
    #[[0 0 0 0 0 0],
    # [0 0 0 0 0 0]]
    # 2 sides, 6 piece bitboards
    self.bitboards = np.zeros((2, 6), dtype=np.uint64)
    # Combined bitboard for all pieces of each color
    self.bb_color = np.zeros(2, dtype=np.uint64)
    # Combined bitboard for all pieces
    self.bb_all = np.uint64(0)
    # Color to move
    self.current_color = Color.WHITE

  def new_game(self):
    # Example: self.bitboards[0][0] contains all white pawns, visually (omit /):
    # 00000000/00000000/00000000/00000000/00000000/00000000/11111111/00000000
    self.bitboards[Color.WHITE][Piece.PAWN] = np.uint64(0x000000000000FF00)
    self.bitboards[Color.WHITE][Piece.KNIGHT] = np.uint64(0x0000000000000042)
    self.bitboards[Color.WHITE][Piece.BISHOP] = np.uint64(0x0000000000000024)
    self.bitboards[Color.WHITE][Piece.ROOK] = np.uint64(0x0000000000000081)
    self.bitboards[Color.WHITE][Piece.QUEEN] = np.uint64(0x0000000000000008)
    self.bitboards[Color.WHITE][Piece.KING] = np.uint64(0x0000000000000010)
    
    self.bitboards[Color.BLACK][Piece.PAWN] = np.uint64(0x00FF000000000000)
    self.bitboards[Color.BLACK][Piece.KNIGHT] = np.uint64(0x4200000000000000)
    self.bitboards[Color.BLACK][Piece.BISHOP] = np.uint64(0x2400000000000000)
    self.bitboards[Color.BLACK][Piece.ROOK] = np.uint64(0x8100000000000000)
    self.bitboards[Color.BLACK][Piece.QUEEN] = np.uint64(0x0800000000000000)
    self.bitboards[Color.BLACK][Piece.KING] = np.uint64(0x1000000000000000)

    return self.bitboards
  
  def apply_move(self, move: Move) -> None:
    pass
    
  def check_win(self, move: Move) -> True:
    pass

  def check_draw(self, state, move):
    pass