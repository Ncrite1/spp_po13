import math

def solve_quadratic(a, b, c):
    if a == 0: raise ValueError("Not a quadratic equation")
    D = b**2 - 4*a*c
    if D < 0: return []
    if D == 0: return [-b / (2*a)]
    return [(-b - math.sqrt(D)) / (2*a), (-b + math.sqrt(D)) / (2*a)]
