# DMISA - Differential Malatya Independent Set Algorithm

Este projeto implementa o algoritmo DMISA para encontrar um Conjunto Independente e uma Cobertura de Vértices em um grafo não direcionado.

## O que o código faz?

- Recebe como entrada um grafo (número de vértices, arestas e suas conexões).
- Calcula o Conjunto Independente máximo aproximado usando a heurística DMISA baseada na centralidade diferencial (DMCA).
- Retorna o conjunto independente (vértices que podem ser selecionados sem conflito) e a cobertura de vértices (vértices que cobrem todas as arestas restantes).

## Requisitos

- Python 3.x
- Biblioteca `networkx`

## Como instalar a biblioteca `networkx`

### No Windows

Abra o Prompt de Comando (ou terminal do VS code) e execute:

python -m pip install --upgrade pip

python -m pip install networkx

Se houver problemas de permissão, execute o Prompt de Comando como Administrador (botão direito > "Executar como administrador") e tente novamente.

### No Windows

python3 -m pip install --upgrade pip

python3 -m pip install networkx

Se estiver usando um ambiente virtual, ative-o antes de instalar.


## Exemplo de entrada

Digite o número de vértices:


7
Digite o número de arestas:

10

Digite as 10 arestas no formato u v:


0 3

2 3

3 1

3 4

3 6

1 4

4 6

1 5

4 5

6 5

Saida:

I (Conjunto Independente): [0, 1, 2, 6]

C (Cobertura de Vértices): [3, 4, 5]
