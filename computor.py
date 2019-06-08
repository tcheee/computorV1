import re
from solver import solver

###########################################
def do_priority_operation(list):
    sign = 1
    a = 0
    b = 0
    boo = 0

    for i in list:
        if (i == "*"):
            boo = 1

    if (boo == 1):
        index = list.index("*") + 1
    for i in list:
        if (i == "-"):
            sign = -1
        elif (i.isdigit()):
            a = int(a) * 10 + int(i)
        if (i == "*"):
            break
    a = sign * a
    sign = 1
    if (boo == 1):
        for i in list[index:]:
            if (i == "-"):
                sign = -1
            elif (i.isdigit()):
                b = int(b) * 10 + int(i)
            if (i == "*" or i == "X"):
                break
    return (a * b)

############################################

def ft_atoi(list):
    sign = 1
    a = 0

    if (len(list) == 2):
        if (list[0] == "-"):
            sign = -1
        if (list[0] == "-" or list[0] == "+") :
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


###########################################
def check_priority_operation(array):
    result = list()
    for elem in array:
        tmp = list(elem)
        if (elem.find("*") > 0):
            elem = do_priority_operation(tmp)
            result.append(elem)
        else:
            elem = ft_atoi(tmp)
            result.append(elem)

    res = 0
    for elem in result:
        res += int(elem)
    return (res)

###########################################

#handle "/" and all its edge cases
#/!\
def parse_eq(equation, x0, x1, x2):
    tmp = list()
    ret = ""

    for x in equation:
        if (x != "+" and x != "-" and x != "="):  # not good in case of - after * or /
            ret = ret + x
        else:
            tmp.append(ret)
            ret = x
    tmp.append(ret)
    #print(tmp)

    for elem in tmp:
        if re.findall('X\^[3-9]', elem) or re.findall('X\^[1-9][0-9]', elem):
            print("Invalid equation")
            raise SystemExit
        if re.findall('X\^2', elem) or re.findall('X\*X', elem):
            x2.append(str(elem))
        elif re.findall('X\^0', elem):
            x0.append(str(elem))
        elif re.findall('X\^1', elem) or re.findall('X', elem):
            x1.append(str(elem))
        else:
            x0.append(str(elem))

## do priority operation and transform all the elem in int;
    x0 = check_priority_operation(x0)
    x1 = check_priority_operation(x1)
    x2 = check_priority_operation(x2)
    #print("a: ", x2)
    #print("b: ", x1)
    #print("c: ", x0)
    #print("------------------")
    return (x0, x1, x2)


############################################
#               main function

eq = input('Enter the equation you want to solve: ')
x0l = list()
x1l = list()
x2l = list()
x0r = list()
x1r = list()
x2r = list()

eq = eq.replace(" ", "")
split = eq.split('=')
equal = re.findall("=", eq)
forbidden = re.findall(r"[^X' '=0-9.+-/^\*]", eq)

left = split[0]
right = split[1]
x0l, x1l, x2l = parse_eq(left, x0l, x1l, x2l)
x0r, x1r, x2r = parse_eq(right, x0r, x1r, x2r)

if len(equal) == 1 and len(forbidden) == 0:
    a = x2l - x2r
    b = x1l - x1r
    c = x0l - x0r
    print("a: ", a)
    print("b: ", b)
    print("c: ", c)
    solver(a, b, c)
else:
    print("Invalid equation")
