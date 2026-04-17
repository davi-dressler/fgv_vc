# Transformada de Fourier

A ideia principal da Análise de Fourier é comparar o sinal com senosoidais de várias frequências $w \in \mathbb{R}$. Como resultado, nós obtemos para cada parâmetro de frequência $w$ um coeficiente de magnitude $d_w \in \mathbb{R} >= 0$. No caso de $d_w$ ser grande, há uma alta similaridade entre o sinal e a senosoidal de frequência $w$, e o sinal contém uma oscilação periódica nessa frequência. No de $d_w$ pequeno, o sinal não contém uma componente periódica nessa frequência.

A transformada de Fourier quebra o sinal nas suas componentes de frequência. 

- OBS: uma propriedade imporatnte é que o sinal original pode ser reconstruído a partir dos coeficientes $d_w$. Para isso, nós basicamente sobrepomos as senosoidais de todas as frequências possíveis, cada uma ponderada pelo respectivo coeficiente $d_w$ (e deslocada por $\varphi_w$ que ainda será explicado).

Essa sobrepovisição ponderada é também chamada de $\textbf{Representação de Fourier}$ do sinal original.

O sinal original e a transforamda de Fourier contêm a mesma quantidade de informação. a diferença está em como elas são representadas. Enquanto o sinal original respresenta a informação através do tempo, a transformada de Fourier representa a informação através da frequência.

- O sinal nos diz quando a nota foi tocado, enquanto a transformada de Fourier nos diz que nota foi tocada(frequência).

## Transformada de Fourier para sinais analógicos

Vamos considerar um sinal analógico, onde tanto o tempo quanto a amplitude são contínuos e reais. Nesse caso um sinal pode ser interpretado como uma função $f: \mathbb{R} \rightarrow \mathbb{R}$ que assimila para cada valor de $t$ (tempo) uma amplitude $f(t)$. A o plotarmos a amplitude ao longo do tempo conseguimos um gráfico que corresponde a waveform do sinal.

## O papel da fase

Nós comparamos o sinal $f$ com oscilações que foram dadas na forma de senosoidais. Matematicamente, uma senosoidal é uma função $g: \mathbb{R} \rightarrow \mathbb{R}$ definida por 

$$g(t) := A\sin(2\pi(wt - \varphi))$$

O parâmetro A corresponde à  $\textbf{Amplitude}$, o parâmetro $w$ que corresponde à $\textbf{Frequência}$, e o parâmetro $\varphi$ que corresponde à $\textbf{Fase}$(mensurada em radianos em radianos normalizados com 1 correspondendo ao ângulo de 360º). 

Na análise de Fourier, nós consideramos as oscilações que são normalizadas em relação a sua potência (energia média) definindo $A = \sqrt{2}$. Assim, para cada $w$ e $\varphi$ nós obtemos uma senosoidal $\textbff{\cos_{w,\varphi}}$ definida por:

$$\textbff{\cos}_{w,\varphi}(t) := \sqrt{2}\cos(2\pi(wt - \varphi))$$

Como a função cosseno é periódica, os parâmetros $\varphi$ e $\varphi + k$ para inteiros $k \in \mathbb{Z}$ produzem a mesma função. Portanto, o parâmetro fase só precisa ser considerado para $\varphi \in [0,1)$.

Ao mensurar quão bem um sinal dado coincide com uma senoide de frequência $w$, nós temos a liberdade de deslocar a senoide no tempo. Esse grau de liberdade é expresso pelo parâmetro $\varphi$.

- OBS: A grau de similaridade entre e a senoide de frequência fixa depende crucialmente da fase.

## Computando similaridades com integrais

Vamos assumir que dadas duas funções $f: \mathbb{R} \rightarrow \mathbb{R}$ e $g: \mathbb{R} \rightarrow \mathbb{R}$. O que significa $f$ e $g$ serem similares? Intuitivamente, se elas são similares devem ter um comportamento parecido ao longo do tempo: se $f$ assume valores positivos então $g$ também, mesma coisa para valores negativos. O comportamento conjunto dessas funções pode ser conseguido a partir da integral do produto das duas funções:

$$ \int_{t \in \mathbb{R}} f(t)*g(t)dt  $$

No caso em que $f$ e $g$ são ambas positivas ou ambas negativas na maior parte do tempo, seu produto será positivo na maioria do tempo e a integral se torna larga. No caso das funções serem dissociadas, o total das áreas positivas e o total das áreas negativas se cancelam resultando em uma integral pequena.

Há algumas maneiras diferentes de fazer essa transformação, mas na transformada de Fourier nós encontramos essa por generalizar o produto interno.

## Primeira definição da Transformada de Fourier

Baseado na medida de similaridade, nós comparamos o sinal original $f$ com senoides $g = \textbf{cos}_{w,t}$. Para uma frequência $w$ fixada, nós definimos:

$$ d_w := \max_{\varphi \in [0,1)} (\int_{t \in mathbb{R}} f(t)\textbf{cos}_{w,t}(t)dt)$$

$$ \varphi_w := \argmax_{\varphi \in [0,1)} (\int_{t \in mathbb{R}} f(t)\textbf{cos}_{w,t}(t)dt)$$

Como vimos a magnitude de $d_w$ expressa a intensidade da frequência $w$ com o sinal $f$. Adicionalmente, o coeficiente de fase $\varphi_w \in [0,1)$ nos diz como o senoide de frequência $w$ precisa ser alocado no tempo para melhor se encaixar ao sinal $f$. 

- A $\textbf{Transformada de Fourier}$ de uma função $f: \mathbb{R} \rightarrow \mathbb{R}$ é definida como a coleção de todos os coeficientes $d_w$ e $\varphi_w$. 
