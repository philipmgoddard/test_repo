print("hello world")

class Dexter():
    def __init__(self, hats):
        self.rats = hats * 3

    def __call__(self):
        print([x for x in range(3) if x != 1])

class Phil(Dexter):
    def __init__(self):
        super().__init__()


print("frogs")
