
# read from file 1 and separate into list split on the new line indicator
with open("./list1.txt") as f:
    list1 = f.read().split("\n")
    f.close()
# read from file 2 and separate into list split on the new line indicator
with open("./list2.txt") as f:
    list2 = f.read().split("\n")
    f.close()
# iterate over list1 and return numbers that are in both lists
result = [int(num) for num in list1 if num in list2]

print(result)