import re

FILE = "part1-solution.txt"
# FILE = "part1-test.txt"


class Node:
    def __init__(self, val):
        self.val = val
        self.parent = None

    def add_child(self, child: Node, is_left_child: bool):
        if is_left_child:
            self.l = child
        self.r = child
        child.parent = self

class PuzzleInverseTree:
    def __init__(self, leaves: List[Node]):
        self.leaves = leaves

    def build_tree(self):
        for leaf in enumerate(self.leaves):
            leaf



def process_line(line: str):
    nums = map(int, line.strip().split(" "))
    rows = []
    for num in nums:
        

with open(FILE) as f:
    for line in f.readlines():
