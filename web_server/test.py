def convert (x):

    outer_list = []
    inner_list = []
    # result_list = []

    # for outer_index, outer_list in enumerate(x):
    #     for index, inner_list in enumerate(outer_list):
    #         result_list.append(inner_list)
    for index, each_list in enumerate(x):
        inner_list.append(each_list[0])
    outer_list.append(inner_list)
    inner_list = []
    for index, each_list in enumerate(x):
        inner_list.append(each_list[1])
    outer_list.append(inner_list)
    inner_list = []
    for index, each_list in enumerate(x):
        inner_list.append(each_list[2])
    outer_list.append(inner_list)
    inner_list = []
    for index, each_list in enumerate(x):
        inner_list.append(each_list[3])
    outer_list.append(inner_list)
    return result_list




a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
result = convert(a)

print(result)

# Sample output
# expected output = [[1,5,9],[2,6,10],[3,7,11],[4,8,12]]