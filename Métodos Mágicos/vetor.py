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
        self.vetor = [1,2,3,4,5]
        self.pessoa = {"Nome": "caio"}
    
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
    def __eq__(self, n):
        return True if self.n1 == n else False
    def __neg__(self):
        return list(map(lambda x: -x if x > 0 else x, self.vetor))
    def __getitem__(self, key):
        if not key in self.pessoa.keys():
               self.pessoa[key] = None
        return self.pessoa[key]
    def __setitem__(self, key, value):
        self.pessoa[key] = value
    def __delitem__(self, key):
        del self.pessoa[key]
    def _call__(seçf, *args, **kwargs):
        print("Fui chamdado", args)

x = Vetor(2)
x(1,2)


print(x.pessoa)

