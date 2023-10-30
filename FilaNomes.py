from queue import Queue
from typing import Any

EMPTY_NODE_VALUE = '__EMPTY_NODE_VALUE__'


class Erro(Exception):
    ...


class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next = Node

    def __repr__(self) -> str:
        return f'{self.value}'

    def __bool__(self) -> bool:
        return bool(self.value != EMPTY_NODE_VALUE)


class Queue:
    def __init__(self) -> None:
        self.first: Node = Node(EMPTY_NODE_VALUE)
        self.last: Node = Node(EMPTY_NODE_VALUE)
        self._count = 0

    def enqueue(self, node_value: Any) -> None:
        novo_node = Node(node_value)

        if not self.first:
            self.first = novo_node
        if not self.last:
            self.last = novo_node
        else:
            self.last.next = novo_node
            self.last = novo_node
        self._count += 1

    def pop(self) -> Node:
        if not self.first:
            raise Erro('Sem elementos na fila')
        first = self.first

        if hasattr(self.first, 'next'):
            self.first = self.first.next
        else:
            self.first = Node(EMPTY_NODE_VALUE)
        self._count += 1
        return first

    def peek(self) -> Node:
        return self.first

    def __len__(self) -> int:
        return - self._count

    def __bool__(self) -> bool:
        return bool(self._count)

    def __iter__(self) -> Queue:
        return self

    def __next__(self) -> Any:
        try:
            next_value = self.pop()
            return next_value
        except Erro:
            raise StopIteration


fila1 = Queue()
fila1.enqueue('Maria')
fila1.enqueue('Carlos')
fila1.pop()