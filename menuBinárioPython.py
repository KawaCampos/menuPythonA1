def somaBin(numB1, bin2):
  return bin(int(numB1, 2) + int(bin2, 2))[2:]
def subBin(numB1, bin2):
  return bin(int(numB1, 2) - int(bin2, 2))[2:]
def menu():
    print(" ---------------------------------")
    print("|\033[31m  \033[1m        MENU PRINCIPAL \033[0;0m        |")
    print("| [\033[32m1\033[0;0m] Decimal —> Binário & Octal  |")
    print("| [\033[32m2\033[0;0m] Binário —> Decimal & Octal  |")
    print("| [\033[32m3\033[0;0m] Cálculo Aritimético         |")
    print("| [0] \033[31mSair do programa. \033[0;0m          |")
    print(" ---------------------------------")
menu()
opcao = int(input("Selecione uma opção: "))
while opcao != 0:
    if opcao == 1:
        ob = int(input("Digite o valor que deseja ser tranformado em binário e octadecimal: "))
        num_bin = bin(ob)
        num_oct = oct(ob)
        print("Binário = ", num_bin)
        print("Octadecimal = ", num_oct)
    elif opcao == 2:   
        binario = int(input("Digite o número (binário) para ser convertido para a base decimal e octadecimal: "))
        n = len(str(binario))
        do = binario
        decimal = 0
        i = 0
        while binario != 0:
            resto = binario % 10
            decimal = decimal + (resto * (2**i))
            n = n - 1
            i = i + 1
            binario = binario // 10
        numoct = oct(do)
        print("Decimal =", decimal)
        print("Octadecimal =", numoct)
    elif opcao == 3:
      print("\033[32mCalcularei os números binários que você inserir\033[0;0m")
      print("")
      binario1 = str(input("Digite o primeiro número binário: "))
      binario2 = str(input("Digite o segundo número binário: "))
      if not all(digito in '01' for digito in binario1) or not all(digito in '01' for digito in binario2):
          print("\033[31m  \033[1mDigite números binários válidos.\033[0;0m")
      else:
          totalSoma = somaBin(binario1, binario2)
          totalSub = subBin(binario1, binario2)
          print("Soma:", totalSoma)
          print("Subtração:", totalSub)
    menu()
    opcao = int(input("Selecione uma opcao: "))
print("Obrigado por usar nosso programa.. Até logo!")