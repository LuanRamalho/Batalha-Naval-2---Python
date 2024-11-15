# Naval Battle :books:

<p>
 <a href="#Sobre">Sobre</a> •  
 <a href="#Características">Características</a> • 
 <a href="#Status">Status do Projeto</a> • 
 <a href="#Requisitos">Requisitos Mínimos</a> 
 :open_file_folder:
</p>

<a name="Sobre"></a>
## Sobre :information_source:
Feito em python como projeto final da disciplina de Algoritimo e Programação Estruturada, trata-se de um jogo de batalha naval que pode ser jogado usando o console do python no modo jogador contra jogador ou jogador contra bot, faz uso de modularização, funções, POO básico, e estruturas de dados simples.

<a name="Características"></a>
## Características :page_facing_up:

Possúi 5 módulos: main.py, Escolha.py, Jogador.py,  Embarcacao.py, Partida.py, PosicionarFrota.py.

* main.py - Módulo principal, responsável por iniciar e finalizar o jogo e permite que o usuário escolha o modo de jogo, faz uso dos modulos Jogador.py, Escolha.py e Partida.py

  ![](https://raw.githubusercontent.com/HenriquePRA/Naval-Battle/screenshots/screenshots/img1.jpg)

* Escolha.py - Módulo que possúi apenas a função Escolha, a função escolha recebe uma variável booleana como argumento dependendo do
estado da variável a embarcação é escolhida automaticamente, caso não seja o caso é apresentado um menu interativo com o qual o usuário 
pode escolher a sua frota de embarcações, retorna um dicionário de dados contendo vetores que contem as embarcações escolhidas.

  ![](https://raw.githubusercontent.com/HenriquePRA/Naval-Battle/screenshots/screenshots/img2.jpg)
  
 * Jogador.py - Módulo que contem a classe Jogador, responsável por guardar a frota, numero de embarcoes, matrizes usadas durante o posicionamento e o jogo, string formada a partir da matriz do jogo, o tipo de jogador(player ou bot) e o nome do jogador.
 
 * Embarcacao.py - Módulo que contem a classe Embarcacao, responavel por armazenar o número de ataques recebidos por uma embarcação
 o maximo de ataques que uma embarcação pode receber dependendo do seu tipo, a quantidade de células do tabuleiro que a embarcação 
 ocupa, o seu tipo, se esta posicionada em um tabuleiro e as posiçoes que ocupa.
 
 * Partida.py - Módulo que contém a função responsável por dar andamento ao jogo em si, invoca variadas funções para dar andemento
 ao jogo.
 
    * Jogadas durante uma partida.
    
    ![](https://raw.githubusercontent.com/HenriquePRA/Naval-Battle/screenshots/screenshots/img3.jpg)
   
    * Finalização de uma partida.
    
    ![](https://raw.githubusercontent.com/HenriquePRA/Naval-Battle/screenshots/screenshots/img4.jpg)
   
 * PosicionarFrota.py - Módulo que contém funções responsáveis por posicionar a frota de um jogador em seus tabuleiro, apesar do seu
 objetivo ser simples sua criação foi a parte mais complexa do projeto tendo em vista as regras do jogo que são
 
    * As embarcações não devem estar em células adjacentes umas das outras
    * As embarcações devem estar posicionadas horizontalmente e verticalmente
    * Todas as embarcaçoes devem formar uma linha reta no tabuleiro
    
<a name="Status"></a>
## Status do Projeto :tada:
Finalizado :v:

<a name="Requisitos"></a>
## Requisitos Mínimos :computer:

1. Python 3.5 ou superior.

## Rodando o projeto :running:

1. Clone o repositório.
2. Execute o arquivo NavalBattle.py usando um interpretador python.
