# ev-manager (Event Manager)

Useful when working with DCCs like Maya, MotionBuilder, Unreal Engine, etc. and you want different tools/scripts to communicate with each other.

## Installation:
```batch
pip install ev-manager
```

## Examples:

### Using classes:

```python
""" my_module.py """

from typing import Callable
from ev_manager import Event

class ExampleEvent(Event[Callable[[int], None]]):
    pass

def my_callback(value: int):
    print(f"Number: {value}")

ExampleEvent.bind(my_callback)
```

```python
>>> from my_module import ExampleEvent
>>> ExampleEvent.emit(5)
>>> "Number: 5"
```


### Using functions:

```python
import ev_manager

def hello_world():
    print("Hello World!")

ev_manager.bind("MyEvent", hello_world)
```

```python
>>> import ev_manager
>>> ev_manager.emit("MyEvent")
>>> "Hello World!"
```


## Available functions:

| Function | Description |
| --- | --- |
| `bind(event, function)` | Bind a function to an event. |
| `unbind(event, function)` | Unbind a function from an event. |
| `unbind_all(*, event, function)` | Either unbind all functions from an event or unbind a function from all events. |
| `is_bound(event, function)` | Check if a function is bound to an event. |
| `emit(event, *args, **kwargs)` | Call all functions bound to an event. |


## Limitations:
Events are per Python instance. So they will for example not be communicating between different applications.