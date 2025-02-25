import numpy as np

from utils.constants import Rank, File

class Square:
  def __init__(self, index: int):
    self.index = np.uint8(index)

  def __str__(self):
    r = self.index // 8
    f = self.index % 8

    return f"{chr(ord('A')+f)}{r+1}"
  
  @classmethod
  def from_position(cls, r: Rank, f: File): 
    # rank * 8 + file
    return cls((r.value << np.uint8(3)) |f.value)
  
  @classmethod
  def from_str(cls, st: str):
    f = np.uint(ord(st[0]) - ord('A'))
    r = np.uint(int(st[1]) - 1)
    # rank * 8 + file
    return cls((r << np.uint8(3)) | f)
  
  def to_bitboard(self):
    return np.uint64(1) << self.index