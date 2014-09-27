##########
# Warmup #
##########

def warmup():
  num = 15
  if num % 3 == 0:
    print('num divisible by 3')
  elif num % 5 == 0:
    print('num divisible by 5')
  elif num % 15 == 0:
    print('num divisible by 3 and 5')
  else:
    print('num not divisible by 3 nor 5')

# warmup()

# Printed output:
# num divisible by 3

# Lesson:
# This question tests on your understanding of if/elif/else.

############
# Warmup 2 #
############

def warmup2():
  num = 15
  if num % 3 == 0:
    print('num divisible by 3')
  elif num % 5 == 0:
    print('num divisible by 5')
  if num % 15 == 0:
    print('num divisible by 3 and 5')
  else:
    print('num not divisible by 3 nor 5')

# warmup2()

# Printed output:
# num divisible by 3
# num divisible by 3 and 5

# Lesson:
# This question tests on your understanding of if/elif/else.

############
# Warmup 3 #
############

def warmup3():
  num = 15
  if num % 3 == 0:
    print('num divisible by 3')
  if num % 5 == 0:
    print('num divisible by 5')
  if num % 15 == 0:
    print('num divisible by 3 and 5')
  else:
    print('num not divisible by 3 nor 5')

# warmup3()

# Printed output:
# num divisible by 3
# num divisible by 5
# num divisible by 3 and 5

# Lesson:
# This question tests on your understanding of if/elif/else.

#######
# Q1  #
#######

def q1():
  i, j, k = 0, 10, 1
  while i < j:
    if k % 2:
      i += k
    else:
      j -= k
    k += 1
  print(j)

# q1()

# Printed output:
# 4

# Lesson:
# This question tests on your understanding of if/else and truth values of numbers.

#######
# Q2  #
#######

def q2():
  i, k = 100, 3
  while i > 0:
    i -= k
    if i % (k + 1):
      k += 1
    else:
      continue
  print(i)

# q2()

# Printed output:
# -2

# Lesson:
# This question tests on your understanding of if/else and truth values of numbers.

#######
# Q3  #
#######

def q3():
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

# q3()

# Printed output:
# 46

# Lesson:
# This question tests on your understanding of truth values of numbers and nested while loops.

#######
# Q4  #
#######

def q4():
  total = 0
  for i in range(10):
    if i % 3 == 0:
      continue
    elif i % 5 == 0:
      break
    total += i
  print(total)

# q4()

# Printed output:
# 7

# Lesson:
# This question tests on your understanding of continue, break and if/elif.

#######
# Q5  #
#######

def q5():
  i, num = 0, 0
  while -100 < num < 100:
    if i % 2 == 0:
      num += i
    else:
      num -= i
    i += 1
  print(num)

# q5()

# Printed output:
# -100

# Lesson:
# This question tests on your understanding of while, if/else and ability to spot trends.

#######
# Q6  #
#######

def q6():
  def foo(num, count):
    if num:
      return 1 + foo(num - num % (10 ** count), count + 1)
    else:
      return 0
  print(foo(987654321, 1))

# q6()

# Printed output:
# 9

# Lesson:
# This question tests on your understanding of truth values of numbers, 
# general arithmetic and recursion.
