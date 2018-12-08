from operator import attrgetter
from collections import namedtuple, deque

test_data = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
Node = namedtuple('Node', ['children', 'metadata'])


def parse_node(raw_data):
    child_no = int(raw_data.popleft())
    metadata_no = int(raw_data.popleft())
    children = []
    metadata = []
    for i in range(child_no):
        children.append(parse_node(raw_data))
    for i in range(metadata_no):
        metadata.append(int(raw_data.popleft()))
    return Node(children, metadata)


def walk_tree(node, key):
    ret = []
    for child in node.children:
        ret.extend(walk_tree(child, key))
    ret.extend(attrgetter(key)(node))
    return ret


def value_node(node):
    ret = 0
    for metadata in node.metadata:
        if len(node.children) >= metadata:
            ret += value_node(node.children[metadata - 1])
    if not node.children:
        return sum(node.metadata)
    return ret


def puzzle1(string):
    raw_data = deque(string.strip().split())
    parsed_nodes = parse_node(raw_data)
    all_metadata = walk_tree(parsed_nodes, 'metadata')
    return sum(all_metadata)


def puzzle2(string):
    raw_data = deque(string.strip().split())
    parsed_nodes = parse_node(raw_data)
    valued_node = value_node(parsed_nodes)
    return valued_node


print(puzzle1(test_data))

with open('8.txt') as f:
    print(puzzle1(f.readline()))

print(puzzle2(test_data))

with open('8.txt') as f:
    print(puzzle2(f.readline()))
