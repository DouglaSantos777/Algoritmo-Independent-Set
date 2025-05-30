import networkx as nx

def dmc_centrality(G, vertices):
    dmc_values = {}
    for v in vertices:
        soma = 0.0
        dv = G.degree(v)
        for u in G.neighbors(v):
            du = G.degree(u)
            if du != 0:  # evitar divisão por zero (grau 0 não faz sentido em vizinhos, mas só pra garantir)
                soma += (dv - du) / du
        dmc_values[v] = soma
    return dmc_values

def vizinhos_ordem_n(G, v, ordem):
    visitados = set([v])
    fronteira = set([v])
    for _ in range(ordem):
        nova_fronteira = set()
        for u in fronteira:
            nova_fronteira.update(set(G.neighbors(u)) - visitados)
        visitados.update(nova_fronteira)
        fronteira = nova_fronteira
    visitados.remove(v)
    return visitados

def DMISA(G_original):
    G = G_original.copy()
    V = set(G.nodes())
    I = set()
    C = set()

    centralidade = dmc_centrality(G, V)

    while V:
        vmin = min(V, key=lambda v: centralidade.get(v, float('inf')))
        I.add(vmin)
        C.update(G.neighbors(vmin))

        viz2 = vizinhos_ordem_n(G, vmin, 2)
        viz3 = vizinhos_ordem_n(G, vmin, 3)
        Vi = viz2.union(viz3)

        centralidade.update(dmc_centrality(G, Vi))

        removidos = set([vmin]) | set(G.neighbors(vmin))
        V -= removidos
        G.remove_nodes_from(removidos)

    return I, C

if __name__ == "__main__":
    G_exemplo = nx.Graph()

    print("Digite o número de vértices:")
    n = int(input())

    print("Digite o número de arestas:")
    m = int(input())

    print(f"Digite as {m} arestas no formato u v:")
    for _ in range(m):
        u, v = map(int, input().split())
        G_exemplo.add_edge(u, v)

    I, C = DMISA(G_exemplo)
    print("\nResultado:")
    print("I (Conjunto Independente):", sorted(I))
    print("C (Cobertura de Vértices):", sorted(C))