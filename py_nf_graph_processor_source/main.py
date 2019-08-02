from py_nf_graph_processor_source.code.nodes import convert_luid_to_node
from py_nf_graph_processor_source.code.nodes import Nodes
from py_nf_graph_processor_source.code.graphviz_processor import generate_graph
from collections import namedtuple


"""1. Populate Graph"""
"""a. read the data store to get a list of the edges (To be upgraded to link to ODBC datasources)"""

def process_edge_list():
    sameAsList = \
       [
            [1001, 1002],
            [1002, 1001],
            [1003, 1004],
            [1005, 1006],
            [1006, 1007],
            [1010, 1009],
            [1010, 1008]
        ]

    Edge = \
        namedtuple(
            'Edge',
            'righthandside lefthandside')  # create a named tuple to store the edge data

    edgelist = \
        []  # create a list to store the Edge namedtuples


    for edge in sameAsList:  # load the edgelist from sameAslist
        edgelist.append(Edge(edge[0], edge[1]))

    """b. specify a node object with a list of connected nodes"""

    """c. read the list of edges and populate the nodes and their lists - keeping a list of the nodes."""

    for edge in edgelist:  # iterate through the edgelist to extract the edges

        """" i. for each edge take the two nodes"""
        """" ii. and iii for each node check the Node registry for the node object and if it doesn't exist create it
        and add the other node to the node's connected node lit"""

        convert_luid_to_node(edge.lefthandside).addnodes(edge.righthandside)
        convert_luid_to_node(edge.righthandside).addnodes(edge.lefthandside)

    generate_graph(Nodes)

"""Render in a graph output object pdf"""

process_edge_list()

