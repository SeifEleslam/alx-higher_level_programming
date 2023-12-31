#!/usr/bin/python3
"""Module for Singly Linked List"""


class Node:
    """Node of singly linked list"""

    def __init__(self, data, next_node=None):
        "Init Node"
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get node data"""
        return self.__data

    @data.setter
    def data(self, data):
        """set node data"""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        """get node next"""
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        """set node next"""
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = next_node


class SinglyLinkedList:
    """singly linked list class"""

    def __init__(self):
        """simple init"""
        self.__head = None

    def sorted_insert(self, value):
        """insert value in sorted order"""
        if not self.__head:
            self.__head = Node(value)
            return
        tmp = self.__head
        while tmp and tmp.next_node and tmp.next_node.data < value:
            tmp = tmp.next_node
        if value < tmp.data:
            new_node = Node(value, tmp)
            self.__head = new_node
        else:
            tmp.next_node = Node(value, tmp.next_node)

    def __repr__(self):
        """return string representation of list"""
        output = ""
        tmp = self.__head
        while tmp:
            output += str(tmp.data) + ("\n" if tmp.next_node else "")
            tmp = tmp.next_node
        return output
