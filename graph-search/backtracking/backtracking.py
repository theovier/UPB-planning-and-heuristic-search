from node import Node
from simplegraphBT import SuccessorUtil, deadend, is_solution_path


def bt(s, is_solution_path, deadend, k):
    util = SuccessorUtil()
    OPEN = [s]

    while OPEN:
        # Select front element in OPEN, no removing.
        n = OPEN[-1]

        if depth(n) == k or util.expanded(n):
            OPEN.pop()

        else:
            successor = util.next_successor(n)
            successor.backpointer = n

            if is_solution_path(successor):
                return successor

            if not deadend(successor):
                OPEN.append(successor)

    return "FAIL"


def bt_recursive(s, next_successor, is_solution_path, deadend, k):
    # todo
    pass


def depth(n):
    depth = 0
    backpointer = n.backpointer
    while backpointer != 'NULL':
        backpointer = backpointer.backpointer
        depth += 1
    return depth


s = Node("A")

goal_node = bt(s, is_solution_path, deadend, 5)
print(goal_node)

