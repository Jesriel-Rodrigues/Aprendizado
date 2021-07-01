import random
import time
import os


os.system('cls')        #limpar tela!
print('=~='*5)          #Painel do minigame
print('  JO-KEN-PO!!')
print('=~='*5)

while True:
    print(                   
        '[0] Para PEDRA!\n'
        '[1] Para PAPEL!\n'
        '[2] Para TESOURA!\n'
        '[3] Para Finalizar'
    )
    
    item = ['PEDRA', 'PAPEL', 'TESOURA', 'FINALIZAR']  

    escolha_pc = random.randrange(0, 3)  #Gerador de escolhas do Bot
    escolha_player = int(input('Escolha uma opção acima para jogar...\n')) #Armazena escolha do usuario
    os.system('cls')


    if escolha_player == 3:   #Condição de Continuação do looping
        break
    else:
        print('JO')
        time.sleep(1)
        print('KEN')
        time.sleep(1)
        print('PO\n')
        time.sleep(1)

        os.system('cls')

        print(f'Escolha do player: {item[escolha_player]}')
        print(f'Escolha do computador: {item[escolha_pc]}\n')

    if item[escolha_player] == item[escolha_pc]: #Processamento do vencedor!
        print('DEU EMPATE!!')
    elif item[escolha_player] == item[0]:
        if item[escolha_pc] == item[1]:
            print('O computador venceu!!')
        elif item[escolha_pc] == item[2]:
            print('Parabens você venceu!!')
    elif item[escolha_player] == item[1]:
        if item[escolha_pc] == item[2]:
            print('O computador venceu!!')
        elif item[escolha_pc] == item[0]:
            print('Parabens você venceu!!')
    elif item[escolha_player] == item[2]:
        if item[escolha_pc] == item[0]:
            print('O computador venceu!!')
    elif item[escolha_pc] == item[1]:
        print('Parabens você venceu!!')
    print('')
    