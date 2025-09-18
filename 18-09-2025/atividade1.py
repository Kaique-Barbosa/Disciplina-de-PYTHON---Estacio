COLUNAS = 70  # Constante usada para formatação do relatório e do menu

#----------------------------------------
# Dicionário que vai armazenar os produtos cadastrados
# A chave será o código do produto (int)
# O valor será uma lista com: [descrição, preço, quantidade, situação]
banco = {}

#----------------------------------------
# Função que gera o próximo código de produto automaticamente
def gerar_codigo():
    if banco:
        # Retorna o maior código existente + 1
        return max(banco.keys()) + 1
    return 1  # Se ainda não tem produto, começa do código 1

#----------------------------------------
# Função para incluir um novo produto no sistema
def incluir():
    try:
        codigo = int(input("Digite o código do produto (0 = auto): "))
        if codigo == 0:
            # Se o código for 0, gera automaticamente
            codigo = gerar_codigo()
        elif codigo in banco:
            print(">> Código já existe.")  # Evita duplicidade de códigos
            return
        descricao = input("Digite o nome do produto: ").strip().upper()  # Nome em maiúsculas
        preco = float(input("Digite o preço do produto: "))
        qtd = int(input("Digite a quantidade do produto: "))
        banco[codigo] = [descricao, preco, qtd, True]  # Situação "True" = Ativo
        print(">> Produto incluído com sucesso!")
    except:
        print(">> Dados inválidos.")  # Captura qualquer erro de digitação/conversão

#----------------------------------------
# Função para alterar o preço de um produto já cadastrado
def alterar():
    try:
        codigo = int(input("Digite o código do produto: "))
        if codigo not in banco:
            print(">> Produto não encontrado.")
            return
        novo_preco = float(input("Digite o novo preço do produto: "))
        banco[codigo][1] = novo_preco  # Atualiza o preço (índice 1 da lista)
        print(">> Preço atualizado com sucesso.")
    except:
        print(">> Erro ao alterar.")  # Caso haja erro na entrada

#----------------------------------------
# Função para excluir um produto do dicionário
def excluir():
    try:
        codigo = int(input("Digite o código do produto: "))
        if codigo not in banco:
            print(">> Produto não encontrado.")
            return
        print(f">> Produto: {banco[codigo][0]}")  # Mostra o nome antes de excluir
        conf = input("Confirmar exclusão (S/N)? ").strip().upper()
        if conf == "S":
            del banco[codigo]  # Remove do dicionário
            print(">> Produto excluído.")
        else:
            print(">> Exclusão cancelada.")
    except:
        print(">> Erro ao excluir.")

#----------------------------------------
# Função que imprime o relatório geral de todos os produtos
def rel_geral():
    if not banco:
        print(">> Nenhum produto cadastrado.")  # Se o dicionário estiver vazio
        return
    
    filtrar = input("Deseja realisar um filtro por preco? S/N \n")
    print(filtrar)
    if filtrar == "S" or "s":
        lista_produtos= tuple(banco.values())
        valor_limite = float(input("Digite o preço máximo"))
        lista_filtrada = tuple(filter(lambda p : p[1] <= valor_limite, lista_produtos))
        for p in lista_filtrada:
            print(f"Produto: {p[0]}")

    print("=" * COLUNAS)
    print("RELATÓRIO GERAL".center(COLUNAS))  # Título centralizado
    print("=" * COLUNAS)
    for cod, val in banco.items():
        situacao = "ATIVO" if val[3] else "INATIVO"  # Verifica se o produto está ativo
        print(f"Código: {cod}")
        print(f"Descrição: {val[0]}")
        print(f"Preço: R$ {val[1]:.2f}")
        print(f"Quantidade: {val[2]}")
        print(f"Situação: {situacao}")
        print("-" * COLUNAS)
    print("=" * COLUNAS)

#------------------------------------------------------------------------------
# Menu principal do programa, roda até o usuário digitar "S"
while True:
    print("=" * COLUNAS)
    print("01 - INCLUIR PRODUTO")
    print("02 - ALTERAR PRODUTO")
    print("03 - EXCLUIR PRODUTO")
    print("04 - RELATÓRIO GERAL")
    print("S  - SAIR")
    print("=" * COLUNAS)
    opcao = input("Digite a opção desejada: ").strip().upper()

    if opcao in ["01", "1"]:
        incluir()  # Chama a função de inclusão
    elif opcao in ["02", "2"]:
        alterar()  # Chama a função de alteração
    elif opcao in ["03", "3"]:
        excluir()  # Chama a função de exclusão
    elif opcao in ["04", "4"]:
        rel_geral()  # Gera o relatório geral
    elif opcao == "S":
        print("Encerrando o programa...")
        break  # Encerra o loop e sai do programa
    else:
        print(">> Opção inválida.")  # Caso o usuário digite algo incorreto