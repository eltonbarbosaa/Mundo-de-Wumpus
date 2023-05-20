
import random
matriz = []
sentirPoco = []
sentirOuro = []
sentirWumpus = []
memoria = []
coluna = None
linha = None

class gerarMatriz(object):

    linha = None
    coluna = None
    
    def gerar(self, y, x):
    
        global coluna, linha
        linha = y
        coluna = x
        self.linha = linha
        self.coluna = coluna

        for i in range(linha):
            LINHA = []
            for j in range(coluna):
                LINHA.append(' ')
            matriz.append(LINHA)

        for i in range(linha):
            LINHA = []
            for j in range(coluna):
                LINHA.append(' ')
            sentirPoco.append(LINHA)

        for i in range(linha):
            LINHA = []
            for j in range(coluna):
                LINHA.append(' ')
            sentirOuro.append(LINHA)

        for i in range(linha):
            LINHA = []
            for j in range(coluna):
                LINHA.append(' ')
            sentirWumpus.append(LINHA)

        for i in range(linha):
            LINHA = []
            for j in range(coluna):
                LINHA.append(' ')
            memoria.append(LINHA)

    def plot(self):
        # cria o mapa principal
        print('\n-------------------------\n\t Mapa\n-------------------------')
        for i in range(self.coluna):
            for j in range(self.linha):
                print(matriz[j])
            break

    def pocos(self):
        # defini a localização dos poços

        for i in range(self.coluna-1):
            while True:
                temp1 = random.randint(0, self.linha-1)
                temp2 = random.randint(0, self.coluna-1)
                if temp1 != 0 and temp2 != 0:
                    if matriz[temp1][temp2] != '2': # 2 - Poco
                        matriz[temp1][temp2] = '2'
                        break

    def ouro(self):
        # defini a localização do ouro
        while True:
            temp1 = random.randint(0, self.linha - 1)
            temp2 = random.randint(0, self.coluna - 1)
            if temp1 != 0 and temp2 != 0:
                if matriz[temp1][temp2] != '2':
                    matriz[temp1][temp2] = '10' # 10 - Ouro
                    break

    def wumpus(self):
        # defini a localização dos wumpus
        while True:
            temp1 = random.randint(0, self.linha - 1)
            temp2 = random.randint(0, self.coluna - 1)
            if temp1 != 0 and temp2 != 0:
                if matriz[temp1][temp2] != '2' and matriz[temp1][temp2] != '10':
                    matriz[temp1][temp2] = '5' # 5 - Wumpus
                    break    
                
    # definindo os mapas de sensações
    def plotPoco(self):
        print('\n-------------------------\n\t Mapa\n-------------------------')
        for i in range(self.coluna):
            for j in range(self.linha):
                print(sentirPoco[j])
            break
        print('-------------------------\nSentir Poco')

    def plotOuro(self):
        print('\n-------------------------\n\t Mapa\n-------------------------')
        for i in range(self.coluna):
            for j in range(self.linha):
                print(sentirOuro[j])
            break
        print('-------------------------\nSentir Ouro')

    def plotWumpus(self):
        print('\n-------------------------\n\t Mapa\n-------------------------')
        for i in range(self.coluna):
            for j in range(self.linha):
                print(sentirWumpus[j])
            break
        print('-------------------------\nSentir Wumpus')

    def plotMemoria(self):
        print('\n-------------------------\n\t Mapa\n-------------------------')
        for i in range(self.coluna):
            for j in range(self.linha):
                print(memoria[j])
            break
        print('-------------------------\nEstouro de Memoria :(')

    def sense_Poco(self):
        for i in range(self.coluna):
            for j in range(self.linha):
                if matriz[i][j] == '2':
                    if i - 1 > self.linha-1:
                        pass
                    else:
                        sentirPoco[i - 1][j] = 'b'
                    if i + 1 > self.linha-1:
                        pass
                    else:
                        sentirPoco[i + 1][j] = 'b'
                    if j - 1 > self.linha - 1:
                        pass
                    else:
                        sentirPoco[i][j - 1] = 'b'
                    if j + 1 > self.linha - 1:
                        pass
                    else:
                        sentirPoco[i][j + 1] = 'b'

    def sense_Ouro(self):
        for i in range(self.coluna):
            for j in range(self.linha):
                if matriz[i][j] == '10':
                    sentirOuro[i][j] = 'B'


    def sense_Wumpus(self):
        for i in range(self.coluna):
            for j in range(self.linha):
                sentirWumpus[i][j] = ' '
        for i in range(self.coluna):
            for j in range(self.linha):
                if matriz[i][j] == '5':
                    if i - 1 > self.linha-1:
                        pass
                    else:
                        sentirWumpus[i - 1][j] = 'F'
                    if i + 1 > self.linha-1:
                        pass
                    else:
                        sentirWumpus[i + 1][j] = 'F'
                    if j - 1 > self.linha - 1:
                        pass
                    else:
                        sentirWumpus[i][j - 1] = 'F'
                    if j + 1 > self.linha - 1:
                        pass
                    else:
                        sentirWumpus[i][j + 1] = 'F'
    
    # inicializando o posicionamento do agente
    def setAgente(self):
        matriz[0][0] = 'A'

class agente_reativo(object):
    flecha = True
    ouro = False
    wumpus = True
    agente = 'A'
    estado_anterior_linha = None
    estado_anterior_coluna = None

    def mover(self):
        agente_reativo.ganhar(agente_reativo)
        variavel = 0

        # definindo os cantos
        if matriz[0][0] == self.agente or matriz[linha-1][0] == self.agente or matriz[0][coluna-1] == self.agente or matriz[linha-1][coluna-1] == self.agente:
            if matriz[0][0] == self.agente:
                print('CANTO1')
                agente_reativo.moverSe(agente_reativo, 0, 0, 'CANTO1')
            if matriz[linha-1][0] == self.agente:
                print('CANTO2')
                agente_reativo.moverSe(agente_reativo, linha-1, 0, 'CANTO2')
            if matriz[0][coluna-1] == self.agente:
                print('CANTO3')
                agente_reativo.moverSe(agente_reativo, 0, coluna-1, 'CANTO3')
            if matriz[linha-1][coluna-1] == self.agente:
                print('CANTO4')
                agente_reativo.moverSe(agente_reativo, linha-1, coluna - 1, 'CANTO4')
        else:
            variavel = 1

        

    def moverSe(self, linha, coluna, info):
        if info == 'CANTO1':
            temp = random.randint(0, 1)
            if temp == 1:
                if agente_reativo.seguranca(agente_reativo, linha, coluna):
                    return True
                else:
                    agente_reativo.consequencia(agente_reativo, linha + 1, coluna)
                    matriz[linha + 1][coluna] = self.agente
            else:
                if agente_reativo.seguranca(agente_reativo, linha, coluna):
                    return True
                else:
                    agente_reativo.consequencia(agente_reativo, linha, coluna + 1)
                    matriz[linha][coluna + 1] = self.agente
        if info == 'CANTO2':
            temp = random.randint(0, 1)
            if temp == 1:
                agente_reativo.seguranca(agente_reativo, linha, coluna)
                agente_reativo.consequencia(agente_reativo, linha-1, coluna)
                matriz[linha - 1][coluna] = self.agente
            else:
                agente_reativo.seguranca(agente_reativo, linha, coluna)
                agente_reativo.consequencia(agente_reativo, linha, coluna+1)
                matriz[linha][coluna + 1] = self.agente
        if info == 'CANTO3':
            temp = random.randint(0, 1)
            if temp == 1:
                agente_reativo.seguranca(agente_reativo, linha, coluna)
                agente_reativo.consequencia(agente_reativo, linha+1, coluna)
                matriz[linha + 1][coluna] = self.agente
            else:
                agente_reativo.seguranca(agente_reativo, linha, coluna)
                agente_reativo.consequencia(agente_reativo, linha, coluna-1)
                matriz[linha][coluna - 1] = self.agente
        if info == 'CANTO4':
            temp = random.randint(0, 1)
            if temp == 1:
                agente_reativo.seguranca(agente_reativo, linha, coluna)
                agente_reativo.consequencia(agente_reativo, linha-1, coluna)
                matriz[linha - 1][coluna] = self.agente
            else:
                agente_reativo.seguranca(agente_reativo, linha, coluna)
                agente_reativo.consequencia(agente_reativo, linha, coluna-1)
                matriz[linha][coluna - 1] = self.agente
        if info == 'SUPERIOR':
            temp = random.randint(0, 2)
            if temp == 0:
                if agente_reativo.seguranca(agente_reativo, linha, coluna):
                    return True
                else:
                    agente_reativo.consequencia(agente_reativo, linha, coluna-1)
                    matriz[linha][coluna-1] = self.agente
            if temp == 1:
                if agente_reativo.seguranca(agente_reativo, linha, coluna):
                    return True
                else:
                    agente_reativo.consequencia(agente_reativo, linha, coluna+1)
                    matriz[linha][coluna+1] = self.agente
            if temp == 2:
                if agente_reativo.seguranca(agente_reativo, linha, coluna):
                    return True
                else:
                    agente_reativo.consequencia(agente_reativo, linha+1, coluna)
                    matriz[linha+1][coluna] = self.agente
        if info == 'INFERIOR':
            temp = random.randint(0, 2)
            if temp == 0:
                if agente_reativo.seguranca(agente_reativo, linha, coluna):
                    return True
                else:
                    agente_reativo.consequencia(agente_reativo, linha-1, coluna)
                    matriz[linha][coluna-1] = self.agente
            if temp == 1:
                if agente_reativo.seguranca(agente_reativo, linha, coluna):
                    return True
                else:
                    agente_reativo.consequencia(agente_reativo, linha, coluna+1)
                    matriz[linha][coluna+1] = self.agente
            if temp == 2:
                if agente_reativo.seguranca(agente_reativo, linha, coluna):
                    return True
                else:
                    agente_reativo.consequencia(agente_reativo, linha-1, coluna)
                    matriz[linha-1][coluna] = self.agente
        if info == 'ESQUERDA':
            temp = random.randint(0, 2)
            if temp == 0:
                if agente_reativo.seguranca(agente_reativo, linha, coluna):
                    return True
                else:
                    agente_reativo.consequencia(agente_reativo, linha, coluna+1)
                    matriz[linha][coluna+1] = self.agente
            if temp == 1:
                if agente_reativo.seguranca(agente_reativo, linha, coluna):
                    return True
                else:
                    agente_reativo.consequencia(agente_reativo, linha+1, coluna)
                    matriz[linha+1][coluna] = self.agente
            if temp == 2:
                if agente_reativo.seguranca(agente_reativo, linha, coluna):
                    return True
                else:
                    agente_reativo.consequencia(agente_reativo, linha-1, coluna)
                    matriz[linha-1][coluna] = self.agente
        if info == 'DIREITA':
            temp = random.randint(0, 2)
            if temp == 0:
                if agente_reativo.seguranca(agente_reativo, linha, coluna):
                    return True
                else:
                    agente_reativo.consequencia(agente_reativo, linha, coluna-1)
                    matriz[linha][coluna-1] = self.agente
            if temp == 1:
                if agente_reativo.seguranca(agente_reativo, linha, coluna):
                    return True
                else:
                    agente_reativo.consequencia(agente_reativo, linha+1, coluna)
                    matriz[linha+1][coluna] = self.agente
            if temp == 2:
                if agente_reativo.seguranca(agente_reativo, linha, coluna):
                    return True
                else:
                    agente_reativo.consequencia(agente_reativo, linha-1, coluna)
                    matriz[linha-1][coluna] = self.agente
        if info == 'CENTRO':
            temp = random.randint(0, 3)
            if temp == 0:
                if agente_reativo.seguranca(agente_reativo, linha, coluna):
                    return True
                else:
                    agente_reativo.consequencia(agente_reativo, linha, coluna-1)
                    matriz[linha][coluna - 1] = self.agente
            if temp == 1:
                if agente_reativo.seguranca(agente_reativo, linha, coluna):
                    return True
                else:
                    agente_reativo.consequencia(agente_reativo, linha+1, coluna)
                    matriz[linha + 1][coluna] = self.agente
            if temp == 2:
                if agente_reativo.seguranca(agente_reativo, linha, coluna):
                    return True
                else:
                    agente_reativo.consequencia(agente_reativo, linha-1, coluna)
                    matriz[linha - 1][coluna] = self.agente
            if temp == 3:
                if agente_reativo.seguranca(agente_reativo, linha, coluna):
                    return True
                else:
                    agente_reativo.consequencia(agente_reativo, linha, coluna+1)
                    matriz[linha][coluna + 1] = self.agente
        if self.agente == '5':
                teste.sense_Wumpus()
                
    def sentir(self):
        return

 

# inicializando a classe principal
teste = gerarMatriz()

# definindo as dimensões do mapa
print('____________________________________________')
print('|-------Bem-vindo ao Mundo de Wumpus--------|')
print('|-------------------------------------------|')
x = int(input('|Digite um valor para dimensao da matriz: '))

# gerantando as matrizes
teste.gerar(x, x)

# imprimindo o mapa principal
teste.plot()
teste.pocos()
teste.plot()
teste.ouro()
teste.plot()
teste.wumpus()
teste.plot()

# imprimindo o mapa de sensações
teste.sense_Poco()
teste.plotPoco()
teste.sense_Ouro()
teste.plotOuro()
teste.sense_Wumpus()
teste.plotWumpus()

# inicializando o posicionamento do agente
teste.setAgente()
teste.plot()

# ininicializando o agente reativo
test = agente_reativo()
test.mover()
teste.plot()
i = 1

#while True:
for j in range(100):
    print(str(i) + ' Movimentos')
    test.mover()
    teste.plot()
    i = i + 1


