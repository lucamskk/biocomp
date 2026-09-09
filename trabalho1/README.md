# Alinhamento de Sequências — Needleman-Wunsch e Smith-Waterman

Implementação em Python de dois algoritmos clássicos de alinhamento de
sequências biológicas, aplicados a sequências de hemoglobina (cadeia alfa)
de quatro espécies: *Homo sapiens*, *Chrysocyon brachyurus* (lobo-guará),
*Gallus gallus* (galinha) e *Oncorhynchus mykiss* (truta arco-íris).

## Conteúdo

| Arquivo | Descrição |
|---|---|
| `needleman_wunsch.py` | Alinhamento **global** — compara as sequências do início ao fim. |
| `smith_waterman.py` | Alinhamento **local** — encontra a sub-região de maior similaridade. |

## Requisitos

- Python 3.x (nenhuma biblioteca externa é necessária)

## Como executar

```bash
python3 needleman_wunsch.py
python3 smith_waterman.py
```

Cada script imprime no terminal os alinhamentos, as pontuações e, no caso do
Needleman-Wunsch, a porcentagem de identidade entre *Homo sapiens* e cada
uma das outras três espécies.

## `needleman_wunsch.py`

Implementa o algoritmo de Needleman-Wunsch (programação dinâmica) para
alinhamento global:

- `needleman_wunsch(seq_a, seq_b, match, mismatch, gap)` — constrói a matriz
  de pontuação e faz o traceback, retornando as duas sequências alinhadas
  (com gaps `-`) e a pontuação final.
- `porcentagem_identidade(align_a, align_b)` — calcula a % de posições
  idênticas em relação ao comprimento total do alinhamento.
- `imprimir_alinhamento(...)` — formata a saída em blocos de 60 colunas,
  com um marcador `|` indicando posições idênticas.

**Parâmetros de pontuação padrão:** match = `+1`, mismatch = `-1`, gap = `-2`.

### Resultado (resumo)

| Espécie comparada | Pontuação | Identidade |
|---|---|---|
| Chrysocyon brachyurus | 90 | 82,27% |
| Gallus gallus | 24 | 58,87% |
| Oncorhynchus mykiss | 14 | 55,94% |

## `smith_waterman.py`

Implementa o algoritmo de Smith-Waterman para alinhamento local. Principais
diferenças em relação ao Needleman-Wunsch: nenhuma célula da matriz pode ser
negativa (`F[i][j] = max(0, ...)`), e o traceback pode partir de qualquer
célula, terminando ao encontrar uma célula com valor 0.

- `smith_waterman_matrix(seq_a, seq_b, match, mismatch, gap)` — constrói a
  matriz de pontuação local.
- `traceback_local(F, seq_a, seq_b, start_i, start_j, ...)` — faz o
  traceback a partir de uma célula específica da matriz (usada tanto para
  encontrar o alinhamento ótimo quanto para o traceback a partir de uma
  posição arbitrária, como `F[4][5]`).
- `smith_waterman(seq_a, seq_b, ...)` — encontra automaticamente a célula de
  maior pontuação da matriz e retorna o alinhamento local ótimo.

### Resultado (resumo)

| Espécie comparada | Pontuação máxima (alinhamento local) |
|---|---|
| Chrysocyon brachyurus | 92 |
| Gallus gallus | 34 |
| Oncorhynchus mykiss | 25 |

## Conclusão

Ambos os algoritmos apontam o **lobo-guará (*Chrysocyon brachyurus*)** como
a espécie com maior similaridade à hemoglobina alfa humana, seguida da
galinha e, por último, da truta arco-íris — resultado consistente com a
proximidade filogenética entre mamíferos.
