from abc import ABC
from abc import ABCMeta
from collections.abc import MutableSequence
from numbers import Complex


class Numero(Complex):
    def __getitem__(self, item):
        super().__getitem__()

num = Numero()
