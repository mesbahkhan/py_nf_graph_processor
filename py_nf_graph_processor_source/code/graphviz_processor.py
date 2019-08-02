from graphviz import Digraph


def generate_graph (Node):
    directedSameAsGraph = Digraph(comment='Same As Graph')


    for key, value in Node._registry.items():
        directedSameAsGraph.node(str(value.node_luid))
        for connectednode in value.connected_nodes:
            directedSameAsGraph.edge(str(value.node_luid), str(connectednode.node_luid))

    print (directedSameAsGraph)

    directedSameAsGraph.view()