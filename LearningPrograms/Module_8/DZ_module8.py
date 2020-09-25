class Fraction:
    def __init__(self, a, b):
        self.chisl = a
        self.znamen = b
        self.drobnoe = a / b

    def __add__(self, other):
        return self.drobnoe + other

    def __radd__(self, other):
        return other + self.drobnoe

    def __sub__(self, other):
        return self.drobnoe - other

    def __rsub__(self, other):
        return other - self.drobnoe


chiselko = Fraction(a=1, b=2)
drugoe = Fraction(a=2, b=1)
print(chiselko + drugoe)
