#Instala as bibliotecas necessárias
from matplotlib import pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


#cria um array numpy de tamanho 11 (de 0 à 10), incrementando 1
np.arange(0, 11, 1)

'''
Cria duas variáveis e as atribuem a uma instância da classe
Antecedent do módulo control. A classe Antecedent é usada para definir uma
variável antecedente em um sistema de controle fuzzy.  Como np.arange(0, 10, 1)
gera um array numpy com valores de 0 a 10 (inclusivo), com um passo de 1. Este
array representa os possíveis valores que as variáveis antecedentes qualidade e
servico podem assumir.
'''
qualidade = ctrl.Antecedent(np.arange(0, 11, 1), 'qualidade')
servico = ctrl.Antecedent(np.arange(0, 11, 1), 'servico')

#exibe o atributo
print(qualidade)

#mostra o seu conjunto universo
print(qualidade.universe)

'''
Aqui, uma variável chamada gorjeta é criada e atribuída a uma instância da
classe Consequent do módulo control (que foi importado anteriormente como ctrl).
A classe Consequent é usada para definir uma variável consequente em um sistema
de controle fuzzy.
np.arange(0, 21, 1) gera um array numpy com valores de 0 a 20 (inclusivo),
com um passo de 1. Este array representa os possíveis valores que a variável
consequente gorjeta pode assumir.
'''
gorjeta = ctrl.Consequent(np.arange(0, 21, 1), 'gorjeta')

#mostra o conjunto universo do consequente
print(gorjeta.universe)

'''
O método automf é usado para criar automaticamente funções de pertinência para
a variável antecedente. O argumento number=3 especifica que três funções de
pertinência devem ser criadas para a variável qualidade e servico.
O argumento names=['ruim', 'boa', 'saborosa'] e names=['ruim', 'aceitável',
'ótimo'] fornece os nomes para as três funções de pertinência criadas. Esses
nomes são usados para identificar as funções de pertinência no sistema
de controle fuzzy.
'''
qualidade.automf(number=3, names=['ruim', 'boa', 'saborosa'])
servico.automf(number=3, names=['ruim', 'aceitável', 'ótimo'])

'''
.view() é usada para visualizar as funções de pertinência (também conhecidas
como funções de membership) definidas para a variável antecedente qualidade em
um sistema de controle fuzzy. Quando você executa essa linha, ela gera uma
representação gráfica das funções de pertinência associadas à variável chamada
'''
qualidade.view()

#exibe uma função de pertinência criadas de forma mais destacada
qualidade['saborosa'].view()

servico.view()

gorjeta.universe

'''
Estas linhas definem uma função de pertinência triangular (trimf) para a
variável consequente gorjeta com o nome 'baixa', 'media' e 'alta'.
'fuzz.trimf' é uma função que cria uma função de pertinência triangular. As
funções triangulares são uma das formas mais comuns de funções de pertinência e
são definidas por três pontos: o ponto de início, o ponto de máximo e o ponto de
fim.
'gorjeta.universe' é o conjunto de valores possíveis para a variável gorjeta.
Exemplo: a linha está dizendo que a função de pertinência 'baixa' deve ser
aplicada a todos os valores no universo de gorjeta. [0, 0, 8] ([inicio, meio,
fim]) define os pontos  da função triangular. Neste caso, a função começa e
termina em 0, e o ponto de máximo é 8. Isso significa que a função de
pertinência 'baixa' terá um valor alto de pertinência para valores próximos a 0
e um valor baixo de pertinência para valores próximos a 8.
'''
'''
gorjeta['baixa'] = fuzz.trimf(gorjeta.universe, [0, 0, 8])
gorjeta['media'] = fuzz.trimf(gorjeta.universe, [2, 10, 18])
gorjeta['alta'] = fuzz.trimf(gorjeta.universe, [12, 20, 20])
'''
gorjeta['baixa'] = fuzz.sigmf(gorjeta.universe, 5, -1)
gorjeta['media'] = fuzz.gaussmf(gorjeta.universe, 10, 3)
gorjeta['alta'] = fuzz.pimf(gorjeta.universe, 10, 20, 20, 21)

gorjeta.view()

'''
definem as regras fuzzy para o sistema de controle
'ctrl.Rule()' é uma função que cria uma regra fuzzy. A regra é composta por uma
condição (ou condições) e uma consequência.
regra = ctrl.Rule(antecedente['função de pertinência'] operador lógico outro
antecedente['outra função de pertinência'] (operador lógico outros
antecedentes['outras função de pertinências']), consequente['função de
pertinência']
As regras variam de acordo com o problema (claro)
'''
regra1 = ctrl.Rule(qualidade['ruim'] | servico['ruim'], gorjeta['baixa'])
regra2 = ctrl.Rule(servico['aceitável'], gorjeta['media'])
regra3 = ctrl.Rule(servico['ótimo'] | qualidade['saborosa'], gorjeta['alta'])

#cria um sistema de controle baseado nas regras criadas anteriormente
sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3])

'''
cria uma instância de um sistema de controle fuzzy para a simulação
'ctrl.ControlSystemSimulation' é uma função da biblioteca skfuzzy que cria
uma instância de um sistema de controle fuzzy para simulação. Uma instância de
simulação permite que você execute o sistema de controle fuzzy com diferentes
entradas e observe as saídas fuzzy resultantes.
'''
sistema = ctrl.ControlSystemSimulation(sistema_controle)

#define os valores de entrada das variáveis (lembrando que aceitam de 0 à 10)
sistema.input['qualidade'] = 10
sistema.input['servico'] = 10

'''
executa o cálculo de saída fuzzy com base nas entradas fornecidas. O sistema de
controle usa as regras definidas para mapear as entradas para prover uma saída
'''
sistema.compute()

#imprime a saida fuzzy
print(sistema.output['gorjeta'])
'''
gera uma visualização gráfica da saída fuzzy com base na simulação do sistema
de controle.
'sim = sistema' é um argumento que especifica que a visualização deve ser
baseada nas saídas fuzzy calculadas pelo sistema de controle fuzzy 'sistema'.
Isso significa que a visualização mostrará como as funções de pertinência para
gorjeta se comportam com base nas entradas que foram usadas para calcular as
saídas fuzzy do sistema.
'''
gorjeta.view(sim = sistema)
#permite que os gráficos fiquem abertos
plt.show()