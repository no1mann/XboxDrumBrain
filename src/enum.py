# Enumeration representation using classes
class Enum(object):
    class __metaclass__(type):
        def __iter__(self):
            for i in self.__dict__:
                if i == self.__dict__[i]:
                    yield i
