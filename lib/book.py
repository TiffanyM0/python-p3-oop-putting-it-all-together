#!/usr/bin/env python3

class Book:
    pass
    def __init__(self, title, page_count):
        self.title = title
        self._page_count= page_count
    
    def getPageCount(self):
        return self._page_count 
    
    def setPageCount(self, page_count):
        if (type(page_count) in (int, float)):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    page_count = property(getPageCount, setPageCount)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        