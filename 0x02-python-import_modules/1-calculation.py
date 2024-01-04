#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    operators = {"+": add, "-": sub, "*": mul, "/": div}

    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, calculator(a, b)))
    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, calculator(a, b)))
    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, calculator(a, b)))
    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, calculator(a, b)))
