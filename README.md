# Autômatos Finitos com Saída - Máquinas de Mely e de Moore
Este trabalho foi desenvolvido para a disciplina de Linguagens Formais e Autômatos, do Instituto Federal do Espírito Santo - IFES lecionada pelo Prof. Doutor Jefferson Oliveira Andrade como forma de requisito de avaliação.

### Autores
Hellesandro Gonzaga de Carvalho: [gonzH](https://github.com/gonzH)<br>
Luiz Antônio Roque Guzzo: [LuizGuzzo](https://github.com/LuizGuzzo)<br>

Vale lembrar que o código do arquivo 'sexp.py' que será visto adiante foi retirado do site [RosettaCode](http://rosettacode.org/wiki/S-Expressions#Python).

### Breve descrição do código fonte
O trabalho foi desenvolvido na linguagem Python dada experiência dos autores em manipulação de string.<br>
A organização do código foi pensada para ser simples de interpretar a execução do código, são basicamente 3 (três) arquivos:<br>
* 'main.py'<br>
    Responsável pela verificação de argumentos de entrada, identifição do tipo de máquina recebida, e chamada das funções do
    corpo do código.<br>
* 'func.py'<br>
    Aqui é onde a magia acontece, todas as funções de conversão, montagem, verificação, leitura e escrita de máquina de Mealy
    e Moore estão dispostas.<br>
    
    Mais adiante veremos um exemplo genérico do comportamento do programa, para facilitar o entendimento vamos brevemente des-
    crever as funções que compõem o arquivo 'func.py'.<br><br>
    
    * 'reading_file(nameFile)': Função de leitura da máquina de entrada, recebe como parâmetro o nome do arquivo a ser aberto.
    Faz a leitura do arquivo e entrega para a função de conversão de 'texto' para 'list' do arquivo de código 'sexp.py'.<br>
    
    * 'write_machine(machine_out, nameFile)': Função de escrita da máquina de saída, recebe como parâmetro o 'dicionário' da
    máquina de saída e o nome do arquivo a ser escrito. A função escreve no arquivo de acordo com a BNF <i>(Backus Naur Form)</i>
    definida na descrição do trabalho.<br>
    
    * 'check_conditions(machine_in)': Função de verificação das características da máquina, recebe como parâmetro o 'dicionário'
    contendo a máquina de entrada. São realizados testes para cada 'chave' visando garantir a estrutura básica da máquina, dado
    a formatação correta da máquina realizado pela função de conversão do arquivo de código 'sexp.py'.<br>
    
    
