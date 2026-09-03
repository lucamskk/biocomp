def needleman_wunsch(seq_a, seq_b, match=1, mismatch=-1,gap=2):
    m, n = len(seq_a), len(seq_b)

    #matriz de pontuação
    F = [[0] * (n+1) for _ in range(m + 1)]