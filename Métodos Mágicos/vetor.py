# class Vetor:
#     ...
# print (dir(int))

# class Vetor:
#     ...
# print (dir(Vetor))

# print(type(Vetor))

class Vetor:
    def __init__(self, n1):
        self.n1 = 1
    
    def __add__(self, n):
        if not isinstance(n, int):
            n = float(n)
        return self.n1 + n
    
    def __sub__(self, n):
        if not isinstance(n, int):
            n = float(n)
        return self.n1 - n
    
    def __mul__(self, n):
        if not isinstance(n, int):
            n = int(n)
        return self.n1 * n
    
    def __pow__(self, n):
        if not isinstance(n, int):
            n = float(n)
        return self.n1 ** n
    
    def __mod__(self, n):
        if not isinstance(n, int):
            n = float(n)
        return self.n1 % n

x = Vetor(10)
print(x * 2)
