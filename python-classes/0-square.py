#!/usr/bin/python3
"""Module defines a Square class."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size):
        """Initialize a new Square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
