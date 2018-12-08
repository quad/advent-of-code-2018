import string
from operator import itemgetter
from collections import defaultdict
import re

test_input = '''Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
'''

# walk through graph, assign work time
# release new nodes to traverse when work is done (not when node is visited)
# make sure only 5 workers are working when there's more items available


def get_next_node(dag, nodes, current_nodes):
    sorted_dag = list(dag.items())
    sorted_dag.sort(key=itemgetter(0))
    for dep_node, pre_nodes in sorted_dag:
        is_it_next_nodes = list(pre_nodes)
        for node in nodes:
            if node in current_nodes and node in is_it_next_nodes:
                is_it_next_nodes.remove(node)
        if len(is_it_next_nodes) == 0:
            del(dag[dep_node])
            return dep_node
    return None


def resolve_graph(dag, nodes):
    visited_nodes = []
    sorted_nodes = list(nodes)
    sorted_nodes.sort()
    for node in sorted_nodes:
        if len(dag[node]) == 0:
            if not visited_nodes:
                visited_nodes.append(node)
                del(dag[node])
    add_node = get_next_node(dag, sorted_nodes, visited_nodes)
    while(add_node):
        visited_nodes.append(add_node)
        add_node = get_next_node(dag, sorted_nodes, visited_nodes)
    return visited_nodes


def timed_graph(dag, nodes):
    letters = string.ascii_uppercase
    timings = range(61, 61 + len(letters))
    letter_timings = {t[0]: t[1] for t in zip(letters, timings)}
    workers = [[0, ''], [0, ''], [0, ''], [0, ''], [0, '']]
    available_nodes = []
    completed_nodes = []
    sorted_nodes = list(nodes)
    sorted_nodes.sort()
    for node in sorted_nodes:
        if len(dag[node]) == 0:
            available_nodes.append(node)
            del(dag[node])
    while(available_nodes or [w for w in workers if w[1] != '']):
        available_nodes.sort()
        for worker in workers:
            if worker[1] == '' and len(available_nodes):
                worker[1] = available_nodes.pop(0)
                worker[0] += letter_timings[worker[1]]
        workers.sort(key=itemgetter(0))
        print(workers)
        empty_workers = []
        for worker in workers:
            if worker[1] == '':
                empty_workers.append(worker)
            else:
                completed_nodes.append(worker[1])
                worker[1] = ''
                for w in empty_workers:
                    w[0] = worker[0]
                break

        new_node = get_next_node(dag, nodes, completed_nodes)
        while(new_node):
            available_nodes.append(new_node)
            new_node = get_next_node(dag, nodes, completed_nodes)

    return workers[4][0]


def puzzle2(strings):
    dag = defaultdict(list)
    nodes = set()
    for line in strings:
        res = re.search('^Step (\w+) must be finished before step (\w+) can begin.', line)
        # build it backwards! YAY
        dag[res[2]].append(res[1])
        nodes.add(res[1])
        nodes.add(res[2])
    res = timed_graph(dag, nodes)
    print(res)


def puzzle1(strings):
    dag = defaultdict(list)
    nodes = set()
    for line in strings:
        res = re.search('^Step (\w+) must be finished before step (\w+) can begin.', line)
        # build it backwards! YAY
        dag[res[2]].append(res[1])
        nodes.add(res[1])
        nodes.add(res[2])
    res = resolve_graph(dag, nodes)
    print(''.join(res))


with open('7.txt') as f:
    #puzzle1(f.readlines())
    puzzle2(f.readlines())
