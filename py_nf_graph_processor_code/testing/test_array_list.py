from py_nf_graph_processor_code.edge_list_processor import process_edge_list
from py_nf_graph_processor_code.graph_processing_service.graph_processor import generate_graph



def test_graph_processor(list:list):

    Nodes = \
        process_edge_list(
            list)

    generate_graph(
        Nodes)

list = \
    [
        [1001, 1002],
        [1002, 1001],
        [1003, 1004],
        [1005, 1006],
        [1006, 1007],
        [1010, 1009],
        [1010, 1008],
        [1001, 1008],
        [1008, 1006],
        [1007, 1004],
        [1003, 1002],
        [1009, 1002],
        [1007, 1008],
        [1009,1004],
        [1008,1003]
    ]

test_graph_processor(
    list)