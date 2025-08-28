#3 cria a função pura maior(a,b) que retorna o maior valor

def maior(a, b) -> str:
    return (f"{a} é o maior valor" if a > b else f"{b} é o maior valor")

print(maior(1, 4))
