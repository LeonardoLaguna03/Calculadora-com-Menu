import funções
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
while True:
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Sair')
    escolha = int(input('Qual é sua escolha? '))
    if escolha == 1:
        print(f'{n1} + {n2} = {funções.soma(n1, n2)}')
    elif escolha == 2:
        print(f'{n1} - {n2} = {funções.subtrair(n1, n2)}')
    elif escolha == 3:
        print('Saindo...')
        break

#Próximas evoluções: melhorar interações com o usuário, multiplicação, divisão, potência, raiz quadrada e histórico dos calcúlos.