# Trabalho 1 para cadeira de Biologia computacional

## Sequências
> Humano (Homo sapiens) [TaxId: 9606]
> 2DN3:A|PDBID|CHAIN|SEQUENCE
> VLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHGKKVADALTNAVAHVDDMPNALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTPAVHASLDKFLASVSTVLTSKY

> Lobo-Guará (Chrysocyon brachyurus) [TaxId: 68728]
> 1FHJ:A|PDBID|CHAIN|SEQUENCE
> VLSPADKTNIKSTWDKIGGHAGDYGGEALDRTFQSFPTTKTYFPHFDLSPGSAQVKAHGKKVADALTTAVAHLDDLPGALSALSDLHAYKLRVDPVNFKLLSHCLLVTLACHHPTEFTPAVHASLDKFFTAVSTVLTSKYR

> Galinha (Gallus gallus) [TaxId: 9031]
> 1HBR:A|PDBID|CHAIN|SEQUENCE
> MLTAEDKKLIQQAWEKAASHQEEFGAEALTRMFTTYPQTKTYFPHFDLSPGSDQVRGHGKKVLGALGNAVKNVDNLSQAMAELSNLHAYNLRVDPVNFKLLSQCIQVVLAVHMGKDYTPEVHAAFDKFLSAVSAVLAEKYR

> Truta Arco-Íris (Oncorhynchus mykiss) [TaxId: 8022]

> 1OUT:A|PDBID|CHAIN|SEQUENCE
> XSLTAKDKSVVKAFWGKISGKADVVGAEALGRMLTAYPQTKTYFSHWADLSPGSGPVKKHGGIIMGAIGKAVGLMDDLVGGMSALSDLHAFKLRVDPGNFKILSHNILVTLAIHFPSDFTPEVHIAVDKFLAAVSAALADKYR

Questão 1.

a) Desenvolva um programa que implemente o algoritmo de Needleman-Wunsch. A implementação deve incluir a criação da matriz de pontuação e a função de traceback para reconstruir o alinhamento.

b) Utilize a função de alinhamento para processar os seguintes pares de sequências:

    Homo Sapiens vs. Chrysocyon brachyurus
    Homo Sapiens vs. Gallus gallus
    Homo Sapiens vs. Oncorhynchus mykiss

Para cada par, imprima o alinhamento global resultante e a pontuação final obtida.

c) Calcule a porcentagem de identidade de sequências para cada um dos pares acima 

d) Baseado nos resultados, identifique qual espécie apresenta a maior similaridade com a sequência Homo Sapiens.
Questão 2

a) Implemente o algoritmo de Smith-Waterman para alinhamento local. Sua implementação deve incluir a criação da matriz de pontuação e a função de traceback.
b) Identifique e extraia a sub-sequência com a maior pontuação para cada par:

    Homo Sapiens vs. Chrysocyon brachyurus
    Homo Sapiens vs. Gallus gallus
    Homo Sapiens vs. Oncorhynchus mykiss

Qual é o valor dessa pontuação e qual é a sub-sequência correspondente?

c) Realize o traceback a partir da célula na linha 4 e coluna 5 da matriz de pontuação. Quais os alinhamento local obtidos para cada par avaliado?

Orientações para Entrega 

Para a sua avaliação, você deverá enviar os seguintes arquivos:

    Código-Fonte: Um arquivo compactado (.zip ou .rar) contendo todos os arquivos de código do seu programa. Certifique-se de que o código está completo e funcional, conforme as instruções da atividade. Inclua arquivo readme.txt com instruções de uso do código desenvolvido.

    Relatório em PDF: Um arquivo em formato PDF contendo as respostas detalhadas para as questões propostas.
