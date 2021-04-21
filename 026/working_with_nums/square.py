
# Numbers should be comma separated values like this: 5,10,30,1,2,7
nums = input("Provide me with comma separated list of numbers you wish to square: (ie: 1, 2, 3, 4, etc) ").split(",")
print([int(n) * int(n) for n in nums])