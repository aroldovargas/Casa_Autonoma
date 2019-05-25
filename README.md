# Casa_Autonoma

## 1.0 Equipe

Integrantes do grupo:<br><br>
Aroldo Vargas: aroldovneto@gmail.com<br>
Lorran Gabriel Araújo: lorrangabriel20@gmail.com<br>

## 1.1 Objetivos¹

Objetivo geral do trabalho é desenvolver uma aplicação cliente/servidor utilizando a biblioteca de programação socket na linguagem Python, versão 3.5. Os objetivos específicos do trabalho são:<br>
◦ Familiarizar-se com a programação utilizando a API socket.<br>
◦ Implementar um protocolo controlar um ambiente de dispositivos inteligentes para residências (smart home devices).<br>
◦ Enviar e receber dados em uma aplicação que utiliza a arquitetura Cliente/Servidor.<br>

## 2.0 Preparando Espaço<br>
### 2.1 Instalação Python²

Ubuntu Debian e derivados<br>
>sudo apt-get update<br>
>sudo apt-get install python3.5<br>

Windows<br>

Veja mais Pagina Oficial <br>


### 2.2 Baixar Repositorio <br>

Ubuntu e Windows<br>
Pode ser baixando o arquivo compactado pelo link<br>
Ou utilizando uma ferramenta do git através do terminal<br>
>git clone https://github.com/LorranGabriel/Casa_Autonoma<br>

## 3.0 Descrição do Projeto

### 3.1 Plano de Projeto<br>

O trabalho propõe o desafio de implementar um protocolo de gerenciamento de dispositivos residenciais, com características conceituais de IoT (internet of things), onde o usuário (residente) tem acesso às informações em tempo real, além de interagir com o sistema, fazendo solicitações que serão explanadas em tópicos posteriores.<br>
Ao iniciar o projeto tivemos a ideia de implementar uma interface gráfica para a visualização da simulação, ela está parcialmente terminada e é possível encontrar passo a passo em nosso repositório. Ideia que tivemos pensando em projetos posteriores que utilizassem a mesma arquitetura, e estudo próprio para capacitação da equipe. Para a implementação está sendo feita utilizando uma biblioteca para python chamada kivy, que fornece ferramentas muito práticas e rápidas para a construção de uma interface gráfica interativa com o usuário.
<br>
### 3.2 Execução<br>
O projeto está dividido em dois processos denominados iniciação e operação. Nos topicos a seguir estão sendo explicadas a forma que os dados estão sendo estruturados.<br>

##### Iniciação<br>

O processo de iniciação, é o processo onde se iniciam os dispositivos e suas localizações. Esse início se dá pela troca de mensagens entre o cliente do dispositivo a ser iniciado e o servidor. Os passos para o processo são:<br>

Obs: Para iniciar um cliente o servidor precisa ter sido iniciado posteriormente<br><br>

	Passo 1. Primeiramente abra o seu terminal ou cmd no diretório da pasta do projeto.<br>

	Passo 2. Executar<br>

Existe na pasta um executável python para iniciar o servidor e 1 cliente de cada tipo simultaneamente, executando a seguinte instrução em seu terminal:<br>
	
>python3 Iniciar.py <br><br>


Para a execução individual de servidor e clientes, serão necessárias as seguintes linhas:<br>

<br>
Servidor: <br>

>python3 server.py<br>
<br>

Cliente para Ar Condicionados:<br>

>python3 consoleAC.py<br>
<br>

Cliente para Lampadas:<br>

>python3 consoleLA.py<br>

<br>
Cliente para Tomadas:<br>

>python3 consoleTM.py<br><br>
 
Cliente para Sensores de Presença:<br>

>python3 consoleSP.py<br><br>


Cliente para Temperatura:<br>

>python3 consoleTR.py<br><br>



	Passo 3. Comunicação cliente servidor.


1.  Cliente se conecta ao servidor e pergunta ao usuário se deseja adicionar dispositivo

2.  Servidor pergunta ao usuário o cômodo onde será inserido

3.  Se Cliente necesita enviar mais informações pergunta ao usuário e envia ao servidor

4.  Se Fim da inserção, cliente começa a emitir relatorios.

	Obs: Para a inicialização de um novo cliente é necessario executar um novo terminal.
 
Após a inicialização de cada cliente de controle de um dispositivo do tipo TM (Tomada),TR (Termometro) ou SP (Sensor de presença), o servidor começa a receber feedbacks de relatórios e toma decisões relacionadas aos demais clientes AR e LA (Ar condicionado e Lampada) e como isso acontece será explanado no processo de Operação.
Após a execução dos componentes a arquitetura fica como o diagrama representado na Figura 1, onde o servidor recebe informações captadas pelos clientes e também envia de acordo com as solicitações.
    Figura 1. - Arquitetura Cliente Servidor (autoria própria da Equipe)



Para conexão simultanea de clientes ao servidor para o envio de feedbacks, estamos utilizando a biblioteca _threads do python. Um codigo-fonte para consulta foi disponibilizado pelo professor.



Operação

O processo de operação ocorre quando se termina de adicionar dispositivos através dos clientes, é onde se inicia a simulação.
Para a solução do desafio proposto, unimos os dispositivos em duplas para melhorar o entendimento e facilitar a manipulação de dispositivos dependentes, estão organizados como no diagrama representado na Figura 2:

	

	
             Figura 2. - Arquitetura da simulação (autoria própria da Equipe)

Para o controle de lampadas acesas na casa, o sensor de presença envia uma verificação para o servidor, se o mesmo alterou seu valor sinalizando que não há ninguem em seu ambiente locado. Se o sinal é recebido o servidor acessa o cliente da lampada alocada no mesmo ambiente do sensor e inicia um cronometro de 10 minutos para o desligamento da lampada. A simulação não utiliza cronômetro fictício, ou seja, 1 minuto na simulação é 1 minuto real.
A operação do servidor também tem como função o acionamento de ar condicionados, que são requisitados a partir do feedback dos termometros alocados nos ambientes, que se  marcarem temperatura maior que 28° em relatorio ao servidor, o mesmo aciona os clientes de numero (ID) do ar alocado no ambiente ligado na temperatura de 22°. Os cliente de ar condicionado são acionados pelo servidor ás 18:00h por definição. 




O relatório gerado é escrito em um arquivo “Registro.txt” localizado na pasta do programa e exibido no console do servidor simultaneamente com a simulação.


4.0 Referencias
¹..Trabalho 1 – Programação socket
²..Site Oficial Python
³..Documentação Oficial da biblioteca de Socket



