#4 criar a função que recebe uma "string" e retorna a string invertida

def inverter(texto) -> str:
    
    for i in range(len(texto ) -1, -1 , -1):
        print(texto[i], end='')
    
inverter("teste")
    
