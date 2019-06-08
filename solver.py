import math

def solver(a, b, c):
    print("\nReduced form: %dX^2 + %dX^1 + %d = 0\n" % (a, b, c))
    if (a == 0 and b == 0):
        if (c == 0):
            print("Well done, you learn that 0 = 0!")
        else:
            print("Invalid equation")
    elif a == 0:
        print("Polynomial degree: 1")
        sol = (-c) / b
        print("x = " + str(sol))
    else:
        print("Polynomial degree: 2")
        delta = b * b - 4 * a * c
        print("Delta: " + str(delta))
        if delta > 0:
            num = -b - math.sqrt(delta)
            den = 2 * a
            print("\nx1 = " + str(num / den))
            num = -b + math.sqrt(delta)
            print("x2 = " + str(num / den))
        elif delta == 0:
            x1 = -b / 2 * a
            print(x1)
        else:
            print('\nComplex solutions:')
            first = -b / (2 * a)
            second = math.sqrt(-delta) / (2 * a)
            print("x1 = " + str(first) + " + i * " + str(second))
            print("x2 = " + str(first) + " - i * " + str(second))
