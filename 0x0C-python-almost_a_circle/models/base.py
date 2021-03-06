#!/usr/bin/python3
'''
create base class
'''
import json
import turtle


class Base:
    '''create new classe named base'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''method of class'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''share data with json format'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return("[]")
        return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        '''save to file'''
        if list_objs:
            liste = []
            for arg in list_objs:
                liste.append(cls.to_dictionary(arg))
        with open(cls.__name__ + ".json",
                  "w", encoding='utf-8') as File:
            x = cls.to_json_string(liste)
            File.write(x)

    @staticmethod
    def from_json_string(json_string):
        '''json to list'''
        if json_string is None or len(json_string) == 0:
            return([])
        else:
            return(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        '''class create'''
        if cls.__name__ == "Square":
            new = cls(1)
        elif cls.__name__ == "Rectangle":
            new = cls(1, 1)
        new.update(**dictionary)
        return(new)

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''draws turtle'''
        for i in list_rectangles:
            rectngle = turtle.Turtle()
            rectngle.setpos(i.x, i.y)
            rectngle.pendown()
            rectngle.forward(i.width)
            rectngle.left(90)
            rectngle.forward(i.height)
            rectngle.left(90)
        for i in list_squares:
            sq = turtle.Turtle()
            sq.setpos(i.x, i.y)
            sq.pendown()
            t.begin_fill()
            for i in range(4):
                rectngle.forward(i.size)
                rectngle.left(90)
