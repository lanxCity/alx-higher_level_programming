#!/bin/bash/python3
""" Write a class Node that defines a node of a singly linked list """


class Node:
    """
    A node class for singly linked list

    This class provides a blueprint for node obj
    with next_node obj

    Attributes:
        __data (int): node data
        __next_node (Node): Node obj
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new node object
        Args:
            data (int): node data
            next_node (Node): Node obj
        """
        # For data
        if not isinstance(data, int):
            raise TypeError("data must be an integer")

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ int: node data"""
        return self.__data

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
    """
    A singly list class

    This class provides a blueprint for ssl obj
    with head node obj

    Attributes:
        __head (Node): Node obj
    """
    def __init__(self):
        """
        Initialize the SinglyLinkedList obj

        Attributes:
            __head (Node): Node obj
        """
        self.__head = None

    def __repr__(self):
        """ str: str representation of singly list  """
        # Sort nodes
        self.sort()

        # printing
        data = ''
        node = self.__head
        while node.next_node:
            data += f'{node.data}\n'
            node = node.next_node

        data += f'{node.data}'
        return data

    def sorted_insert(self, new_data):
        """ int: new node data """
        new_node = Node(new_data)

        # for first node
        if not self.__head:
            self.__head = new_node
            return

        # Adding of new node
        current = self.__head
        while current.next_node:
            current = current.next_node

        current.next_node = new_node
        return

    def sort(self):
        """ int: sort data """

        # Storing all nodes in a list
        raw_nodes = []
        current = self.__head
        while True:
            raw_nodes.append(current)
            if not current.next_node:
                break
            current = current.next_node

        # Sorting
        sorted_nodes = []
        while len(raw_nodes):
            least = raw_nodes[0]
            for n in raw_nodes:
                if n.data <= least.data:
                    least = n
            sorted_nodes.append(least)
            raw_nodes.remove(least)

        # Re-arrange into the node
        counter = 0
        self.__head = sorted_nodes[counter]
        current = self.__head

        while counter < len(sorted_nodes):
            if counter < len(sorted_nodes) - 1:
                current.next_node = sorted_nodes[counter + 1]
                # new current node
                current = sorted_nodes[counter + 1]

            else:
                current.next_node = None

            counter += 1

        return
