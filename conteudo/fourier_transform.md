# Transformada de Fourier

A ideia principal da Análise de Fourier é comparar o sinal com senosoidais de várias frequências $w \in \mathbb{R}$. Como resultado, nós obtemos para cada parâmetro de frequência $w$ um coeficiente de magnitude $d_w \in \mathbb{R} >= 0$. No caso de $d_w$ ser grande, há uma alta similaridade entre o sinal e a senosoidal de frequência $w$, e o sinal contém uma oscilação periódica nessa frequência. No de $d_w$ pequeno, o sinal não contém uma componente periódica nessa frequência.

A transformada de Fourier quebra o sinal nas suas componentes de frequência. 

- OBS: uma propriedade imporatnte é que o sinal original pode ser reconstruído a partir dos coeficientes $d_w$. Para isso, nós basicamente sobrepomos as senosoidais de todas as frequências possíveis, cada uma ponderada pelo respectivo coeficiente $d_w$ (e deslocada por $\phi_w$ que ainda será explicado).

Essa sobrepovisição ponderada é também chamada de $\textbf{Representação de Fourier}$ do sinal original.

O sinal original e a transforamda de Fourier contêm a mesma quantidade de informação. a diferença está em como elas são representadas. Enquanto o sinal original respresenta a informação através do tempo, a transformada de Fourier representa a informação através da frequência.

- O sinal nos diz quando a nota foi tocado, enquanto a transformada de Fourier nos diz que nota foi tocada(frequência).

## Transformada de Fourier para sinais analógicos

Vamos considerar um sinal analógico, onde tanto o tempo quanto a amplitude são contínuos e reais. Nesse caso um sinal pode ser interpretado como uma função $f: \mathbb{R} \rightarrow \mathbb{R}$ que assimila para cada valor de $t$ (tempo) uma amplitude $f(t)$. A o plotarmos a amplitude ao longo do tempo conseguimos um gráfico que corresponde a waveform do sinal.

## O papel da fase

Nós comparamos o sinal $f$ com oscilações que foram dadas na forma de senosoidais. Matematicamente, uma senosoidal é uma função $g: \mathbb{R} \rightarrow \mathbb{R}$ definida por 

<center>

$g(t) := A\sin(2\pi(wt - \phi))$

</center>
