# Ex 1 Create a generator that generates the squares of numbers up to some number N.
def square_numbers(n):
    for num in range( 2 , n + 1):
        yield num ** 2
n=int(input())
square_num = square_numbers(n)
print(",".join(map(str, square_num)))

#Ex 2 Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

def even_numbers(n):
    for num in range(1,n+1):
        if (num % 2 == 0):
            yield num
n = int (input())
even_num = even_numbers(n)
print (",".join(map(str,even_num)))

#Ex 3 Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def number_s(n):
    for num in range(1 , n+1):
        if (num % 3 == 0 and num % 4 == 0):
            yield num 
n=int(input())
numbers = number_s(n)
print (",".join(map(str,numbers)))

#Ex 4 Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a,b):
    for num in range(a, b+1):
        yield num ** 2
a=int(input())
b=int(input())
for square in squares (a, b):
    print(square)

#Ex 5 Implement a generator that returns all numbers from (n) down to 0.
def countdown(n):
    for num in range(n, -1, -1):
        yield num
n = int(input("Enter a number: "))
for number in countdown(n):
    print(number)