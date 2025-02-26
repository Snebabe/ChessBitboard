import numpy as np

from board.chessboard import ChessBoard
from move.move import Move
from move.movegen import MoveGen

from utils.constants import Color
# Wrapper ish som MCTS och Boten ska prata med
class Chess:
  def __init__(self):
    # kanske inte behövs
    pass

  def get_initial_state(self) -> ChessBoard: # -> state
    state = ChessBoard()
    state.new_game()
    return state

  def get_next_state(self, state: ChessBoard, action: Move) -> ChessBoard: # -> state
    state.apply_move(action)
    return state

  def get_valid_moves(self, state: ChessBoard): # -> kanske map(a1a2 = 0, a1a3 = 1 ...)
    # kommer nog vara mer komplicerad
    return MoveGen.gen_legal_moves(state)
  
  def check_win(self, state: ChessBoard, action: Move) -> bool:
    pass

  def check_draw(self, state: ChessBoard, action: Move) -> bool:
    pass

  def get_value_and_terminated(self, state: ChessBoard, action: Move) -> tuple[int, bool]: # -> (int, bool)
    return 0, False

  def get_opponent(self, player: Color) -> Color: # -> player
    return Color.BLACK if player == Color.WHITE else Color.WHITE

  def get_opponent_value(self, value: int) -> int: # -> value
    return -value

  def change_perspective(self, state: ChessBoard, player: Color) -> ChessBoard: # -> state
    # kanske inte ens behövs 
    pass

  def get_encoded_state(self, state: ChessBoard): # -> state
    # Encode for AI
    # Konvertera till input stacks
    # killgissar
    bitboards = state.bitboards
    encoded_state = np.stack((bitboards))
    return encoded_state