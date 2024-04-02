'''
PIL (Python Imaging Library) é uma biblioteca de processamento de imagens 
fornece uma coleção de funcionalidades para manipular imagens, incluindo a
leitura, escrita, processamento e exibição de imagens em vários formatos 
Foi substituída pelo Pillow (uma bifurcação de PIL)
'''
from PIL import Image
import cv2
import numpy as np

'''
#para importar o drive pessoal
from google.colab import drive
drive.mount('/content/drive')
'''
#para abrir arquivos 'zipados'
import zipfile
path = 'caminho da base de dados zipada'
zip_object = zipfile.ZipFile(file=path, mode='r')
zip_object.extractall('./')
zip_object.close()

import os
#lista todos os arquivos que estão na pasta de treinamento
os.listdir('caminho da base de treinamento')

def dados_imagem():
  #listar todos os diretórios
  caminhos = [os.path.join('caminho da base de treinamento', f) for f in os.listdir('caminho da base de treinamento')]
  #lista de imagens
  faces = []
  #lista de id's das pessoas
  ids = []
  #para cada caminho/imagem:
  for caminho in caminhos:
    '''
    se estiver executando no colab, essa linha praticamente vai ignorar esse 
    caminho e continuar para a próxima etapa do for, sem gerar erros.
    O colab basicamente tenta verificar se os arquivos estão presentes nesse
    caminho mostrado
    if caminho == '/content/yalefaces/treinamento/.ipynb_checkpoints':
      continue
    '''
    #abra a imagem em tons de cinza 'L', 'P' é para rgb
    imagem = Image.open(caminho).convert('L')
    #passamos a imagem para o numpy, na forma de array, passando o tipo de dado
    imagem_np = np.array(imagem, 'uint8')
    '''
    pega apenas o id da pessoa, com base no path da base de dados, retirando
    o que for o nome do objeto 'nome do objeto' e pegando apenas o número de id
    considerando o seguinte salvamento "nome do objeto01", resultado após a 
    execução da linha: "01"
    '''
    id = int(os.path.split(caminho)[1].split('.')[0].replace('nome do objeto', ''))
    #insere na lista de id's
    ids.append(id)
    #insere a imagem na lista de faces
    faces.append(imagem_np)
  #retorna as duas listas
  return np.array(ids), faces

#cria uma lista de ids de imagens(np.array(ids)) e uma matriz de faces
ids, faces = dados_imagem()

#printa todos os ids
print(ids)

#printa a matriz de faces
print(faces[0])

#cria o algoritmo lbph
lbph = cv2.face.LBPHFaceRecognizer_create()
#faz o treinamento com as faces e os ids passados
lbph.train(faces, ids)
'''
cria um arquivo classificador LBPH em openCV, que é o arquivo utilizado para
classificar (semelhante aos classificadores que poderíamos buscar no link
mencionado no arquivo deteccao_de_faces.py na seção cv2.CascadeClassifier)
'''
lbph.write('classificadorLBPH.yml')

#cria um objeto capaz de reconhecer as faces
reconhecedor = cv2.face.LBPHFaceRecognizer_create()
#carregamos o classificador
reconhecedor.read('/local onde foi salvo o classificador/classificadorLBPH.yml')

#criamos uma imagem de teste
imagem_teste = 'local da imagem de teste'

#abrimos a imagem na variável imagem, convertido em tons de cinza 'L'
imagem = Image.open(imagem_teste).convert('L')
#transforma a imagem em uma matriz de inteiros de 8 bits 'uint8'
imagem_np = np.array(imagem, 'uint8')
print(imagem_np)

'''
faz a previsão de id, _ confiança da resposta (que não será utilizada '_')
'''
idprevisto, _ = reconhecedor.predict(imagem_np)
#verificar o id previsto
idprevisto

#verificar se o id é o correto
idcorreto = int(os.path.split(imagem_teste)[1].split('.')[0].replace('subject', ''))
idcorreto

'''
insere na imagem os o texto 'P: {id_previsto}' onde mostra o id que foi previsto
pelo algoritmo classificador e 'C: {id_correto}' onde mostra o id correto na
base de dados

cv2.putText(imagem, 'mensagem', 'local para inserir o texto em coordenadas de
pixel', fonte do texto, tamanho da fonte e a cor do texto bgr (rgb))
'''
cv2.putText(imagem_np, 'P: ' + str(idprevisto), (x,y + 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,0))
cv2.putText(imagem_np, 'C: ' + str(idcorreto), (x,y + 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,255,0))
#exibe a imagem com as alterações
cv2.imshow(imagem_np)