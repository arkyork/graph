from dataclasses import dataclass
from node import Node


@dataclass(frozen=True)
class Edge():
    start: Node
    end: Node
    weight: float = 1.0


