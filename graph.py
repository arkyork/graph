from dataclasses import dataclass,field
from node import Node
from edge import Edge

@dataclass
class Graph:
    # 有向 or 無向
    directed: bool = False
    
    nodes: set[Node] = field(default_factory=set)
    # グラフの再現のために利用

    edges: list[Node] = field(default_factory=list)

    # 隣接リスト
    adjacency: dict[Node,dict[Node,float]] = field(default_factory=dict)

    # ノードの追加
    def add_node(self, name: str) -> Node:
        node = Node(name)

        # nodesに含まれていない場合
        if not node in self.nodes:
            self.nodes.add(node)
            self.adjacency[node] = {}

        return node

    # エッジの追加
    def add_edge(self, start: str ,end: str,weight: float = 1.0):
        start_node = self.add_node(start)
        end_node = self.add_node(end)

        edge = Edge(start, end, weight)

        self.edges.append(edge)

        # 隣接リストの更新
        self.adjacency[start_node][end_node] = weight

        # 無向グラフである場合、コストが同じになる
        if not self.directed:
            self.adjacency[end_node][start_node] = weight

    # オブジェクトを再生成するため
    def __repr__(self) -> str:
        return f"""Graph(
            directed={self.directed},
            nodes={self.nodes},
            edges={self.edges},
            adjacency={self.adjacency}
        )
        """
