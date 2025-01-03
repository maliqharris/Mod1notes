import sys
a = []

for over9000 in range(8999):
    a.append(a)  

print(sys.getrefcount(a))  

