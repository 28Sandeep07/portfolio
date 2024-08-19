## @file example.py
#  This file demonstrates the use of Doxygen for Python code.

## @brief A simple example class.
#
#  This class is used to illustrate how to document Python code with Doxygen.
class Example:
    ## @brief Initialize the Example class.
    #
    #  @param value The initial value for the Example instance.
    def __init__(self, value):
        """
        Initialize the Example class.
        """
        self.value = value

    ## @brief Get the value.
    #
    #  @return The current value of the instance.
    def get_value(self):
        """
        Return the current value.
        """
        return self.value

    ## @brief Set a new value.
    #
    #  @param new_value The new value to set.
    def set_value(self, new_value):
        """
        Set a new value.
        """
        self.value = new_value
