Data Abstraction
==

##### Data Abstraction
- Abstracts away irrelevant details, exposes what is necessary.
- Separates usage from implementation.
- Serves as a building block for other compound data.

##### Guidelines for Creating Compound Data
- Constructors
  - Means to create compound data from primitive data
- Selectors (accessors)
  - Means to access individual components of compound data
- Predicates
  - Means to ask `True`/`False` questions about the compound data
- Printers
  - Means to display compound data in human-readable form

##### Tuples
- A new data type to store data in a sequential form
- Data can be accessed via index
- Tuples can store tuples within itself
- Slicing syntax is the same as string slicing syntax
- What is the syntax for a tuple with a single element?

##### Tuple Selectors
- `foo`:returns all the elements of `foo`
- `foo[0]`: returns 1st element of `foo`
- `foo[1:]`: returns tail of `foo` (rest of `foo` without 1st element)
- `foo[a:b]`: returns tuple consisting of the (a+1)th to the bth element of `foo`, i.e. b is not inclusive
- `foo[a:b:c]`: returns tuple consisting of the (a+1)th to the bth element of `foo`, i.e. b is not inclusive, at intervals of c
- `foo[-1]`: returns last element of `foo`, i.e. 1st element from the back
- `len(foo)`: return number of elements of `foo`

```
x = (1, 2, 3, 4, 5)
x[0] # => 1
x[1:] # => (2, 3, 4, 5)
x[0:] # => (1, 2, 3, 4, 5)
x[1:3] # => (2, 3)
x[1:2] # => (2,)
x[-1] # => 5
x[:3:2] # => (1, 3)
len(x) # => 4 
```

##### Equality
1. Identity
  - Means the SAME object (reference in memory)
  - We use the `is` operator to test for identity
  - Identical objects are equivalent

2. Equivalence
  - Two objects are equivalent (even if they are not the same object)
  - We use the `==` operator to test for equivalence
  - Equivalent objects **MAY NOT** be identical

```
a = (1, 2)
b = (1, 2)
a == b # True
a is b # False
c = a
a == c # True
a is c # True
b is c # False
```
