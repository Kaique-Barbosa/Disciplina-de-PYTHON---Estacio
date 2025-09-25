#Cadastro de Produtos:

#Loop para fazer o MENU
COLUNAS=70
#----------------------------------------
#Dicionário
banco={}

#Função gerar código
def gerar_codigo() -> int:
    if len(banco):
        # Gera uma lista com todas as chaves do dicionário (banco)
        #    Captura a última chave
        #        Transforma em um valor inteiro e soma um
        return int( list( banco.keys() )[-1]) + 1 
    else:
        return '1'

#Função Incluir 
def incluir():
  codigo = gerar_codigo
  descricao = input("DIGITE O NOME DO PRODUTO: ").upper().strip()
  preco = float(input("DIGITE O PREÇO DO PRODUTO: "))
  qtd = int(input("DIGITE A QUANTIDADE DO PRODUTO: "))
  situacao = True
  banco[codigo] = [descricao, preco, qtd, situacao]

#Função Alterar
def alterar():
  codigo = int(input("DIGITE O CÓDIGO DO PRODUTO: "))
  if not banco.get(codigo):
    print("PRODUTO NÃO ENCONTRADO")
    return None
  novo_preco = float(input("DIGITE O NOVO PREÇO DO PRODUTO: "))
  banco[codigo][1] = novo_preco

#Função Excluir
def excluir():
  codigo = int(input("DIGITE O CÓDIGO DO PRODUTO: "))
  lista = banco.get(codigo)
  if lista:
    print(f"PRODUTO: {lista[0]}")
    conf= input("CONFIRMA EXCLUSÃO(S/N)?").upper()
    if conf =="S":
      del banco[codigo]
      print("PRODUTO EXCLUIDO")
    else:
      print("EXCLUSÃO CANCELADA")
  else:
    print("PRODUTO NÃO ENCONTRADO")

#Função Relatório
def rel_geral():
    lista_produtos = tuple(banco.values())
    valor_limite = float(input("DIGITE O PREÇO MÁXIMO: "))
    lista_filtrada = tuple(filter(lambda p:p[1] <= valor_limite, lista_produtos))
    for p in lista_filtrada:
        print(f"PRODUTO:{p[0]}, PREÇO R${p[1]}")
"""
  for chave, valor in banco.items():
    print(f"\nCÓDIGO: {chave}")
    print(f"DESCRIÇÃO: {valor[0]}")
    print(f"PREÇO:R${valor[1]:.2f}")
    print(f"QUANTIDADE: {valor[2]}")
    situacao= "ATIVO" if valor[3] else "INATIVO"
    print(f"SITUAÇÃO: {situacao}")
    """
    

#------------------------------------------------------------------------------
while True:
  print("="*COLUNAS)
  print("1- INCLUIR")
  print("2- ALTERAR")
  print("3- EXCLUIR")
  print("4- RELATÓRIO GERAL")
  print("."*COLUNAS)
  print("S- SAIR")
  opcao = input("DIGITE A OPÇÃO DESEJADA: ")

  match opcao.upper().strip():
    case "1":
      incluir()
    case "2":
      alterar()
    case "3":
      excluir()
    case "4":
      rel_geral()
    case "S":
      exit()
    case _:
      print("OPÇÃO INVÁLIDA")