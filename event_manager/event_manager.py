from __future__ import annotations

from typing import Hashable, Callable


def get_event_dict(ensure_exists: bool = False) -> dict | None:
    if ensure_exists and "eventmanager_dict" not in globals():
        new_dict = {}
        globals()["eventmanager_dict"] = new_dict
        return new_dict

    return globals().get("eventmanager_dict")


def get_event_functions(event: Hashable, ensure_exists: bool = False) -> list[Callable] | None:
    event_dict = get_event_dict()
    if ensure_exists and event not in event_dict:
        new_list = []
        event_dict[event] = new_list
        return new_list

    return event_dict.get(event)


def bind(event: Hashable, function: Callable):
    """
    Bind a function to a event

    ### Parameters:
        - event: The event to bind to, identifed by a hasable object, e.g. a string.
        - function: The function to bind
    """
    if not callable(function):
        raise TypeError(f"function must be callable, not {type(function)}")

    events = get_event_functions(event, True)
    if function not in events:
        events.append(function)


def unbind(event: Hashable, function: Callable):
    """
    Unbind a function from a event

    ### Parameters:
        - event: The event to unbind to, identifed by a hasable object, e.g. a string.
        - function: The function to unbind
    """
    events = get_event_functions(event, False)
    if events and function in events:
        events.remove(function)


def unbind_all(event: Hashable | None = None, function: Callable | None = None):
    """
    Unbind all function either globally or from a spesific event

    ### Parameters:
        - event: The event to unbind all functions from, if event is None this function will unbind all functions from all events.
    """
    if event is None:
        event_dict = get_event_dict(False)
        if event_dict:
            event_dict.clear()
    else:
        events = get_event_functions(event, False)
        if events:
            events.clear()


def is_bound(event: Hashable, function: Callable):
    """
    Check if a function is bound to a event

    ### Parameters:
        - event: The event to unbind to, identifed by a hasable object, e.g. a string.
        - function: The function to unbind
    """
    events = get_event_functions(event, False)
    if events:
        return function in events
    return False


def emit(event: Hashable, *args, **kwargs):
    functions = get_event_functions(event)
    if functions:
        for function in functions:
            function(*args, **kwargs)
