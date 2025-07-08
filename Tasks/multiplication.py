def multi(num):
    bigTable = []

    for i in range(1, num + 1):
        smalltable = []
        for j in range(1, i + 1):
            result = i * j
            smalltable.append(result)
            print(f"{i} x {j} = {result}")

        print(smalltable)
        bigTable.append(smalltable)

    print(bigTable)


# number = int(input("Enter a number: "))

# bigTable = []

# for i in range(1, number + 1):
#     smalltable = []
#     for j in range(1, i + 1):
#         result = i * j
#         smalltable.append(result)
#         print(f"{i} x {j} = {result}")

#     print(smalltable)
#     bigTable.append(smalltable)


# print(bigTable)
