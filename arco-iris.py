import cv2

vid_e_img = int(input("(1)criar video      (2)criar imagem: "))
save_dir = input("diretorio onde frames sao salvos, obviamente ele tem que existir: ")
fator_de_mudanca = int(input("A suavidade do gradiente de cor: "))



def gerenciamento_de_cores(grau,filtr):
    cor_atual = 0

    if(filtr[0][0][0] != 255 and filtr[0][0][1] != 0):
        filtr[0:][0:] = [filtr[0][0][0] + grau,filtr[0][0][1] - grau,filtr[0][0][2]]

    elif(filtr[0][0][1] != 255 and filtr[0][0][2] != 0):
        filtr[0:][0:] = [filtr[0][0][0],filtr[0][0][1] + grau,filtr[0][0][2] - grau]

    elif(filtr[0][0][2] != 255 and filtr[0][0][0] != 0):
        filtr[0:][0:] = [filtr[0][0][0] - grau,filtr[0][0][1],filtr[0][0][2] + grau]



    return filtr

def gerarar_arcoiris(quantidade, imagens):
    ciclo = 0
    nome = 0

    dimencao_do_filtro = cv2.imread(imagens[0])
    dimencao_do_filtro[0:][0:] = [0,255,0]
    filtro = dimencao_do_filtro

    for imagem in imagens:
        ler = imagem
        while(quantidade != 0):
            img = cv2.imread(ler)
            ciclo_copia = ciclo


            filtro = gerenciamento_de_cores(fator_de_mudanca,filtro)

            img = img + filtro


            ciclo_str = str(nome)
            cv2.imwrite(save_dir + "/" + ciclo_str + ".png",img)
            nome += 1

            ciclo += 1
            quantidade -= 1

if(vid_e_img == 2):
    diretorio = input("imagem de escolha: ")
    todas_as_imagens = []
    todas_as_imagens.append(diretorio)
    quantidade_de_imagens = int(input("quantas imagens você quer?: "))
    gerarar_arcoiris(quantidade_de_imagens, todas_as_imagens)

elif(vid_e_img == 1):
    print("HA HA, achou q era uma outra funçãoooo, mas ERA EUUUUUU!!!!")
else:
    print("essa opcao nao exite, talvez vc esteja desapontato. Mas se anime, vamos considerar isso um easter egg pode ser?")
