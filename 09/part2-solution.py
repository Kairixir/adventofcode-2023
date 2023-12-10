import numpy as np

FILE = "part2-solution.txt"
FILE = "part2-test.txt"


class PuzzleInverseTree:
    def __init__(self, leaves):
        self.leaves = leaves
        self.nodes = None

    def build_tree_postfix(self, full: bool = False):
        nodes = [self.leaves]
        for i in range(len(nodes[0]) - 1, 0, -1):
            nodes.append(np.zeros(i))
            for j in range(len(nodes[0]) - i):
                nodes[j + 1][i - 1] = nodes[j][i] - nodes[j][i - 1]
            if not nodes[len(nodes) - 1].any() and not full:
                break
        self.nodes = nodes

    def build_tree_prefix(self):
        nodes = [self.leaves]
        for i in range(len(nodes[0])):
            for j in range(i):
                nodes[j + 1][i - j - 1] = nodes[j][i - j] - nodes[j][i - j - 1]
                # nodes[p1 + 1][p2 - 1] = nodes[p1][p2] - nodes[p1][p2 - 1]
            #   if not nodes[len(nodes) - 1].any():
            #       break
            nodes.append(np.zeros(len(nodes[0]) - i - 1))
        self.nodes = nodes

    def build_tree(self, postfix: bool) -> None:
        if postfix:
            self.build_tree_postfix()
        else:
            self.build_tree_prefix()

    def print_tree(self) -> None:
        if self.nodes is None:
            print("Tree is not built")
            exit(1)
        print(self.nodes)
        for i in range(len(self.nodes)):
            print(self.nodes[i])

    def next_val(self):
        result = 0
        for level in reversed(self.nodes):
            result = level[0] - result
        return result


def process_line(line: str):
    nums = np.array(list(map(int, line.strip().split(" "))))
    pit = PuzzleInverseTree(nums)
    pit.build_tree_postfix(True)
    pit.print_tree()
    return pit.next_val()


with open(FILE) as f:
    total = 0
    for line in f.readlines():
        total += process_line(line)

print(total)
