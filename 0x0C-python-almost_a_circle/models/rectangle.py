#!/usr/bin/python3

'''A module that models a rectangle'''

Base = __import__("base").Base


class Rectangle(Base):
    '''A class that models a Rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        A constructor for the Rectangle class

        Args:
            width: int
            height: int
            x: int
            y: int
            y: int
            id: int
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        '''
        A method that returns a custom string showing the class attributess
        '''
        name = type(self).__name__
        ID = self.id
        x = self.x
        y = self.y
        width = self.width
        height = self.height
        return f'[{name}] ({ID}) {x}/{y} - {width}/{height}'

    @property
    def width(self):
        '''A getter function for the width attribute'''
        return self.__width

    @width.setter
    def width(self, width):
        '''
        A setter function for the width attribute

        Args:
            width: int
        '''
        if isinstance(width, (int, float)):
            if width <= 0:
                raise ValueError("width must be > 0")
            self.__width = width
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        '''A getter function for the height attribute'''
        return self.__height

    @height.setter
    def height(self, height):
        '''
        A setter function for the height attribute

        Args:
            height: int
        '''
        if isinstance(height, (int, float)):
            if height <= 0:
                raise ValueError("height must be > 0")
            self.__height = height
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        '''A getter function for the x attribute'''
        return self.__x

    @x.setter
    def x(self, x):
        '''
        A setter function for the x attribute

        Args:
            x: int
        '''
        if isinstance(x, (int, float)):
            if x < 0:
                raise ValueError("x must be >= 0")
            self.__x = x
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        '''A getter function for the y attribute'''
        return self.__y

    @y.setter
    def y(self, y):
        '''
        A setter function for the y attribute

        Args:
            y: int
        '''
        if isinstance(y, (int, float)):
            if y < 0:
                raise ValueError("y must be >= 0")
            self.__y = y
        else:
            raise TypeError("y must be an integer")

    def area(self):
        '''
        A function that returns the area value of the Rectangle isinstance

        Returns:
            area: int/float
        '''
        return self.height * self.width

    def display(self):
        '''
        A function that prints a design representation of a Rectangle
        '''
        for i in range(self.height):
            for j in range(self.width):
                for k in range(self.x):
                    print(' ', end='')
                print("#", end='')
            print()

    def update(self, *args, **kwargs):
        '''
        A function that updates the values of the attributes in the class

        Args:
            *args: tuple
            **kwargs: dict
        Exceptions:
            IndexError
            KeyError
        '''
        if isinstance(args, (list, tuple)):
            if len(args) > 0 and len(args) <= 5:
                try:
                    super().id = args[0]
                    self.width = args[1]
                    self.height = args[2]
                    self.x = args[3]
                    self.y = args[4]
                except IndexError:
                    pass
            else:
                raise ValueError("number of arguments exceed expected number")
        else:
            for attr, value in kwargs.items():
                if not hasattr(self, attr):
                    raise AttributeError(f"invalid attribute name: '{attr}'")
                setattr(self, attr, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle instance.

        Returns:
            dict
        """
        return {
            "x": self.__x,
            "y": self.__y,
            "id": self.id,
            "height": self.__height,
            "width": self.__width,
        }
