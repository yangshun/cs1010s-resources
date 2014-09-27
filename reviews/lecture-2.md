Functional Abstraction
==

##### General Form
```python
def <name>(<formal parameters>):
  <body>
```

##### Purpose of Functions
- Input Parameters -> Function -> Output
- Just need to know what a function does
- Don't need to know how it does the job! Hence implementations can differ
- Output of function is determined by `return`. Function terminates when a value is returned
- What if function does not return anything? The return value will be `None`

##### Variable Scope
```python
x = 10
def square(x):
  return x * x

square(5) # => 25 not 100
# A new local variable x is created when the function parameter is also called x

def addx(y):
  return y + x

addx(3) # => 13
# If no x is found among the function parameters, x in the function will be bound to the x in the outer scope

pi = 22/7

def circle(radius):
  pi = 3.14
  return pi * radius * radius

circle(1) # => 3.14
# A local variable pi is created within circle, hence subsequent reference 
# to pi in the function will refer to the local variable
```
