Introduction to CS1010S & Python
==

##### Variables
- Start with 'a' to 'z' or 'A' to 'Z' or '_'
- Contain only alphanumeric characters or '_'
- Case-sensitive! Applies to functions too. Because functions are also variables!

##### Types
- `int`: 8, 45, 1234
- `float`: 2.3, 3.141592653
- `bool`: `True`, `False`
- `str`: `"CS1010S"`, `"cs1010s"`, `"CS 1010S"`. Note that spaces are characters too!
- `None`: Keyword representing null
- Convert between types using `int()`, `float()`, `str()`

##### Assignment
- `abc = 28`
- `my_string = 'This is a string.'`
- Shorthand assignment: `a, b = 1, 2`

##### Operators
- Arithmetic: `+`, `-`, `*`, `/`, `**`, `//`, `%`
- Comparison: `>`, `>=`,`<`, `<=`, `==`, `!=`
- Boolean: `and`, `or`, `not`

##### Truth Values
- `False`: 
  - `None`
  - `False`
  - Zero of any numeric type: `0`, `0.0`
  - Any empty sequence: `''`, `()`, `[]`
  - Any empty mapping: `{}`
  - ```
    >>> False == 0 # True
    ```
- `True`:
  - Any non-`False` value
  - ```
    >>> True == 1 # True
    ```

##### Conditional
```
# Standard Usage
a = 1
if a < 2:
  b = a * 2
else:
  b = a * 3

# Ternary Operator
b = a * 2 if a < 2 else a * 3
```
- Must an `if` statement be used together with `else`? **NO**.
- Differentiate between
```
if a > 0:
  print('a > 0')
elif a == 0:
  print('a == 0')
elif a %= 2:
  print('a divisible by 2')
else:
  print('a < 0')
```
VS
```
if a > 0:
  print('a > 0')
if a == 0:
  print('a == 0')
if a %= 2:
  print('a divisible by 2')
else:
  print('a < 0')
```

##### String
- `+` is used to concatenate (join) strings together
- There is no usage of `-` for strings!
- `*` is used to join multiple instances of that string together
- `in` is used to check for existence of a string within another string
- Comparison operators will compare strings in dictionary order. Strings that appear behind in the dictionary have a bigger value.
```
'a' < 'b' # True
'a' < 'ab' # True
```
- A string is a sequence of characters, and can be indexed. First character is indexed with 0.
- `s[start:stop:step]`. Note that the `stop` parameter is non-inclusive.
- Ommitting `start`/`stop` implies the initial/end respectively
```
s = 'abcdef'
s[0:2] # => 'ab'
s[1:2] # => 'b'
s[:2] # => 'ab'
s[1:5:3] # => 'be'
s[::2] # => 'ace'
```
