sinal = False

while not sinal:
    num1 = int(input("Digite um número: "))

    while not sinal:
        operador = input("Digite um operador: ")
        num2 = int(input("Digite outro número: "))

        match operador:
            case "+":
                result = num1 + num2
                print(result)

            case "-":
                result = num1 - num2
                print(result)

            case "*":
                result = num1 * num2
                print(result)

            case "^":
                result = num1 ** num2
                print(result)

            case "/":
                if (num2 == 0):
                    sinal = True
                    print("Operação Inválida")
                    break
                else:
                    result = num1 / num2
                    print(result)

            case _:
                sinal = True
                print("Operador inválido")
                break
        acao = input("Você deseja continuar/resetar/sair ?")
        lawer_acao = acao.lower()

        match lawer_acao:
            case "s" | "sair":
                sinal = True
                break

            case "c" | "continuar":
                num1 = result


            case "r" | "resetar":
                num1 = 0
                result = 0
                break