#!/usr/bin/env python3

class Shoe:
    pass
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size
    
    def getSize(self):
        return self._size
    
    def setSize(self, size):
        if (type(size) in (int, float)):
            self._size = size
        else:
            print("size must be an integer")
    size = property(getSize, setSize)

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New" 

    