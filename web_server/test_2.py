# Write a python program to fetch the data from the two files and check the matching words present in the both files.
# Check how many times matching words repeated in the both files and print which files having less number of repeated words and its count value.

# Example
#
# File1.txt:
#
# “test
# python
# test
# developer”
#
# File2.txt:
#
# “test
# python
# python
# test
# test”
#
# Expected
# Output:
#
# test: 2
#
# python: 1

string_1 = "test python test developer"
string_2 = "test python python test test"

def file_operatio(string1, string2):
    set_a = set(string1.split(" "))
    set_b = set(string2.split(" "))
    result = set_a.intersection(set_b)
    for each_item in result:
        a = list(set_a).count(each_item)
        b = list(set_b).count(each_item)
        count = a if a < b else b
        print(each_item + "-->" + count)


file_operatio(string_1, string_2)