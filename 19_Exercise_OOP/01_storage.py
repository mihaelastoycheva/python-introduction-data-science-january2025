class Storage:
    # storage = []  -> class attribute

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = []

    def add_product(self, product: str):
        if self.capacity > 0:
            self.storage.append(product)
            self.capacity -= 1


    def get_storage(self):
        return self.storage

    # @classmethod
    # def pesho(cls):
    #     pass


storage = Storage(5)  # creating object from class Object

storage.add_product("apple")
storage.add_product("orange")
storage.add_product("lemon")
storage.add_product("banana")

print(storage.get_storage())
