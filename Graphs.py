class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.int_value = int(value[1:])
        if value[0].lower()=='m':
            self.type = "man"
        elif value[0].lower =='w':
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

    def search(self, node1_value, node2_value):         #search for an edge with the held for nodes values
        if self.node_from.value == node1_value and self.node_to.value == node2_value:
            return self


class Graph:
    def __init__(self,nodes_number, nodes=[],edges=[]) -> None:
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
            self.nodes.append(from_found)

        if not to_found:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        
        new_edge = Edge(from_found,to_found,weight)
        self.edges.append(new_edge)

    def reverse_edges(self, node1_val, node2_val):          #reverse edges for residual graph
        start_node = None 
        end_node = None
        for node in self.nodes:
            if node1_val == node.value:
                start_node = node 
            
            if node2_val == node.value:
                end_node = node

        for edge in self.edges:
            if edge.node_from.value == start_node.value and edge.node_to.value == end_node.value:
                self.edges.remove(edge.search(node1_val,node2_val))
                self.edges.append(Edge(end_node,start_node))
              

    def adjacency_matrix(self):

        reversed_pair_count = 0

        for edge in self.edges:
            if edge.node_from.value[0] == 'w' and edge.node_to.value[0] == 'm':
                reversed_pair_count +=1

        for _ in range(reversed_pair_count):                #reverse edges for each earlier reversed pair to undo the effects in sdjacent matrix
            for edge in self.edges:
                # print(f"{edge.node_from.value},{edge.node_to.value}")
                if edge.node_from.value[0] == 'w' and edge.node_to.value[0] == 'm':
                    self.reverse_edges(edge.node_from.value, edge.node_to.value)


        matrix =[[0 for _ in range(0,self.nodes_number+1)] for _ in range(1,self.nodes_number+1)]
       
        for edge in self.edges:
            matrix[edge.node_from.int_value - 1][edge.node_to.int_value] = edge.weight
            

        return matrix

        

        
