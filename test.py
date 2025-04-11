# var= [[1,2],[2,3],[3,4],['a','b']]
# var2=[]
# for i in var[::-1]:
#     var2.append(i[::-1])
# print(var2)


# a,b=2,3
# a,b=b,a
# print(a,b)



# def print_adjaceny_list(V, edges):
#     adj_list = {i: [] for i in range(V)}
#     print(adj_list)
# V=3
# edges=[[0,1],[1,2],[2,3]]
# print_adjaceny_list(V,edges)

V = 3
edges = [[0,1],[1,2],[2,3]]
adj_list=[]
for i in range(V):
    adj_list.append([])
for edge in edges:
    from_node = edge[0]
    to_node = edge[1]
    adj_list[from_node].append(to_node)
for i in range(V):
    print(i, "->", *adj_list[i])