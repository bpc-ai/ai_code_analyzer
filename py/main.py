import re
import networkx as nx
from config import regex_map
import matplotlib.pyplot as plt


def check_entry_exit_node(line):
    if "ENTRY" in line:
        return ["ENT"]
    elif "EXIT" in line:
        return ["EXT"]
    else:
        return None


def get_nodes(line, i):
    sub_nodes = list()
    node_name = line.split(" ")[0].strip()
    ret = check_entry_exit_node(line)
    if not ret:
        node_lines = [node_line.strip() for node_line in line.split(r"\l")][1:-1]
        for node_line in node_lines:
            node_line = node_line.replace("\\", "")
            for sym, regex in regex_map.items():
                if re.findall(regex, node_line):
                    sub_nodes.append(f"{sym}_{i}")
        return node_name, sub_nodes
    else:
        return node_name, ret


def expand_node(node):
    edges = list()
    if len(node) > 1:
        for i in range(0, len(node) - 1, 1):
            edges.append((node[i], node[i + 1]))
        return [edges[0][0], edges, edges[-1][1]]
    else:
        return [node[0], node[0], node[0]]


def get_edge(line, node_groups):
    edges = list()
    line_sp = line.split("->")
    n1 = line_sp[0].strip()
    n2 = line_sp[1].strip()[:-1]
    node1 = node_groups.get(n1)
    start1, es1, end1 = expand_node(node1)
    node2 = node_groups.get(n2)
    start2, es2, end2 = expand_node(node2)
    if isinstance(es1, list):
        edges.extend(es1)
        edges.append((end1, start2))
    else:
        edges.append((start1, start2))
    if isinstance(es2, list):
        edges.extend(es2)
    return edges


def get_graph(lines):
    node_groups = dict()
    node_count = 0
    for line in lines:
        if "->" not in line:
            key, val = get_nodes(line, node_count)
            node_groups[key] = val
            node_count += 1
    edges = list()
    for line in lines:
        if "->" in line:
            es = get_edge(line, node_groups)
            for e in es:
                if e not in edges:
                    edges.append(e)
    G = nx.DiGraph()
    G.add_edges_from(edges)
    return G


def draw_graph(G):
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size=500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, arrows=True)
    plt.show()


if __name__ == '__main__':
    with open("app.dot", "r") as fd:
        init_lines = fd.readlines()
    ext_lines = list()
    for init_line in init_lines:
        if init_line.startswith("	Node"):
            ext_lines.append(init_line)
    ext_lines.reverse()
    G = get_graph(ext_lines)
    draw_graph(G)
    print("c")
