"""1. Populate Graph"""

"""a. read the data store to get a list of the edges (To be upgraded to link to ODBC datasources)"""
from collections import namedtuple

sameAsList = [[1001, 1002], [1002, 1001], [1003, 1004], [1005, 1006], [1006, 1007], [1010, 1009], [1010, 1008]]

Edge = namedtuple('Edge', 'righthandside lefthandside')  # create a named tuple to store the edge data
edgelist = []  # create a list to store the Edge namedtuples

for edge in sameAsList:  # load the edgelist from sameAslist
    edgelist.append(Edge(edge[0], edge[1]))

"""b. specify a node object with a list of connected nodes"""


def convert_luid_to_node(node_luid_for_appending):
    if node_luid_for_appending in Node._registry:  # check nodes exists
        return Node._registry[node_luid_for_appending]  # return node if found
    else:
        return Node(node_luid_for_appending, [])  # retrun newly created node if not found


class Node(object):
    _registry = {}  # registry for keeping a list of nodes

    def __init__(self, node_luid, connected_nodes):
        self.node_luid = node_luid  # node property for storing the node id taken from the sameAsList luids
        self._registry.update({self.node_luid: self})  # node property for adding the node to the Node class registry
        self.connected_nodes = set()  # node property for storing the set of connected node objects

    def addnodes(self, node_luid_for_appending):  # adds a node and node luid to the nodes connected nodes list
        node_for_appending = convert_luid_to_node(node_luid_for_appending)  # retreive node using luid
        self.connected_nodes.add(node_for_appending)  # add node to connected node set


"""c. read the list of edges and populate the nodes and their lists - keeping a list of the nodes."""

for edge in edgelist:  # iterate through the edgelist to extract the edges

    """" i. for each edge take the two nodes"""
    """" ii. and iii for each node check the Node registry for the node object and if it doesn't exist create it
    and add the other node to the node's connected node lit"""

    convert_luid_to_node(edge.lefthandside).addnodes(edge.righthandside)
    convert_luid_to_node(edge.righthandside).addnodes(edge.lefthandside)

"""Render in a graph output object pdf"""

from graphviz import Digraph

directedSameAsGraph = Digraph(comment='Same As Graph')

for key, value in Node._registry.items():
    directedSameAsGraph.node(str(value.node_luid))
    for connectednode in value.connected_nodes:
        directedSameAsGraph.edge(str(value.node_luid), str(connectednode.node_luid))

print (directedSameAsGraph)

directedSameAsGraph.view()