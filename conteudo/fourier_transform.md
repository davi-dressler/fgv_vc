# Transformada de Fourier

A ideia principal da Análise de Fourier é comparar o sinal com senoidais de várias frequências $w \in \mathbb{R}$. Como resultado, nós obtemos para cada parâmetro de frequência $w$ um coeficiente de magnitude $d_w \in \mathbb{R} >= 0$. No caso de $d_w$ ser grande, há uma alta similaridade entre o sinal e a senosoidal de frequência $w$, e o sinal contém uma oscilação periódica nessa frequência. No de $d_w$ pequeno, o sinal não contém uma componente periódica nessa frequência.

A transformada de Fourier quebra o sinal nas suas componentes de frequência. 

- OBS: uma propriedade imporatnte é que o sinal original pode ser reconstruído a partir dos coeficientes $d_w$. Para isso, nós basicamente sobrepomos as senoidais de todas as frequências possíveis, cada uma ponderada pelo respectivo coeficiente $d_w$ (e deslocada por $\varphi_w$ que ainda será explicado)

Essa sobrepovisição ponderada é também chamada de $\textbf{Representação de Fourier}$ do sinal original.

O sinal original e a transforamda de Fourier contêm a mesma quantidade de informação. a diferença está em como elas são representadas. Enquanto o sinal original respresenta a informação através do tempo, a transformada de Fourier representa a informação através da frequência.

- O sinal nos diz quando a nota foi tocado, enquanto a transformada de Fourier nos diz que nota foi tocada(frequência).

## Transformada de Fourier para sinais analógicos

Vamos considerar um sinal analógico, onde tanto o tempo quanto a amplitude são contínuos e reais. Nesse caso um sinal pode ser interpretado como uma função $f: \mathbb{R} \rightarrow \mathbb{R}$ que assimila para cada valor de $t$ (tempo) uma amplitude $f(t)$. A o plotarmos a amplitude ao longo do tempo conseguimos um gráfico que corresponde a waveform do sinal.

## O papel da fase

Nós comparamos o sinal $f$ com oscilações que foram dadas na forma de senosoidais. Matematicamente, uma senosoidal é uma função $g: \mathbb{R} \rightarrow \mathbb{R}$ definida por 

$$g(t) = A\sin(2\pi(wt - \varphi))$$

O parâmetro A corresponde à  $\textbf{Amplitude}$, o parâmetro $w$ que corresponde à $\textbf{Frequência}$, e o parâmetro $\varphi$ que corresponde à $\textbf{Fase}$(mensurada em radianos em radianos normalizados com 1 correspondendo ao ângulo de 360º). 

Na análise de Fourier, nós consideramos as oscilações que são normalizadas em relação a sua potência (energia média) definindo $A = \sqrt{2}$. Assim, para cada $w$ e $\varphi$ nós obtemos uma senoidal $cos_{w,\varphi}(t)$ definida por:

$$cos_{w,\varphi}(t) := \sqrt{2}\cos(2\pi(wt - \varphi))$$

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

$$ d_w := \max_{\varphi \in [0,1)} (\int_{t \in \mathbb{R}} f(t)\textbf{cos}_{w,t}(t)dt)$$

$$ \varphi_w := \argmax_{\varphi \in [0,1)} (\int_{t \in \mathbb{R}} f(t)\textbf{cos}_{w,t}(t)dt)$$

Como vimos a magnitude de $d_w$ expressa a intensidade da frequência $w$ com o sinal $f$. Adicionalmente, o coeficiente de fase $\varphi_w \in [0,1)$ nos diz como o senoide de frequência $w$ precisa ser alocado no tempo para melhor se encaixar ao sinal $f$. 

- A $\textbf{Transformada de Fourier}$ de uma função $f: \mathbb{R} \rightarrow \mathbb{R}$ é definida como a coleção de todos os coeficientes $d_w$ e $\varphi_w$. 

## Números Complexos

Vamos primeiro revisar os números complexos. Os números complexos estendem os número reais ao introduzir um número imaginário $i^2 = -1$. Cada número complexo pode ser escrito como $c = a + bi$, onde $a \in \mathbb{R}$ é a parte real e $b \in \mathbb{R}$ é a parte imaginária de $c$. O conjunto dos complexos, $\mathbb{C}$, pode ser representado como um plano 2-dimensional: a horizontal corresponde a parte real, e a vertical, a imaginária. Nesse plano, cada número complexo $c = a +bi$ é especificado pea coordenada cartesiana $(a,b)$. 

Há também uma outra forma de representar os complexos, conhecida como representação em coordenada polar. Nesse caso, $c$ é repressentado por seu valor absoluto $|c|$ e o ângulo $\gamma \in [0,2\pi)$ entre o eixo horizontal positivo e o vetor correpondente a $|c|$. Para obter $|c|$ a partir de suas coordenadas polares, usamos:

$$\exp(i\gamma) = \cos(\gamma) + i\sin(\gamma)$$

Os valores dessa função giram em torna do círculo unitário dos complexos com um período de $2\pi$. A partir disso, nós obtemos a representação em coordenada polar:

$$ c = |c| * \exp(i\gamma)$$

## Definição complexa da Transformada de Fourier

A principal ideia é usar nosso coeficientes $d_w$ e $\varphi_w$ como coordenadas polares para transformá-los em um único número complexo. Por conta de razões técnicas, introduz-se alguns fatores adicionais e um sinal negativo à fase para resultar no coeficiente complexo:

$$c_w = \frac{d_w}{\sqrt{2}}*\exp(2\pi i (-\varphi_w))$$

Isso nos leva diretamente à tranformada de Fourier de $f$. Para cada frequência $w$, nós obtemos um coeficientecomplexo $c_w$. Essa lista de coeficientes consegue ser resumida por uma função complexa:

$$ \hat{f}(w) = c_w$$

A função $\hat{f}$ é denotada como a $\textbf{Transformada de Fourier}$ de $f$, e seus valores $\hat{f}(w) = c_w$ são chamados de $\textbf{coeficientes de Fourier}$. Um dos principais resultados da análise de fourier é que a transformada de Fourier pode ser computada pela seguinte fórmula compacta:

$$\hat{f}(w) = \int_{t \in \mathbb{R}}f(t)\exp(-2\pi iwt)dt$$
$$= \int_{t \in \mathbb{R}}f(t)\cos(-2\pi iwt)dt + i \int_{t \in \mathbb{R}}f(t)\sin(-2\pi iwt)dt$$



