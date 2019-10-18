class Stack:

    def __init__(self):
        """Constructor to set up data type using a Python list"""
        self._data = list()

    def push(self, item):
        """Pushes an item to the stack

        Parameters:
        item: item to add to stack
        """
        self._data.append(item)

    def pop(self):
        """Pops an item from the stack"

        Returns:
        item: item popped from stack
        """
        if len(self) < 1 :
            raise Exception('Stack is empty')
        item = self._data[-1]
        del self._data[-1]
        return item

    def peek(self):
        """Peeks the top of the stack

        Returns:
        item: top of stack
        """
        return self._data[-1]

    def __len__(self):
        """Length of stack

        Returns:
        Length of stack
        """
        return len(self._data)
