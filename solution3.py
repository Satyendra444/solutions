import math

def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    sqrt_discriminant = math.sqrt(discriminant)
    root1 = (-b + sqrt_discriminant) / (2*a)
    root2 = (-b - sqrt_discriminant) / (2*a)
    return (root1, root2)
print(find_roots(2, 10, 8))
