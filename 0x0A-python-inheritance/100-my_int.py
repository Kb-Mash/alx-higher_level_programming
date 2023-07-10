#!/usr/bin/python3
"""a class MyInt that inherits from int"""


class MyInt(int):
    """== and != operators inverted"""

    def __eq__(self, value):
        """override == opeartor with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """override != operator with == behavior"""
        return self.real == value
