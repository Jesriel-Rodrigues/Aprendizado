import os
os.system('cls')
import random
num = random.randrange(11)
cont = 1
opc = None
tentativa = None
while tentativa != num:
    tentativa = int(input('Tente acertar o numero de 0 a 10!\n'))
    if tentativa == num:
        os.system('cls')
        print(f'Parabens você acertou com {cont} tentativas!\n')
        opc = str(input('Você deseja continuar? [S] ou [N]\n').upper()) 
        if opc == 'S':
            num = random.randint(0,10)
            cont = 0
        elif opc == 'N':
            os.system('cls')
            break    
    elif tentativa < num:
        os.system('cls')
        print(f'Sua resposta foi {tentativa} tente um numero maior!\n')
    elif tentativa > num:
        os.system('cls')
        print(f'Sua resposta foi {tentativa} tente um numero menor!\n')
    cont += 1
    