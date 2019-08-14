from py_nf_graph_processor_code.graph_processing_service.nodes import convert_luid_to_node
from py_nf_graph_processor_code.graph_processing_service.nodes import Nodes
from py_nf_graph_processor_code.graph_processing_service.graph_processor import generate_graph
from collections import namedtuple

"""1. Populate Graph"""
"""a. read the data store to get a list of the edges (To be upgraded to link to ODBC datasources)"""

def process_edge_list(sameAsList):

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

        convert_luid_to_node(
            edge.lefthandside).\
                    add_nodes(
                        edge.righthandside)

        convert_luid_to_node(
            edge.righthandside).\
                add_nodes(edge.lefthandside)

    return (Nodes)


"""Render in a graph output object pdf"""