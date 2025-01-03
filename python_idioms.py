#unpackking

a, b = (1, 2) # a = 1, b = 2 
c, d, e, f = (3, 4, 5, 6)
# enumerate

for i, val in enumerate({"aplle" "banana"}):
    print(i, val)

# zip

for x, y in zip([1, 2], [3, 4]):
    print(x, y)

# Context Manager (with statement)


with open("test.txt", "w") as f:
    f.write("Hello")