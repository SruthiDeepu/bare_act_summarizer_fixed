from graphviz import Digraph

def generate_flowchart(summary):
    dot = Digraph()
    lines = summary.split("\n")
    for i, line in enumerate(lines):
        if line.strip():
            dot.node(f"{i}", line.strip())
            if i > 0:
                dot.edge(f"{i-1}", f"{i}")
    return dot.source
