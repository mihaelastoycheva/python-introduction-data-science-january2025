class Building:
    elevator_capacity = 4
    stairs_lights = 20

# @classmethod   -> decorator
# @property

    def __init__(self, name: str, last_name: str):  # Constructor
        # self._name = name          -> the "_name" with underscore means protected
        # self.__name = name         -> the "__name" with underscore means private
        self.name = name  # self = this
        self.last_name = last_name

    def change_last_name(self, new_name: str):  # in classes def is called methods (not functions)
        self.last_name = new_name


# class Apartment(Building):    -> Apartment extends Building
#     def __init__(self):
#         super().__init__()


foreigner = Building("George", "Smith")
foreigner_name = foreigner.name

print(foreigner.__dict__)  # return all attributes of the object
print(Building.elevator_capacity)

#  instance attribute outside the constructor:
foreigner.favorite_song = "Smoke on the water"

foreigner.change_last_name("Brown")
print(foreigner.last_name)
