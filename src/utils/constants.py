from enum import IntEnum

class Color(IntEnum):
  WHITE = 0
  BLACK = 1

  def __invert__(self):
    return Color.BLACK if self == Color.WHITE else Color.WHITE
  
class Piece(IntEnum):
  PAWN = 0
  KNIGHT = 1
  BISHOP = 2
  ROOK = 3
  QUEEN = 4
  KING = 5

  def to_char(self):
    match self:
      case Piece.PAWN: return 'p'
      case Piece.KNIGHT: return 'n'
      case Piece.BISHOP: return 'b'
      case Piece.ROOK: return 'r'
      case Piece.QUEEN: return 'q'
      case Piece.KING: return 'k'

class Rank(IntEnum):
  ONE = 0
  TWO = 1
  THREE = 2
  FOUR = 3
  FIVE = 4
  SIX = 5
  SEVEN = 6
  EIGHT = 7

class File(IntEnum):
  A = 0
  B = 1
  C = 2
  D = 3
  E = 4
  F = 5
  G = 6
  H = 7