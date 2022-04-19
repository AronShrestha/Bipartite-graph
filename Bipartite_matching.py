from Graphs import Graph

def create_max_flow_network(n,k,jump_edge = 3):
                                            
    # for i in range(n):                #for jump_egde =1
    #     men_no = i+1                #match man and woman who know each other.
    #     if men_no >= n:
    #         known_women = 1
    #     else:
    #         known_women = men_no + 1
    #     for _ in range(k):
    #         graph.insert_edge(f'm{men_no}',f'w{known_women}')           #insert edge between man and woman who know each other.
    #         known_women += 1
    #         if known_women > n:
    #             known_women = 1
    
    graph = Graph(n)              # the case is deduced from the above commented code with jump_edge = 1
    for i in range(n):
        men_no = i+1                #match man and woman who know each other.
        if men_no + jump_edge > n:
            known_women = men_no + jump_edge - n
        else:
            known_women = men_no + jump_edge
        for _ in range(k):
            graph.insert_edge(f'M{men_no}',f'W{known_women}')           #insert edge between man and woman who know each other.
            known_women += 1
            if known_women > n:
                known_women = 1


    for row in graph.adjacency_matrix():
        print(row)
    print()
    print("Adding source and sink to the network.")
    print()
    for person_no in range(1,n+1):          #In our problem, no. of men = no. of women
        graph.insert_edge('S1',f'M{person_no}')
        graph.insert_edge(f'W{person_no}','T1')

    return graph

def create_max_flow_network_from_file(filename):
    graph = Graph(9)
    external_file = open(filename)
    for line in external_file:
        graph.insert_edge(line.split()[0],line.split()[1])

    for row in graph.adjacency_matrix():
        print(row)
    print()
    print("Adding source and sink to the network.")
    print()
    for person_no in range(1,10):          #In our problem, no. of men = no. of women
        graph.insert_edge('S1',f'M{person_no}')
        graph.insert_edge(f'W{person_no}','T1')

    return graph

def dfs(graph,start_node_val,end_node_val, dfs_path_pair = [], visited =[]):        #DFS traversal to find a path between source and sink
    if start_node_val not in visited:
        visited.append(start_node_val)              #mark a node as visited
        path_found = False
        if start_node_val == end_node_val:
            path_found = True
            bipartite_pair = [element for element in dfs_path_pair if 'S1' not in element and 'T1' not in element]      #extract bipartite pair i.e.pair of man and woman from a dfs path.
            return bipartite_pair
        if not path_found:
            to_search_edges = [edge for edge in graph.edges if edge.node_from.value == start_node_val]
            for edge in to_search_edges:
                dfs_path_pair.append((start_node_val,edge.node_to.value))
                bipartite_pair = dfs(graph, edge.node_to.value, end_node_val, dfs_path_pair, visited)               #recursively find a path between spource and sink
                return bipartite_pair
    

def residual_graph(graph):
    flow = 0
    dancing_pairs = []
    bipartite_pair = dfs(graph,'S1','T1')
    while bipartite_pair is not None:
        try:
            [(men,women)] = bipartite_pair
            dancing_pairs.append(bipartite_pair[0])         #mark the first pair from dfs as the matched pair.
            graph.reverse_edges('S1',men)               # make residual graph by reversing all the edges of dfs path.
            graph.reverse_edges(men,women)
            graph.reverse_edges(women,'T1')
            flow = flow+1
            bipartite_pair = dfs(graph,'S1','T1', dfs_path_pair = [], visited =[])          #find dfs in residual graph
        except:
            break
    print(f"{flow} pairs are matched with each other.")
    print("The pairs are: ", dancing_pairs)


if __name__ == '__main__':
    print()
    input_type = int(input("How do you want to present the input?\n 1.Give no. of nodes and edges per node as input.\n 2.Take input from a file.\n => "))
    print()
    if input_type == 1:
        no_of_people = int(input("Enter the number of men/women in the party: "))
        known_people = int(input("How many women does a man know / how many men does a woman know? "))
        print()
        if no_of_people >= known_people:
            mygraph = create_max_flow_network(no_of_people , known_people)
            # mygraph = create_max_flow_network_from_file()
            residual_graph(mygraph)
        else:
            print(f"A man can't know {known_people} women when only {no_of_people} women exists.")

    elif input_type ==2:
        mygraph = create_max_flow_network_from_file('paired_edges.dat')
        residual_graph(mygraph)

    else:
        print("Please enter the valid input. (1 or 2)")

    