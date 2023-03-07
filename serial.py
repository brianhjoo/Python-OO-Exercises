class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """ Takes a starting value and returns next sequential number """
        self.start = start
        self.curr_val = start
        self.has_been_called = False

    def generate(self):
        """ Displays initial start value, then increments start value by one
         with each call afterwards """

        if not self.has_been_called:
            self.has_been_called = True
            return self.start
        else:
            self.curr_val += 1
            return self.curr_val








