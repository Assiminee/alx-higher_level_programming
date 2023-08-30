#!/usr/bin/python3
""" defines a node of a singly linked list """


class Node:
    """ Node class body """
    def __init__(self, data, next_node=None):
        """ initializes an object of the Node class """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ getter for the instance attribute 'data' """
        return self.__data

    @data.setter
    def data(self, value):
        """ setter for the instance attribute 'data' """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ getter for the instance attribute 'next_node' """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ setter for the instance attribute 'next_node' """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


""" defines a singly linked list """


class SinglyLinkedList:
    """ SinglyLinkedList class body """

    def __init__(self):
        """ initializes an object of the SinglyLinkedList class """
        self.__head = None

    def __str__(self):
        """ returns the string representation of the linked list
        sorted in ascending order """
        nodes = []
        while self.__head:
            nodes.append(self.__head.data)
            self.__head = self.__head.next_node
        return "\n".join(str(val) for val in sorted(nodes))

    def sorted_insert(self, value):
        """ inserts a new Node at the beginning of the
        singly linked list """
        new_node = Node(value, self.__head)
        self.__head = new_node
