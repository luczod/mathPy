""""
the probability of the union of the two sets (A or B)
the probability of the intersect of the two sets (A and B)
"""

from sympy import FiniteSet

s = FiniteSet(1, 2, 3, 4, 5, 6)
a = FiniteSet(2, 3, 5)
b = FiniteSet(1, 3, 5)
e = a.union(b)

result = len(e)/len(s) # type: ignore
print("Event A OR Event B: {0}".format(result))

s = FiniteSet(1, 2, 3, 4, 5, 6)
a = FiniteSet(2, 3, 5)
b = FiniteSet(1, 3, 5)
e = a.intersect(b)

result = len(e)/len(s) # type: ignore
print("Event A AND Event B: {0}".format(result))