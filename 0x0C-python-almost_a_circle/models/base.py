#!/usr/bin/python3
"""Defines the base class"""
import json
import csv
import turtle


class Base:
    """base project class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes the base class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """prints the json string representation
        of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string to file"""
        js_str = '[]'
        js_list = []
        if list_objs is not None:
            for i in list_objs:
                js_list.append(i.to_dictionary())
            if len(js_list) > 0:
                js_str = Base.to_json_string(js_list)
        with open(cls.__name__ + '.json', 'w') as n:
            n.write(js_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of JSON string
        representation of json_string"""
        if json_string is None or len(json_string) == 0:
            return list()
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attrs already set"""
        a = None
        if cls.__name__ == "Square":
            a = cls(1)
        elif cls.__name__ == "Rectangle":
            a = cls(1, 1)
        cls.update(a, **dictionary)
        return a

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        obj_list = []
        try:
            with open(cls.__name__ + '.json', 'r', encoding='utf-8') as n:
                list_output = cls.from_json_string(n.read())
                for i in list_output:
                    obj_list.append(cls.create(**i))
        except Exception:
            pass
        return obj_list

    @staticmethod
    def draw_square(turt, x, y, size):
        """Draws a square using a turtle object"""

        turt.showturtle()
        turt.up()
        turt.goto(x, y)
        turt.down()
        turt.goto(x, y)
        for i in range(4):
            turt.forward(size)
            turt.left(90)
        turt.hideturtle()

    @staticmethod
    def draw_rect(turt, x, y, width, height):
        """Draws a rectangle using a turtle object"""

        turt.showturtle()
        turt.up()
        turt.goto(x, y)
        turt.down()
        turt.goto(x, y)
        for i in range(2):
            turt.forward(width)
            turt.left(90)
            turt.forward(height)
            turt.left(90)
        turt.hideturtle()

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module"""
        turt = turtle.Turtle()
        turt.screen.bgcolor("green")
        turt.pensize(2)
        turt.shape("turtle")

        turt.color("beige")
        for rect in list_rectangles:
            Base.draw_rect(turt, rect.x, rect.y, rect.width, rect.height)

        turt.color("blue")
        for sq in list_squares:
            Base.draw_square(turt, sq.x, sq.y, sq.size)
        turtle.exitonclick()

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes to file.csv"""
        with open(cls.__name__ + '.csv', 'w', newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write('[]')
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                write = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for i in list_objs:
                    write.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """loads data from file.csv"""
        try:
            with open(cls.__name__ + '.csv', 'r', newline='') as csvfile:
                if cls.__name__ == 'Rectangle':
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                list_dict = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dict = [dict([i, int(j)] for i, j in k.items())
                             for k in list_dict]
                return [cls.create(**k) for k in list_dict]
        except IOError:
            return []


    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares.
        Args:
           - list_rectangles: list of all rectangles
           - list_squares: list of all squares
        """

        import turtle
        import time
        from random import randrange

        t = turtle.Turtle()
        turtle.bgcolor("white")
        t.color("black", "cyan")
        t.pensize(5)
        t.shape("square")

        for i in (list_rectangles + list_squares):
            t.penup()
            t.setpos(0, 0)
            turtle.Screen().colormode(255)
            t.pencolor((randrange(255), randrange(255), randrange(255)))
            Base.draw_rect(t, i)
            time.sleep(1)
        time.sleep(5)

    @staticmethod
    def draw_rect(t, rect):
        """Method to draw a rectangle or square."""

        t.penup()
        t.setpos(rect.x, rect.y)
        t.pendown()
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
        t.left(90)
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
