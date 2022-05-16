#1
# def countdown(num):
#     output = []
#     for i in range (num, -1, -1):
#         output.append(i)
#     return output

# print(countdown(5))

#2
# def print_return(list):
#     print(list[0])
#     return list[1]

# print(print_return([1,2]))

#3
# def sum_length(list):
#     return list[0] + len(list)

# print(sum_length([1, 2, 3, 4]))

#4
# def greater_than(list):
#     output = []
#     for i in range (0, len(list)):
#         if len(list) < 2:
#             False
#         elif list[i] > list[1]:
#             output.append(list[i])
#     print(len(output))
#     return output

# print(greater_than([1, 2, 3, 4, 5]))

#5
def length_value(size, value):
    output = []
    for i in range (0, size):
        output.append(value)
    return output

print(length_value(4,7))
