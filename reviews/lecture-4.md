Higher Order Functions
==

##### Importing Modules
- `import X` imports the module `X` 
  - Can use `X.func()` to refer to a function defined in `X`
- `from X import *` imports the module X, and creates references to all public objects in X
  - Simply use `func()`. Don't need to prefix with `X`
- `from X import a, b, c` imports the module X and creates references to the specified objects
  - Can use `a`, `b`, and `c` in your program

##### Lambdas
- `lambda`s are functions defined in **one** line.
```
lambda <params>: <return value>
```
- Compare these two snippets
```
def f(a):
  return a * 2

f = lambda a: a * 2
```
- They are the same.
- Must a `lambda` accept parameters? NO. Just like functions do not have to.
- When you do `def f(...)`, you are actually creating a variable called `f` of the function type.

##### Higher Order Functions
1. Functions can be inputs to other functions
2. Functions can be return values from other functions
3. Both 1 & 2 can happen at the same time!

##### Functions as return values
```
def make_x_multiplier(n):
  return lambda x: x * n

multiply3 = make_x_multiplier(3):
type(multiply3) # => <class 'function'>
multiply3(4) # => 12
multiply5 = make_x_multiplier(5):
multiply5(4) # => 20
```

##### Higher Order Functions
- Just need to know `fold2`, because `sum`, `product` and `fold` are more specific versions of `fold2`.
- Don't have to memorize because they are given in appendix. But you need to note what each parameter represents.