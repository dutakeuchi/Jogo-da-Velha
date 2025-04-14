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

def usuarioNumero(nEscolhidos):
    print ('Seu turno')
    valid = False
    ## validação para escolher uma posição disponível
    while valid == False:
        res = (input ('Escolha uma posição: '))
        try:
            res = int(res)
            if 0 < res <10:
                if res in lista:
                    valid = True
                    lista[res-1] = 'o'
                    nEscolhidos.append(res)
                    print( jogo(lista))
                    print('\n')
                else:
                    print ('Posição já ocupada. Selecione uma nova posição')
            else:
                print ('Valor inválido. Escolha um posição entre 1 e 9 dos disponíveis')
        except:
            print('Digite um valor válido')

    valid = False

    

def compuNumero(dificuldade, nEscolhidos, nComputador):
    valid = False
    ganhou =[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
            

    
##    ## checa se falta somente um número para o usuário ganhar
##    for i in range(len(ganhou)):
##        v = list(set(ganhou[i]) - set(nEscolhidos))
##        if len(v) == 1:
##             weight[v[0]-1] = int(dificuldade)
##        
##    while valid == False:
##        ## a função random.choices retorna uma lista, mesmo que esteja com um único elemento. Por isso o uso do [0]
##        ## para selecionar o primeiro valor da lista
##        res = random.choices(list(range(1,10)),weight, k=1)[0]
##        if res in lista:
##            valid = True
##            lista[res-1] = 'x'
##            lComp.append(res)
##        else:
##            continue
##    valid = False
##    print('Turno do computador. Número escolhido', res)
##    print(jogo(lista))
##    print('\n')


## alteração para testar a função de se faltar somente um número para o computador
## ganhar, o computador selecionar este número
    ## checa se falta somente um número para o usuário ganhar
    for i in range(len(ganhou)):
        c = list(set(ganhou[i]) - set(nComputador))
        v = list(set(ganhou[i]) - set(nEscolhidos))
        if len(c) == 1:
            res = c[0]
            if res in lista:
                lista[res-1] = 'x'
                nComputador.append(res)
                print('Turno do computador. Número escolhido', res)
                print(jogo(lista))
                print('\n')
                valid = True
                break
        if len(v) == 1:
            weight[v[0]-1] = int(dificuldade)*3
        
    while valid == False:
        ## a função random.choices retorna uma lista, mesmo que esteja com um único elemento. Por isso o uso do [0]
        ## para selecionar o primeiro valor da lista
        res = random.choices(list(range(1,10)),weight, k=1)[0]
        if res in lista:
            valid = True
            lista[res-1] = 'x'
            lComp.append(res)
            print('Turno do computador. Número escolhido', res)
            print(jogo(lista))
            print('\n')
        else:
            continue


    
        
    


## início do programa
import random

print ("Jogo da Velha")
print("Você é o jogador 'o' e o computador é o jogador 'x'")

## variável para saber se quer jogar novamente
jogar = 's'

##enquanto jogar for 's', o jogo será jogado
while jogar == 's':

    ## relação das posições possíveis de jogar
    lista = list(range(1,10))

    ## validador para não escolher um número já escolhido
    valid = False

    ## lista das posições do usuário
    lUser = []

    ## lista das posições do computador, gerado aleatoriamente
    lComp = []

    ## contador do número de rodadas jogadas
    i = 0

    ## peso para a escolha dos números disponíveis pelo computador
    weight = [1]*9

    print(jogo(lista))
    print ('\n')
    
    ## verifica se o input colocado atende aos parâmetros
    while valid == False:
        dific = input ('Selecione o nível de dificuldade de 1 a 10 ')
        try:
            dific = int(dific)
            if 0 < dific <= 10:
                valid = True
                continue
            else:
                print ('Digite um número entre 1 e 10')
        except:
            print ('Digite um valor válido')

    valid = False

    while i <= 9:
        usuarioNumero(lUser)
        i +=1

        if ganhador(lUser) == 1:
            print('Parabéns, você ganhou!')
            print('\n')
            break

        if i == 9:
            print('Não houve ganhadores. Jogo empatado!')
            print('\n')
            break
        else:
            compuNumero(dific,lUser, lComp)
            i +=1

            if ganhador(lComp) == 1:
                print('Você perdeu. O computador ganhou!')
                print('\n')
                break

    while valid == False:
        jogar = input ('Deseja jogar novamente? (S ou N) ').lower()
        try:
            if jogar == 's' or jogar == 'n':
                valid = True
            else:
                print ('Resposta inválida! Digite S ou N')
        except:
            continue
        
    print ('\n')

print('Fim de jogo. Obrigado por participar!')
    
            
        
        
