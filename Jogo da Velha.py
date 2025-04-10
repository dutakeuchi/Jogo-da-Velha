## função para chamar a representação de cada posição. Ao adicionar a lista, mostra
## as posições que podem ser escolhidas
def jogo(lista):
    return (' ' + str(lista[0]) + ' | ' + str(lista[1]) + ' | ' + str(lista[2]) + '\n'+
        '-----------' + '\n'+
        ' ' + str(lista[3]) + ' | ' + str(lista[4]) + ' | ' + str(lista[5]) + '\n'+
        '-----------' + '\n' +
        ' ' + str(lista[6]) + ' | ' + str(lista[7]) + ' | ' + str(lista[8]))

##função para verificar se houve ganhadores
def ganhador(lista):
    ### relação de todos os jogos ganhadores possíveis
    ganhou =[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for i in range(len(ganhou)):
        v = (set (lista) & set(ganhou[i]))
        if len(v)== 3:
             return 1
        else:
            continue 

import random

print ("Jogo da Velha")
print("Você é o jogador 'o' e o computador é o jogador 'x'")

## variável para saber se quer jogar novamente
jogar = 's'

##enquanto jogar for 's', o jogo será jogado
while jogar == 's':

    ## relação das posições possíveis de jogar
    lista = [1,2,3,4,5,6,7,8,9]

    ## validador para não escolher um número já escolhido
    valid = False

    ## lista das posições do usuário
    lUser = []

    ## lista das posições do computador, gerado aleatoriamente
    lComp = []

    ## contador do número de rodadas jogadas
    i = 0


    print(jogo(lista))
    print ('\n')

    while i <= 9:
        print ('Seu turno')
        ## validação para escolher uma posição disponível
        while valid == False:
            res = (input ('Escolha uma posição: '))
            try:
                res = int(res)
                if 0 < res <10:
                    if res in lista:
                        valid = True
                        lista[res-1] = 'o'
                        lUser.append(res)
                        i +=1
                    else:
                        print ('Posição já ocupada. Selecione uma nova posição')
                else:
                    print ('Valor inválido. Escolha um posição entre 1 e 9 dos disponíveis')
            except:
                print('Digite um valor válido')

        valid = False
        
        ## mostra a situação do jogo atual
        print( jogo(lista))
        print('\n')

        ##verifica se você ganhou o jogo
        if ganhador(lUser) == 1:
            print('Parabéns, você ganhou!')
            break

        ##ao atingir as nove jogadas possíveis, o while é interrompido e declarado empate
        if i == 9:
            print('Não houve ganhadores. Jogo empatado!')
            break
        else:
            ##enquanto não atinge as nove jogadas, o jogo continua
            ## validação da posição escolhida pelo computador
            while valid == False:
                res = random.randint(1,9)
                if res in lista:
                    valid = True
                    lista[res-1] = 'x'
                    lComp.append(res)
                    i += 1
                else:
                    continue
            valid = False
            print('Turno do computador')
            print(jogo(lista))
            print('\n')

            ## verifica se o computador ganhou o jogo
            if ganhador(lComp) == 1:
                print('Você perdeu. O computador ganhou!')
                break

    ## verifica se quer jogar novamente        
    while valid == False:
        jogar = input ('Deseja jogar novamente? (S ou N)').lower()
        try:
            if jogar == 's' or jogar == 'n':
                valid = True
            else:
                print ('Resposta inválida! Digite S ou N')
        except:
            continue
        
    print ('\n')

print('Fim de jogo. Obrigado por participar!')
