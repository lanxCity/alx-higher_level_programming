#!/bin/bash/python3
""" Write a class Node that defines a node of a singly linked list """

class Node:
    """
    A node class for singly linked list

    This class provides a blueprint for node obj
    with next_node obj

    Attributes:
        __data (int): node data
        __next_node Node: Node obj
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new node object
        Args:
            data (int): node data
            next_node (Node): Node obj
        """
        self.data = data
        self.next_node = next_node

    # def __repr__(self):
    #    return '{}'.format(self.__data)

    # For data
    @property
    def data(self):
        """ int: node data"""
        return '{:d}'.format(self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    # For next node
    @property
    def next_node(self):
        """ Node: next node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
            return

        raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    li = []

    def __init__(self):
        self.__head = 0

    def __repr__(self):
        nodes_li = ''

        for i in SinglyLinkedList.li:
         #   nodes += '{:d}\n'.format(n.data)
            print(i.data)

        #return nodes

    def sorted_insert(self, value):
        SinglyLinkedList.li.append(Node(value))

        # Convert to int and sort
        new_nodes = [n.data for n in  SinglyLinkedList.li]

        sorted_n = 
        print(new_nodes)























