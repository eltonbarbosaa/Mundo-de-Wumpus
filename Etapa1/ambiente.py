# Importar o módulo random
import random

# Definir a classe Ambiente
class Ambiente:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.matriz = [[' '] * tamanho for _ in range(tamanho)]
        self.posicao_inicial = (0, 0)
        
    def gerar_ambiente(self):
        # Definir quantidade de objetos
        quantidade_pocos = 2
        quantidade_wumpus = 1
        quantidade_ouro = 1
        
        # Posicionar poços
        posicoes_livres = self.obter_posicoes_livres()
        posicoes_pocos = random.sample(posicoes_livres, quantidade_pocos)  # Selecionar posições aleatórias para os poços
        for posicao in posicoes_pocos:
            self.matriz[posicao[0]][posicao[1]] = '2'  # Posicionar os poços na matriz
        
        # Posicionar Wumpus
        posicoes_livres = self.obter_posicoes_livres()
        posicao_wumpus = random.choice(posicoes_livres)  # Selecionar uma posição aleatória para o Wumpus
        self.matriz[posicao_wumpus[0]][posicao_wumpus[1]] = '5'  # Posicionar o Wumpus na matriz
        
        # Posicionar ouro
        posicoes_livres = self.obter_posicoes_livres()
        posicao_ouro = random.choice(posicoes_livres)  # Selecionar uma posição aleatória para o ouro
        self.matriz[posicao_ouro[0]][posicao_ouro[1]] = '10'  # Posicionar o ouro na matriz
        
        # Definir percepções
        self.definir_percepcoes('5', 'F')  # Wumpus emite fedor
        self.definir_percepcoes('10', 'B')  # Ouro emite brilho
        self.definir_percepcoes('2', 'b')  # Poço emite brisa
        
        # Definir posição inicial do agente
        self.posicao_inicial = (0, 0)
        
    def obter_posicoes_livres(self):
        posicoes_livres = []
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                if (i, j) != (0, 0):
                    posicoes_livres.append((i, j))  # Adicionar as posições livres à lista
        return posicoes_livres
    
    def definir_percepcoes(self, objeto, percepcao):
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                if self.matriz[i][j] == objeto:
                    self.adicionar_percepcao((i-1, j), percepcao)  # Acima
                    self.adicionar_percepcao((i+1, j), percepcao)  # Abaixo
                    self.adicionar_percepcao((i, j-1), percepcao)  # Esquerda
                    self.adicionar_percepcao((i, j+1), percepcao)  # Direita
        
    def adicionar_percepcao(self, posicao, percepcao):
        if self.validar_posicao(posicao):
            i, j = posicao
            if self.matriz[i][j] == ' ':
                self.matriz[i][j] = percepcao  # Adicionar a percepção à posição da matriz
        
    def validar_posicao(self, posicao):
        i, j = posicao
        return 0 <= i < self.tamanho and 0 <= j < self.tamanho
        
    
    def mostrar_ambiente(self):
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                print(f'{self.matriz[i][j]:^5}', end=' ')  # Imprimir o valor da posição formatado centralizado
            print()

# Exemplo de uso
tamanho = int(input('Digite o tamanho da matriz do ambiente: '))  # Solicitar o tamanho da matriz ao usuário

ambiente = Ambiente(tamanho)  # Criar um objeto Ambiente com o tamanho informado
ambiente.gerar_ambiente()  # Gerar o ambiente aleatoriamente
ambiente.mostrar_ambiente()  # Mostrar o ambiente na saída
