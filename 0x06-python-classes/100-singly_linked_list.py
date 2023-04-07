#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        if next_node and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self) -> str:
        value_arr = []
        traverse(self.head, value_arr)
        value_arr.sort()
        return "".join(
            map(lambda x: str(x) + "\n"
                if value_arr.index(x) != len(value_arr) - 1
                else str(x), value_arr))

    def sorted_insert(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            temp = self.head
            new_node.next_node = temp
            self.head = new_node


def traverse(head, arr):
    arr.append(head.data)
    if head.next_node is None:
        return ""
    return traverse(head.next_node, arr)
