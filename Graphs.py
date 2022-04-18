class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.int_value = int(value[1:])
        if value[0].lower()=='m':
            self.type = "man"
        elif value[0].lower == 'w':
            self.type = "woman"
        elif value[0].lower == 's':
            self.type = "source"
        else:
            self.type = "sink"        
        self.edges =[]

class Edge:
    def __init__(self, node_from,node_to,weight = 1) -> None:  
        self.weight = weight
        self.node_from = node_from
        self.node_to = node_to


class Graph:
    def __init__(self,nodes_number, nodes=[],edges=[]) -> None:
        self.__size =0
        self.nodes = nodes
        self.edges = edges
        self.nodes_number = nodes_number

    def insert_node(self,node_value):
        for node in self.nodes:
            if node.value == node_value:
                exist_already = True
                break
        if exist_already:
            print("Node already exists.")    
        else:
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
        
        if not from_found:
            from_found = Node(node_from_val)
            print(from_found.value)
            self.nodes.append(from_found)

        if not to_found:
            to_found = Node(node_to_val)
            print(to_found.value)
            self.nodes.append(to_found)
        
        new_edge = Edge(from_found,to_found,weight)
        self.edges.append(new_edge)


    def adjacency_matrix(self):
        matrix =[[0 for _ in range(0,self.nodes_number+1)] for _ in range(1,self.nodes_number+1)]
       
        for edge in self.edges:
            matrix[edge.node_from.int_value - 1][edge.node_to.int_value] = edge.weight
            

        return matrix
        # max_index = self.find_max_index()
        # matrix =[[0 for i in range(max_index+1)] for j in range(max_index+1)]
        # print(matrix)
        # for edge in self.edges:
        #     matrix[edge.node_from.value][edge.node_to.value] = edge.weight

        # return matrix
    
    # def find_max_index(self):
    #     max_index = -1
    #     if len(self.nodes) == 0:
    #         return "Empty list"
        
    #     else:
    #         for node in self.nodes:
    #             if node.value > max_index:
    #                 max_index = node.value

    #     return max_index

graph = Graph(3)
graph.insert_edge('m1', 'w1',1)
graph.insert_edge('m2', 'w2',1)
graph.insert_edge('m3', 'w3',1)
graph.insert_edge('m3', 'w1',1)
print(graph.adjacency_matrix())
        

        
