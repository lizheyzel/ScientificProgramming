from fractions import Fraction
from quadeqtools import print_matrix

## Our goal is to find the quadratic equation through three given points.

# Start with three points with integer values for x and y:
points = [(3, 4), (5, 2), (10, 7)]

# Generate an augmented matrix from these  
m = []
for i in range(3):
    row = []
    row.append(Fraction(points[i][0]) ** 2)
    row.append(Fraction(points[i][0]))
    row.append(Fraction(1))
    row.append(Fraction(points[i][1]))
    m.append(row)

print_matrix(m)

# Set the first value in row 1 to 1
val = 1 / m[0][0]
for i in range(len(m[0])):
    m[0][i] *= val

print_matrix(m)

# Use row 1 to make the first value in rows 2 and 3 equal 0
val1 = -m[1][0]
val2 = -m[2][0] 
for i in range(len(m[0])):
    m[1][i] += val1 * m[0][i]
    m[2][i] += val2 * m[0][i]

print_matrix(m)

# Set the first non-zero value in row 2 to 1
val = 1 / m[1][1]
for i in range(len(m[0])):
    m[1][i] *= val

print_matrix(m)

# Use row 2 to make the 2nd value in row 3 equal 0
val = -m[2][1]
for i in range(len(m[1])):
    m[2][i] += val * m[1][i]

print_matrix(m)

# Set the coefficient of c (the 3rd value in the 3rd row of m) to 1
