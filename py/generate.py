import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from config import mappings, embedding_map


def get_node_sym(ln):
    for regex, sym in mappings.items():
        res = regex.findall(ln)
        if len(res) == 1:
            lbl = ln.split("[label")[0].strip()
            return lbl, sym
    return "-1", "U"


def get_path_emb(path, max_len):
    path_emb = list()
    for symbol in path:
        emb = embedding_map.get(symbol)
        path_emb.extend(emb)
    curr_len = len(path_emb)
    if curr_len >= max_len:
        max_len = curr_len
    return path_emb, max_len


def get_path_label(path):
    return 1


def get_training_data(gr):
    training_data = list()
    max_len = -np.inf
    for path in nx.all_simple_paths(gr, source='A', target='B'):
        path_emb, max_len = get_path_emb(path, max_len)
        training_data.append([path_emb, get_path_label(path)])
    for td in training_data:
        cur_len = len(td[0])
        td[0].extend([0 for _ in range(0, max_len - cur_len, 1)])
    return training_data


if __name__ == "__main__":
    G = nx.DiGraph()
    with open("sample.i", "r") as fd:
        lines = fd.readlines()
    label_symbol_map = dict()
    for line in lines:
        line = line.strip()
        if "label" in line:
            label, symbol = get_node_sym(line)
            label_symbol_map[label] = symbol
    edges = list()
    for line in lines:
        line = line.strip()
        if "->" in line:
            ln_sp = line.split("->")
            n1 = label_symbol_map.get(ln_sp[0].strip())
            n2 = label_symbol_map.get(ln_sp[1][:-1].strip())
            edges.append((n1, n2))
    G.add_edges_from(edges)
    train_data = get_training_data(G)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size=500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, arrows=True)
    plt.show()
    print("c")
