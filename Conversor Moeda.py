def euro_credits():
    print("")
    saldo = int(input("Introduza aqui o seu saldo: "))
    moeda_rt = saldo * 2
    print("Você tem", moeda_rt, 'moedas RT.')


def menu():
    print("")
    print("Conversor de Moeda RT")
    print("")
    print("0 - Sair")
    print("1 - Converter para Moeda RT")
    opcao = int(input("Opção desejada: "))

    if opcao == 0:
        print("")
        print("Obrigado por usar o programa!")

    if opcao == 1:
        euro_credits()

    else:
        print("")


menu()
