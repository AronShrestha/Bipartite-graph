from Graphs import Graph

#A dfs function that recursively checks best possible matching 
def Check_matching(n,graph,men_index,check_list,seen):
    for i in range(n):
        if graph[i][men_index] and seen[i] == False: # first condition: i is for ith women and particular man with index men-index will be true iif that particular women of ith index is ready to dance that particular men .And 2nd condition is that they havent talk with eachother about dancing (seen)

            seen[i] = True
        #below condition holds if particular women i not assigned to a man or they have other option 
            if check_list[i] == -1 or Check_matching(n,graph,check_list[i],check_list,seen):
                check_list[i] = men_index # assigning particular man to particular women
                return True
    return False

def maximum_matching(n,graph):
    check_list =[-1]*n #this is an array keeping record of women dancing with men,so the value check_list[i] is the woman dancing with ith man
    max_flow =0
    for men_index in range(n):
        seen=[False]*n
        if Check_matching(n,graph,men_index,check_list,seen):
            max_flow += 1
        
    
    return max_flow,check_list



graph = Graph(3)
graph.insert_edge('m0','w0',1)
graph.insert_edge('m0', 'w1',1)
graph.insert_edge('m1', 'w0',1)
graph.insert_edge('m2','w2',1)
adjacency_matrix = graph.adjacency_matrix()
max_number,partner =maximum_matching(len(adjacency_matrix),adjacency_matrix)
print("maximum partner :",max_number)
print(partner)
max_partner_graph={}
for men,women in enumerate(partner):
    i='m'+str(men) 
    j='w'+str(women)
    max_partner_graph[i]=[j]

print(max_partner_graph)




