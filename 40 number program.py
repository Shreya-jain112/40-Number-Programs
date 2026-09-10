# DSA - 40 Number Programs in Python
# Name: Shreya Jain
# Roll No.: 2400300100383
#
# Simple student-style solutions with input and output.

# 1. Sum of Digits
n = int(input("Enter a number: "))
temp = abs(n)
s = 0
while temp > 0:
    s += temp % 10
    temp //= 10
print("Sum of digits =", s)


# 2. Reverse of a Number
n = int(input("Enter a number: "))
temp = abs(n)
rev = 0
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
if n < 0:
    rev = -rev
print("Reverse =", rev)


# 3. Palindrome Number
n = int(input("Enter a number: "))
if str(abs(n)) == str(abs(n))[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# 4. Digital Root
n = int(input("Enter a number: "))
n = abs(n)
while n >= 10:
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    n = total
print("Digital root =", n)


# 5. Count Digits
n = int(input("Enter a number: "))
print("Number of digits =", len(str(abs(n))))


# 6. Product of Digits
n = int(input("Enter a number: "))
n = abs(n)
if n == 0:
    product = 0
else:
    product = 1
    while n > 0:
        product *= n % 10
        n //= 10
print("Product of digits =", product)


# 7. Armstrong Number
n = int(input("Enter a number: "))
digits = str(abs(n))
power = len(digits)
total = 0
for digit in digits:
    total += int(digit) ** power
if total == abs(n):
    print("Armstrong")
else:
    print("Not Armstrong")


# 8. Strong Number
import math
n = int(input("Enter a number: "))
total = 0
for digit in str(abs(n)):
    total += math.factorial(int(digit))
if total == abs(n):
    print("Strong")
else:
    print("Not Strong")


# 9. Spy Number
n = int(input("Enter a number: "))
digits = str(abs(n))
sum_digits = 0
product_digits = 1
for digit in digits:
    sum_digits += int(digit)
    product_digits *= int(digit)
if sum_digits == product_digits:
    print("Spy")
else:
    print("Not Spy")


# 10. Perfect Number
n = int(input("Enter a number: "))
total = 0
for i in range(1, n):
    if n % i == 0:
        total += i
if total == n:
    print("Perfect")
else:
    print("Not Perfect")


# 11. Automorphic Number
n = int(input("Enter a number: "))
square = n * n
if str(square).endswith(str(n)):
    print("Automorphic")
else:
    print("Not Automorphic")


# 12. Neon Number
n = int(input("Enter a number: "))
square = n * n
total = 0
while square > 0:
    total += square % 10
    square //= 10
if total == n:
    print("Neon")
else:
    print("Not Neon")


# 13. Duck Number
n = input("Enter a number: ")
if "0" in n[1:]:
    print("Duck")
else:
    print("Not Duck")


# 14. Harshad Number
n = int(input("Enter a number: "))
total = sum(int(d) for d in str(abs(n)))
if total != 0 and n % total == 0:
    print("Harshad")
else:
    print("Not Harshad")


# 15. Swap First and Last Digit
n = input("Enter a number: ")
if len(n) == 1:
    result = n
else:
    result = n[-1] + n[1:-1] + n[0]
print("After swapping =", result)


# 16. Largest Digit
n = input("Enter a number: ")
print("Largest digit =", max(int(d) for d in n if d.isdigit()))


# 17. Smallest Digit
n = input("Enter a number: ")
print("Smallest digit =", min(int(d) for d in n if d.isdigit()))


# 18. Remove Zero Digits
n = input("Enter a number: ")
result = n.replace("0", "")
print("After removing zeros =", result)


# 19. Prime Number
n = int(input("Enter a number: "))
prime = True
if n < 2:
    prime = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break
if prime:
    print("Prime")
else:
    print("Not Prime")


# 20. Prime Digits Only
n = input("Enter a number: ")
prime_digits = True
for digit in n:
    if digit not in "2357":
        prime_digits = False
        break
if prime_digits:
    print("All Prime")
else:
    print("Not All Prime")


# 21. Count Even Digits
n = input("Enter a number: ")
count = 0
for digit in n:
    if int(digit) % 2 == 0:
        count += 1
print("Even digits =", count)


# 22. Count Odd Digits
n = input("Enter a number: ")
count = 0
for digit in n:
    if int(digit) % 2 != 0:
        count += 1
print("Odd digits =", count)


# 23. Sum of Even Digits
n = input("Enter a number: ")
total = 0
for digit in n:
    if int(digit) % 2 == 0:
        total += int(digit)
print("Sum of even digits =", total)


# 24. Sum of Odd Digits
n = input("Enter a number: ")
total = 0
for digit in n:
    if int(digit) % 2 != 0:
        total += int(digit)
print("Sum of odd digits =", total)


# 25. Fibonacci Check
n = int(input("Enter a number: "))
a, b = 0, 1
found = False
while a <= n:
    if a == n:
        found = True
        break
    a, b = b, a + b
if found:
    print("Fibonacci")
else:
    print("Not Fibonacci")


# 26. Decimal to Binary
n = int(input("Enter a decimal number: "))
if n == 0:
    binary = "0"
else:
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
print("Binary =", binary)


# 27. Binary to Decimal
binary = input("Enter a binary number: ")
decimal = 0
for digit in binary:
    decimal = decimal * 2 + int(digit)
print("Decimal =", decimal)


# 28. GCD of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
while b != 0:
    a, b = b, a % b
print("GCD =", abs(a))


# 29. LCM of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
x, y = abs(a), abs(b)
while y != 0:
    x, y = y, x % y
if a == 0 or b == 0:
    lcm = 0
else:
    lcm = abs(a * b) // x
print("LCM =", lcm)


# 30. Count Factors
n = int(input("Enter a number: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
print("Number of factors =", count)


# 31. Sum of Factors (excluding the number itself)
n = int(input("Enter a number: "))
total = 0
for i in range(1, n):
    if n % i == 0:
        total += i
print("Sum of factors =", total)


# 32. Buzz Number
n = int(input("Enter a number: "))
if n % 7 == 0 or n % 10 == 7:
    print("Buzz")
else:
    print("Not Buzz")


# 33. Happy Number
n = int(input("Enter a number: "))
seen = set()
while n != 1 and n not in seen:
    seen.add(n)
    total = 0
    for digit in str(n):
        total += int(digit) ** 2
    n = total
if n == 1:
    print("Happy")
else:
    print("Not Happy")


# 34. Sunny Number
n = int(input("Enter a number: "))
x = int((n + 1) ** 0.5)
if x * x == n + 1:
    print("Sunny")
else:
    print("Not Sunny")


# 35. Disarium Number
n = int(input("Enter a number: "))
digits = str(abs(n))
total = 0
for i in range(len(digits)):
    total += int(digits[i]) ** (i + 1)
if total == abs(n):
    print("Disarium")
else:
    print("Not Disarium")


# 36. Peterson Number
import math
n = int(input("Enter a number: "))
total = 0
for digit in str(abs(n)):
    total += math.factorial(int(digit))
if total == abs(n):
    print("Peterson")
else:
    print("Not Peterson")


# 37. Factorial
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial =", fact)


# 38. Fibonacci Series
n = int(input("Enter number of terms: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()


# 39. Power of Number
base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
answer = 1
for i in range(abs(exponent)):
    answer *= base
if exponent < 0:
    answer = 1 / answer
print("Power =", answer)


# 40. Magic Number
n = int(input("Enter a number: "))
while n > 9:
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    n = total
if n == 1:
    print("Magic")
else:
    print("Not Magic")
