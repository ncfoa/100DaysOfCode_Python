
# numbers should be provided as comma separated values 1,2,3,4,5
nums = input("Provide me with a list of numbers to filter: (ie: 1,2,3,4,5) ").split(",")
print([int(num) for num in nums if int(num) % 2 == 0])