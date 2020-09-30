class Fraction:
    def __init__(self, a, b):
        self.chisl = a
        self.znamen = b
        self.zelaya_chast = a // b
        self.plav_t = a / b

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
    def __init__(self, a, b):
        super().__init__(a=a, b=b)

    def getint(self):
        return self.a // self.b

    def getFloat(self):
        return  self.a / self.b


# chiselko = Fraction(a=1, b=2)
# drugoe = Fraction(a=2, b=1)
# # print(chiselko)
# # print(drugoe)
# # # print(chiselko - drugoe)
# # # print(drugoe - chiselko)
# # print(5 - chiselko)
# # Sum_fract = chiselko + drugoe
# # print(chiselko + drugoe)
# Kirusha = Fraction(a=22, b=174)
# print(Kirusha * chiselko)
# print(Kirusha * 5)
# print(int(drugoe))
# print(float(Kirusha))
Deniska = OperationsOnFraction(a=10, b=5)
print(Deniska.getFloat())
