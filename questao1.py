import os
import time

vetor_preco = []
vetor_exames = []
preco_bruto = 0
preco_total = 0
pagamento = ''
desconto = ''

while True:  # Menu para entrada de dados
    print('''
=======================MENU=========================
1 - Hemograma Completo                   R$50.00
2 - Raio-X                               R$150.00
3 - Ultrassonografia                     R$200.00
4 - Eletrocardiograma                    R$170.00
5 - Tomografia                           R$180.00
6 - Ressonância Magnética                R$230.00
7 - Exame de Glicose                     R$70.00

0 - Encerrar Programa
====================================================
    ''')
    try:
        opcao = int(input('Digite o código correspondente: '))  # Filtragem de opções
    except ValueError:
        print("Opção inválida! Digite um número.")
        time.sleep(2)
        os.system('cls || clear')
        continue

    match opcao:
        case 1:
            print('\nHemograma Completo solicitado')
            vetor_exames.append("1. Hemograma Completo")
            vetor_preco.append(50)
        case 2:
            print('\nRaio-X solicitado')
            vetor_exames.append("2. Raio-X")
            vetor_preco.append(150)
        case 3:
            print('\nUltrassonografia solicitada')
            vetor_exames.append("3. Ultrassonografia")
            vetor_preco.append(200)
        case 4:
            print('\nEletrocardiograma solicitado')
            vetor_exames.append("4. Eletrocardiograma")
            vetor_preco.append(170)
        case 5:
            print('\nTomografia solicitada')
            vetor_exames.append("5. Tomografia")
            vetor_preco.append(180)
        case 6:
            print('\nRessonância Magnética solicitada')
            vetor_exames.append("6. Ressonância Magnética")
            vetor_preco.append(230)
        case 7:
            print('\nExame de Glicose solicitado')
            vetor_exames.append("7. Exame de Glicose")
            vetor_preco.append(70)
        case 0:
            print('\nPrograma Encerrado com êxito')
            break
        case _:
            print('\nOpção inválida, tente novamente')
            time.sleep(2)
            os.system('cls || clear')
            continue

    print('\nVocê deseja pedir outro exame? (S/N)')
    outra_solicitacao = input().strip().lower()
    if outra_solicitacao == 's':
        os.system('cls || clear')
        print('Nova solicitação:\n')
        continue
    elif outra_solicitacao == 'n':
        os.system('cls || clear')
        break
    else:
        print("Opção inválida, tente novamente")
        time.sleep(2)
        os.system('cls || clear')

preco_bruto = sum(vetor_preco)
if preco_bruto > 0:
    print('''
    =================Forma de pagamento===============
    Selecione a forma de pagamento:
    1 - Convênio
    2 - Particular
    3 - Cartão de Crédito
    ================================================== 
    ''')
    forma_pagamento = input('Digite a forma de pagamento: ').strip()

    match forma_pagamento:
        case '1':
            print('Convênio selecionado')
            pagamento = 'Convênio'
            preco_total = preco_bruto * 0.85
            desconto = "Desconto de 15% no valor"
        case '2':
            print('Particular selecionado')
            pagamento = 'Particular'
            preco_total = preco_bruto
            desconto = "Sem desconto"
        case '3':
            print('Cartão de crédito selecionado')
            pagamento = 'Cartão de crédito'
            preco_total = preco_bruto * 1.08
            desconto = "Acréscimo de 8% no valor"
        case _:
            print("Forma de pagamento inválida! Considerando pagamento particular.")
            pagamento = 'Particular'
            preco_total = preco_bruto
            desconto = "Sem desconto"

    print('\nOs exames selecionados foram:')
    for exame in vetor_exames:
        print(exame)
    print(f'\nValor bruto: R${preco_bruto:.2f}')
    print(f'Forma de pagamento: {pagamento}')
    print(desconto)
    print(f'Valor final: R${preco_total:.2f}')
    