#a) algoritmo de smith-waterman
def smith_waterman_matrix(seq_a, seq_b, match=1, mismatch=-1, gap=-2):
    m, n = len(seq_a), len(seq_b)
    F = [[0] * (n + 1) for _ in range(m + 1)]
 
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            s = match if seq_a[i - 1] == seq_b[j - 1] else mismatch
            diagonal = F[i - 1][j - 1] + s
            cima = F[i - 1][j] + gap
            esquerda = F[i][j - 1] + gap
            F[i][j] = max(0, diagonal, cima, esquerda)
 
    return F

def traceback_local(F, seq_a, seq_b, start_i, start_j, match=1, mismatch=-1, gap=-2):
    align_a, align_b = "", ""
    i, j = start_i, start_j
    caminho = [(i, j)]
 
    while i > 0 and j > 0 and F[i][j] != 0:
        atual = F[i][j]
        s = match if seq_a[i - 1] == seq_b[j - 1] else mismatch
 
        if atual == F[i - 1][j - 1] + s:
            align_a = seq_a[i - 1] + align_a
            align_b = seq_b[j - 1] + align_b
            i -= 1
            j -= 1
        elif atual == F[i - 1][j] + gap:
            align_a = seq_a[i - 1] + align_a
            align_b = "-" + align_b
            i -= 1
        elif atual == F[i][j - 1] + gap:
            align_a = "-" + align_a
            align_b = seq_b[j - 1] + align_b
            j -= 1
        else:
            break
 
        caminho.append((i, j))
 
    return align_a, align_b, caminho


def smith_waterman(seq_a, seq_b, match=1, mismatch=-1, gap=-2):
    F = smith_waterman_matrix(seq_a, seq_b, match, mismatch, gap)
 
    max_score = 0
    i_max = j_max = 0
    for i in range(len(F)):
        for j in range(len(F[0])):
            if F[i][j] > max_score:
                max_score = F[i][j]
                i_max, j_max = i, j
 
    align_a, align_b, _ = traceback_local(
        F, seq_a, seq_b, i_max, j_max, match, mismatch, gap
    )
 
    return align_a, align_b, max_score, (i_max, j_max), F

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

#b) subsequencia de maior pontuacao pra cada par
if __name__ == "__main__":
    referencia = "Homo sapiens"
    seq_ref = sequencias[referencia]
 
    matrizes = {} 
 
    print("#" * 70)
    print("Alinhamento local otimo (maior pontuacao) de cada par")
    print("#" * 70)
 
    for especie, seq in sequencias.items():
        if especie == referencia:
            continue
 
        align_ref, align_esp, score, pos_max, F = smith_waterman(seq_ref, seq)
        matrizes[especie] = F
 
        print(f"\n{referencia} vs. {especie}")
        print("-" * 70)
        print(f"Pontuacao maxima        : {score}")
        print(f"Posicao na matriz (i,j) : {pos_max}")
        print(f"Sub-sequencia ({referencia}) : {align_ref}")
        print(f"Sub-sequencia ({especie}) : {align_esp}")

#c) traceback a partir do F[4][5]
    print("\n" + "#" * 70)
    print("Traceback a partir da celula F[4][5] da matriz")
    print("#" * 70)
 
    LINHA, COLUNA = 4, 5  # F[4][5]
 
    for especie, seq in sequencias.items():
        if especie == referencia:
            continue
 
        F = matrizes[especie]
        valor_celula = F[LINHA][COLUNA]
 
        align_ref, align_esp, caminho = traceback_local(
            F, seq_ref, seq, LINHA, COLUNA
        )
 
        print(f"\n{referencia} vs. {especie}")
        print("-" * 70)
        print(f"Valor de F[{LINHA}][{COLUNA}]      : {valor_celula}")
        if align_ref == "" and align_esp == "":
            print("Traceback nao produz alinhamento: F[4][5] = 0 "
                  "(nao ha alinhamento local terminando nessa celula).")
        else:
            print(f"Alinhamento local ({referencia}) : {align_ref}")
            print(f"Alinhamento local ({especie}) : {align_esp}")
