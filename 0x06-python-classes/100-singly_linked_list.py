#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def date(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, (self, None)):
            raise TypeError("next_node must be a Node object")
