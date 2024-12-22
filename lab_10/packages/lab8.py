def calc(op, i=0):
    result = i
    def operation(i):
        nonlocal result
        if op == "+":
            result += i
        elif op == "-":
            result -= i
        elif op == "*":
            result *= i
        elif op == "/":
            result /= i
        print(result)
        return result
    return operation


def lab10(zn, i, nxt, kol):
    test=calc(zn, i)
    for _ in range (kol):
        test(nxt)
