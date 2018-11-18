class Node:

    def __init__(self, name):
        self.backpointer = "NULL"
        self.name = name

    def __str__(self):
        return "({}) -> {}".format(self.name, self.backpointer)

