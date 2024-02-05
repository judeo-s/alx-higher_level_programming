#!/usr/bin/python3

'''
A module that has a custom class that inherits the properties of the list class
It also contains a public instance method that prints the list
'''


class MyList(list):
    '''
    A custom class that inherits attributes of the list class
    '''

    def print_sorted(self):
        '''
        A public instance method that prints the list
        '''
        print(sorted(self))
