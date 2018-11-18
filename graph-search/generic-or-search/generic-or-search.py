"""

demo graph:

       A
       |
+------+-----+
|      |     |
B      C     D
    +-----+
    |     |
   (E)   (F)


parenthesis mark goal nodes.
"""


def generic_or_search(s, successors, is_solution_path):
    OPEN = [[s]]

    if is_solution_path(s):
        return s

    while OPEN:

        # Choose a solution base from OPEN.
        current_solution_base = OPEN.pop()

        # Determine last node in the current solution base
        n = current_solution_base[-1]

        for successor in successors(n):
            # Extend current solution base b.
            extended_solution_base = current_solution_base.copy()
            extended_solution_base.append(successor)

            # Check if solution base is a solution path
            if is_solution_path(extended_solution_base):
                return extended_solution_base

            # Store extended solution base on OPEN waiting for extension.
            OPEN.append(extended_solution_base)

    return "FAIL"


def demo_successor(n):
    if n == "A":
        return ["B", "C", "D"]
    if n == "C":
        return ["E", "F"]
    return []


def demo_solution_path(solution_base):
    return solution_base == ["A", "C", "E"] or solution_base == ["A", "C", "F"]

s = "A"
print(generic_or_search(s, demo_successor, demo_solution_path))




