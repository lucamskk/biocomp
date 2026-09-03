def needleman_wunsch(seq_a, seq_b, match=1, mismatch=-1,gap=2):
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

    #completa oq sobrou
    while i > 0:
        align_a = seq_a[i-1] + align_a
        align_b = "-" + align_b
        i -= 1
    while j > 0:
        align_a = "-" + align_a
        align_b = seq_b[j-1] + align_b
        j -= 1

    return align_a, align_b, F[m][n]