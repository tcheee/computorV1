import math
from drawer import draw

def solver(a, b, c):
    print(a)
    print("\nReduced form: %.2fX^2 + %.2fX^1 + %.2f = 0\n" % (float(a), float(b), float(c)))
    if (a == 0 and b == 0):
        if (c == 0):
            print("Well done, you learn that 0 = 0!")
        else:
            print("Invalid equation")
    elif a == 0:
        print("Polynomial degree: 1")
        sol = (-c) / b
        print("x = " + str(sol))
        ans = input('Do you want a graph, yes or no? : ')
        if (ans == "yes"):
            draw(a, b, c)
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
            ans = input('Do you want a graph, yes or no? : ')
            if (ans == "yes"):
                draw(a, b, c)
        elif delta == 0:
            x1 = -b / 2 * a
            print("\nx = " + str(x1))
            ans = input('Do you want a graph, yes or no? : ')
            if (ans == "yes"):
                draw(a, b, c)
        else:
            print('\nComplex solutions:')
            first = -b / (2 * a)
            second = math.sqrt(-delta) / (2 * a)
            print("x1 = " + str(first) + " + i * " + str(second))
            print("x2 = " + str(first) + " - i * " + str(second))
