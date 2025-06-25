from dataclasses import dataclass

from nodes import Node


@dataclass
class Edge:
    n1: Node
    n2: Node
    weight: int