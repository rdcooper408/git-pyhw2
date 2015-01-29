Python Homework 2 1/28/15
How many "hello's" are printed?

# 1)
for i in range(3, 17):
print 'hello'

1.) 14

# 2)
for j in range(12):
8 if j % 3 == 0:
print 'hello'

2.) 4

# 3)
 for j in range(15):
 j % 5 == 3:
 print 'hello'
elif j % 4 == 3:
 print 'hello'

3.) 5

# 4)
z = 0
while z != 15:
print 'hello'
z = z + 3

4.) 5

# 5)
z = 12
while z < 100:

	if z == 31:
	for k in range(7):
	print 'hello'
						7
elif z == 18:
print 'hello'
						1
z = z + 1

5.) 8

# What does fooXX do?
	def foo1(x):
 return x ** 0.5
 
 This returns the square root of X
 

def foo2(x, y):
if x > y:
return x
return y

This returns the larger value of the two inputs


def foo3(x, y, z):
if x > y:
tmp = y
y = x
x = tmp

if y > z:
tmp = z
z = y
y = tmp
if x > y:
tmp = y
y = x
x = tmp
return [x, y, z]

This function simply orders the input from least to greatest

def foo4(x):
result = 1
for i in range(1, x + 1):
result = result * i
return result

This function returns the factorial of X

def foo5(x):
if x == 1:
return 1
return x * foo5(x - 1)

This function also returns the factorial of X
