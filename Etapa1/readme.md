# **ETAPA 1**

<figure>
<center> 
<img src='https://drive.google.com/uc?export=view&id=1kLssH5_OMj55O3xwJz1DOYYwqkNMuJ6A' width="600" />

  
</center>
</figure>

## **Ambiente Mundo-Wumpos**

<p ALIGN=justify ></p>
Nessa primeira implementação, vamos estar gerando o ambiente da simulação. Para isso é necessário criar a classe Ambiente que possui métodos para gerar o ambiente e posicionar os objetos que são definidos como: wumpus=5, poços=2 e ouro=10, além de definir esses objetos, fizemos as percepções que cada um emite wumpus=F, poços=b e ouro=B. O ambiente é definido por uma matriz, onde cada posição pode conter um objeto ou uma percepção. Já iniciamos nosso ambiente com o número de objetos definidos no programa, o usuário vai definir somente o tamanho da matriz inicialmente e ela deve ser maior ou igual a 3.
Em resumo, a primeira etapa do código está dividida entre:

<br>•	Importa o módulo Random para gerar números aleatórios.
<br>•	Definir a classe "Ambiente" com métodos para gerar o ambiente, posicionar objetos, definir percepções e mostrar o ambiente.
<br>•	O método "gerar_ambiente" define a quantidade de objetos (poços, Wumpus e ouro), seleciona posições aleatórias para os objetos e os posiciona na matriz do ambiente.
<br>•	O método "obter posições livres" retorna as posições da matriz que estão livres (não ocupadas por objetos).
<br>•	O método "definir_percepcoes" percorre a matriz e define as percepções para os objetos encontrados.
<br>•	O método "adicionar percepção" adiciona a percepção em uma determinada posição da matriz, desde que a posição seja válida e esteja vazia.
<br>•	O método "validar posição" verifica se uma posição é válida dentro da matriz.
<br>•	O método "mostrar ambiente" exibe o ambiente na saída, formatando cada posição da matriz.
<br>•	No exemplo de uso, o código solicita ao usuário o tamanho da matriz do ambiente, cria um objeto "Ambiente" com esse tamanho, gera o ambiente aleatoriamente e o mostra na saída.

<p ALIGN=justify ></p>

