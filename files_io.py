

# with open("data.txt", "w") as f:
#     f.write("Hello, file!")

# with open("data.txt", "r") as f:
#     content = f.read()
#     print("We wrote " + content)


file = ("data.txt")

with open(file, "w") as f:
    f.write("Hello, file!")

with open("data.txt", "r") as f:
    content = f.read()
    print("We wrote " + content)