
cdef class B:
    cdef int _size
    def __init__(self):
        self._size = 42

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        self._size = size

    @property
    def name(self):
        if self.size != 42:
            raise RuntimeError("B has no name")
        else:
            return "forty-two"
