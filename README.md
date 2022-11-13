# event_manager

## Installation:
```batch
pip install event_manager
```

## Examples:

```python
import event_manager

def hello_world():
    print("Hello World")

event_manager.bind(hello_world, "MyEvent")
```

```python
>>> import event_manager
>>> event_manager.emit("MyEvent")
>>> "Hello World"
```



## Limitations:
Events are per Python instance. So they will for example not be commuicating between different applications.