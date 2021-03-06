#!/usr/bin/python3
'''
return subclass or not
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class BaseGeometry'''

    def __init__(self, size):
        '''init conctructer'''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        '''area'''
        return(self.__size * self.__size)
