from fractions import Fraction

values = [Fraction(1, 3), Fraction(1, 6), Fraction(1, 2)]
total = sum(values, Fraction(0))
print(f"{total.numerator}/{total.denominator}")
