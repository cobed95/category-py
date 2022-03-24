from typing import Callable, Generic, TypeVar

A = TypeVar("A")
B = TypeVar("B")
C = TypeVar("C")


class Morphism1(Generic[A, B]):
    def __init__(self, f: Callable[[A], B]) -> None:
        self._f = f

    def compose(self, other: "Morphism1[B, C]") -> "Morphism1[A, C]":
        def _composed(a: A) -> C:
            return other(self(a))

        return Morphism1(_composed)

    def __call__(self, a: A) -> B:
        return self._f(a)

    def __or__(self, other: "Morphism1[B, C]") -> "Morphism1[A, C]":
        return self.compose(other)


Morphism = Morphism1
