#2 crie uma função pura que retorna se o valor é par ou impar


def descobrir(valor) -> str:
    
    return  valor % 2 == 0 
    
    
numero_digitado = int(input("Digite o numero: "))

if descobrir(numero_digitado):
    print("numero é par")
    
else:
    print("numero é impar")
