# eventmanager

## Installation:
```batch
pip install eventmanager
```

## Examples:

```python
import eventmanager

def hello_world():
    print("Hello World")

eventmanager.bind(hello_world, "MyEvent")
```

```python
>>> import eventmanager
>>> eventmanager.emit("MyEvent")
>>> "Hello World"
```



## Limitations:
Events are per Python instance. So they will for example not be communicating between different applications.