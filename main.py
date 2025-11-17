from graph import Graph

# 有効グラフ
g = Graph(directed=True)

# 追加
g.add_edge("A", "B", 3)
g.add_edge("A", "C", 1)
g.add_edge("B", "C", 7)

print(g)