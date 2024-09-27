# Exercise 01
## Uses for modulus
Sure, here's the information in markdown format:

The modulus operator in Python is denoted by the `%` symbol and is used to find the remainder of a division operation. It can be used for a variety of purposes, including:

1. **Checking for even or odd numbers:** The modulus operator can be used to determine whether a number is even or odd by checking the remainder of the division of the number by 2. If the remainder is 0, the number is even; if the remainder is 1, the number is odd.
   ```python
   if num % 2 == 0:
       print("Even")
   else:
       print("Odd")
   ```
2. **Finding the last digit of a number:** The modulus operator can be used to find the last digit of a number by taking the remainder of the division of the number by 10.
   ```python
   last_digit = num % 10
   ```
3. **Cycling through a sequence:** The modulus operator can be used to cycle through a sequence of values by taking the remainder of the division of the current index by the length of the sequence.
   ```python
   index = (index + 1) % len(sequence)
   ```
4. **Implementing a clock:** The modulus operator can be used to implement a clock that wraps around to 0 after reaching a certain value. For example, a 12-hour clock can be implemented by taking the remainder of the division of the current hour by 12.
   ```python
   hour = (hour + 1) % 12
   ```
5. **Generating random numbers:** The modulus operator can be used to generate a sequence of pseudo-random numbers by applying a mathematical formula to a seed value and taking the remainder of the division of the result by a certain value.
   ```python
   seed = (seed * a + b) % m
   ```
6. **Checking for divisibility:** The modulus operator can be used to check whether one number is divisible by another number by checking whether the remainder of the division is 0.
   ```python
   if num % divisor == 0:
       print("Divisible")
   else:
       print("Not divisible")
   ```
7. **Implementing a hash function:** The modulus operator can be used to implement a hash function, which is a mathematical function that maps a large set of values to a smaller set of values. The hash function can be used to quickly look up values in a data structure such as a hash table.
   ```python
   hash_value = hash(value) % table_size
   ```

Overall, the modulus operator is a versatile tool that can be used in a variety of contexts to solve a wide range of problems. Its ability to find the remainder of a division operation makes it a useful tool for a variety of mathematical and programming tasks.

## XOR in Python
The logical XOR operation, also known as exclusive OR, is a logical operation that takes two boolean values as input and returns a boolean value as output. The XOR operation returns `True` if and only if exactly one of the input values is `True`. In other words, the XOR operation returns `True` if the input values are different, and `False` if the input values are the same.

In Python, the logical XOR operation can be computed using the `^` operator. Here's an example:

```python
# Compute the logical XOR of two boolean values
result = True ^ False
print(result)  # Output: True
```

In this example, the `^` operator is used to compute the logical XOR of `True` and `False`. The result is `True`, since the input values are different.

The `^` operator can also be used with non-boolean values in Python, but it performs a bitwise XOR operation rather than a logical XOR operation. To perform a logical XOR operation on non-boolean values, you can use the `!=` operator instead:

```python
# Compute the logical XOR of two non-boolean values
result = (x != y)
print(result)  # Output: True if x and y are different, False if x and y are the same
```

In this example, the `!=` operator is used to compute the logical XOR of `x` and `y`. The result is `True` if `x` and `y` are different, and `False` if `x` and `y` are the same.

### Alternate XOR Method Based on Boolean Logic
It is possible to compute the logical XOR operation using only the `and` and `or` operators in Python. Here's an example:

```python
# Compute the logical XOR of two boolean values using only and and or
result = (x and not y) or (not x and y)
print(result)  # Output: True if x and y are different, False if x and y are the same
```

In this example, the `and` and `or` operators are used to compute the logical XOR of `x` and `y`. The expression `(x and not y)` is `True` if `x` is `True` and `y` is `False`, and `False` otherwise. The expression `(not x and y)` is `True` if `x` is `False` and `y` is `True`, and `False` otherwise. The logical XOR of `x` and `y` is `True` if either `(x and not y)` or `(not x and y)` is `True`, and `False` otherwise.

This technique can be used to compute the logical XOR of non-boolean values as well, by comparing the values using the `==` operator instead of using the values directly:

```python
# Compute the logical XOR of two non-boolean values using only and and or
result = (x == y1) and (x != y2) or (x != y1) and (x == y2)
print(result)  # Output: True if x is different from y1 and y2, False if x is the same as y1 and y2
```

In this example, the `and` and `or` operators are used to compute the logical XOR of `x`, `y1`, and `y2`. The expression `(x == y1) and (x != y2)` is `True` if `x` is equal to `y1` and not equal to `y2`, and `False` otherwise. The expression `(x != y1) and (x == y2)` is `True` if `x` is not equal to `y1` and equal to `y2`, and `False` otherwise. The logical XOR of `x`, `y1`, and `y2` is `True` if either `(x == y1) and (x != y2)` or `(x != y1) and (x == y2)` is `True`, and `False` otherwise.

## Re-writing Conditionals
### Chained Conditional
* Before
```python
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')
```
* After asking for chained conditional
```python
if x == y:
    print('x and y are equal')
elif x < y:
    print('x is less than y')
else:
    print('x is greater than y')
```

### Single conditional
* Before
```python
if 0 < x:
    if x < 10:
        print('x is a positive single-digit number.')
```
* After asking for chained conditional
```python
if 0 < x < 10:
    print('x is a positive single-digit number.')
```

### Unnecessary Complexity
* Before
```python
if not x <= 0 and not x >= 10:
    print('x is a positive single-digit number.')
```
* After
```python
if 0 < x < 10:
    print('x is a positive single-digit number.')
```

## What's Wrong
* Before Recursion...
```python
def countdown_by_two(n):
    if n == 0:
        print('Blastoff!')
    else:
        print(n)
        countdown_by_two(n-2)
```
* After AI Fix
```python
def countdown_by_two(n):
    # Base case: if n is less than 2, print 'Blastoff!' and return
    if n < 2:
        print(n)
        print('Blastoff!')
    else:
        # Recursive case: print n and call the function again with n-2
        print(n)
        countdown_by_two(n-2)
```