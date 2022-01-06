"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    #better
    """
    Algorithm

    We will use a hash map to store the reference of the copy of all the nodes that have already been visited and copied. 
    The key for the hash map would be the node of the original graph and corresponding value would be the corresponding 
    cloned node of the cloned graph.
    
    The visited is used to prevent cycles and get the cloned copy of a node.

    Add the first node to the queue. Clone the first node and add it to visited hash map.

    Do the BFS traversal.

    Pop a node from the front of the queue.
    Visit all the neighbors of this node.
    If any of the neighbors was already visited then it must be present in the visited dictionary. Get the clone of this neighbor from visited in that case.
    Otherwise, create a clone and store in the visited.
    Add the clones of the neighbors to the corresponding list of the clone node.
    """


    
    """ 
    1. create a empty queue and a dict. create an empty return_list too.
    2. add the root node to the queue.
    while queue is not empty:
        - pop element
        - if element is in the dict:
            - assign current_new_node to the corresponding val from the nodes_dict
        - else:
            - create a new node, with the element's value
            - add it to the nodes_dict
        - loop through the neighbors of the element
            - if neighbor is in the dict:
                - append to the neighbors of the new_node the val from nodes_dict
            - else:
                - add the element to the queue
                - create a new node based on the element
                - add it to the dict with element as the key
        at the end of every loop, append to return_list the current_new_node
    return current_new_node[0]


    bfs*
    """
    def cloneGraph(self, node: 'Node') -> 'Node':
        nodes_queue = []
        nodes_dict = {}
        nodes_queue.append(node)
        return_list = []
        while nodes_queue:
            current_old_node = nodes_queue.pop(0)
            if current_old_node in nodes_dict:
                current_new_node = nodes_dict[current_old_node]
            else:
                current_new_node = Node(val=current_old_node.val)
                nodes_dict[current_old_node] = current_new_node
            for neighbor in current_old_node.neighbors:
                if neighbor in nodes_dict:
                    current_new_node.neighbors.append(nodes_dict[neighbor])
                else:
                    nodes_queue.append(neighbor)
                    new_node = Node(val=neighbor.val)
                    nodes_dict[neighbor] = new_node
                    current_new_node.neighbors.append(new_node)
                    nodes_dict[current_old_node] = current_new_node
            return_list.append(current_new_node)
        return return_list[0]

"""
Complexity Analysis

Time Complexity : O(N + M), where NN is a number of nodes (vertices) and MM is a number of edges.

Space Complexity : O(N). 
This space is occupied by the visited dictionary and in addition to that, space would also be occupied by the queue since we are adopting the BFS approach here. 
The space occupied by the queue would be equal to O(W) where WW is the width of the graph. Overall, the space complexity would be O(N).
"""