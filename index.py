def menu():
    print("[1]Converter para binário:")
    print("[2]Converter para octadecimal:")
    print("[3]Converter para hexadecimal:")
    print("[0] Sair do programa.")
    
menu()
opção = int(input("Selecione uma opção: "))

while opção != 0:
    if opção == 1:
        bin = int(input("Digite o valor que deseja ser tranformado em binário: "))
    elif opção == 2:
        octa = int(input)
    elif opção == 3:          
        dividendo = int(input("Digite um numero (Base decimal) para ser convertido em Binário: "))
        numero_digitado = dividendo
        quociente = 1
        lista = []
        while quociente >= 1:
            resto = dividendo % 2
            lista.insert(0,resto)
            quociente = dividendo // 2
            dividendo = quociente
            binario = ''.join([str(item) for item in lista])
            print("O número",numero_digitado,", quando convertido em binário, vale:",binario) 
    if opção == 2:
        print("test.v2")
    if opção == 3:
        print("test.v3")    
    if opção == 0:
        print("Obrigado por usar nosso programa.. Até logo!")
    else:
        print("Opção inválida.")

        
  
    print()
    menu()
    opção = int(input("Selecione uma opção:"))
