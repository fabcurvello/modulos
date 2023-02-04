def ler_str(mensagem):
    resposta = input(mensagem)
    while (resposta == ""):
        print("ERRO: Por favor, digite a sua resposta!")
        resposta = input(mensagem)
    return resposta


def ler_int(mensagem):
    try:
        numero = int(ler_str(mensagem))
    except:
        print("ERRO: O valor inserido precisa ser um número inteiro!")
        numero = ler_int(mensagem)
    finally:
        return numero


def ler_float(mensagem):
    try:
        numero = float(ler_str(mensagem))
    except:
        print("ERRO: O valor inserido precisa ser um número real (float)!")
        numero = ler_float(mensagem)
    finally:
        return numero


if (__name__ == "__main__"):
    print("\n--- Utilizando o Arquivo Python teclado.py ---\n")