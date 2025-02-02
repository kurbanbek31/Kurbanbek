#ex1
class IOString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    def print_String(self):
        print(self.str1.upper())

str1 = IOString()
str1.get_String()
str1.print_String()

#ex2
class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length*self.length

aSquare= Square(3)
print aSquare.area()

#ex3
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())

#ex4
class string:
    def __init__(self, string):
        self.string = string

    def getString(self):
        return self.string

    def printString(self):
        self.string = self.string.upper()
        return self.string


s = string(input())
t = s.getString()
print(t)
up = s.printString()
print(up)


#ex5
class Bank_account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        print("Pleas, enter the sum you want to put in deposit:")
        money = float(input())
        self.balance += money
        return Bank_account(self.owner, self.balance)

    def withdraw(self):
        print("Please, enter the sum you want to take:")
        taken = float(input())
        while taken > self.balance:
            print("Please, enter the sum you want to take:")
            taken = float(input())
        self.balance -= taken
        return Bank_account(self.owner, self.balance)

    def __str__(self):
        return f"{self.owner} have {self.balance} money in his deposit."


account = Bank_account(input(), float(input()))
account = Bank_account.deposit(account)
account = Bank_account.withdraw(account)
print(account)
#ex6
def filter_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


n = int(input())
l = []
for i in range(n):
    x = int(input())
    l.append(x)
primes = list(filter(filter_prime, l))
print(primes)


