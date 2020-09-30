class Fraction:
    def __init__(self, chisl, znamen):
        self.chisl = chisl
        self.znamen = znamen
        self.zelaya_chast = chisl // znamen
        self.plav_t = chisl / znamen

    def __str__(self):
        return "{}/{}".format(self.chisl, self.znamen)

    def __add__(self, other):
        if hasattr(other, 'chisl'):
            perv = self.chisl * other.znamen
            vtor = self.znamen * other.chisl
            return "{} + {} = {}/{}".format(self.__str__(), other.__str__(), perv + vtor, self.znamen * other.znamen)
        else:
            return "{} + {} = {}/{}".format(self.__str__(), other, self.chisl + (self.znamen * other), self.znamen)

    def __radd__(self, other):
        if hasattr(other, 'chisl'):
            perv = self.chisl * other.znamen
            vtor = self.znamen * other.chisl
            return "{} + {} = {}/{}".format(other.__str__(), self.__str__(), perv + vtor, self.znamen * other.znamen)
        else:
            return "{} + {} = {}/{}".format(other, self.__str__(), self.chisl + (self.znamen * other), self.znamen)

    def __sub__(self, other):
        if hasattr(other, 'chisl'):
            perv = self.chisl * other.znamen
            vtor = self.znamen * other.chisl
            return "{} - {} = {}/{}".format(self.__str__(), other.__str__(), perv - vtor, self.znamen * other.znamen)
        else:
            return "{} - {} = {}/{}".format(self.__str__(), other, self.chisl - (self.znamen * other), self.znamen)

    def __rsub__(self, other):
        if hasattr(other, 'chisl'):
            perv = self.chisl * other.znamen
            vtor = self.znamen * other.chisl
            return "{} - {} = {}/{}".format(other.__str__(), self.__str__(), perv - vtor, self.znamen * other.znamen)
        else:
            return "{} - {} = {}/{}".format(other, self.__str__(), (self.znamen * other) - self.chisl, self.znamen)

    def __mul__(self, other):
        if hasattr(other, 'chisl'):
            perv = self.chisl * other.chisl
            vtor = self.znamen * other.znamen
            return "{} * {} = {}/{}".format(self.__str__(), other.__str__(), perv, vtor)
        else:
            return "{} * {} = {}/{}".format(self.__str__(), other.__str__(), self.chisl * other, self.znamen)

    def __rmul__(self, other):
        if hasattr(other, 'chisl'):
            perv = self.chisl * other.chisl
            vtor = self.znamen * other.znamen
            return "{} * {} = {}/{}".format(other.__str__(), self.__str__(), perv, vtor)
        else:
            return "{} * {} = {}/{}".format(other.__str__(), self.__str__(), self.chisl * other, self.znamen)

    def __int__(self):
        return self.chisl // self.znamen

    def __float__(self):
        return self.chisl / self.znamen


class OperationsOnFraction(Fraction):
    def __init__(self, chisl, znamen):
        super().__init__(chisl=chisl, znamen=znamen)

    def getint(self):
        return self.chisl // self.znamen

    def getFloat(self):
        return self.chisl / self.znamen


chiselko = Fraction(chisl=1, znamen=2)
drugoe = Fraction(chisl=2, znamen=1)
print(chiselko)
print(drugoe)
print(chiselko - drugoe)
print(drugoe - chiselko)
print(5 - chiselko)
Sum_fract = chiselko + drugoe
print(chiselko + drugoe)
Kirusha = Fraction(chisl=22, znamen=174)
print(Kirusha * chiselko)
print(Kirusha * 5)
print(int(drugoe))
print(float(Kirusha))
Deniska = OperationsOnFraction(chisl=10, znamen=5)
print(Deniska.getFloat())
