
cook_book = {}

# Задача №1
print("Задача №1:")


def cookbook(FILE_NAME):
    with open(FILE_NAME) as file:
        count = 1
        count_ingr = 0
        for line in file:
            line = line.split()
            if not line:
                continue
            if count == 1:
                cook_name = str(" ".join(line))
                cook_book[cook_name] = []
                count += 1
            elif count == 2:
                count_ingr = int(*line)
                count += 1
                continue
            if count_ingr > 0:
                i = line.index("|")
                cook_book[cook_name].append(
                    {'ingredient_name': " ".join(line[0:i]),
                     'quantity': line[i+1], 'measure': " ".join(line[i+3:])})
                count_ingr -= 1
                if count_ingr == 0:
                    count = 1


cookbook("recipes.txt")
print(cook_book)


# Задача №2

print("Задача №2:")


def get_shop_list_by_dishes(dishes: list, person_count: int):
    global d
    d = {}
    for dish in dishes:
        for cook in cook_book[dish]:
            if not cook['ingredient_name'] in d:
                d[cook['ingredient_name']] = {'measure': cook['measure'],
                                              'quantity': int(cook['quantity']) * person_count}
            else:
                d[cook['ingredient_name']
                  ]['quantity'] += int(cook['quantity'])*person_count


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(d)

# Задача №3
print("Задача №3:")


def reading_file(LIST_FILES: list, LIST=[], D={}, d={}):
    for FILE_NAME in LIST_FILES:
        with open(FILE_NAME) as f1:
            for line in f1:
                LIST.append([line.strip()])
        D[FILE_NAME, len(LIST)] = LIST
        d[FILE_NAME] = len(LIST)
        LIST = []
    return D, d


FILES = ["1.txt", "2.txt", "3.txt"]
D, d = reading_file(FILES)
sorted_tuple = sorted(d.items(), key=lambda x: x[1])
d = dict(sorted_tuple)
list_f = list(d.items())

for l in list_f:
    with open("result.txt", "a") as res:
        res.write(l[0]+"\n"+str(l[1])+"\n")
        for dic in D[l]:
            res.write("".join(dic)+"\n")
print('Result 3-the task is messed up in the file "result.txt"')


print("Thank you for your attention!!!")
