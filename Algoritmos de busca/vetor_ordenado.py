'''
numpy é uma biblioteca python usada para trabalhar
com dados numéricos em Python de forma mais simples
e mais eficiente
'''
import numpy as np

#cria uma classe que ordena vetores "automaticamente"
class VetorOrdenado:
    '''
    inicia a classe com seus construtores, sendo self
    um parâmetro para referir a própria instância da classe
    e capacidade o máxima de elementos que esse vetor deve ter 
    ''' 
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        #inicializa todos os valores com o tipo int(mas sem atribuir um valor específico)
        self.valores = np.empty(self.capacidade, dtype=int)
    
    #O(n)
    def imprime(self):
        #se a última posição estiver vazia, printa
        if self.ultima_posicao == -1:
            print("O vetor está vazio")
        #se não, printa todos os valores no vetor
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])

    #O(n)
    def insere(self, valor):
        #se a última posição do vetor estiver preenchida
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        
        posicao = 0

        #se não estiver totalmente preenchido, percorre todo o vetor
        for i in range(self.ultima_posicao + 1):
            posicao = i
            #se o valor na posição atual for maior que o valor inserido pare de percorrer
            if self.valores[i] > valor:
                break
            #se for igual à última posição, a posição recebe incremento de 1
            if i == self.ultima_posicao:
                posicao = i + 1
        
        #define x como a ultima posição do vetor
        x = self.ultima_posicao
        
        #enquanto x for maior ou igual à posição
        while x >= posicao:
            #pegamos o valor na posição atual e inserimos na posição seguinte
            self.valores[x + 1] = self.valores[x]
            #reduzimos x em 1 para remanejarmos todos os valores uma casa à frente
            x -= 1

        #inserimos o valor inserido na posição ordenada
        self.valores[posicao] = valor
        #incrementamos a última posição final ocupada do vetor em 1
        self.ultima_posicao += 1
    

#cria um vetor com 10 de tamanho
vetor = VetorOrdenado(10)

#imprime o vetor
vetor.imprime()

#insere valores
vetor.insere(6)
#vetor.imprime()

vetor.insere(8)
#vetor.imprime()

vetor.insere(4)
#vetor.imprime()

vetor.insere(5)
#vetor.imprime()

vetor.insere(1)
#vetor.imprime()

vetor.insere(10)
vetor.imprime()


