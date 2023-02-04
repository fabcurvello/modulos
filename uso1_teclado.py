import util.teclado

nome = util.teclado.ler_str("Qual o seu nome? ")
idade = util.teclado.ler_int("Qual a sua idade? ")
salario = util.teclado.ler_float("Qual o seu salário? ")

print(f"\nNome inserido: {nome}")
print(f"Idade inserida: {idade}")
print(f"Salário inserido: R$ {salario}")