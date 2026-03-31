# Baixando e importando a biblioteca OpenCV
Para baixar a biblioteca, execute no terminal:
```python
pip install opencv-python
```

Para importar no seu arquivo:
```python
import cv2 as cv
```

# Carregando uma imagem 
Para processar uma uma imagem umas a função:
```python
img = cv.imread("caminho-para-a-imagem\nome-da-imagem.png")
```

É possível acessar pixels com indexação igual é feito no numpy. É possível modificar os pixels da mesma forma.

# Acessando propriedades de uma imagem
Para acessar seu formato:
```python
print(img.shape)
```

Para acessar o número total de pixels:
```python
print(img.size)
```

Para acessar o datatype:
```python
print(img.dtype)
```
# ROI (Region of Intesrest)

A partir da indexação é possível fazer operações como:
![Texto alternativo](imagens\messi5.png)

```python
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball
```

![Texto alternativo](imagens\messi_bola_duplicada.png)


