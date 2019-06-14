import re
from solver import solver
import numpy as np
import matplotlib.pyplot as plt

##########################################################################################################################################################################################################################################

def handle_multi(elem):
    if (elem.find("^") != - 1):
        index = elem.index("^")
        for i in elem[index:]:
            if (i == "*"):
                print("ERROR: don't handle parenthesis ...")
                exit()
    return (elem)
    
def handle_div(elem):
    up = 0
    down = 0
    a = 0
    b = 0
    sign = 1
    boo = 0
    for i in elem:
        if (i == "-" and boo == 0):
            sign = -1
        elif (i.isdigit() and boo == 0):
            a = int(a) * 10 + int(i)
        elif (i == "^"):
            boo = 1
        elif (i.isdigit() and boo == 1):
            up = int(up) * 10 + int(i)
        elif (i == "/"):
            break
    index = elem.index("/") + 1
    if boo == 0 and elem[:index].find("X") != -1 :
        up = 1
    boo = 0
    sign = 1
    a = a * sign
    index = elem.index("/") + 1
    for i in elem[index:]:
        if (i == "-" and boo == 0):
            sign = -1
        elif (i.isdigit() and boo == 0):
            b = int(b) * 10 + int(i)
        elif (i == "^"):
            boo = 1
        elif (i.isdigit() and boo == 1):
            down = int(down) * 10 + int(i)
        else :
            continue
    b = b * sign
    if boo == 0 and elem[index:].find("X") != -1 :
        down = 1

    if (up - down > 2 or up - down < 0):
        print("Invalid Equation")
        exit()
    else :
        value = int(a) / int(b) 
        return (str(str(value) + "X^" + str(up - down)))



def x_edgecases_handler(array):
    result = list()
    for elem in array:
        if (elem.find("X") != -1 and (elem.find("*") != -1 or elem.find("/") != -1)):
            if (elem.find("*") != -1):
                nb = elem.count("X")
                if (nb >= 3):
                    print("Invalid Equation")
                    exit()
                elem = handle_multi(elem)
                result.append(elem)
            elif (elem.find("/") != -1):
                elem = handle_div(elem)
                result.append(elem)
        else:
            result.append(elem)
    return(result)


##########################################################################################################################################################################################################################################


def do_priority_operation(list):
    sign = 1
    a = 0
    b = 0
    boo = 0

    for i in list:
        if (i == "*"):
            boo = 1
        elif (i == "/"):
            boo = 2
    if (boo == 1):
        index = list.index("*") + 1
    elif (boo == 2):
       index = list.index("/") + 1
    for i in list:
        if (i == "-"):
            sign = -1
        elif (i.isdigit()):
            a = int(a) * 10 + int(i)
        elif (i == "*" or i == "/"):
            break
    a = sign * a
    sign = 1
    if (boo > 0):
        c = ""
        for place, i in enumerate(list[index:]):
            if (i == "-" and c == ""):
                sign = -1
            elif (i.isdigit() and c == ""):
                b = int(b) * 10 + int(i)
            elif (c == "*" and (i.isdigit() or (i == "-" or i == "+"))):
                boo = 3
                if (sign == 1):
                    ind = index + place - 1
                else:
                    ind = index + place - 2
                break
            elif (i == "*" or i == "/" or i == "X"):
                if (i == "*"):
                    c = i
                else :
                    if (b == 0):
                        b = 1
                    break
    b = sign * b
    if (boo == 1):
        return (a * b)
    elif (boo == 2):
        return (a / b)
    elif (boo == 3):
        rest = "".join(map(str, list[ind:]))
        st = str(str(str(a * b)) + rest)
        return (st)

#########################################################################################################################################################################################################################################


def ft_atoi(list):
    sign = 1
    a = 0

    if (len(list) == 2):
        if (list[0] == "-"):
            sign = -1
        if (list[0] == "-" or list[0] == "+"):
            if (list[1] == "X"):
                return (sign)
    for i in list:
      if (i == "-"):
          sign = -1
      elif (i.isdigit()):
          a = int(a) * 10 + int(i)
      if (i == "*" or i == "X"):
          break
    return (sign * a)


def ft_atof(list):
    sign = 1
    a = 0
    b = 0
    boo = 0

    if (len(list) == 2):
        if (list[0] == "-"):
            sign = -1
        if (list[0] == "-" or list[0] == "+"):
            if (list[1] == "X"):
                return (sign)
    for i in list:
      if (i == "-"):
          sign = -1
      elif (i == "."):
          boo = 1
      elif (i.isdigit() and boo == 0):
          a = int(a) * 10 + int(i)
      elif (i.isdigit() and boo == 1):
          b = int(b) * 10 + int(i)
      if (i == "*" or i == "X"):
          break

    if (not(str(a).isdigit())):
        print("ERROR")
        exit()
        return ("ERROR")
    elif (sign == -1):
        return (float(str("-" + str(a) + "." + str(b))))
    else:
        return (float(str(str(a) + "." + str(b))))


#########################################################################################################################################################################################################################################


def check_priority_operation(array):
    result = list()
    for elem in array:
        tmp = list(elem)
        if (elem.find("*") > 0):
            while (type(elem) is not(int)):
                elem = do_priority_operation(tmp)
                if (type(elem) is str):
                    tmp = list(elem)
            result.append(elem)
        elif (elem.find("/") > 0):
            elem = do_priority_operation(tmp)
            result.append(elem)
        elif (elem.find(".") > 0):
            elem = ft_atof(tmp)
            result.append(elem)
        else:
            check = elem.find("X")
            check_sign = elem.find("-")
            check_zero = elem.find("0")
            elem = ft_atoi(tmp)
            if (check != -1 and elem == 0 and check_sign != -1 and check_zero == -1):
                elem = -1
            elif (check != -1 and elem == 0 and check_zero == -1):
                elem = 1
            result.append(elem)
    res = 0
    for elem in result:
            res += float(elem)
    return (res)

#########################################################################################################################################################################################################################################


def parse_eq(equation, x0, x1, x2):
    tmp = list()
    ret = ""
    bef = ""
    for x in equation:
        if (x != "+" and x != "-" and x != "="):
            ret = ret + x
        elif (bef == "*" and (x == "+" or x == "-")):
            ret = ret + x
        elif (bef == "^" and x == "-"):
            print("ERROR: not handling negative value after '^'.")
            exit()
        else:
            tmp.append(ret)
            ret = x
        bef = x
    tmp.append(ret)

    print(tmp)
    tmp = x_edgecases_handler(tmp) ##check if X^2 * X or X^5/X^2
    print(tmp)

    for elem in tmp:
        if re.findall('X\^[3-9]', elem) or re.findall('X\^[1-9][0-9]', elem):
            print("Invalid equation")
            exit()
        if re.findall('X\^2', elem) or re.findall('X\*X', elem):
            x2.append(str(elem))
        elif re.findall('X\^0', elem):
            x0.append(str(elem))
        elif re.findall('X\^1', elem) or re.findall('X', elem):
            x1.append(str(elem))
        else:
            x0.append(str(elem))

## do priority operation and transform all the elem in int; #handle "/" and all its edge case
    print("X^2: ", x2)
    x0 = check_priority_operation(x0)
    x1 = check_priority_operation(x1)
    x2 = check_priority_operation(x2)
    return (x0, x1, x2)


##########################################################################################################################################################################################################################################
####         main function
##########################################################################################################################################################################################################################################

eq = input('Enter the equation you want to solve: ')
x0l = list()
x1l = list()
x2l = list()
x0r = list()
x1r = list()
x2r = list()

if (eq.find("=") == -1):
    print("Invalid equation")
    exit()
elif (eq.index("=")):
    index = eq.index("=")
    check0 = re.findall('[0-9]', eq[index:])
    if (len(check0) == 0):
        print("Invalid equation")
        exit()

eq = eq.replace(" ", "")
eq = eq.replace("*X^0", "*1")
eq = eq.replace("+X^0", "+1")
eq = eq.replace("+X^1", "+1X^1")
eq = eq.replace("+X^2", "+1X^2")
split = eq.split('=')
equal = re.findall("=", eq)
forbidden = re.findall(r"[^X' '=0-9.+-/^\*]", eq)

left = split[0]
right = split[1]
x0l, x1l, x2l = parse_eq(left, x0l, x1l, x2l)
x0r, x1r, x2r = parse_eq(right, x0r, x1r, x2r)

if (len(equal) == 1 and len(forbidden) == 0):
    a = x2l - x2r
    b = x1l - x1r
    c = x0l - x0r
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    solver(a, b, c)
else:
    print("Invalid equation")
