from fractions import Fraction
import sys

values = [Fraction(1, 3), Fraction(1, 6), Fraction(1, 2)]
total = sum(values, Fraction(0))
sys.stdout.buffer.write(f"{total.numerator}/{total.denominator}\n".encode("ascii"))
