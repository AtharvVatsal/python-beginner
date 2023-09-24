numbers = [2, 2, 33, 4, 5, 0, 12, 4, 33]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)