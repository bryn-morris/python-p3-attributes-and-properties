#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:

    def __init__(self, name = "dog", breed = "Pug"):
        self.name = name
        self.breed = breed

    def name_getter(self):
        return self._name
    
    def name_setter(self, name):
        if (type(name) == str) and (1 <= len(name) <= 25):
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    def breed_getter(self):
        return self._breed

    def breed_setter(self,breed):
        if(breed in APPROVED_BREEDS):
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")  
    
    
    name = property(name_getter,name_setter,)
    breed = property(breed_getter, breed_setter)

     

        
