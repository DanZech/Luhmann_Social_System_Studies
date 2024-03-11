import matplotlib.pyplot as plt
import networkx as nx

def draw_autopoiesis_systems_graph():
    # Criar um grafo direcionado
    G = nx.DiGraph()

    # Sistemas e seus códigos binários
    systems_codes = {
        "Legal": "legal/ilegal",
        "Econômico": "pagamento/não pagamento",
        "Político": "poder/não poder",
        "Científico": "verdadeiro/falso",
        "Educacional": "aprovado/reprovado",
        "Religioso": "sagrado/profano",
        "Arte": "belo/feio",
        "Saúde": "saudável/doente"
    }

    # Adicionar sistemas como nós no grafo
    for system, code in systems_codes.items():
        G.add_node(system, label=f"{system}\n({code})")

    # Relações entre sistemas (exemplos)
    relations = [
        ("Político", "Legal"), ("Político", "Econômico"), ("Político", "Científico"),
        ("Político", "Educacional"), ("Político", "Religioso"), ("Político", "Arte"),
        ("Político", "Saúde"), ("Econômico", "Saúde"), ("Legal", "Econômico"),
        ("Científico", "Educacional"), ("Educacional", "Saúde")
    ]
    G.add_edges_from(relations)

    # Layout circular para enfatizar a autopoiese
    pos = nx.circular_layout(G)

    # Desenhar os nós com seus rótulos
    nx.draw(G, pos, with_labels=False, node_size=4000, node_color='lightblue', edge_color='gray')
    labels = nx.get_node_attributes(G, 'label')
    nx.draw_networkx_labels(G, pos, labels, font_size=12)

    # Desenhar arestas indicando interações
    nx.draw_networkx_edges(G, pos, edgelist=relations, edge_color='gray', arrows=True)

    # Adicionar loops para simbolizar a autopoiese
    for system in systems_codes.keys():
        G.add_edge(system, system)
        nx.draw_networkx_edges(G, pos, edgelist=[(system, system)], edge_color='red', arrows=False)
        plt.gca().add_patch(plt.Circle(pos[system], 0.15, color='red', fill=False))

    plt.axis('off')
    plt.show()

draw_autopoiesis_systems_graph()