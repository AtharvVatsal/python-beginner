for x in range(6):
    y = "x" * x
print(y)
for x in range(3):
    y = "x" * x
print(y)
for x in range(5):
    y = "x" * x
print(y)
for x in range(3):
    y = "x" * x
print(y)
for x in range(3):
    y = "x" * x
print(y)   

print("-------------------------")
#A better way to code

number = [5, 2, 5, 2, 2]
for x_count in number:
    output = ''
    for x1 in range(x_count):
        output = output + 'x'
    print(output)

#printing L

letter = [2, 2, 2, 2, 6]
for l_count in letter:
    output = ''
    for l_times in range(l_count):
        output += 'L'
    print(output)