def get_node(line):
    node_lines = [node_line.strip() for node_line in line.split(r"\l")][1:-1]
    print("c")


def get_edge():
    pass


def get_graph(lines):
    for line in lines:
        if "->" in line:
            get_edge()
        else:
            get_node(line)


if __name__ == '__main__':
    with open("app.dot", "r") as fd:
        init_lines = fd.readlines()
    ext_lines = list()
    for init_line in init_lines:
        if init_line.startswith("	Node"):
            ext_lines.append(init_line)
    ext_lines.reverse()
    get_graph(ext_lines)
    print("c")
