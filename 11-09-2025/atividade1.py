
colunas = 70
banco = {}

#--------------------------------------------------
def incluir():
    codigo = int(input("Informe o código do produto: "))
    descricao = input("Informe o descrição do produto: ").upper().strip()
    preco = float(input("Informe o preço: "))
    quantidade = int(input("Informe o quantidade: "))
    situacao = True
    
    banco[codigo]=[descricao, preco, quantidade, situacao]
    
    print(banco)
    
    
def alterar():
    codigo = int(input("Informe o código: "))
    if not banco.get(codigo):
        print("Produto não encontrado! ")
        return None
    novo_preco = float(input("Digite o novo preço do produto: "))
    banco[codigo] [1] = novo_preco
    print(banco)

def excluir():
    codigo = int(input("Informe o código: "))
    if not banco.get(codigo):
        print("Produto não encontrado! ")
        return None
    lista = banco.get(codigo)
    if lista:
        print(F"Produto: {lista[0]}")
        conf = input("Confirma a exclusão (S / N)?").upper()
        if conf == 'S':
            del banco[codigo]
    print(banco)
    
def relatorio():
    for chave, valor in banco.items():
        print(F"Código: {chave}, Descrição: {valor[0]}, Preço: {valor[1]}, Quantidade: {valor[2]} ", end="")
        
        print(F"Situacao: {"Ativo" if valor[3] else "inativo"}")
#--------------------------------------------------

while True:
    print("=" * colunas)
    print("1 - Incluir")
    print("2 - Alterar")
    print("3 - Excluir")
    print("4 - Relatório")
    print("." * colunas)
    print("S - sair")
    opcao = input("")
    
    match (opcao.upper().strip()):
        case '1':
            incluir()
        case '2':
            alterar()
        case '3':
            excluir()
        case '4':
            relatorio()
        case 'S':
            exit()
        case _:
            print("Opção inválida")