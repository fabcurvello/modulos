'''
Um módulo é um arquivo contendo definições e instruções Python
que podem ser importados para utilização de seus recursos.

Os módulos padrões do Python estão documentados em
https://docs.python.org/pt-br/3/py-modindex.html
'''

from random import randint
from math import pi, pow, sqrt as raiz

print(f"Sorteio de um número entre 1 e 10: {randint(1,10)}")
print(f"Valor de PI: {pi}")
print(f"5 elevado ao quadrado: {pow(5,2)}")
print(f"Raiz quadrada de 36: {raiz(36)}") #raiz é sqrt que foi apelidado no import

