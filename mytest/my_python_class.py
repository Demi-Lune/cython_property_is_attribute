class A:
    @property
    def size(self):
        return 42

    @property
    def name(self):
        raise RuntimeError("A has no name")
