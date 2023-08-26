
import random
import time

totalPlayer = []
dadosForas = []
vez = 0
dadosRodada = []
dadosPassos = []
tirosRodadas = 0

#adiciona os jogadores
def adicPlayer(nome, cerebros, tiros, vitimas):
    player = {"nome": nome, "cerebros": cerebros, "tiros": tiros, "vitimas": vitimas}
    totalPlayer.append(player)

#controla os turnos
def trocaTurno():
    global vez
    if vez == quantJogadores - 1:
        vez = 0
    else:
        vez +=1
    time.sleep(2)


#sortea os dados e verifica eles
def sortearDados():
    global vez, tirosRodadas, dado, dadosPassos
    time.sleep(2)
    dadosRodada = dadosPassos.copy()
    while len(dadosRodada) < 3:
        dado = (random.randrange(1, 14))
        while dado in dadosForas:
            dado = (random.randrange(1, 14))
        while dado in dadosRodada:
            dado = (random.randrange(1,14))
        dadosRodada.append(dado)
    dadosPassos = []
    while len(dadosRodada) !=0:
        i=0
        dado = dadosRodada[i]
        dadosRodada.remove(dado)
        i = i+1

        if dado <= 5:
            print("Foi sorteado o dado Verde""(",dado,")")
            dado_verde = "CPCTPC"
            resultadoDado = random.choice(dado_verde)

        elif 5 < dado < 9:
            print("Foi sorteado o dado amarelo""(",dado,")")
            dado_amarelo = "TPCTPC"
            resultadoDado = random.choice(dado_amarelo)

        else:
            print("Foi sorteado o dado vermelho", "(",dado,")")
            dado_vermelho = "TPTCPT"
            resultadoDado = random.choice(dado_vermelho)

        if resultadoDado == "C":
            print("O jogador comeu um cerebro " )
            totalPlayer[vez]["cerebros"] += 1
            dadosForas.append(dado)
            time.sleep(2)

        elif resultadoDado == "T":
            print("O jogador tomou um tiro")
            totalPlayer[vez]["tiros"] += 1
            tirosRodadas += 1
            dadosForas.append(dado)
            time.sleep(2)

        else:
            print("O jogador deixou a vitima escapar")
            totalPlayer[vez]["vitimas"] += 1
            dadosPassos.append(dado)
            time.sleep(2)


quantJogadores = int(input("Insira a quantidade de jogadores: "))
while quantJogadores <2:
        if quantJogadores <2:
            print("Você precisa de,no minimo,  2x jogadores")
            quantJogadores = int(input("Insira a quantidade de jogadores: "))
        else:
            print("Pode continuar")

for i in range(quantJogadores):
        nome = input("Insira o nome do jogador: ")
        adicPlayer(nome, cerebros=0, tiros=0, vitimas=0)
print("Vai começar o jogo Zombie Dices")
time.sleep(2)

while totalPlayer[vez]["cerebros"] < 12:
    print("A vez de " + totalPlayer[vez]["nome"] + " vai começar")
    time.sleep(2)
    sortearDados()
    time.sleep(2)
    print(totalPlayer[vez])

    if tirosRodadas ==3:
        print("Você tomou 3x tiros na rodada. Perdeu a vez")
        trocaTurno()
        tirosRodadas = 0

    elif input("Deseja passar a vez : (s/n) ") == 's':
        trocaTurno()

print("O jogador " + totalPlayer[vez]["nome"] + " ganhou o jogo")