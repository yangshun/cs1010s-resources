CS1010S Midterm Tracing Questions
==

Trace the following code and give the printed output.

###### Warmup
```python
num = 15
if num % 3 == 0:
  print('num divisible by 3')
elif num % 5 == 0:
  print('num divisible by 5')
elif num % 15 == 0:
  print('num divisible by 3 and 5')
else:
  print('num not divisible by 3 nor 5')
```

###### Warmup 2
```python
num = 15
if num % 3 == 0:
  print('num divisible by 3')
elif num % 5 == 0:
  print('num divisible by 5')
if num % 15 == 0:
  print('num divisible by 3 and 5')
else:
  print('num not divisible by 3 nor 5')
```

###### Warmup 3
```python
num = 15
if num % 3 == 0:
  print('num divisible by 3')
if num % 5 == 0:
  print('num divisible by 5')
if num % 15 == 0:
  print('num divisible by 3 and 5')
else:
  print('num not divisible by 3 nor 5')
```

###### Q1
```python
i, j, k = 0, 10, 1
while i < j:
  if k % 2:
    i += k
  else:
    j -= k
  k += 1
print(j)
```

###### Q2
```python
i, k = 100, 3
while i > 0:
  i -= k
  if i % (k + 1):
    k += 1
  else:
    continue
print(i)
```

###### Q3
```python
i = 1
result = 0
while i < 10:
  j = 1
  while j < 100:
    j += 1
    if not (j % i):
      break
  result += j
  i += 1
print(result)
```

###### Q4
```python
total = 0
for i in range(10):
  if i % 3 == 0:
    continue
  elif i % 5 == 0:
    break
  total += i
print(total)
```

###### Q5
```python
i, num = 0, 0
while -100 < num < 100:
  if i % 2 == 0:
    num += i
  else:
    num -= i
  i += 1
print(num)
```

###### Q6
```python
def foo(num, count):
  if num:
    return 1 + foo(num - num % (10 ** count), count + 1)
  else:
    return 0
print(foo(987654321, 1))
```
