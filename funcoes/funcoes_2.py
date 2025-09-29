def minha_funcao(x , y):
    return x + y

resultado = minha_funcao(1,2)

print(resultado)

def minha_funcao2(x, y, z=15):
    if z > 1:
        return z*(x + y)
    else: 
        return z/(x + y)
    
resultado2 = minha_funcao2(5,6, z=0.7)
print(resultado2)
import re 

def clean_string(string):
    resul = []
    for valor in string:
        valor = valor.strip()
        valor = re.sub("[!#?]", "", valor)
        valor = valor.title()
        resul.append(valor)
    return resul

states = ["   Alabama ", "Georgia!", "Georgia", "georgia", "FlOrIda",           
"south   carolina##", "West virginia?"]

limpeza = clean_string(states)
print(limpeza)

def gerador(n=10):
    print(f"Gerando quadrados de 1 a {n ** 2}")
    for i in range(1, n + 1):
        yield i ** 2

gen = gerador()

for x in gen:
    print(x, end="")
    