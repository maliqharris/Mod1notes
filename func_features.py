funs = [1, 2, 3, 4, 5]

circles = [x*x for x in funs]
evens = list(filter(lambda x: x% 2 == 0, funs))

print(circles, evens)