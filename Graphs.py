


class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.edges =[]

class Edge:
    def __init__(self, node_from,node_to,weight = 1) -> None:  
        self.weight = weight
        self.node_from = node_from
        self.node_to = node_to


class Graph:
    def __init__(self,nodes=[],edges=[]) -> None:
        self.__size =0
        self.nodes = nodes
        self.edges = edges

    def insert_node(self,node_value):
        new_node = Node(node_value)
        self.nodes.append(new_node)
    
    def insert_edge(self,node_from_val,node_to_val,weight=1):
        from_found = None 
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node 
            
            if node_to_val == node.value:
                to_found = node
        
        if from_found == None :
            from_found = Node(node_from_val)
            self.nodes.append(from_found)

        if to_found == None :
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        
        new_edge = Edge(from_found,to_found,weight)
        self.edges.append(new_edge)


    def adjacency_matrix(self):
        max_index = self.find_max_index()
        matrix =[[0 for i in range(max_index+1)] for j in range(max_index+1)]
        print(matrix)
        for edge in self.edges:
            matrix[edge.node_from.value][edge.node_to.value] = edge.weight

        return matrix
    
    def find_max_index(self):
        max_index = -1
        if len(self.nodes) == 0:
            return "Empty list"
        
        else:
            for node in self.nodes:
                if node.value > max_index:
                    max_index = node.value

        return max_index

graph = Graph()
graph.insert_edge(0, 2,1)
graph.insert_edge(1, 3,1)
graph.insert_edge(1, 4,1)
graph.insert_edge(3, 4,1)
graph.insert_edge(5, 4,1)
graph.insert_edge(4, 5,1)
print(graph.adjacency_matrix())
        

        