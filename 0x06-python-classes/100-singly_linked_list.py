#!/usr/bin/python3

"""
A simple module implementing a node class and a linked list 
"""


class Node:
    """A node class for singly linked lists"""

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
    """A singly linked list data structure"""

    def __init__(self):
        self.head = None

    def __str__(self) -> str:
        value_arr = []
        temp_head = self.head
        while temp_head.next_node is not None:
            value_arr.append(temp_head.data)
            temp_head = temp_head.next_node
        value_arr.sort()
        return "".join(
            map(lambda x: str(x) + "\n"
                if value_arr.index(x) != len(value_arr) - 1
                else str(x), value_arr))

    def sorted_insert(self, value):
        """Insert a new node into the linked list"""
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            temp = self.head
            new_node.next_node = temp
            self.head = new_node
        # self.head = traverse(self.head)


def traverse(head, arr=[], new_head=None):
    """Traverse through the linked list and sort the elements
    Returns:
        A new linked list head
    """
    arr.append(head.data)
    if head.next_node is None:
        for item in arr:
            if new_head is None:
                new_head = Node(item)
            else:
                new_node = Node(item)
                temp = new_head
                new_node.next_node = temp
                new_head = new_node
        return new_head
    return traverse(head.next_node, arr)
