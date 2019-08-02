

class Nodes(object):
    _registry = {}  # registry for keeping a list of nodes

    def __init__(self, node_luid, connected_nodes):
        self.node_luid = node_luid  # node property for storing the node id taken from the sameAsList luids
        self._registry.update({self.node_luid: self})  # node property for adding the node to the Node class registry
        self.connected_nodes = set()  # node property for storing the set of connected node objects

    def addnodes(self, node_luid_for_appending):  # adds a node and node luid to the nodes connected nodes list
        node_for_appending = convert_luid_to_node(node_luid_for_appending)  # retreive node using luid
        self.connected_nodes.add(node_for_appending)  # add node to connected node set



def convert_luid_to_node(node_luid_for_appending):
    if node_luid_for_appending in Nodes._registry:  # check nodes exists
        return Nodes._registry[node_luid_for_appending]  # return node if found
    else:
        return Nodes(node_luid_for_appending, [])  # retrun newly created node if not found