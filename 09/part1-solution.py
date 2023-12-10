import numpy as np

FILE = "part1-solution.txt"
# FILE = "part1-test.txt"


class PuzzleInverseTree:
    def __init__(self, leaves):
        self.leaves = leaves
        self.nodes = None

    def build_tree(self):
        nodes = [self.leaves]
        for i in range(len(nodes[0]) - 1, 0, -1):
            nodes.append(np.zeros(i))
            for j in range(len(nodes[0]) - i):
                nodes[j + 1][i - 1] = nodes[j][i] - nodes[j][i - 1]
            if not nodes[len(nodes) - 1].any():
                break
        self.nodes = nodes

    def print_tree(self) -> None:
        if self.nodes is None:
            print("Tree is not built")
            exit(1)
        print(self.nodes)
        for i in range(len(self.nodes)):
            print(self.nodes[i])

    def next_val(self):
        total = 0
        for level in self.nodes:
            total += level[-1]
        return total


def process_line(line: str):
    nums = np.array(list(map(int, line.strip().split(" "))))
    pit = PuzzleInverseTree(nums)
    pit.build_tree()
    return pit.next_val()


with open(FILE) as f:
    total = 0
    for line in f.readlines():
        total += process_line(line)

print(total)
