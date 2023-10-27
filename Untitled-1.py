num_rows = int(input("Enter the number of rows for the trinomial triangle: "))

coefficient = 0

for n in range(num_rows):
    coefficient = 1
    for k in range(0, n + 1):
        if k != 0:
            coefficient = coefficient * (n - k + 1) // k
        print(f"{coefficient}", end=" ")
    print()