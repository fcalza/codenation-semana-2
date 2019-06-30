
def somar(valor1, valor2):
    return valor1 + valor2

def dividir(valor1, valor2):
    try:
        divisao_zero(valor2)
        return valor1/valor2
    except:
        print("divisor zerado")


def divisao_zero(divisor):
    if divisor == 0:
        raise ValueError("divisor nao pode ser zerado")
    return divisor