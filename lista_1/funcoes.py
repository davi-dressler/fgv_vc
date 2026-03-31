import cv2
import numpy as np

imagem = cv2.imread("lista_1\PoucoContraste.png")

def alterar_luminancia_contraste(imagem, luminancia, contraste):
    
    imagem = imagem + luminancia
    
    cv2.imshow("Janela da Imgem", imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#
alterar_luminancia_contraste(imagem, 0, 0)

#setosa.io/ev/image-kernels/