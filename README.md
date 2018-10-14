# Autômatos Finitos com Saída<br>Máquinas de Mealy e de Moore
Este trabalho foi desenvolvido para a disciplina de Linguagens Formais e Autômatos, do Instituto Federal do Espírito Santo - IFES lecionada pelo Prof. Doutor Jefferson Oliveira Andrade como forma de requisito de avaliação.
<br><br>
### Autores
Hellesandro Gonzaga de Carvalho: [gonzH](https://github.com/gonzH)<br>
Luiz Antônio Roque Guzzo: [LuizGuzzo](https://github.com/LuizGuzzo)<br>

Vale lembrar que o código do arquivo 'sexp.py' que será visto adiante foi retirado do site [RosettaCode](http://rosettacode.org/wiki/S-Expressions#Python), onde não encontramos autor para creditar.
<br><br>
### Breve descrição do código fonte
O trabalho foi desenvolvido na linguagem Python dada experiência dos autores em manipulação de string.<br>
A organização do código foi pensada para ser simples de interpretar a execução do código, são basicamente 3 (três) arquivos:<br>
* `main.py`<br>
    Responsável pela verificação de argumentos de entrada, identifição do tipo de máquina recebida, e chamada das funções do
    corpo do código.<br>
* `func.py`<br>
    Aqui é onde a magia acontece, todas as funções de conversão, montagem, verificação, leitura e escrita de máquina de Mealy
    e Moore estão dispostas.<br>
    
    Mais adiante veremos um exemplo genérico do comportamento do programa, para facilitar o entendimento vamos brevemente des-
    crever as funções que compõem o arquivo `func.py`.<br><br>
    
    * `reading_file(nameFile)`: Função de leitura da máquina de entrada, recebe como parâmetro o nome do arquivo a ser aberto.
    Faz a leitura do arquivo e entrega para a função de conversão de `texto` para `lista` do arquivo de código `sexp.py`.<br>
    
    * `write_machine(machine_out, nameFile)`: Função de escrita da máquina de saída, recebe como parâmetro o `dicionário` da
    máquina de saída e o nome do arquivo a ser escrito. A função escreve no arquivo de acordo com a BNF <i>(Backus Naur
    Form)</i> definida na descrição do trabalho.<br>
    
    * `check_conditions(machine_in)`: Função de verificação das características da máquina, recebe como parâmetro o `dicionário`
    contendo a máquina de entrada. São realizados testes para cada `chave` visando garantir a estrutura básica da máquina, dado
    a formatação correta da máquina realizado pela função de conversão do arquivo de código `sexp.py`.<br>
    
    * `moore_machine(sexpList)`: Função de construção da máquina de <i>Moore</i> em `dicionário` a partir da `lista` que repre-
    senta a máquina em <i>S-Expression</i>, este é parâmetro de entrada. Organiza a `lista` em um `dicionário` que representa
    uma máquina de <i>Moore</i>.<br>
    
    * `mealy_machine(sexpList)`: Função de construção da máquina de <i>Mealy</i> em `dicionário` a partir da `lista` que repre-
    senta a máquina em <i>S-Expression</i>, este é o parâmetro de entrada. Organiza a `lista` em `dicionário` que representa 
    uma máquina de <i>Mealy</i>.<br>
    
    * `moore_to_mealy(machine_in)`: Função de conversão de máquina de <i>Moore</i> para <i>Mealy</i>, recebe como parâmetro um
    `dicionário` representando a máquina de <i>Moore</i>. A função consiste em transformar um `dicionário` contendo a máquina de
    <i>Moore</i> em um novo `dicionário` contendo uma máquina de <i>Mealy</i> equivalente. A lógica se baseia na verificação dos
    `valores` das `chaves` do `dicionário` de entrada e representação desses dados em um novo `dicionário` de acordo com a
    estrutura de <i>Mealy</i>.<br>
    
    * `mealy_to_moore(machine_in)`: Função de conversão de máquina de <i>Mealy</i> para <i>Moore</i>, recebe como parâmetro um
    `dicionário` representando a máquina de <i>Mealy</i>. A função consiste em transformar um `dicionário` contendo a máquina de
    <i>Mealy</i> em um novo `dicionário` contendo uma máquina de <i>Moore</i> equivalente. A lógica se baseia na verificação dos
    `valores` das `chaves` do `dicionário` de entrada e representação desses dados em um novo `dicionário` de acordo com a
    estrutura de <i>Moore</i>.<br><br>
    
* `sexp.py`<br>
    Esse arquivo, conforme sugerido na descrição do trabalho para visualização de exemplo, optamos por utilizá-lo na conversão
    de arquivo de texto de entrada em uma lista, esta que é a única função (`print_sexp`) declarada no arquivo de código além da
    função de impressão.<br><br>
    
### Comportamento do programa
O comportamento do programa durante a execução é bastante simples. <br>
Dada a entrada dos dados, a seguinte sequência é esperada:<br><br>

* Moore: <br>
`reading_file(nameFile)` -> `moore_machine(sexpList)` -> `check_conditions(machine_in)` -> `moore_to_mealy(machine_in)` -> `write_machine(machine_out, nameFile)`<br>
* Mealy: <br>
`reading_file(nameFile)` -> `mealy_machine(sexpList)` -> `check_conditions(machine_in)` -> `mealy_to_moore(machine_in)` -> `write_machine(machine_out, nameFile)`<br><br>

### Nome e Modo de uso do programa
Os nomes já foram introduzidos na seção de descrição do código fonte.<br>
O código foi desenvolvido para o ambiente Linux, dessa forma a descrição da execução atende esse propósito apenas.<br>
Tendo todos os arquivos na pasta, informe o caminho para o terminal e execute o comando:<br>
```
python3 main.py -i arquivoEntrada.txt -o arquivoSaida.txt
```
>ATENÇÃO: O código rejeita qualquer comando de entrada com a quantidade de argumentos diferente de 5

<br>

### Informações adicionais
São consideradas válidas entradas de máquinas de <i>Mealy</i> e <i>Moore</i> as entradas seguindo as respectivas estruturas em
<i>S-Expression</i>: <br>

* Mealy: <br>
```
(mealy
( symbols-in a b)
( symbols-out 0 1)
( states q0 q1 q2 q3 )
( start q0 )
( finals q3 )
( trans
( q0 q1 a 0) ( q0 q3 b 0) ( q1 q2 b 1) ( q1 q3 a 1)
( q2 q3 a 0) ( q2 q3 b 1) ( q3 q0 b 1) ( q3 q3 a 1 ) ) )
```
* Moore: <br>
```
(moore
( symbols-in a b)
( symbols-out 0 1)
( states q0 q0 ' q1 q2 q3 q3 ' )
( start q0 )
( finals q3 q3 ' )
( trans
( q0 q1 a ) ( q0 q3 b) ( q1 q3 ' a ) ( q1 q2 b)
( q2 q0 ' a ) ( q2 q3 ' b) ( q3 q3 ' a ) ( q3 q0 ' b)
( q3 ' q3 ' a ) ( q3 ' q0 ' b ) )
( out-fn
( q0 ( ) ) ( q0 ' 1) ( q1 0)
( q2 1) ( q3 0) ( q3 ' 1 ) ) )
```
