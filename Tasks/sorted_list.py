# list = []
# for i in range(5):
#     i = int(input('enter numbers: '))
#     list.append(i)

# asc_list = sorted(list)
# desc_list = sorted(list,reverse=True)

# print(list)
# print(asc_list)
# print(desc_list)


def sort():
    user_input = input("Enter numbers separated by spaces: ")
    numbers = [int(num) for num in user_input.split()]

    asc_list = sorted(numbers)
    desc_list = sorted(numbers, reverse=True)

    print("Original:", numbers)
    print("Ascending:", asc_list)
    print("Descending:", desc_list)