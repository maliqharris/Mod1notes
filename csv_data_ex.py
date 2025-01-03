import csv
#with makes sure is closed
with open("data.scv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["Alice", 31])

with open("data.csv", "r" ) as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)