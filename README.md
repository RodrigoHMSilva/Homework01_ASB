Trabalho realizado por 
Daniela Deodato 202000199;
Ioana Chichirita 202000180;
Jorge Santos 202000171;
Rodrigo Silva 202000193;
no âmbito da Unidade Curricular Análise de Sequências Biológicas 



Este ficheiro descreve como utilizar e o que faz o programa


Primeiro, a utilização.
Para a utilização do programa é necessário, no terminal, escrever "python3 Hw1.py "email" "database" "term", onde o email será o email do utilizador, o database é que tipo de base de dados que quer (ex.: nucleotide, protein) e o term é o organismo que pretende ver as sequências (ex.: "Psammodromus algirus[org] AND cytb[gene]")



Agora a função do programa.
Este script dá origem a um programa com 2 funções. A primeira recebe os termos passados no terminal e procura por esses termos. Seguidamente, guarda-os em 2 variáveis (queryKey e webEnv) que vai ser retornados no fim da função. A segunda, com ajuda das variáveis, procura as sequências do organismo desejado e devolve-as em formato FASTA. Os resultados são apresentados no terminal.
