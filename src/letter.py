class Letter:
    def __init__(self, let, theme):
        self.letter = let
        if theme:
            self.color = (0, 0, 0)
        else:
            self.color = (255, 255, 255)
