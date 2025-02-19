class Catalogue:

    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product: str):  # self - accessing from the instance of the class
        self.products.append(product)

    # ? class method
    # ? static method

    def get_by_letter(self, first_letter: str):
        return [product for product in self.products if product[0] == first_letter]

    def __repr__(self):  # similar to toString() | method to return the result
        return (f"Items in the {self.name} catalogue: \n"
                f"\n". join(sorted(self.products)))


catalogue = Catalogue("Furniture")

catalogue.add_product("Sofa")
catalogue.add_product("Desk")
catalogue.add_product("Mirror")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")

print(catalogue.get_by_letter("C"))
print(catalogue)
