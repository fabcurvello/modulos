from util import teclado

nome = teclado.ler_str("Qual o seu nome? ")
idade = teclado.ler_int("Qual a sua idade? ")
salario = teclado.ler_float("Qual o seu salário? ")

print(f"\nNome inserido: {nome}")
print(f"Idade inserida: {idade}")
print(f"Salário inserido: R$ {salario}")
