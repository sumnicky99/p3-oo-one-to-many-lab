# Define a class named 'Pet'
class Pet:
    # Class variable to hold possible pet types
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    # Class variable to store all instances of Pet
    all = []

    # Constructor method to initialize instance variables
    def __init__(self, name, pet_type, owner=None):
        self.name = name  # Assign the name of the pet
        self.pet_type = pet_type  # Assign the type of the pet
        self.owner = owner  # Assign the owner of the pet (defaults to None)
        Pet.all.append(self)  # Add the current instance to the list of all pets

    # Getter method for the pet_type property
    @property
    def pet_type(self):
        return self._pet_type

    # Setter method for the pet_type property
    @pet_type.setter
    def pet_type(self, pet_type):
        # Check if the provided pet_type is valid
        if pet_type not in self.PET_TYPES:
            # Raise an exception if the pet_type is not valid
            raise Exception('Not a valid pet type.')
        self._pet_type = pet_type  # Set the pet_type if it is valid

    # Getter method for the owner property
    @property
    def owner(self):
        return self._owner

    # Setter method for the owner property
    @owner.setter
    def owner(self, owner):
        # Check if the provided owner is of type Owner or None
        if not (isinstance(owner, Owner) or not owner):
            # Raise an exception if the provided owner is not of type Owner or None
            raise Exception("Object is not of type Owner")
        self._owner = owner  # Set the owner if it is valid

# Define a class named 'Owner'
class Owner:
    # Constructor method to initialize the name of the owner
    def __init__(self, name):
        self.name = name  # Assign the name of the owner

    # Method to get all pets owned by this owner
    def pets(self):
        # Return a list comprehension filtering pets by the current owner
        return [pet for pet in Pet.all if pet.owner == self]

    # Method to add a pet to this owner
    def add_pet(self, pet):
        # Check if the provided object is of type Pet
        if not isinstance(pet, Pet):
            # Raise an exception if the provided object is not of type Pet
            raise Exception("Input object is not of type Pet")
        pet.owner = self  # Set the owner of the provided pet to this owner

    # Method to get sorted list of pets owned by this owner
    def get_sorted_pets(self):
        # Return a sorted list of pets based on their names
        return sorted(self.pets(), key=lambda pet: pet.name)
