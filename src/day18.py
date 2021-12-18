from utils import read_lines
import math


class Node:
    def __init__(self):
        self.left: Node = None
        self.data: int = 0
        self.depth = 0
        self.right: Node = None
        self.parent: Node = None
        self.type = 'pair'


def to_string(node):
    if node.type == 'number':
        return str(node.data)
    return '['+to_string(node.left)+',' + to_string(node.right) + ']'


def parse(line: str) -> Node:
    depth = 0
    root = Node()

    currentnode = root
    currentchar = ''

    for char in line:
        if char == '[':
            depth += 1

            new_node_left = Node()
            new_node_left.depth = depth
            new_node_left.parent = currentnode
            new_node_right = Node()
            new_node_right.depth = depth
            new_node_right.parent = currentnode

            currentnode.left = new_node_left
            currentnode.right = new_node_right

            currentnode = new_node_left

            currentchar = ''
        elif char == ']':
            currentnode = currentnode.parent
            depth -= 1
            currentchar = ''
        elif char == ',':
            currentnode = currentnode.parent.right
            currentchar = ''
        else:
            currentchar += char
            currentnode.data = int(currentchar)
            currentnode.type = 'number'

    return root


def left_neighbor(node: Node):
    """
    find the node to the left of this one
    """

    # keep going up until we can go left,
    # then go right as long as possible
    parent = node.parent
    previous = node
    while parent is not None:
        # check left
        left = parent.left
        if left != previous and left is not None:
            node = left
            while True:
                if node.right is None:
                    return node
                node = node.right
        previous = parent
        parent = parent.parent
    return None


def right_neighbor(node: Node):
    """
    find the node to the right of this one
    """

    # keep going up until we can go right,
    # then go left as long as possible
    parent = node.parent
    previous = node
    while parent is not None:
        # check right
        right = parent.right
        if right != previous and right is not None:
            node = right
            while True:
                if node.left is None:
                    return node
                node = node.left
        previous = parent
        parent = parent.parent
    return None


def explode(node):
    x, y = node.left.data, node.right.data

    ln = left_neighbor(node)
    if ln is not None:
        assert ln.type == 'number'
        ln.data += x
    rn = right_neighbor(node)
    if rn is not None:
        assert rn.type == 'number'
        rn.data += y

    node.left = None
    node.right = None
    node.data = 0
    node.type = 'number'


def split(node: Node):
    assert node.type == 'number'
    if node.data < 10:
        return

    val = node.data
    node.data = 0
    node.type = 'pair'

    new_node_left = Node()
    new_node_left.type = 'number'
    new_node_left.depth = node.depth+1
    new_node_left.data = math.floor(val/2)
    new_node_left.parent = node

    new_node_right = Node()
    new_node_right.type = 'number'
    new_node_right.depth = node.depth+1
    new_node_right.data = math.ceil(val/2)
    new_node_right.parent = node

    node.left = new_node_left
    node.right = new_node_right


def find_deep_nodes(node: Node) -> list[Node]:
    """
    left-to-right recursive traversal
    """
    if node is None:
        return []

    if node.type == 'pair' and node.depth == 4:
        return [node]

    return find_deep_nodes(node.left) + find_deep_nodes(node.right)


def find_high_nodes(node: Node) -> list[Node]:
    """
    left-to-right recursive traversal
    """
    res = []
    if node is not None:
        res = find_high_nodes(node.left)
        if node.data > 9:
            res.append(node)
        res = res + find_high_nodes(node.right)
    return res


def increase_depth(node: Node):
    if node is not None:
        node.depth += 1
        increase_depth(node.left)
        increase_depth(node.right)


def reduce(root: Node) -> Node:
    assert root.type == 'pair'

    while True:
        deep_nodes = find_deep_nodes(root)
        for deep_node in deep_nodes:
            explode(deep_node)

        high_nodes = find_high_nodes(root)
        if len(high_nodes) == 0:
            return root
        split(high_nodes[0])


def add(root1: Node, root2: Node) -> Node:
    increase_depth(root1)
    increase_depth(root2)
    new_root = Node()
    new_root.depth = 0
    new_root.left = root1
    new_root.right = root2
    root1.parent = new_root
    root2.parent = new_root
    return new_root


def lines_sum(lines):
    lines = [parse(line) for line in lines]

    current_result = lines[0]

    for line in lines[1:]:
        sum = add(current_result, line)
        current_result = reduce(sum)

    return current_result


def magnitude(node: Node) -> int:
    if node.type == 'number':
        return node.data
    return 3*magnitude(node.left) + 2*magnitude(node.right)


def run1(lines):
    res = lines_sum(lines)
    return magnitude(res)


def run2(lines):
    results = []
    for i in range(len(lines)):
        for j in range(len(lines)):
            # super inefficient, parsing all lines again
            lines_parsed = [parse(line) for line in lines]
            if i == j:
                continue
            res = magnitude(reduce(add(lines_parsed[i], lines_parsed[j])))
            results.append(res)

    return max(results)


if __name__ == '__main__':
    input = read_lines('inputs/day18.txt')
    print('[Part1]:', run1(input))
    print('[Part2]:', run2(input))
