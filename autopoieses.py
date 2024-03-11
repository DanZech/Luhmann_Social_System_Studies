import matplotlib.pyplot as plt
import networkx as nx

def create_graph():
    G = nx.DiGraph()

    # Definição dos sistemas e suas conexões básicas
    systems = ["Legal", "Econômico", "Político", "Científico", "Educacional", "Religioso", "Arte", "Saúde"]
    connections = [
        ("Político", "Legal"), ("Político", "Econômico"), ("Científico", "Educacional"),
        ("Saúde", "Econômico"), ("Educacional", "Político")
    ]

    for system in systems:
        G.add_node(system)
    G.add_edges_from(connections)

    return G

def draw_graph(G, highlight=None):
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42)

    # Desenha todos os nós e arestas com uma configuração padrão
    nx.draw_networkx_nodes(G, pos, node_size=5000, node_color="lightblue", alpha=0.6)
    nx.draw_networkx_edges(G, pos, edge_color="gray")
    nx.draw_networkx_labels(G, pos)

    # Se um sistema for selecionado, destaca-o
    if highlight:
        nx.draw_networkx_nodes(G, pos, nodelist=[highlight], node_size=5000, node_color="orange", alpha=0.9)
        nx.draw_networkx_edges(G, pos, edgelist=G.edges(highlight), edge_color="red", width=2)

    plt.title("Teoria dos Sistemas de Luhmann")
    plt.axis('off')
    plt.show()

def system_explanation(system):
    explanations = {
        "Legal": "O sistema legal regula as normas e leis da sociedade, baseando-se no código binário legal/ilegal.",
        "Econômico": "O sistema econômico lida com transações e recursos, operando no código pagamento/não pagamento.",
        # Adicionar explicações para outros sistemas conforme necessário
    }
    return explanations.get(system, "Explicação não disponível.")

def main():
    G = create_graph()

    print("Sistemas disponíveis: Legal, Econômico, Político, Científico, Educacional, Religioso, Arte, Saúde")
    system = input("Escolha um sistema para aprender mais sobre ele: ")

    draw_graph(G, highlight=system)
    print(system_explanation(system))

if __name__ == "__main__":
    main()