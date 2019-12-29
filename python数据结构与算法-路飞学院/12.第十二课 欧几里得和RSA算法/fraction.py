class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        x = self.gcd_no_rec(a, b)
        self.a /= x
        self.b /= x

    @classmethod
    def gcd_no_rec(cls, a, b):
        # 最大公约数
        while b > 0:
            r = a % b
            a = b
            b = r
        return a

    @classmethod
    def zgs(cls, a, b):
        # 最小公倍数
        x = cls.gcd_no_rec(a, b)
        return a * b / x

    def __str__(self):
        return "%d/%d" % (self.a, self.b)

    # 运算符重载函数__add__
    def __add__(self, other):
        # 3/5 + 2/7
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        # 算出最小公倍数
        denom = self.zgs(b, d) # 分母
        molecule = a * (denom / b) + c * (denom / d) # 分子
        return Fraction(molecule, denom)


f = Fraction(30, 16)
print(f)
a = Fraction(1, 3)
b = Fraction(1, 2)
print(a+b)