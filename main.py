class House:
    def __init__(self):
        self.numberOfFloors = 0

    def set_new_number_of_floors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)


if __name__ == '__main__':
    house = House()
    house.set_new_number_of_floors(7)
