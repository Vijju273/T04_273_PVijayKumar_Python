'''Operators:
===============
1. Explain in detail about all operators

a.Arithmetic Operators:
------------------------
Arithmetic operators are used to performing mathematical operations like addition, subtraction, multiplication, and division.
+ Addition, - subtraction, * multiplication, / division, % modulus, // floor division,
** exponential
---------------------------------------------------------------------------------------------

b.Assignment operators:
-------------------------
Assignment operator is used to assign value to the event, property, or variable. We use this operator in python to assign values to variables. We have multiple Assignment operators
= is x=5, += is x=x+5, -= is x=x-5, *= is x=x*5, /= is x=x/5, %= is x=x%5,
//=, **=, &=, |=, ^=, <<=, >>=
-----------------------------------------------------------

c.Comparison/relational operators:
-----------------------------------
Comparison of Relational operators compares the values. It either returns True or False according to the condition.
== is equals, != is not equal, > is greater than, < is lesser than, >= is greater than or
equal to, <= is lesser than or equal to
--------------------------------------------------

d.Logical:
-------------------------------
Logical operators perform Logical AND, Logical OR, and Logical NOT operations. It is used to combine conditional statements.

and returns True if both values are are true, ‘or’ returns True if one statement is true,
not will reverse the result
--------------------------------------------------

e.Identity operators:
---------------------
is and is not are the identity operators both are used to check if two values are located on the same part of the memory. Two variables that are equal do not imply that they are identical.

‘is’ returns True if both variables are the same object, ‘is not’ returns True if both
variables are not the same object.
---------------------------------------------------

f.Bitwise operators:
--------------------
Bitwise operators act on bits and perform the bit-by-bit operations. These are used to operate on binary numbers.
These are used to compare binary numbers
➔ & - AND - Sets each bit to 1 if both bits are 1
➔ | - OR - Sets each bit to 1 if one of two bits is 1
➔ ^ - XOR - Sets each bit to 1 if only one of two bits is 1
➔ ~ - NOT - Inverts all the bits
➔ << - Zero fill left shift - Shift left by pushing zeros in from the right and let the
leftmost bits fall off
➔ >> - Signed right shift - Shift right by pushing copies of the leftmost bit in from
the left, and let the rightmost bits fall off
----------------------------------------------------------

g. Boolean Operators:
---------------------------
Boolean Operators are those that result in the Boolean values of True and False. These include and, or and not. While and & or require 2 operands, not is a unary operator. Boolean operators are most commonly used in arithmetic computations and logical comparisons.
---------------------------------------------------

h. Membership Operator

This In operator is used in python to evaluate if a particular value is there or not in a sequence. The In operator returns True if it the specified element found in the list, otherwise it returns false.
---------------------------------------------------------------------------------------------

2. == vs is
----------------
==  : is for value equality. It's used to know if two objects have the same value.
is : is for reference equality. It's used to know if two references refer (or point) to the same object, i.e if they're identical.
----------------------------------------------------------

3. Operator precedence.
-------------------------
P – Parentheses
E – Exponentiation
M – Multiplication     (Multiplication and division have the same precedence)
D – Division
A – Addition     (Addition and subtraction have the same precedence)
S – Subtraction
The modulus operator helps us extract the last digit/s of a number. For example:
x % 10 -> yields the last digit
x % 100 -> yield last two digits
---------------------------------------


'''

# Examples:
# Addition Operator
a = 2
b = 3
res = a + b
print(res)

# Subtraction Operator
a = 2
b = 3
res = a - b
print(res)

# Multiplication Operator
a = 2
b = 3
res = a * b
print(res)

# Division Operator
a = 2
b = 3
res = a / b
print(res)

# Modulus Operator
a = 2
b = 3
res = a % b
print(res)

# Floor division Operator
a = 2
b = 3
res = a // b
print(res)

# Relational Operator(Equal to)
a=10
b=20
print(a==b)

# Relational Operator(Less than)
a=10
b=20
print(a<b)

# Relational Operator(Greater than)
a=10
b=20
print(a>b)

# Relational Operator(Less than or equal to)
a=10
b=20
print(a<=b)

# Relational Operator(Greater than or equal to)
a=10
b=20
print(a>=b)

# Relational Operator(Not equal to)
a=10
b=20
print(a!=b)

# Logical Operator(AND gate)
a=10
b=20
print(a and b)

# Logical Operator(OR gate)
a=10
b=20
print(a or b)

# Logical Operator(NOT gate)
a = 10
b = 20
print(a not b)

# Assignment Operator
a = 5
b = a
print(b)


# Add and Assign Operator
a = 3
b = 5
a += b
print(a)


# Subtract and Assign Operator
a = 3
b = 5
a -= b
print(a)


# Multiply and Assign Operator
a = 3
b = 5
a *= b
print(a)


# Division and Assign Operator
a = 3
b = 5
a /= b
print(a)

# Modulus and Assign Operator
a = 3
b = 5
a %= b
print(a)


# Floor Division and Assign Operator
a = 3
b = 5
a//= b
print(a)


# Exponent and Assign Operator
a = 3
b = 5
a **= b
print(a)


# Bitwise AND and Assign Operator
a = 3
b = 5
a &= b
print(a)


# Bitwise OR and Assign Operator
a = 3
b = 5
a |= 7
print(a)


# Bitwise XOR and Assign Operator
a = 3
b = 5
a ^= 7
print(a)


# Bitwise Right Shift and Assign
a = 3
b = 5
a >>= 7
print(a)

# Bitwise Right Shift and Assign
a = 3
b = 5
a <<= 7
print(a)

# Bitwise Operator:
# Bitwise AND
a=10
b=7
c=a&b
print(c)

# Bitwise OR
a=10
b=7
c=a|b
print(c)

# Bitwise NOT
a=10
b=~a
print(b)

# Bitwise XOR
a = 10
b = 7
c = a ^ b
print(c)

# Bitwise Right Shift
a = 10
b = a >> 7
print(b)

# Bitwise Left Shift
a=10
b=a << 7
print(b)