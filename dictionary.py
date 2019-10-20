from linked_list import LinkedList

class CustomDictionary:

    def __init__(self, dictlen):
        self._dictlen = dictlen
        self._data = [None] * self._dictlen

    def set(self, key, value):
        dict_loc = self.get_index(key)
        dict_tuple = tuple([key, value])
        if self._data[dict_loc] is None:
            newlist = LinkedList()
            self._data[dict_loc] = newlist
        self._data[dict_loc].insert_front(dict_tuple)
        if len(self._data[dict_loc]) > 5:
            self.expand()

    def get(self, key):
        dict_loc = self.get_index(key)
        indexlist = self._data[dict_loc]
        if indexlist is None:
            return None
        for i in indexlist:
            if i[0] == key:
                return i[1]
        return None

    def contains(self, key):
        dict_loc = self.get_index(key)
        indexlist = self._data[dict_loc]
        if indexlist is None:
            return False
        for i in indexlist:
            if i[0] == key:
                return True
        return False

    def get_index(self, key):
        dict_loc = hash(key) % self._dictlen
        return dict_loc

    def delete(self, key):
        dict_loc = self.get_index(key)
        indexlist = self._data[dict_loc]
        if indexlist is None:
            return None
        for i in indexlist:
            if i[0] == key:
                deltuple = i
        indexlist.delete(deltuple)
        return None

    def expand(self):
        templist = []
        for i in self._data:
            if i is not None:
                for j in i:
                    templist.append(j)
        self._dictlen = self._dictlen * 2
        self._data.clear()
        self._data = [None] * self._dictlen
        for k in templist:
            self.set(k[0], k[1])

