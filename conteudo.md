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

![Legenda](https://github.com/davi-dressler/fgv_vc/blob/main/imagens/messi5.jpg)

```python
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball
```

![Legenda](https://github.com/davi-dressler/fgv_vc/blob/main/imagens/messi_bola_ducplicada.jpg)

# Splitting and Merging canais de imagem

```python
b, g, r = cv.split(img)
img = cv.merge((b,g,r))
```
Se quisermos selecionar apenas um canal também podemos fazer:
```python
b = img[:, :, 0]
```

- Cuidado: cv.split() is a costly operation (in terms of time). So use it only if necessary. Otherwise go for Numpy indexing.


