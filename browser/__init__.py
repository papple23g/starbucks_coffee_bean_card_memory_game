"""
Mock brython functions for local testing and debugging.

WHen installed with pip running a script containing brython calls will catch syntax errors 
without hitting unresolved brython calls

$ python devel_script.py

The script can also be debugged using idle, our your IDE of choice
"""

"""
class _mockbrython1(dict):
    items = []

    def __le__(self, other):
        self.items.append(other)

    def __missing__(self, attr):
        return _mockbrython()

    def __getattr__(self, attr):
        return _mockbrython()

    def __setattr__(self, attr, value):
        pass

    def __hash__(self):
        return 0

"""




from _collections_abc import dict_values
from typing import Any, Callable
from .html import EV
class ClassList():
    def add(self, cls: str) -> None:
        pass

    def remove(self, cls: str) -> None:
        pass


class Query():
    def getvalue(self) -> Any:
        pass


class _mockbrython(dict):
    def __init__(self, *args, **kwargs):
        self.style = self  # _mockbrython1()
        self.args = args
        self.kwargs = kwargs
        for k, v in kwargs.items():
            setattr(self, k, v)
        pass

    def __call__(self, *args, **kwargs):
        return self

    def __le__(self, other):
        pass

    def __add__(self, other):
        """ Brython overloads the add operater to concatenate 2 brython objects
            We mock this by returning a _mockbrython, 
            except where the other operand is an int when we return a zero
        """

        if type(other) == _mockbrython:
            return self
        else:
            return 0

    def __radd__(self, other):
        """ and make symmetric """
        if type(other) == _mockbrython:
            return self
        else:
            return 0

    def __sub__(self, other):
        return 0

    def __int__(self):
        return 0

    def __mul__(self, other):
        return 0

    def __truediv__(self, other):
        return 0

    def __getattr__(self, attr):
        return self

    def __getitem__(self, attr):
        return self

    def __eq__(self, other):
        return True

    def __hash__(self):
        return 0

    def bind(self, event_str: str, func: Callable[[EV], Any]):
        pass

    def unbind(self, event_str: str, func: Callable[[EV], Any]):
        pass

    @property
    def value(self) -> Any:
        pass

    @property
    def text(self) -> Any:
        pass

    @property
    def classList(self) -> ClassList:
        pass

    @property
    def children(self) -> list['_mockbrython']:
        pass

    @property
    def query(self) -> Query:
        pass

    @property
    def createElement(self) -> '_mockbrython':
        pass


document = _mockbrython()
doc = _mockbrython()


def alert(*args, **kwargs):
    pass


""" This is not what @bind does in real life. 
    We just supply a hook that can be called to exercise the event handler
"""


def bind(target, evt):
    def decorator(func):
        def wrapper(evt):
            func(evt)
        return wrapper
    return decorator


self = _mockbrython()


class DOMEvent:
    def __init__(self, id):
        self.currentTarget = _mockbrython(id=id)
        self.target = _mockbrython(id=id)

    def preventDefault(self):
        pass
