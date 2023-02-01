# Bipartite-graph


This project, ‘Bipartite Matching,’ is the mini project implementing the Ford-Fulkerson Algorithm. This project involves implementing a type of graph known as a bipartite graph, making max flow networks, and finding maximum matching.


A bipartite graph is a graph whose vertices can be divided into two independent sets, U and V, such that every edge(U, V) connects a vertex from U to V or a vertex from V to U.In our project, the two distinct vertices were woman and man.


In a bipartite graph, matching is a set of edges chosen from a set of edges such that no two edges share the same endpoints. A maximum matching is a maximum number of matching that can be made for that graph, given that there exists no matching greater than maximum matching. However, more than one maximum matching for a given bipartite graph may exist. Maximum flow is the maximum amount of flow that the network would allow to flow from source to sink; Ford-Fulkerson is one of the algorithms to build a max flow network. The flow value is always 1 in our project as it’s a bipartite matching graph.


For this project, we first made a graph with two disjoint sets of vertices, men and women. Then we built the maximum flow network and evaluated the maximum flow using the depth-first search technique.

