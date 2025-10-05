num = 7

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
num = 543
last_digit = num % 10
print(last_digit)


sequence = ['a', 'b', 'c']
index = 0

# cycle forward
index = (index + 1) % len(sequence)
print(sequence[index])


hour = 11
hour = (hour + 1) % 12
print(hour)


seed = 5
a = 3
b = 7
m = 10

seed = (seed * a + b) % m
print(seed)


num = 15
divisor = 5

if num % divisor == 0:
    print("Divisible")
else:
    print("Not divisible")

value = "apple"
table_size = 10
hash_value = hash(value) % table_size
print(hash_value)


result = True ^ False
print(result)


x = 5
y = 10
result = (x != y)
print(result)


num = 15
divisor = 5

if num % divisor == 0:
    print("Divisible")
else:
    print("Not divisible")

value = "apple"
table_size = 10
hash_value = hash(value) % table_size
print(hash_value)

result = True ^ False
print(result)

x = 5
y = 10
result = (x != y)
print(result)

x = 5
y = 10

if x == y:
    print('x and y are equal')
elif x < y:
    print('x is less than y')
else:
    print('x is greater than y')

x = 7

if 0 < x < 10:
    print('x is a positive single-digit number.')

def countdown_by_two(n):
    if n <= 0:   # base case
        print("Blastoff!")
    else:
        print(n)
        countdown_by_two(n - 2)

countdown_by_two(10)

10
8
6
4
2
print("Blastoff!")
