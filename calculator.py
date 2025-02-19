import math
import string
import os
os.system('cls')
dig = list(string.digits)
operations = ["+", "-", "*", "/", "=", "^", "|", "!"]
par = ["(", ")"]
neop = ["+", "-", "*", "/", "=", "^", "|", "("]
nsop = ["+", "-", "*", "/", "=", "^", "!", ")"]
nrop = ["+", "-", "*", "/", "="]
viable = dig + operations + par

def letterremove(a, b):
    nl = ""
    for i in a:
        if i in b:
            nl = nl + i
    nl = nl + "s"
    return (list(nl))

def breakdown(a, b):
    bdl = []
    pos = 0
    num = ""
    for i in a:
        if i != "s":
            if i not in b:
                bdl.append(i)
            else:
                num = num + (i)
                if a[a.index(i, pos) + 1] not in dig:
                    bdl.append(int(num))
                    num = ""
        pos += 1
    return (bdl)
    
def mathe(a, b, c, d, e):
    pos = 0
    end = 0
    start = 0
    nclose = 0
    if a.count("(") >= 1 and a.count(")") >= 1:
        op = []
        for i in a:
            if i == "(" or i == ")":
                op.append(i)
        while True:
            if ")" in a and "(" in a:
                if op.index(")") < op.index("("):
                    a.pop(a.index(")"))
                    op.pop(op.index(")"))
                else:
                    break
            else:
                break
        a.reverse()
        op.reverse()
        while True:
            if "(" in a and ")" in a:
                if op.index("(") < op.index(")"):
                    a.pop(a.index("("))
                    op.pop(op.index("("))
                else:
                    break
            else:
                break
        a.reverse()
        op.reverse()
        if a.count("(") != a.count(")"):
            if a.count("(") > a.count(")"):
                while a.count("(") > a.count(")"):
                    a.pop(a.index("("))
                    op.pop(op.index("("))
            else:
                while a.count(")") > a.count("("):
                    a.pop(a.index(")"))
                    op.pop(op.index(")"))
        if op[op.index("("):op.index("(") + 2].count("(") == 1:
            while True:
                if op[op.index("(") + 1:op.index(")") + 2].count(")") == 2:
                    a.pop(a.index(")"))
                    op.pop(op.index(")"))
                else:
                    if op[op.index("(", nclose):].count("(") > 1:
                        nclose = op.index("(", nclose) + 1
                    else:
                        break
        nclose = 0
        a.reverse()
        op.reverse()
        if op[op.index(")"):op.index(")") + 2].count(")") == 1:
            while True:
                if op[op.index(")") + 1:op.index("(") + 2].count("(") == 2:
                    a.pop(a.index("("))
                    op.pop(op.index("("))
                else:
                    if op[op.index(")", nclose):].count(")") > 1:
                        nclose = op.index(")", nclose) + 1
                    else:
                        break
        a.reverse()
        op.reverse()
        nclose = 0
        
    if a.count("(") == 0 or a.count(")") == 0:
        for i in a:
            if i == "(" or i == ")":
                a.pop(a.index(i))
                
    while True:
        if a[-1] in b:
            a.pop(-1)
        else:
            end = 1
        if a[0] in c:
            a.pop(0)
        else:
            start = 1
        if end == 1 and start == 1:
            break
    for i in a:
        if i in e:
            if a[a.index(i, pos) + 1] in d:
                a.pop(a.index(i, pos) + 1)
            else:
                pos += 1
    return (a)

def solve(a):
    if "(" in a:
        a.insert(0, "(")
        a.append(")")
        pare = a
        nopr = {}
        recure = 0
        def parent(p):
            inp = 0
            inpc = 0
            par = []
            fir = 0
            if "(" in p:
                for i in p:
                    if i == "(":
                        inp += 1
                        inpc = 1
                    if inpc == 1 and inp <= 1:
                        par.append(i)
                    elif inpc == 1 and inp > 1 and fir == 0:
                        par.append("h")
                        fir = 1
                    if i == ")":
                        inp -= 1
                    if inp == 0 and inpc == 1:
                        break
            else:
                par = 0
            return (par)
        def reparent(p):
            inp = 0
            inpc = 0
            par = []
            if "(" in p:
                for i in p:
                    if i == "(":
                        inp += 1
                        inpc = 1
                    if inpc == 1:
                        par.append(i)
                    if i == ")":
                        inp -= 1
                    if inp == 0 and inpc == 1:
                        break
            else:
                par = 0
            return (par)
        
        def concatenation(a):
            for i in range(a.count("~")):
                a[a.index("~") - 1] = (a[a.index("~") - 1]) * (a[a.index("~") + 1])
                a.pop(a.index("~") + 1)
                a.pop(a.index("~"))
            return(a)

    if ("+" in a) or ("-" in a):
        def addsub(a):
            while True:
                if "-" in a and "+" in a:
                    if a.index("+") < a.index("-"):
                        a[a.index("+") - 1] = (a[a.index("+") - 1]) + (a[a.index("+") + 1])
                        a.pop(a.index("+") + 1)
                        a.pop(a.index("+"))
                    elif a.index("-") < a.index("+"):
                        a[a.index("-") - 1] = (a[a.index("-") - 1]) - (a[a.index("-") + 1])
                        a.pop(a.index("-") + 1)
                        a.pop(a.index("-"))
                elif "-" in a and "+" not in a:
                    for i in range(a.count("-")):
                        a[a.index("-") - 1] = (a[a.index("-") - 1]) - (a[a.index("-") + 1])
                        a.pop(a.index("-") + 1)
                        a.pop(a.index("-"))
                    break
                elif "+" in a and "-" not in a:
                    for i in range(a.count("+")):
                        a[a.index("+") - 1] = (a[a.index("+") - 1]) + (a[a.index("+") + 1])
                        a.pop(a.index("+") + 1)
                        a.pop(a.index("+"))
                    break
            return (a)

    def divmul(a):
        while True:
            if "/" in a and "*" in a:
                if a.index("*") < a.index("/"):
                    a[a.index("*") - 1] = (a[a.index("*") - 1]) * (a[a.index("*") + 1])
                    a.pop(a.index("*") + 1)
                    a.pop(a.index("*"))
                elif a.index("/") < a.index("*"):
                    a[a.index("/") - 1] = (a[a.index("/") - 1]) / (a[a.index("/") + 1])
                    a.pop(a.index("/") + 1)
                    a.pop(a.index("/"))
            elif "/" in a and "*" not in a:
                for i in range(a.count("/")):
                    a[a.index("/") - 1] = (a[a.index("/") - 1]) / (a[a.index("/") + 1])
                    a.pop(a.index("/") + 1)
                    a.pop(a.index("/"))
                break
            elif "*" in a and "/" not in a:
                for i in range(a.count("*")):
                    a[a.index("*") - 1] = (a[a.index("*") - 1]) * (a[a.index("*") + 1])
                    a.pop(a.index("*") + 1)
                    a.pop(a.index("*"))
                break
        return (a)
        
    if ("^" in a) or ("!" in a) or ("|" in a):
        def expfacsqu(a):
            while True:
                if ("^" in a) and ("!" in a) and ("|" in a):
                    if (a.index("^") < a.index("!")) and (a.index("^") < a.index("|")):
                        a[a.index("^") - 1] = (a[a.index("^") - 1]) ** (a[a.index("^") + 1])
                        a.pop(a.index("^") + 1)
                        a.pop(a.index("^"))
                    elif (a.index("!") < a.index("^")) and (a.index("!") < a.index("|")):
                        a[a.index("!") - 1] = math.factorial(a[a.index("!") - 1])
                        a.pop(a.index("!"))
                    elif (a.index("|") < a.index("^")) and (a.index("|") < a.index("!")):
                        a[a.index("|") + 1] = math.sqrt(a[a.index("|") + 1])
                        a.pop(a.index("|"))
                elif ("^" in a) and ("!" in a) and ("|" not in a):
                    if a.index("^") < a.index("!"):
                        a[a.index("^") - 1] = (a[a.index("^") - 1]) ** (a[a.index("^") + 1])
                        a.pop(a.index("^") + 1)
                        a.pop(a.index("^"))
                    elif a.index("!") < a.index("^"):
                        a[a.index("!") - 1] = math.factorial(a[a.index("!") - 1])
                        a.pop(a.index("!"))
                elif ("^" in a) and ("|" in a) and ("!" not in a):
                    if a.index("^") < a.index("|"):
                        a[a.index("^") - 1] = (a[a.index("^") - 1]) ** (a[a.index("^") + 1])
                        a.pop(a.index("^") + 1)
                        a.pop(a.index("^"))
                    elif a.index("|") < a.index("^"):
                        a[a.index("|") + 1] = math.sqrt(a[a.index("|") + 1])
                        a.pop(a.index("|"))
                elif ("!" in a) and ("|" in a) and ("^" not in a):
                    if a.index("!") < a.index("|"):
                        a[a.index("!") - 1] = math.factorial(a[a.index("!") - 1])
                        a.pop(a.index("!"))
                    elif a.index("|") < a.index("!"):
                        a[a.index("|") + 1] = math.sqrt(a[a.index("|") + 1])
                        a.pop(a.index("|"))
                elif ("^" in a) and ("!" not in a) and ("|" not in a):
                    for i in range(a.count("^")):
                        a[a.index("^") - 1] = (a[a.index("^") - 1]) ** (a[a.index("^") + 1])
                        a.pop(a.index("^") + 1)
                        a.pop(a.index("^"))
                    break
                elif ("!" in a) and ("|" not in a) and ("^" not in a):
                    for i in range(a.count("!")):
                        a[a.index("!") - 1] = math.factorial(a[a.index("!") - 1])
                        a.pop(a.index("!"))
                    break
                elif ("|" in a) and ("^" not in a) and ("!" not in a):
                    for i in range(a.count("|")):
                        a[a.index("|") + 1] = math.sqrt(a[a.index("|") + 1])
                        a.pop(a.index("|"))
                    break
            return (a)
        
    if "(" in a:
        while True:
            if parent(pare) == 0:
                break
            else:
                recure += 1
                nopr[f"pare{recure}"] = parent(pare)
                pare = reparent(pare)
                pare.pop(0)
                pare.pop(-1)

        while recure != 1:
            if ("^" in nopr[f"pare{recure}"]) or ("!" in nopr[f"pare{recure}"]) or ("|" in nopr[f"pare{recure}"]):
                nopr[f"pare{recure}"] = expfacsqu(nopr[f"pare{recure}"])
            if "~" in nopr[f"pare{recure}"]:
                nopr[f"pare{recure}"] = concatenation(nopr[f"pare{recure}"])
            if ("/" in nopr[f"pare{recure}"]) or ("*" in nopr[f"pare{recure}"]):
                nopr[f"pare{recure}"] = divmul(nopr[f"pare{recure}"])
            if ("+" in nopr[f"pare{recure}"]) or ("-" in nopr[f"pare{recure}"]):
                nopr[f"pare{recure}"] = addsub(nopr[f"pare{recure}"])
            ans = nopr[f"pare{recure}"]
            ans.pop(0)
            ans.pop(-1)
            if str(nopr[f"pare{recure - 1}"][nopr[f"pare{recure - 1}"].index("h") - 1]).isdigit() == True:
                nopr[f"pare{recure - 1}"].insert(nopr[f"pare{recure - 1}"].index("h"), "~")
            if str(nopr[f"pare{recure - 1}"][nopr[f"pare{recure - 1}"].index("h") + 1]).isdigit() == True:
                nopr[f"pare{recure - 1}"].insert(nopr[f"pare{recure - 1}"].index("h") + 1, "~")
            nopr[f"pare{recure - 1}"].insert(nopr[f"pare{recure - 1}"].index("h"), ans[0])
            nopr[f"pare{recure - 1}"].pop(nopr[f"pare{recure - 1}"].index("h"))
            nopr.pop(f"pare{recure}")
            recure -= 1
        while True:
            if ("^" in nopr[f"pare{recure}"]) or ("!" in nopr[f"pare{recure}"]) or ("|" in nopr[f"pare{recure}"]):
                nopr[f"pare{recure}"] = expfacsqu(nopr[f"pare{recure}"])
            if "~" in nopr[f"pare{recure}"]:
                nopr[f"pare{recure}"] = concatenation(nopr[f"pare{recure}"])
            if ("/" in nopr[f"pare{recure}"]) or ("*" in nopr[f"pare{recure}"]):
                nopr[f"pare{recure}"] = divmul(nopr[f"pare{recure}"])
            if ("+" in nopr[f"pare{recure}"]) or ("-" in nopr[f"pare{recure}"]):
                nopr[f"pare{recure}"] = addsub(nopr[f"pare{recure}"])
            ans = nopr[f"pare{recure}"]
            ans.pop(0)
            ans.pop(-1)
            break
        a = ans
    else:
        while True:
            if ("^" in a) or ("!" in a) or ("|" in a):
                a = expfacsqu(a)
            if ("/" in a) or ("*" in a):
                a = divmul(a)
            if ("+" in a) or ("-" in a):
                a = addsub(a)
            break
    return (a)

print("""welcome to calculator
the symbols are this:

+ for plus (x+y)
- for minus (x-y)
| for negative numbers (|x)
* for multiplication (x*y)
/ for division (x/y)
^ for exponents (x^y)
! for factorial (x!)
| for sqaure root (|x)
() for parenthesis (x+(y+z))   concatenation (x(y+z))
if you add non connecting parenthesis or to many of one they will get removed and the answer might be different

order of operations is pecdmas
parenthesis   exponents   concatenation   division/multiplication   addition/substraction
    (x)       x^ |x  x!       x(y)           x/y        x*y            x+y       x-y

example expression: 8(1+6!)^2
if you add a = then it will say true or false
""")

while True:
    eq = str(input("")).replace(" ", "")
    eq = mathe(breakdown(letterremove(eq, viable), dig), neop, nsop, nrop, operations)
    print(*eq, "computer simplified form")
    print(*solve(eq), "answer")