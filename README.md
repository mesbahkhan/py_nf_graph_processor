# graph processor

# same as processing

Populate Graph

* read the data store to get a list of the edges.
* specify a node object with a list of connected nodes.
* read the list of edges and populate the nodes and their lists - keeping a list of the nodes.
  * for each edge, take the two node LUIDs
    * for each node LUID - get the node object
      * If the node does not exist - create it
For each node object
add the other node object to the list of connected nodes
Calculate connected components
pick a node at random and collect all the connected nodes
make this list/set an equivalence class - store this somehow
pick a node not in any of the equivalence classes and repeat.
