#pep8 - pip install flake8
#comando flake8 no terminal vai calidar alumas da regras no diretório
from datetime import datetime


#######################Módulos
#import absoluto
from models import somar
print(somar(2,4))

import models
print(models.somar(2,5))

from models import somar as somar_float
print(somar_float(3,9))

######################## Exceptions


class TratamentoDasExceptions(Exception):
    pass


class AlgumaCoisaError(TratamentoDasExceptions):
    status_code = 400
    msg = "Requisição inválida"

class ZeroDivisionError(TratamentoDasExceptions):
    msg = "valor informado é incorreto"


def teste_exception(numero):
    if numero < 0:
        raise AlgumaCoisaError("teeeeeeeeeee")
try:
    teste_exception(-1)
    print("agora vai")
except:
    print("deu ruim")

try:
    teste_exception(3)
    print("agora vai")
except:
    print("deu ruim")

try:
    teste_exception(-3)
    print("agora vai")
except TratamentoDasExceptions as ex:
    print("deu ruim")
    print(ex.status_code)
    print(ex.msg)


try:
    models.dividir(23,0)
except TratamentoDasExceptions as ex:
    print(ex.msg)

models.dividir(23,3)



########################3#decorators

def teste_decorator(func):
    def wrapper(*args, **kwargs):
        print("vou extender o comportamento")
        retorno = None
        try: 
            retorno = func(*args, **kwargs)
        except:
            print("deu algum erro inesperado")
        print("parei de extender")
        return retorno

    return wrapper

@teste_decorator
def minha_funcao(nome):
    print("estou na minha funcao nome", nome)

@teste_decorator
def minha_funcao_2(nome, nome2=None):
    print("estou na minha funcao nome", nome, nome2)
    return True

minha_funcao("asrasr")
minha_funcao_2("asrasr", "Asaaaa2")
teste = minha_funcao_2("asrasr", "Asaaaa2")
print(teste)

from time import sleep

def count_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        retorno = func(*args, **kwargs)
        final_time = datetime.now()
        print(final_time-initial_time)
        print("tempo d exec:", final_time-initial_time)
        return retorno
    return wrapper

@count_time
def slow_function(wait_time):
    sleep(wait_time)

slow_function(1)


################## list e dict comprehensions
numeros = [1, 2, 3, 4, 5]
numeros2 = []
limite = 10
counter = 1
while counter <= limite:
    numeros2.append(counter)
    counter +=1

for i in range(1, 11):
    numeros2.append(counter)
    counter +=1

numero3 = [i for i in range(1, 11)]
numero4 = [i+23 for i in range(1, 121)]
print(numeros2)
print(numero3)
print(numero4)

teste_dict = {str(i): 10 for i in range(10)}
print(type(teste_dict))
print(teste_dict)


########### lambda functions
#lambda = função anonima, sem nome definido

teste_lambda = lambda x, y: x*2 + y
print(teste_lambda(2, 20))

teste_lambda = lambda *args: args
print(teste_lambda(2, 20))


################# Map, reduce, filter
#>>>>>>>Map, para uma funcao e uma lista recebido, chama a funcao para cada elemento da lista

valores = [1, 2, 3]
resultados = map(lambda x: x**2, valores)
print(resultados)
resultados = list(map(lambda x: x**2, valores))
print(resultados)

#>>>>>>>reduce
#recebendo dois elementos, pode iteragir entre os dois primeiro e depois o resultado com o terceiro
from functools import reduce
valores = [10, 20, 30]
resultado = reduce(lambda x,y: x*y, valores)
#10 * 20 = 200 * 30 = 6000
print(resultado)

valores = [10, 20, 30, 50, 60]
resultado = reduce(lambda x,y: x+y, valores)
# 10 + 20 + 30 + 50 + 60 = 170
print(resultado)
print(sum(valores))

#>>>>>>>filter
valores = [10, 20, 30, 50, 60]
resultado = list(filter(lambda x: x if x > 30 else False, valores))
print(resultado)
resultado = list(filter(lambda x: True if x > 30 else False, valores))
print(resultado)

teste = reduce(lambda x,y : x+y , filter(lambda x: True if x > 30 else False, valores))
print(teste)


##################### generators

exemplo = range(10)
print(exemplo)
print(type(exemplo))

def primeiros_numeros(n):
    count = 0
    while count < n:
        yield count, 'retorno multiplo'
        #yield, 
        count+=1

numero = primeiros_numeros(10)
print(type(numero))
numero = next(primeiros_numeros(10))
print(type(numero))

generator = primeiros_numeros(10)
n1 = next(generator)
n2 = next(generator)
print(n1, n2)
for i, segundo_retorno in generator:
    print(i, segundo_retorno)


class Meurange:
    def __init__(self, n):
        self.n = n
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            num = self.count
            self.count+=1
            return num
        else:
            raise StopIteration()

somatorio = sum(Meurange(5))
print(somatorio)

############### ContextManager
#garantir que um acesso de recurso caro naõ fique aberto caso esquecer um arquivo.close()
arquivo = open("./input.txt", 'r')
print(arquivo.readlines())

print(arquivo.readlines())
arquivo.close()

with open("./input.txt", 'r') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

#print(arquivo.readlines())
print(arquivo.closed)


#################Algumas bibliotecas
import requests
import json
#https://youtu.be/Hy42xqWBFgE?t=8946









