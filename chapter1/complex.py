# Python also supports complex numbers with the imaginary part identified by
# the letter j or J
# (as opposed to the letter i used in mathematical notation, 2 + 3i).
# Both the real and imaginary parts are floating point numbers.

a = 2 + 3j
print(type(a))  # <class 'complex'>

a = complex(2, 3)
print(a)  # (2 + 3j)

z = 2 + 3j
print(z.real, z.imag)  # 2.0, 3.0
