Wumpus Algoritmo Genético
Para executar o script, siga os seguintes passos:

1. Abra um terminal ou prompt de comando.
2. Navegue até o diretório onde o arquivo main.py está localizado.
3. Execute o seguinte comando:

$ python main.py
Certifique-se de ter o Python instalado corretamente em seu sistema antes de executar o comando acima.

Além disso, existem alguns parâmetros que você pode passar para a instância Ambiente. Aqui estão os parâmetros disponíveis:

dimensao: Um número inteiro que define a dimensão do problema. Por padrão, o problema está configurado para uma matriz 4x4.
tamanho_populacao: Um número inteiro que representa a quantidade de indivíduos na primeira geração. O valor padrão é 20.
geracao_parada: Um número inteiro que representa o número máximo de gerações. O valor padrão é 10.
Você pode ajustar esses parâmetros conforme necessário, passando-os para a instância Ambiente da seguinte maneira:

ag = Ambiente(dimensao=4, tamanho_populacao=20, geracao_parada=10)
Depois de configurar os parâmetros desejados, basta executar o script main.py como mencionado anteriormente para iniciar o algoritmo genético com os parâmetros fornecidos.
