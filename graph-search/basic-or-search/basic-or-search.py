from node import Node
from puzzle import successor_8_puzzle, solution_path_8_puzzle, starting_board_configuration


def basic_or_search(s, successors, is_solution_path):
    OPEN = [s]
    CLOSED = []

    if is_solution_path(s):
        return s

    while OPEN:

        # Choose a solution base represented by n and remove it from OPEN
        n = OPEN.pop()

        # Store n on CLOSED for easy access.
        CLOSED.append(n)

        for successor in successors(n):

            # Extend solution base represented by n.
            successor.backpointer = n

            # Check if the successor-node represents a solution path.
            if is_solution_path(successor):
                return successor

            # PUSH; Store the successor-node on OPEN waiting for expansion
            OPEN.append(successor)

    return "FAIL"


s = Node(starting_board_configuration)
goal_node = basic_or_search(s, successor_8_puzzle, solution_path_8_puzzle)

print(goal_node)
