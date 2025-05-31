class Pet:
    PET_TYPES = ["dog",
                 "cat",
                 "rodent",
                 "bird",
                 "reptile",
                 "exotic"]
    
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner class.")
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, value):
        if value not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {value}.")
        self._pet_type = value


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Pet must be an instance of Pet class")
        pet.owner = self

    def get_sorted_pets(self):
        sorted_pets = sorted(self.pets(), key=lambda pet: pet.name)
        if not all(isinstance(p, Pet) for p in sorted_pets):
            raise Exception("All items must be Pet instnaces.")
        return sorted_pets