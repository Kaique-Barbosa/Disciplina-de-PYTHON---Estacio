COLUNAS=70
#----------------------------------------
#Dicionário
banco={}

#------------------------------------------------------------------------------
while True:
 print("="*COLUNAS)
 print("01- INCLUIR")
 print("02- ALTERAR")
 print("03- EXCLUIR")
 print("04- RELATÓRIO GERAL")
 print("."*COLUNAS)
 print("S- SAIR")
 opcao = input("DIGITE A OPÇÃO DESEJADA: ")
 match opcao.upper().strip():
   case "01":
     incluir()
   case "02":
     alterar()
   case "03":
     excluir()
   case "04":
     rel_geral()
   case "S":
     exit()
   case _:
     print("OPÇÃO INVÁLIDA")
 opcao = input("DIGITE A OPÇÃO DESEJADA: ")