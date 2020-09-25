class Multyplier:

    def __init__(self, factor=2):
        self.factor = factor

    def __call__(self, *args):
        res = []
        for item in args:
            res.append(item * self.factor)
        return res


mul_by_27 = Multyplier(factor=27)
result = mul_by_27(1, 2, 3, 4)
print(result)

# multipiers = []
# for factor in (2, 3, 4, 5):
#     mul = Multyplier(factor=factor)
#     multipiers.append(mul)
# print(multipiers)
#
# for mul in multipiers:
#     print(mul(10, 20, 30))
