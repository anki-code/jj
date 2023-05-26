<p align="center">
<b>enJoy Json</b> (JJ) is to syntax highlighting and formatting the json, javascript or python dict object in error-tolerant manner.
</p>

<p align="center">
If you like the idea click ⭐ on the repo and <a href="https://twitter.com/intent/tweet?text=Nice%20xontrib%20for%20the%20xonsh%20shell!&url=https://github.com/xonsh/xontrib-jupyter" target="_blank">tweet</a>.
</p>


## Installation

To install use PyPi:

```xsh
pip install git+https://github.com/anki-code/jj
```

## Usage

### Get json from stream
```xsh
echo '{"name": "John Doe", \'age\': 30, "city": "New York"}' | jj
```
```json
{
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
```

### In case of object error

```xsh
echo '{"name":' | jj
# JSON dict error: Expecting value: line 2 column 1 (char 9)
# Python dict error: '{' was never closed (<unknown>, line 1)
# JavaScript dict error: Unexpected end of input
```
