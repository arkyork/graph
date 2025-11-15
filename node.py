from dataclasses import dataclass

# ノード
@dataclass(frozen=True)
class Node():
    name: str