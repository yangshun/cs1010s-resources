Recursion, Iteration & Order of Growth
==

##### Recursion
- A function that calls itself is called a recursive function.
- When a problem can be broken down into a smaller problem(s) that has the same method of solving as itself, this is a big hint for you to do recursion.
- Let's revisit our favourite factorial function:
```
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
```
- To calculate `factorial(5)`, we need to calculate `factorial(4)`, and so forth.
- But the function calls cannot go on forever; need to terminate somewhere. 
  - Hence we need a **BASE CASE**. Typically `n = 0` or `n = 1`.
- Assume you know how to solve the problem for `n-1`, how can you use that information to solve the problem for `n`?

###### Types of Recursion
- Linear Recursion:
  - Factorial: `fact(5)` -> `fact(4)` -> `fact(3)` -> `fact(2)` -> `fact(1)` -> `fact(0)`
- Tree Recursion:
  - Fibonacci:
```
def fib(n):
  if n == 0: 
    return 0
  elif n == 1: 
    return 1
  else: 
    return fib(n - 1) + fib(n - 2)
```
- Mutual Recursion
```
def ping(n):
  if (n == 0): 
    return n
  else: 
    print("Ping!")
    pong(n - 1)

def pong(n):
  if (n == 0): 
    return n
  else: 
    print("Pong!")
    ping(n - 1)
```
  - What is the time complexity of `ping`/`pong`?

##### Iteration
- Iteration means a repetition of a mathematical or computational procedure applied to the result of a previous application

###### `while` loop
```
while <expression>:
  <body>
```
- **expression**: a statement that will evaluate to `True` or `False`.
- **body**: block of code that will be evaluated if predicate <expression> is `True`.
- Code within body will have to update variables or contain `break` so that the while loop does not run forever.
```
def factorial(n):
  counter, result = 1, 1
  while counter <= n:
    result *= counter
    counter += 1
  return result
```

###### `for` loop
```
for i in range([start,] stop[, step]):
  <body>
```
- <body> is to be evaluated once for each value of `i`.
- <body> can make use of variable `i` in its code.
- **NOT** necesssary to use `i` in the code.
- **ALL** for loops can be re-written to use `while`. 
  - Just need to create an additional `i` variable that behaves like `counter` in the while example above.
```
def factorial(n):
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result
```

###### `break`
- Stops termination and breaks out of the **current** `while`/`for` loop it is in.

###### `continue`
- Skips the rest of the code for the current iteration. Goes to the next iteration directly (or next value of i).

##### Complexity
- Time: How long it takes to run a program
  - Number of operations/steps
  - Each line in a program can be treated as an operation
- Space: How much memory we need to run the program
  - Variables and functions take up memory space
  - A function is also a variable!

##### Order of Growth
- Rough measure of the resources used by a computational process
- Common complexities:

| Order | Type |
|---|---|
| O(1) | Constant |
| O(n) | Linear |
| O(n^2) | Quadratic |
| O(n^3) | Cubic |
| O(log n) | Logarithmic (Base is not important) |
| O(nlog n) | - |
| O(2^n) | Exponential |
- Identify dominant term, ignore smaller terms
- Ignore additive or multiplicative constants

##### Recursion vs Iteration
- **Recursion** 
  - A recursive process contains deferred operations.
  - This means that the result of some operations are not computed on the spot.
  - They have to be stored in memory and wait for the subsequent recursive calls to return its value.
  - Hence memory space is proportional to the maximum number of recursive calls stored in memory at any point in time.
  - The maximum number of recursive calls is related to **N**.
- **Iteration**
  - An iterative process does not have deferred operations.
  - Variables are used to store the intermediate computation results.
  - Variables are repeatedly overwritten in each iteration. Hence no additional variables are required.
  - Hence memory space is constant. It is not affected by **n**.

###### Recursive Process
- Time is proportional to the number of operations (steps, function calls, etc)

##### Process and Order Comparison
| Process | Time | Space |
| --- | --- | --- |
| Linear Recursion | O(n) | O(n) |
| Tree Recursion (2 branches) | O(2^n) | O(n) |
| For/While Loop | O(n) | O(1) |
| For loop in For loop | O(n^2) | O(1) |

- Note that this list is non-exhaustive and you shouldn't be memorizing it. 
- There are unlimited combinations. E.g. you can put a linear recursive function within a for loop.
- Understand why the complexity is as such for the above table and apply it to any mixed combinations.
