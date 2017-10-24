class OOP(object):
    """docstring for OOP
"""

    def __init__(self, name):
        super(OOP, self).__init__()
        self.name = name

    def print_self(self):
    	print(self.name)

oop=OOP("fd");
oop.print_self()