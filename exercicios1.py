"""
FSÇS UM PROGRAMA QUE PEÇA AO USUÁRIO PARA DIGITAR UM NÚMERO INTEIRO, INFORME SE ESSE NÚMERO É PAR OU ÍMPAR. CASO O USUÁRIO NÃO DIGITE UM NÚMERO INTEIRO, INFORME QUE NÃO É UM NÚMERO INTEIRO
"""
num_int = input("Digite um número inteiro: ")

if num_int.isdigit():
  num_int = int(num_int)

  if num_int %2 == 0:
    print(f"{num_int} é par")

  else:
    print(f"{num_int} é ímpar")  

else:
  print("Você não digitou um número inteiro.")




"""
FAÇA UM PROGRAMA QUE PERGUNTE A HORA AO USUÁRIO E, BASEANDO-SE NO HORÁRIO DESCRITO, EXIBA A SALDAÇÃO ADEQUADA (BOM DIA, BOA TARDE BOA NOITE)
"""
hora = input("Digite o horário: ")

if hora.isdigit():
  hora = int(hora)
  if hora < 0 or hora > 23:
    print("Digite hora entre 0-23!")
  else:  
    if hora <= 11:
      print("Bom dia")
    elif hora == 12 or hora <= 17:
      print("Boa tarde")
    else:
      print("Boa noite") 
else:
  print("Digite um horário entre 0-23")     


"""
FAÇA UM PROGRAMA QUE PEÇA O PRIMEIRO NOME DO USUÁRIO. SE O NOME TIVER 4 LETRAS OU MENOS, IMPRIMA (SEU NOME É MUITO CURTO), SE TIVER 5 OU 6 LETRAS, (SEU NOME É NORMAL) E SE TIVER MAIS DE 6 LETRAS, IMPRIMA(SEU NOME É LONGO)
"""

nome = input("Digite seu primeiro nome: ")
qtd_nome = len(nome)

if qtd_nome <= 4:
  print("Seu nome é curto")
elif qtd_nome == 5 or qtd_nome == 6:
  print("Seu nome é normal")
else:
  print("Seu nome é longo")  
