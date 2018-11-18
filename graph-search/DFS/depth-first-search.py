from node import Node
from simplegraph import successors, deadend, is_solution_path


def dfs(s, successors, is_solution_path, deadend, k):

    OPEN = [s]
    CLOSED = []

    while OPEN:
        n = OPEN.pop()
        CLOSED.append(n)

        if depth(n) == k:
            # cleanup_closed()
            CLOSED.clear()

        else:
            for successor in successors(n):
                successor.backpointer = n

                if is_solution_path(successor):
                    return successor

                OPEN.append(successor)

                if deadend(successor):
                    OPEN.pop()

                    # cleanup_closed()
                    CLOSED.clear()

            if not successors(n):
                # cleanup_closed()
                CLOSED.clear()

    return "FAIL"


def depth(n):
    depth = 0
    backpointer = n.backpointer
    while backpointer != "NULL":
        backpointer = backpointer.backpointer
        depth += 1
    return depth


s = Node("A")
goal_node = dfs(s, successors, is_solution_path, deadend, 5)
print(goal_node)

