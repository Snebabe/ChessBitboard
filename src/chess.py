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

  def get_initial_state(self) -> ChessBoard: # -> state (bitboards)
    state = ChessBoard()
    state.new_game()
    return state

  def get_next_state(self, state: ChessBoard, action: Move) -> ChessBoard: # -> state
    return state.apply_move(action)

  def get_valid_moves(self, state: ChessBoard): # -> map(a1a2 = 0, a1a3 = 1 ...)
    # kommer nog vara mer komplicerad
    return MoveGen.gen_legal_moves(state)

  def get_value_and_terminated(self, state: ChessBoard, action: Move): # -> (int, bool)
    if state.check_win(state, action):
      return 1, True
    if state.check_draw(state, action):
      return 0, True
    return 0, False

  def get_opponent(self, player: Color): # -> player
    return Color.BLACK if player == Color.WHITE else Color.WHITE

  def get_opponent_value(self, value: int): # -> value
    return -value

  def change_perspective(self, state: ChessBoard, player: Color): # -> state
    # kanske inte ens behövs 
    pass

  def get_encoded_state(self, state: ChessBoard): # -> state
    # Encode for AI
    # Konvertera till input stacks
    # killgissar
    bitboards = state.bitboards
    encoded_state = np.stack((bitboards))
    return encoded_state
    pass