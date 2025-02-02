

x *= 28.3495231
    return x
    
x= int(input())
print(ounces(x))

#ex2
def f_to_c(f):
    return (5.0/9.0) * (f - 32)

f = 86
c = f_to_c(f)

print "{0} fahrenheit is {1} centigrade".format(f, c)

#ex3
def solve(numlegs, numheads):
    for i in range(1, numheads+1):
        if (i*4)+(numheads-i)*2 == numlegs:
            ans=f"{i} rabbits,{numheads-i} chickens"
            return ans
print("Enter number of legs:")
numlegs=int(input())
print("Enter number of heads")
numheads=int(input())
print(solve(numlegs,numheads))

#ex4
def filter_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print("Enter size of list:")
n = int(input())
print("Enter elements of list:")
l = list()
for i in range(n):
    x = int(input())
    if filter_prime(x):
        l.append(x)
print(1)
#
#ex5
import itertools
s = input()
elements = list(s)
permutations = list(itertools.permutations(elements))
print([''.join(permutations) for permutations in permutations])

#ex6
s = input()
s = s.split()[::-1]
l = list()
for i in s:
    l.append(i)
print(" ".join(l))

#ex7
def has__33(lst):
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1] == 3:
            return True
    return False


l = list()
print("Enter size of list:")
n = int(input())
print("Enter elements of list:")
for i in range(n):
    x = int(input())
    l.append(x)
print(has__33(l))
#ex8
def spy_game(nums):
    for i in range(0,len(nums)):
        if nums[i] == 0:
            for x in range(i+1,len(nums)):
                if nums[x] == 0:
                    for y in range(x+1,len(nums)):
                        if nums[y] == 7:
                            return True
                else:
                    return False

#ex9
import math


def volume_of_sphere(radius):
    return 4/3*radius**3*math.pi


print("Enter radius of sphere:")
radius = float(input())
print(volume_of_sphere(radius))

#ex10
def unique_array(lst):
    ans = []
    for i in range(len(lst)):
        check = False
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                if i != j:
                    check = True
        if check != 1:
            ans.append(lst[i])
    return ans


print("Enter size of list:")
n = int(input())
print("Enter elements of list:")
l = list()
for i in range(n):
    x = int(input())
    l.append(x)
print(unique_array(l))


#ex11
def palindrome(s):
    t = s[::-1]
    if t == s:
        return True
    return False

print("Enter string to check:")
s = input()
print(palindrome(s))
   

#ex12
def histogram(lst):
    for i in lst:
        print("*"*i)


print("Enter size of list")
n = int(input())
l = list()
print("Enter elements of list")
for i in range(n):
    x = int(input())
    l.append(x)
histogram(l)

#ex13
import random
number = random.randint(1, 20)
tries = 1
print("Hello! What is your name?")
name = input()
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
g = "Take a guess."
print(g)
n = int(input())
while (n != number):
    if (n < number):
        print("Your guess is too low.")
    elif (n > number):
        print("Your guess is too high.")
    print(g)
    tries += 1
    n = int(input())

print(f"Good job, {name}! You guessed my number in {tries} guesses!")
    
#ex14
print("Choose one of functions")
print("1.Unique_array    2.Volume_of_sphere    3.Histogram")
print("4.Ounces    5.Spygame    6.Heads,Legs")
print("7.Filter_prime    8.has_33    9.Celcius")
print("If you choose 0 then,calculator will stop working")
n = int(input())
while n != 0:
    if n == 1:
        from unique import unique_array
    elif n == 2:
        from volume import volume_of_sphere
    elif n == 3:
        from histogram import histogram
    elif n == 4:
        from ounces import ounces
    elif n == 5:
        from spygame import spygame
    elif n == 6:
        from heads_legs import solve
    elif n == 7:
        from prime import filter_prime
    elif n == 8:
        from has__33 import has__33
    elif n == 9:
        from fahrenheit import celcius
    else:
        print("Choose the number 1-9 or 0 to stop calculator")
    print("Choose one of functions")
    print("1.Unique_array    2.Volume_of_sphere    3.Histogram")
    print("4.Ounces    5.Spygame    6.Heads,Legs")
    print("7.Filter_prime    8.has_33    9.Celcius")
    n = int(input())
print("Well done!")

 