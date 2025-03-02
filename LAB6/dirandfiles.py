import os
a = int(input("Vvedite nomer zadaniya:  "))
if a==1:
    path = input("Vvedite put' k failam:  ")
    print("Only directories:  ")
    print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
    print("Only files:  ")
    print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
    print("All directories and files:  ")
    print([ name for name in os.listdir(path)])
if a==2:
    path = input("Vvedite put' k failam:  ")
    print('Exist:', os.access(path, os.F_OK))
    print('Readable:', os.access(path, os.R_OK))
    print('Writable:', os.access(path, os.W_OK))
    print('Executable:', os.access(path, os.X_OK))
if a==3:
    path = input("Vvedite put' k failam:  ")
    print('Exist:', os.access(path, os.F_OK))
    if os.access(path, os.F_OK):
        print("All directories and files:  ")
        print([ name for name in os.listdir(path)]) 
    else:
        print("[]")
if a==4:
    path = input("Vvedite put' k failam:  ")
    file = open(path, 'r')
    content = file.read()
    lines = content.split('\n')
    print (str(len(lines))+" lines")
if a==5:
    path = input("Vvedite put' k failam:  ")
    list = input("Vvedite list:  ").split()
    with open(path, 'w') as file:
        for x in list:
            file.write("%s\n" % x)
if a==6:
    for i in range(65, 91):
        filename=chr(i) + ".txt"
        open(filename, 'w')
    print("Done! ")
if a==7:
    path1 = input("Vvedite put' k 1 failam:  ")
    path2 = input("Vvedite put' k 2 failam:  ")
    with open(path1,'r') as first, open(path2,'a') as second:
            for x in first:
                second.write(x)
if a==8:
    path = input("Vvedite put' k failam:  ")
    if os.access(path, os.F_OK):
        os.remove(path)
        print("Done! ")
    else: print("File does not exist!")