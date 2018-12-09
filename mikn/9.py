from operator import itemgetter
from collections import defaultdict


class Node:
    def __init__(self, value, next_item=None, prev_item=None):
        self.value = value
        self.prev = prev_item
        self.next = next_item


class CircularLinkedList:
    def __init__(self, input_list):
        self._list = []  # pure storage
        prev_item = None
        node = None
        last = Node(input_list.pop(), None)
        node = last
        prev_item = last
        for item in input_list[::-1]:
            node = Node(item, prev_item, node)
            self._list.append(node)
            prev_item = node
        self._first = node
        last.next = self._first
        self._first.prev = last
        self._current = self._first
        self.next = self.__next__

    def __next__(self):
        if not self._current:
            raise StopIteration()
        ret = self._current
        self._current = self._current.next
        return ret

    def pop(self):
        deleted = self._current
        self._current.prev.next = self._current.next
        self._current.next.prev = self._current.prev
        self._current = self._current.next
        return deleted

    def add(self, node):
        next_node = self._current.next
        self._current.next.prev = node
        self._current.next = node
        node.next = next_node
        node.prev = self._current
        self._current = node

    def prev(self):
        self._current = self._current.prev
        return self._current

    def __iter__(self):
        return self

    def reset(self):
        self._current = self._first


def puzzle1(total_players, last_marble):
    players = defaultdict(int)
    marbles = CircularLinkedList([0])
    current_value = 0
    current_player = 0
    while(current_value < last_marble):
        current_value += 1
        current_player += 1
        if current_player > total_players:
            current_player = 1
        if current_value % 23 == 0:
            for _ in range(7):
                marbles.prev()
            captured_val = marbles.pop().value
            players[current_player] += current_value + captured_val
            continue
        next(marbles)
        marbles.add(Node(current_value))
    winners = list(players.items())
    winners.sort(key=itemgetter(1), reverse=True)
    print(winners.pop(0))


puzzle1(9, 25)
puzzle1(10, 1618)
puzzle1(13, 7999)
puzzle1(17, 1104)
puzzle1(21, 6111)
puzzle1(30, 5807)
puzzle1(468, 71010)
puzzle1(468, 71010 * 100)
