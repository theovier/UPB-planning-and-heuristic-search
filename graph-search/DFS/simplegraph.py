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


def deadend(n):
    return successors(n) == 0


def is_solution_path(n):
    return n.name == "G" or n.name == "H"


#            A
#        B        C
#     D     E       F
#         G   H

