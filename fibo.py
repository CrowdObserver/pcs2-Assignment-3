def Fib(n, g = {"F0" : 0, "F1" : 1}):
    if "F" + str(n) not in g:
        f = Fib(n - 1) + Fib(n-2)
        g["F"+str(n)] = f
    else:
        return g["F"+str(n)]
    return f