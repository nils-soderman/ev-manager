# ev-manager (Event Manager)

Useful when working with DCCs like Maya, MotionBuilder, Unreal Engine, etc. and you want different tools/scripts to communicate with each other.

## Installation:
```batch
pip install ev-manager
```

## Examples:

```python
import ev_manager

def hello_world():
    print("Hello World")

ev_manager.bind(hello_world, "MyEvent")
```

```python
>>> import ev_manager
>>> ev_manager.emit("MyEvent")
>>> "Hello World"
```

## Limitations:
Events are per Python instance. So they will for example not be communicating between different applications.