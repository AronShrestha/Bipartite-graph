


class Node:
    def __init__(self,value) -> None:   
        if value[0].lower()=='m':
            i = len(value)
            index =''
            for _ in range(i):
                index =index + value[_]           
            
        else:
            j=len(value)
            index = ''
            for _ in range(j):
                index =index + value[_]
            
        index=int(index[1:])
            
   
        self.value = index

        self.edges =[]

class Edge:
    def __init__(self, node_from,node_to,weight = 1) -> None:  
        self.weight = weight
        self.node_from = node_from
        self.node_to = node_to


class Graph:
    def __init__(self,number,nodes=[],edges=[]) -> None:
        self.__size =0
        self.nodes = nodes
        self.edges = edges
        self.n = int(number)
        

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
        matrix =[[0 for i in range(0,self.n+1)] for j in range(1,self.n+1)]
       
        for edge in self.edges:
            matrix[edge.node_from.value][edge.node_to.value] = edge.weight
            

        return matrix
    
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
graph.insert_edge('m0','w1',1)
graph.insert_edge('m2', 'w1',1)
graph.insert_edge('m1', 'w3',1)

print(graph.adjacency_matrix())
        

        