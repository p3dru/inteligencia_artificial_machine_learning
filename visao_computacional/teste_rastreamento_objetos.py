import cv2 as cv

#cria o rastreador
rastreador = cv.TrackerCSRT_create()
#inicializa o video que queremos rastrear o objeto
video = cv.VideoCapture('link do video')
#pega o primeiro frame
ok, frame = video.read()

#identifica a região de interesse para que possamos rastrear
#abre uma caixa com uma imagem para selecionarmos o que queremos rastrear
bbox = cv.selectROI(frame)
#mostra as coordenadas do que selecionamos
#print(bbox)

#inicializizamos o rastreador com o frame desejado e o objeto selecionado
ok = rastreador.init(frame, bbox)

while True:
    #realiza o rastreamento no video indefinidamente
    ok, frame = video.read()
    #o critério de parada é quando terminar de capturar o último frame do vídeo
    #ao final do video o valor de ok será False, caso não tivesse o critério de
    #parada, o while continuaria executando
    if not ok:
        break

    #para acompanhar a região de interesse a cada frame
    ok, bbox = rastreador.update(frame)

    #enquanto estiver acompanhando
    if ok:
        #para cada coordenada recebida no bbox
        (x, y, w, h) = [int(v) for v in bbox]
        #crie um retângulo no frame, iniciando na posição x, y de tamanho (x + w, y + h)
        #de cor (0, 255, 0), tamanho da linha, tipo da linha
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2, 1)
    #caso não consiga identificar, exiba a frase "Falha no carregamento", na posição (100, 80)
    else:
        cv.putText(frame, 'Falha no rastreamento', (100, 80),
                    cv.FONT_HERSHEY_SIMPLEX, .75, (0, 0, 255), 2)
    
    #exiba o video com a frase rastreando a cada frame
    cv.imshow('Rastreando', frame)
    #se a tecla hex 27 (esc) for pressionada, finalize
    if cv.waitKey(1) & 0XFF == 27:
        break
