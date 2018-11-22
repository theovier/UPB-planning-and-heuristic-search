from node import Node


# just a simple sample graph
def successors(n):
    if n.name == "A":
        return [Node("B"), Node("C")]
    if n.name == "B":
        return [Node("D"), Node("E")]
    if n.name == "C":
        return [Node("F")]
    if n.name == "D":
        return []
    if n.name == "E":
        return [Node("G"), Node("H")]
    return []


class SuccessorUtil:
    # hardcoded nodes and successors in this simple example
    successorPointer = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0}

    def next_successor(self, n):
        i = self.successorPointer[n.name]
        self.successorPointer[n.name] = i + 1
        return successors(n)[i]

    def expanded(self, n):
        i = self.successorPointer[n.name]
        return len(successors(n)) == i


def deadend(n):
    return successors(n) == 0


def is_solution_path(n):
    return n.name == "G" or n.name == "H"




#            A
#        B        C
#     D      E       F
#         G     H

