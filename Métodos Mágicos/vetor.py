# class Vetor:
#     ...
# print (dir(int))

# class Vetor:
#     ...
# print (dir(Vetor))

# print(type(Vetor))

class Vetor:
    def __init__(self):
        self.n1 = 1
    
    def __add__(self, n):
        return self.n1 + n

x = Vetor()
print( x + 3)