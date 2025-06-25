from dataclasses import dataclass


@dataclass
class Node:
    id: int

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        pass