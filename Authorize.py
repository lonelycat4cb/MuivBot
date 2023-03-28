db = {}
with open('DataBase.txt') as file:
    for line in file:
        key, *value = line.split()
        db[key] = value

print(db)