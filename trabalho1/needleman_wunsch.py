#a) Algoritmo de needleman_wunsch

def needleman_wunsch(seq_a, seq_b, match=1, mismatch=-1,gap=-2):
    m, n = len(seq_a), len(seq_b)

    #matriz de pontuação
    F = [[0] * (n+1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(1, n + 1):
            score = match if seq_a[i-1] == seq_b[j-1] else mismatch
            diag = F[i-1][j-1] + score
            up = F[i-1][j] + gap
            left = F[i][j-1] + gap
            F[i][j] = max(diag, up, left)

    #traceback
    align_a, align_b = "", ""
    i, j = m, n
    while i > 0 and j > 0:
        score = match if seq_a[i-1] == seq_b[j-1] else mismatch
        if F[i][j] == F[i-1][j-1] + score:
            align_a = seq_a[i-1] + align_a
            align_b = seq_b[j-1] + align_b
            i -= 1
            j -= 1
        elif F[i][j] == F[i-1][j] + gap:
            align_a = seq_a[i-1] + align_a
            align_b = "-" + align_b
            i -= 1
        else:
            align_a = "-" + align_a
            align_b = seq_b[j-1] + align_b
            j -= 1

    #completa gaps que sobraram
    while i > 0:
        align_a = seq_a[i-1] + align_a
        align_b = "-" + align_b
        i -= 1
    while j > 0:
        align_a = "-" + align_a
        align_b = seq_b[j-1] + align_b
        j -= 1

    return align_a, align_b, F[m][n]

#c) calcula a porcentagem de identidade

def porcentagem_identidade(align_a, align_b):
    identicos = sum(1 for a, b in zip(align_a, align_b) if a == b and a != "-")
    return (identicos / len(align_a)) * 100

def imprimir_alinhamento(nome_a, nome_b, align_a, align_b, largura=60):
    marcador = "".join("|" if a == b and a != "-" else " "
                        for a, b in zip(align_a, align_b))
    for i in range(0, len(align_a), largura):
        print(f"{nome_a:<12}: {align_a[i:i+largura]}")
        print(f"{'':<12}  {marcador[i:i+largura]}")
        print(f"{nome_b:<12}: {align_b[i:i+largura]}\n")

        
    
#sequencias

sequencias = {
    "Homo sapiens": (
        "VLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHGKKVADALTNAVAHVDDMPNAL"
        "SALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTPAVHASLDKFLASVSTVLTSKY"
    ),
    "Chrysocyon brachyurus": (
        "VLSPADKTNIKSTWDKIGGHAGDYGGEALDRTFQSFPTTKTYFPHFDLSPGSAQVKAHGKKVADALTTAVAHLDDLPGAL"
        "SALSDLHAYKLRVDPVNFKLLSHCLLVTLACHHPTEFTPAVHASLDKFFTAVSTVLTSKYR"
    ),
    "Gallus gallus": (
        "MLTAEDKKLIQQAWEKAASHQEEFGAEALTRMFTTYPQTKTYFPHFDLSPGSDQVRGHGKKVLGALGNAVKNVDNLSQAM"
        "AELSNLHAYNLRVDPVNFKLLSQCIQVVLAVHMGKDYTPEVHAAFDKFLSAVSAVLAEKYR"
    ),
    "Oncorhynchus mykiss": (
        "XSLTAKDKSVVKAFWGKISGKADVVGAEALGRMLTAYPQTKTYFSHWADLSPGSGPVKKHGGIIMGAIGKAVGLMDDLVG"
        "GMSALSDLHAFKLRVDPGNFKILSHNILVTLAIHFPSDFTPEVHIAVDKFLAAVSAALADKYR"
    ),
}

# execuçao do main

if __name__ == "__main__":
    referencia = "Homo sapiens"
    seq_ref = sequencias[referencia]
 
    resultados = {}
 
    for especie, seq in sequencias.items():
        if especie == referencia:
            continue
 
        align_ref, align_esp, score = needleman_wunsch(seq_ref, seq)
        identidade = porcentagem_identidade(align_ref, align_esp)
        resultados[especie] = (score, identidade)
 
        print("=" * 70)
        print(f"{referencia} vs. {especie}")
        print("=" * 70)
        imprimir_alinhamento(referencia, especie, align_ref, align_esp)
        print(f"Pontuacao do alinhamento: {score}")
        print(f"Identidade de sequencia : {identidade:.2f}%\n")
 
    # d) Especie mais similar ao Homo sapiens
    especie_mais_similar = max(resultados, key=lambda k: resultados[k][1])
    print("=" * 70)
    print("RESUMO COMPARATIVO")
    print("=" * 70)
    for especie, (score, identidade) in resultados.items():
        print(f"{especie:<25} | Pontuacao: {score:>5} | Identidade: {identidade:6.2f}%")
 
    print(f"\nEspecie com maior similaridade ao Homo sapiens: "
          f"{especie_mais_similar} ({resultados[especie_mais_similar][1]:.2f}% de identidade)")
