'''
importamos o openCV que é uma biblioteca open source para processamento de
imagens e visão computacional
'''
import cv2

#inicializamos a imagem em uma variável
imagem = cv2.imread('visao_computacional\imagens\corpos.png')

'''
essa importação é necessária apeans caso estejamos utilizando com colab, é uma
modificação que o google fez para que o open cv rode normalmente
-> from google.colab.patches import cv2_imshow
cv2_imshow(imagem)
'''

#exibe a imagem
cv2.imshow('Imagem Original', imagem)

'''
definimos um detector de faces, aqui é utilizado um arquivo xml já treinado, 
inserido no CascadeClassifier é possível obter no link a seguir:
https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_fullbody.xml
'''
detector_corpo = cv2.CascadeClassifier('visao_computacional\codigos_treinados_cascadeClassifier\haarcascade_fullbody.xml')

'''
alteramos para tons de cinza, auxilia na diminuição de tempo de processamento,
pois define apenas um canal de cor ao invés do RGB convencional
'''

imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
# Exibe a imagem original
cv2.imshow('Imagem em Cinza', imagem_cinza)

#aplicamos o detector de face na imagem com o detectMultiScale
'''
imagem_cinza é a imagem que iremos rodar a detecção,
scaleFactor é como se fosse um zoom, onde ajuda na identificação de objetos
com base em ampliação,
minSize é o valor mínimo do objeto que queremos identificar em pixels
'''
deteccoes = detector_corpo.detectMultiScale(imagem_cinza, scaleFactor=1.1, minSize=(30,30))

'''
indica os pontos de cada face em uma matriz cada elemento da matriz é uma lista
onde os dois primeiros elementos da lista é a posição x e y de início da face e
os dois últimos são os tamanhos da face encontrada em pixels, isso ajuda a
traçar um retângulo sobre essa face
dtype=int32 refere-se a um tipo de dado inteiro de 32 bits
'''
deteccoes

#informa a quantidade de faces detectadas
len(deteccoes)

#para cada coordenada de detecções (l = largura, a = altura)
for (x, y, l, a) in deteccoes:
  #print(x, y, l, a)
  '''
  cria um retângulo sobre a imagem passando a imagem original as dimensões do
  retângulo (x + l, y + a) que são as linhas delimitadoras do retângulo, a cor 
  do retângulo criado em escala RGB e o tamanho da borda
  ''' 
  cv2.rectangle(imagem, (x, y), (x + l, y + a), (145, 125, 225), 2)
#exibe a imagem com os contornos
cv2.imshow('Imagem com retângulos', imagem)

#espera até que uma tecla seja pressionada para fechar as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()