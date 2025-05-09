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
    def __init__(self, name: str = "Brian", breed: str = "Shar Pei"):
        self.name = name  
        self.breed = breed 
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, new_name: str):
        if not isinstance(new_name, str) or not (1 <= len(new_name) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = new_name

    @property
    def breed(self) -> str:
        return self._breed
    
    @breed.setter
    def breed(self, new_breed: str):
        if new_breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = new_breed