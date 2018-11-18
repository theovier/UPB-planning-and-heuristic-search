from node import Node
import copy


# problem specific function
def successor_8_puzzle(n):
    # just return non-empty ones
    return [x for x in [successor_up(n), successor_down(n), successor_left(n), successor_right(n)] if x]


def successor_up(n):
    return shift_tiles(n, -1, 0)


def successor_down(n):
    return shift_tiles(n, 1, 0)


def successor_right(n):
    return shift_tiles(n, 0, 1)


def successor_left(n):
    return shift_tiles(n, 0, -1)


def shift_tiles(n, row_shift, column_shift):
    row, column = n.null_position

    target_row = row + row_shift
    target_column = column + column_shift

    if not in_boundary(target_row, target_column):
        return []

    config = copy.deepcopy(n.board_config)

    # swap places of 0 and tile specified by the shift.
    config[row][column], config[target_row][target_column] = config[target_row][target_column], 0
    return Node(config)


def in_boundary(row, column):
    return 0 <= row <= 2 and 0 <= column <= 2


# nodes now represent solution bases via their backpointer paths
# problem specific function
def solution_path_8_puzzle(n):
    return n.board_config == target_board_configuration


starting_board_configuration = [
    [1, 2, 3],
    [0, 8, 4],
    [7, 6, 5]
]

target_board_configuration = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]