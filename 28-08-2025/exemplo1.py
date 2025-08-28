#1
def calcular_quadrado(b) -> float:

    '''
    esta funcao calcula o quadrado de um valor \n 
    args: b = base \n
    saida: O quadrado de 'B' \n
    '''
    return b**2

entrada = float(input("Digite o valor para elevar ao quadrado \n"))
print(calcular_quadrado(entrada))
