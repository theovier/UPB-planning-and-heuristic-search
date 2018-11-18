class Node:

    def __init__(self, board_configuration):
        self.backpointer = 0
        self.board_config = board_configuration
        self.null_position = self.find_null_tile(board_configuration)

    def find_null_tile(self, config):
        val = 0
        return [(index, row.index(val)) for index, row in enumerate(config) if val in row][0]

    def __str__(self):
        return "Node {} with backpointer to \n \t {}".format(self.board_config, self.backpointer)

