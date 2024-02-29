from __future__ import annotations

import typing

from . import ev_manager

T_function = typing.TypeVar("T_function", bound=typing.Callable)


class Event(typing.Generic[T_function]):
    """ 
    Base class for events.

    ### Example:
    ```python
    class Example(ev_manager.Event[typing.Callable[[int], None]]):
        pass

    def example_handler(value: int):
        print(value)

    Example.bind(example_handler)

    Example.emit(5)
    """
    @classmethod
    def get_id(cls) -> str:
        """ The id to use when registering the event with the event manager """
        return f"{cls.__module__}.{cls.__name__}"

    @classmethod
    def bind(cls, function: T_function):
        """ Bind a handler to this event """
        ev_manager.bind(cls.get_id(), function)

    @classmethod
    def unbind(cls, function: T_function):
        """ Unbind a handler from this event """
        ev_manager.unbind(cls.get_id(), function)

    @classmethod
    def unbind_all(cls):
        """ Unbind all handlers from this event """
        ev_manager.unbind_all(event=cls.get_id())

    @classmethod
    def is_bound(cls, function: T_function) -> bool:
        """ Check if a function is bound to this event """
        return ev_manager.is_bound(cls.get_id(), function)

    @classmethod
    def emit(cls, *args, **kwargs):
        """ Call all functions bound to this event """
        ev_manager.emit(cls.get_id(), *args, **kwargs)
