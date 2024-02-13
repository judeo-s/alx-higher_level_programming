#!/usr/bin/python3

'''A module that models a square'''

Rectangle = __import__("rectangle").Rectangle


class Square(Rectangle):
    '''A class that models a Square'''

    def __init__(self, size, x=0, y=0, id=None):
        '''
        A constructor that defines and initializes all attributes of the class

        Args:
            size: int
            x: int
            y: int
            id: int
        '''
        super().__init__(size, size,  x, y, id)
        self.size = size

    def __str__(self):
        '''
        A method that returns a custom string showing the class attributes
        '''
        name = self.__class__.__name__
        ID = self.id
        x = self.x
        y = self.y
        size = self.width

        return f"[{name}] ({ID}) {x}/{y} - {size}"

    @property
    def size(self):
        '''A function that returns the size of a square'''
        return self.width

    @size.setter
    def size(self, width):
        '''
        A function that sets the value of the size attribute of a square

        Args:
            width: int
        '''
        self.width = width
        self.height = width

    def update(self, *args, **kwargs):
        '''
        A function that updates the values in the Square class

        Args:
            *args: tuple
            **kwargs: dict
        Exceptions:
            IndexError
            KeyError
        '''
        if isinstance(*args, (list, tuple)):
            if len(args) > 0 and len(args) <= 4:
                try:
                    self.id = args[0]
                    self.size = args[1]
                    self.x = args[2]
                    self.y = args[3]
                except IndexError:
                    pass
            else:
                raise ValueError("number of arguments exceed expected number")
        else:
            for attr, value in kwargs.items():
                if not hasattr(self, attr):
                    raise AttributeError(f"invalid attribute name: '{attr}'")

                setattr(self, attr, value)

    def to_dictionary(self) -> dict:
        """
        Returns the dictionary representation of a Square instance.

        Returns:
            dict
        """
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y,
        }
