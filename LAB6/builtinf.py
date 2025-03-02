from time import sleep
import math
a = int(input("Vvedite nomer zadaniya:  "))
if a==1:
    list = []
    x = input("Vvedite elementy massiva:   ").split()
    n = len(x)
    for i in range(n):
        list.append(int(x[i]))
    s = sum(list)
    print("list: " + str(list))
    print(s)
if a==2:
    word = input("Vvedite slovo ili slovosochitanie:   ")
    u = 0
    l = 0
    for x in word:
        if x.isupper():
            u +=1
        elif x.islower(): 
            l+=1
    print("Lower:  " + str(l))
    print("Upper:  "+ str(u))
if a==3:
    word = input("Vvedite slovo ili slovosochitanie:   ")
    ans = "\033[32m {}" .format('It is palindrome! ') + "\033[37m {}".format('')
    n = len(word)
    for i in range(n-1):
        if word[i]!=word[n-i-1]:
            ans = "It is\033[31m {}" .format('NOT') + "\033[37m {}".format("palindrome") 
    print(ans)
if a==4:
    n = int(input("Vvedite chislo:  "))
    t = int(input("Vvedite vremya ozhidaniya:   "))
    sleep(t/1000)
    print("Square root of " + str(n) +  " after "+ str(t)+" miliseconds is "+ str(math.sqrt(n)))
if a==5:
    list = []
    t = 'TRUE'
    x = input("Vvedite elementy massiva:   ").split()
    n = len(x)
    for i in range(n):
        list.append(x[i])
    for x in list:
        if x=='true':
            continue
        else:
            t = 'FALSE'
    print(t)