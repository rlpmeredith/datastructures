class LinkedList:
    
    def __init__(self):
        """Constructor to set up list control"""
        self.head = None
        self.list_len = 0

    def insert_front(self, value):
        """ Insert an item at the front of the list """
        new_node = Node(None, value)
        new_node.set_next(self.head)
        self.head = new_node
        self.list_len += 1

    def pop_front(self):
        """ Remove an item from the front of the list

        Returns:
        pop_value: value popped
        """
        pop_value = self.head.get_value()
        self.head = self.head.get_next()
        self.list_len -= 1
        return pop_value


    def __len__(self):
        """ Returns the length of the list

        Returns:
        count: length of list
        """
        cur_node = self.head
        count = 0
        while cur_node:
            count += 1
            cur_node = cur_node.get_next()
        return count

    def delete(self, value):
        """Searches and deletes all instances of value

        Parameters:
        value: value to be deleted
        """

        cur_node = self.head
        prev_node = None
        while cur_node is not None:
            if cur_node.get_value() == value:
                if cur_node == self.head:
                   self.head = cur_node.get_next()
                   cur_node = cur_node.get_next()
                   self.list_len -= 1
                else:
                    prev_node.next_node = cur_node.get_next()
                    cur_node = cur_node.get_next()
                    self.list_len -= 1
            else:
                prev_node = cur_node
                cur_node = cur_node.get_next()

    def reverse(self):
        """Reverses order of list """

        cur_node = self.head
        prev_node = None
        next_node = None
        while cur_node is not None:
            next_node = cur_node.next_node
            cur_node.next_node = prev_node
            prev_node = cur_node
            cur_node = next_node
        self.head = prev_node

    def to_array(self):
        result = list()
        cur_node = self.head
        while cur_node is not None:
            result.append(cur_node.value)
            cur_node = cur_node.next_node
        return result

    def __iter__(self):
        current = self.head
        for i in range(len(self)):
            yield current.value
            current = current.next_node

class Node:

    def __init__(self, next_node = None, value = None):
        """Constructor for node

        Parameters:
        next_node: next node object
        value: node data
        """
        self.next_node = next_node
        self.value = value

    def get_value(self):
        """Get data from node

        Returns:
        value: node data
        """
        return self.value

    def get_next(self):
        """Get reference to next node

        Returns:
        Reference to next node
        """
        return self.next_node

    def set_next(self, new_next):
        """Set next node object

        Parameters:
        new_next: next node object
        """
        self.next_node = new_next

