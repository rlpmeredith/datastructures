class Queue:
    
    def __init__(self):
        self._data = list()
    
    def enqueue(self, item):
        """Add item to the queue.

        Parameters:
        item: item to add to the queue
        """
        self._data.append(item)
            
    def dequeue(self):
        """Remove item from the queue.

        Returns:
        item: First item in queue
        """
        item = self._data[0]
        del self._data[0]
        return item

    def peek(self):
        """Return first item in queue

        Returns:
        item: First item in queue
        """
        return(self._data[0])

    def __len__(self):
        """Length of queue

        Returns:
        length: Length of queue
        """
        return len(self._data)
