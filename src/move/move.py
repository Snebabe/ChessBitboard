class Move:
  def __init__(self, src, dest, promo=None):
    self.src = src
    self.dest = dest
    self.promo = promo

  def __str__(self):
    s = f"{str(self.src)} -> {str(self.dest)}"
    if self.promo:
      s += " TODO"

    return s
    