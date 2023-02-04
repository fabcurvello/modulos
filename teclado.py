def ler_str(mensagem):
    return input(mensagem)


def ler_int(mensagem):
    try:
        numero = int(ler_str(mensagem))
    except:
        print("ERRO: O valor inserido precisa ser um número inteiro")
        numero = ler_int(mensagem)
    finally:
        return numero


def ler_float(mensagem):
    try:
        numero = float(ler_str(mensagem))
    except:
        print("ERRO: O valor inserido precisa ser um número real (float)")
        numero = ler_float(mensagem)
    finally:
        return numero


nome = ler_str("Qual o seu nome? ")
print(nome)

idade = ler_int("Qual a sua idade? ")
print(idade)

salario = ler_float("Qual o seu salário? ")
print(salario)