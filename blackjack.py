import random
import time

class Baralho:
    def __init__(self):
        self.cartas = [
            'A',2, 3, 4, 5, 6, 7, 8, 9,'J','Q','K'
        ]

        self.baralho_completo = {
            'Ouros':'',
            'Espada':'',
            'Copas':'',
            'Paus':''
        }
        self.n0 = []
        self.n1 = []
        self.n2 = []
        self.n3 = []
        self.contar_rodada: int
        self.pontuacao = 0
        self.contar_rodada = 0
        self.contar_embaralhar = 0
        self.pontos_dealer = []
        self.pontos_jogador = []
        self.pontuacao_partida = {}

    ##Embaralha as cartas
    def embaralhar_cartas(self):
        random.shuffle(self.cartas)
        n0 = random.sample(self.cartas, len(self.cartas))
        n1 = random.sample(n0, len(n0))
        n2 = random.sample(n1, len(n1))
        n3 = random.sample(n2, len(n2))
        self.baralho_completo['Ouros'] = n0
        self.baralho_completo['Espada'] = n1
        self.baralho_completo['Copas'] = n2
        self.baralho_completo['Paus'] = n3

        return(self.baralho_completo)

    #Distribuir cartas
    def distribuir_cartas(self, *jogadores):
        if self.contar_embaralhar == 0:
            self.baralho = self.embaralhar_cartas()
            self.contar_embaralhar = 1
            lista_random = [0, 1, 2, 3]
            n = random.choice(lista_random)
            self.naipe_dealer = list(self.baralho)[n]
            self.carta_dealer = self.baralho[self.naipe_dealer][0]               
            self.naipe_jogador = list(self.baralho)[n]
            self.carta_jogador = self.baralho[self.naipe_jogador][0]

        for jogador  in jogadores:
            if int(self.contar_rodada) > 1 and jogador == 'Dealer':
                if self.contar_embaralhar == 0:
                    lista_random = [0, 1, 2, 3]
                    n = random.choice(lista_random)
                    self.naipe_dealer = list(self.baralho)[n]
                    self.carta_dealer = self.baralho[self.naipe_dealer][0]   
                    self.carta_dealer = self.baralho[self.naipe_dealer][1]
                    del self.baralho[self.naipe_dealer][0]
                    del self.baralho[self.naipe_dealer][1]
                    print ("Carta oculta para o Dealer")
                else:
                    lista_random = [0, 1, 2, 3]
                    n = random.choice(lista_random)
                    self.naipe_dealer = list(self.baralho)[n]
                    self.carta_dealer = self.baralho[self.naipe_dealer][0]
                    self.contar_embaralhar = 1
                    self.carta_dealer = self.baralho[self.naipe_dealer][1]
                    del self.baralho[self.naipe_dealer][0]
                    del self.baralho[self.naipe_dealer][1]
                    print ("Carta oculta para o Dealer")

            else:
                if self.contar_embaralhar == 0:
                    lista_random = [0, 1, 2, 3]
                    n = random.choice(lista_random)
                    self.naipe_jogador = list(self.baralho)[n]
                    self.carta_jogador = self.baralho[self.naipe_jogador][0]
                    self.contar_embaralhar = 1
                    del self.baralho[self.naipe_jogador][0]
                    if jogador == 'Dealer' and int(self.contar_rodada) > 1:
                        print ("Carta oculta para o Dealer")
                    elif jogadores == 'Dealer':                      
                        print("Carta "+str(self.carta_dealer)+" de "+str(self.naipe_dealer)+" para o "+str(jogador))
                    else:
                        print("Carta "+str(self.carta_jogador)+" de "+str(self.naipe_jogador)+" para o "+str(jogador))                       
                else:
                    lista_random = [0, 1, 2, 3]
                    n = random.choice(lista_random)
                    self.naipe_jogador = list(self.baralho)[n]
                    self.carta_jogador = self.baralho[self.naipe_jogador][0]
                    self.contar_embaralhar = 1
                    del self.baralho[self.naipe_jogador][0]
                    if jogador == 'Dealer' and int(self.contar_rodada) > 1:
                        print ("Carta oculta para o Dealer")
                    elif jogador == 'Dealer':                      
                        print("Carta "+str(self.carta_dealer)+" de "+str(self.naipe_dealer)+" para o "+str(jogador))
                    else:
                        print("Carta "+str(self.carta_jogador)+" de "+str(self.naipe_jogador)+" para o "+str(jogador))
        self.contar_rodada = self.contar_rodada + 1
        
        print("Rodada atual: "+str(self.contar_rodada))



    #Contabilizar os pontos
    def contar_pontos(self, *jogadores):
        for jogador in jogadores:
            if jogador == 'Dealer':
                if self.carta_dealer == 'A':
                    self.pontos_dealer.append(1)

                elif self.carta_dealer == 'K' or self.carta_dealer == 'Q' or self.carta_dealer == 'J':
                    self.pontos_dealer.append(10)

                else:
                    self.pontos_dealer.append(self.carta_dealer)

            else:
                if self.carta_jogador == 'A':
                   self.pontos_jogador.append(1)

                elif self.carta_jogador == 'K' or self.carta_jogador == 'Q' or self.carta_jogador == 'J':
                    self.pontos_jogador.append(10)

                else:
                    self.pontos_jogador.append(self.carta_jogador)   
        print("Dealer com a carta : "+str(self.pontos_dealer[0])+" "+str(self.naipe_dealer)+" virada")
        print("Pontos jogador: "+str(sum(self.pontos_jogador)))
        return self.pontos_dealer, self.pontos_jogador      


    #Calcular resultado
    def calcular_resultado(self, pontos, jogador):
        if sum(pontos) > 21:
            print((str(jogador)+" estorou a mão com ")+str(pontos))
            msg = 1
        elif sum(pontos) == 21:
            print("Blackjack para "+str(jogador))
            msg = 2
        else:
            return sum(pontos)
        return msg

Bara = Baralho()
Jogador = 'Jogador'
Dealer = 'Dealer'
start_game = 0
menu_once = 0
continua_game = 0
while start_game == 0:
    if menu_once == 0:
        input_menu = input(" 1 - Começar: \n 2 - Sair: \n")
        menu_once = 1
    if input_menu == str(2):
        start_game = 1
    else:
        print("Embaralhando as cartas \n")
        time.sleep(1)
        print("Dealer entregando as cartas \n")
        Bara.distribuir_cartas(Dealer, Jogador)
        Bara.distribuir_cartas(Dealer)
        pontos = Bara.contar_pontos(Dealer, Jogador)
        resultado_jogador = Bara.calcular_resultado(pontos[1], Jogador)
        resultado_dealer = Bara.calcular_resultado(pontos[0], Dealer)
        time.sleep(1)
        while continua_game == 0:
            escolha = input(" 1 - Sacar: \n 2 - Parar: \n")
            if escolha == str(2):
                continua_game = 1
                start_game = 1




                
