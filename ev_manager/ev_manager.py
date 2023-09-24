from __future__ import annotations

from typing import Hashable, Callable


def get_event_dict(ensure_exists: bool = False) -> dict | None:
    """ 
    Get the event dictionary. The dictionary is a reference to the actual dictionary, so it can be modified.
    Returns None if the dictionary does not yet exist and ensure_exists is False.

    ### Parameters:
        - ensure_exists: If True, ensure that the dictionary exists.
    """
    if ensure_exists and "eventmanager_dict" not in globals():
        new_dict = {}
        globals()["eventmanager_dict"] = new_dict
        return new_dict

    return globals().get("eventmanager_dict")


def get_event_functions(event: Hashable, ensure_exists: bool = False) -> list[Callable] | None:
    """ 
    Get the list of functions bound to a event. The list is a reference to the actual list, so it can be modified.
    Returns None if the event does not yet exist and ensure_exists is False.

    ### Parameters:
        - event: The event to get the functions for, identifed by a hasable object, e.g. a string.
        - ensure_exists: If True, ensure that the event exists and return an empty list that can be modified.
    """
    event_dict = get_event_dict(ensure_exists)
    if ensure_exists and event not in event_dict:
        new_list = []
        event_dict[event] = new_list
        return new_list

    if not event_dict:
        return None

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

    functions = get_event_functions(event, True)
    if functions is not None and function not in functions:
        functions.append(function)


def unbind(event: Hashable, function: Callable, by_ref: bool = False):
    """
    Unbind a function from a event

    ### Parameters:
        - event: The event to unbind to, identifed by a hasable object, e.g. a string.
        - function: The function to unbind
        - by_ref: If True, unbind the function by reference, otherwise unbind by name
    """
    functions = get_event_functions(event, False)
    if functions:
        if by_ref:
            if function in functions:
                functions.remove(function)
        else:
            for func in functions:
                if func.__module__ == function.__module__ and func.__name__ == function.__name__:
                    functions.remove(func)


def unbind_all(*, event: Hashable | None = None, function: Callable | None = None, by_ref: bool = False):
    """
    Unbind all functions from a event or unbind a function from all events.

    ### Parameters:
        - event: If provided, unbind all functions from this event
        - function: If provided, unbind this function from all events
        - by_ref: If True, unbind the function by reference, otherwise unbind by name (Only applicable if function is provided)
    """
    if event:
        functions = get_event_functions(event, False)
        if functions:
            functions.clear()
    if function:
        event_dict = get_event_dict(False)
        if event_dict:
            for functions in event_dict.values():
                if by_ref:
                    if function in functions:
                        functions.remove(function)
                else:
                    for func in list(functions):
                        if func.__module__ == function.__module__ and func.__name__ == function.__name__:
                            functions.remove(func)


def is_bound(event: Hashable, function: Callable, by_ref: bool = False) -> bool:
    """
    Check if a function is bound to a event

    ### Parameters:
        - event: The event to unbind to, identifed by a hasable object, e.g. a string.
        - function: The function to unbind
        - by_ref: If True, check if the function is bound by reference, otherwise check by name
    """
    functions = get_event_functions(event, False)
    if functions:
        if by_ref:
            return function in functions
        else:
            for func in functions:
                if func.__module__ == function.__module__ and func.__name__ == function.__name__:
                    return True
    return False


def emit(event: Hashable, *args, **kwargs):
    """
    Call all functions bound to a specific event.

    ### Parameters:
        - event: The event to emit, identifed by a hasable object, e.g. a string.
        - args: Optional arguments to pass to the bound functions
        - kwargs: Optional keyword arguments to pass to the bound functions
    """
    functions = get_event_functions(event)
    if functions:
        for function in functions:
            function(*args, **kwargs)
